"""Verifica dimensiones, alfa, contenido, base y diferencias de piernas."""
from pathlib import Path
import json
import numpy as np
from PIL import Image

root = Path(__file__).resolve().parent
report = {}
for person in ('coordinadora', 'operador'):
    for action, count in (('caminar', 4), ('celebrar', 2)):
        name = f'{person}-{action}.png'
        im = Image.open(root / name)
        assert im.size == (68*count, 108), name
        assert im.mode == 'RGBA', name
        a = np.array(im)
        assert set(np.unique(a[:, :, 3])) == {0, 255}, name
        frames = [a[:, i*68:(i+1)*68] for i in range(count)]
        bases = []
        for i, frame in enumerate(frames):
            ys, xs = np.where(frame[:, :, 3] != 0)
            assert len(xs) > 0, (name, i)
            assert abs((int(xs.min())+int(xs.max()))/2 - 33.5) <= 1, (name, i)
            bases.append(int(ys.max()))
            assert ys.max() == (101 if action == 'celebrar' and i == 1 else 107)
        entry = {'dimensiones': list(im.size), 'alfa': [0, 255], 'bases': bases}
        if action == 'caminar':
            # Compare the bottom 32 rows, excluding the arms and torso.
            changes = [int(np.any(frames[i][76:] != frames[(i+1)%count][76:], axis=2).sum())
                       for i in range(count)]
            silhouettes = [int(np.count_nonzero(frames[i][76:, :, 3] !=
                                               frames[(i+1)%count][76:, :, 3]))
                           for i in range(count)]
            assert min(changes) > 30 and min(silhouettes) > 20, name
            entry['pixeles_distintos_piernas_entre_cuadros'] = changes
            entry['cambios_silueta_piernas'] = silhouettes
        report[name] = entry
text = json.dumps(report, ensure_ascii=False, indent=2)
(root / 'verificacion.json').write_text(text+'\n')
print(text)
