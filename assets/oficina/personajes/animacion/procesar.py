"""Compone las tiras desde los originales con Pillow y NumPy."""
from pathlib import Path
from collections import deque
import json
import numpy as np
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parent


def clean(im):
    a = np.array(im.convert('RGBA'))
    mask = a[:, :, 3] >= 160
    seen = np.zeros(mask.shape, dtype=bool)
    best = []
    h, w = mask.shape
    for y, x in zip(*np.where(mask)):
        if seen[y, x]:
            continue
        seen[y, x] = True
        queue = deque([(int(y), int(x))])
        component = []
        while queue:
            yy, xx = queue.popleft()
            component.append((yy, xx))
            for ny, nx in ((yy-1, xx), (yy+1, xx), (yy, xx-1), (yy, xx+1)):
                if 0 <= ny < h and 0 <= nx < w and mask[ny, nx] and not seen[ny, nx]:
                    seen[ny, nx] = True
                    queue.append((ny, nx))
        if len(component) > len(best):
            best = component
    a[:, :, 3] = 0
    yy, xx = zip(*best)
    a[yy, xx, 3] = 255
    a[a[:, :, 3] == 0] = 0
    im = Image.fromarray(a)
    return im.crop(im.getbbox())


def palette_match(im, ref):
    refdata = np.array(ref)
    palette = np.unique(refdata[refdata[:, :, 3] >= 240, :3], axis=0).astype(np.int32)
    a = np.array(im)
    opaque = a[:, :, 3] == 255
    pixels = a[opaque, :3].astype(np.int32)
    for start in range(0, len(pixels), 128):
        chunk = pixels[start:start+128]
        indices = ((chunk[:, None] - palette[None]) ** 2).sum(axis=2).argmin(axis=1)
        pixels[start:start+128] = palette[indices]
    a[opaque, :3] = pixels.astype(np.uint8)
    return Image.fromarray(a)


def main():
    for person in ('coordinadora', 'operador'):
        ref = Image.open(ROOT.parent / f'{person}-pie.png').convert('RGBA')
        bbox = ref.getbbox()
        height = bbox[3] - bbox[1]
        for action, count in (('caminar', 4), ('celebrar', 2)):
            source = Image.open(ROOT / 'originales' / f'{person}-{action}.png').convert('RGBA')
            frames = [clean(source.crop((round(i*source.width/count), 0,
                                        round((i+1)*source.width/count), source.height)))
                      for i in range(count)]
            scale = height / frames[0].height
            sheet = Image.new('RGBA', (68*count, 108))
            for i, frame in enumerate(frames):
                # Preserve scale through the jump rather than stretching bent legs.
                factor = scale if action == 'celebrar' else height / frame.height
                size = (round(frame.width*factor), round(frame.height*factor))
                assert size[0] <= 68 and size[1] <= 108, size
                frame = frame.resize(size, Image.Resampling.NEAREST)
                frame = palette_match(frame, ref)
                bottom = 102 if action == 'celebrar' and i == 1 else 108
                sheet.alpha_composite(frame, (i*68 + (68-frame.width)//2, bottom-frame.height))
            out = ROOT / f'{person}-{action}.png'
            sheet.save(out)
    preview = Image.new('RGB', (1088, 432*4), '#84939c')
    for row, name in enumerate(('coordinadora-caminar', 'operador-caminar',
                                'coordinadora-celebrar', 'operador-celebrar')):
        im = Image.open(ROOT / f'{name}.png')
        im = im.resize((im.width*4, 432), Image.Resampling.NEAREST)
        preview.paste(im, (0, row*432), im)
    preview.save(ROOT / 'vista-previa.png')


if __name__ == '__main__':
    main()
