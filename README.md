# ⚡ SparkFlow — Juego de lógica y circuitos

**SparkFlow** es un juego educativo gratuito de diez misiones progresivas para aprender comparaciones, condiciones y rutas de automatización con datos JSON. Es un proyecto personal independiente, no afiliado a instituciones educativas.

🎮 **Jugar en línea:** https://sagitari01.github.io/sparkflow/

## Objetivos de aprendizaje

- Leer y escribir objetos JSON con claves, texto, números y booleanos.
- Comparar valores mediante `>`, `<`, `>=`, `<=`, `==` y `!=`.
- Combinar condiciones **AND (Y)** y **OR (O)**.
- Configurar rutas independientes y comprobar por qué una chispa atraviesa o no cada filtro.
- Observar la ejecución separada de varios documentos JSON, detectar errores y corregirlos.
- En las misiones **4, 8 y 10**, escribir un JSON desde cero y validar su sintaxis, sus tipos y sus resultados.

## Jugar en línea

1. Abre https://sagitari01.github.io/sparkflow/ en Chrome, Edge, Firefox o Safari.
2. Indica si jugarás individualmente o en grupo e ingresa los nombres para el informe.
3. Lee el objetivo específico de la misión y los resultados esperados.
4. **Selecciona una ruta** del circuito. Ninguna comienza preseleccionada ni con el filtro completado.
5. En el panel Filtros, elige el campo, selecciona un operador e introduce el valor. Cuando necesites dos condiciones, utiliza AND u OR según el objetivo.
6. En las **misiones 4, 8 y 10**, abre el panel JSON y escribe el objeto pedido. Los campos comienzan vacíos y el juego valida llaves, comillas, tipos de datos, claves y valores. Si hay un error, explica cómo corregirlo.
7. Ejecuta la simulación, observa el resultado de cada JSON y ajusta los filtros hasta superar la misión.
8. Al terminar, descarga o imprime el informe con tus resultados y los JSON escritos.

En teléfonos utiliza las pestañas **Circuito**, **Filtros** y **JSON** y desliza el circuito horizontalmente para examinar todas sus rutas.

## Descargar y jugar sin conexión

1. En la parte inferior del juego pulsa el enlace **«descarga el archivo index.html»**.
2. Guarda el archivo como **`index.html`** en una carpeta de tu computador, por ejemplo `Documentos/SparkFlow`.
3. Abre el Explorador de archivos (Windows) o Finder (macOS) y localiza el archivo.
4. Haz doble clic en `index.html`. Si el sistema no lo abre, usa **Abrir con** y selecciona Chrome, Edge, Firefox o Safari.
5. El juego funcionará en el navegador aunque estés desconectado. No necesitas instalar Node.js, usar comandos, iniciar un servidor ni crear una cuenta.
6. Al terminar, utiliza **Descargar informe** o **Imprimir informe** para conservar tus resultados en HTML o PDF.

Si deseas descargar el juego desde GitHub, abre el archivo `index.html` en la rama `main`, pulsa **Raw** y guarda el documento con la extensión `.html`.

## Cómo funciona

El proyecto consiste en **un único archivo `index.html`**, con HTML, CSS y JavaScript integrados. GitHub Pages publica el sitio, pero no ejecuta lógica en un servidor.

Las rutas ya están conectadas: el objetivo es configurar sus condiciones. Las últimas cuatro misiones aumentan el número de rutas paralelas; en niveles avanzados se incluyen generadores y una compuerta que requiere varias entradas. Esta compuerta es una mecánica del juego, **no una función de unión automática de rutas de Make**.

La escritura de JSON es parte obligatoria de los desafíos 4 (un campo numérico), 8 (números y booleanos) y 10 (un JSON de seis campos). Los documentos creados se incluyen en el informe local.

## Privacidad y progreso

Los nombres, el progreso, los filtros y los JSON escritos se guardan en el almacenamiento local del navegador. No se envían a GitHub ni a ningún servidor de resultados, no se sincronizan entre dispositivos y pueden perderse si se borran los datos del navegador. Descarga el informe al finalizar.

## Publicación

El proyecto se publica desde `main` → `/(root)` mediante GitHub Pages. Cada actualización de `index.html` se publica automáticamente después de completar el despliegue. No requiere compilación ni dependencias externas.

## Autoría

Proyecto personal independiente.
