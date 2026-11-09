# ⚡ SparkFlow — Juego de lógica y rutas de automatización

**SparkFlow** es un juego educativo interactivo de **10 misiones progresivas** para aprender a interpretar datos JSON, configurar condiciones y observar cómo un flujo de información atraviesa diferentes rutas. Está diseñado para aprender experimentando, sin conocimientos previos de programación y sin instalar aplicaciones.

**Jugar online:** https://sagitari01.github.io/sparkflow/

## Objetivo del juego

Restaurar una central energética configurando correctamente los filtros de sus circuitos. Cada misión muestra uno o varios documentos JSON con datos diferentes. Las rutas ya están conectadas: la tarea del jugador es **seleccionar cada ruta y definir la condición que decidirá si la energía pasa o se bloquea**.

Se practican las comparaciones `>`, `<`, `>=`, `<=`, `==` y `!=`, las condiciones combinadas **AND (Y)** y **OR (O)**, la comparación exacta de texto (respetando mayúsculas/minúsculas), los valores booleanos `true` y `false` y la evaluación de múltiples rutas en paralelo y la **escritura manual de JSON**. En las misiones **4, 8 y 10**, el participante debe crear un objeto JSON desde cero, sin una plantilla precompletada.

El juego tiene diez misiones; las **misiones 7, 8 y 9 incluyen cuatro rutas configurables** y la **misión 10 incluye cinco rutas finales más un filtro de entrada**. En algunas misiones los destinos actúan como generadores que necesitan activarse simultáneamente para abrir una compuerta. Esa compuerta es una **mecánica pedagógica del juego**: no representa una unión automática de rutas en Make u otras herramientas.

## Opción A — Jugar desde internet

1. Abre https://sagitari01.github.io/sparkflow/ desde un navegador moderno (Chrome, Edge, Firefox o Safari).
2. Indica si jugarás **individualmente** o **en grupo** y escribe los nombres de los participantes.
3. Lee el objetivo y los resultados esperados para cada JSON de la misión.
4. **Selecciona una ruta** pulsando el botón correspondiente o su línea del circuito. Al entrar no hay rutas preseleccionadas ni condiciones rellenadas.
5. En el editor, elige el dato del JSON, el operador y escribe el valor; añade otra condición y elige AND u OR cuando corresponda.
6. En las misiones **4, 8 y 10**, abre el panel JSON y escribe el objeto solicitado desde cero. La comprobación valida llaves, comillas dobles, claves, valores, tipos (`number`, `boolean`, `string`) y que la entrada active los destinos correctos. Un JSON inválido detiene la simulación y muestra un error explicativo.
7. Ejecuta la simulación, observa el recorrido de **cada JSON** y revisa la respuesta de cada ruta. Ajusta los filtros si fallan las pruebas.
8. Completa misiones para desbloquear las siguientes. Al terminar, descarga o imprime tu informe con nombres, misiones, resultados y los JSON escritos en los desafíos.

En celulares, utiliza las pestañas **Circuito**, **Filtros** y **JSON**. En pantallas pequeñas, desplaza el circuito horizontalmente para explorar todas las rutas.

## Opción B — Descargar y jugar sin conexión desde tu computador

1. Desde la página web del juego, baja hasta el pie de página y pulsa **«descarga el archivo index.html»**. También puedes abrir el repositorio y descargar el archivo `index.html` de la rama `main`.
2. Guarda el archivo como **`index.html`**, por ejemplo en una carpeta nueva llamada `SparkFlow` en tu Escritorio o Documentos.
3. Busca el archivo con el Explorador de archivos (Windows) o Finder (macOS).
4. Haz doble clic en **`index.html`**. Se abrirá en tu navegador predeterminado. Si no se abre, haz clic derecho → **Abrir con** → Chrome, Edge, Firefox o Safari.
5. Completa el registro inicial y juega normalmente. No hace falta usar terminal, instalar Node.js, tener una cuenta de GitHub ni ejecutar un servidor.
6. Al finalizar, pulsa **Descargar informe** o **Imprimir informe**; puedes guardar una copia en PDF desde el diálogo de impresión del navegador.

**Importante:** debes abrir el archivo `.html` en un navegador, **no** en un editor de texto. El archivo contiene HTML, CSS y JavaScript, por lo que no necesita otros archivos ni conexión a internet para funcionar.

## Progreso y privacidad

- El progreso y los nombres se guardan en el **almacenamiento local del navegador** (`localStorage`) del dispositivo donde juegas.
- **No** se envían los nombres ni las respuestas a GitHub: GitHub Pages solamente entrega el archivo estático.
- No hay cuentas, ranking online, servidor de resultados ni sincronización automática entre dispositivos.
- Si cambias de navegador, computadora, perfil o borras los datos del sitio, puedes perder el progreso. **Descarga tu informe** al terminar.
- La versión online y el archivo local pueden guardar progresos separados, porque utilizan orígenes distintos.

## Publicación y actualización

El proyecto utiliza GitHub Pages desde la rama `main` y la carpeta `/(root)`. El archivo `index.html` es la página de entrada. Para publicar cambios, reemplaza `index.html` en `main` y comprueba el despliegue en la pestaña **Actions** del repositorio.

## Licencia y autoría

Proyecto personal independiente. No está asociado ni patrocinado por una institución educativa. No se declara una licencia de reutilización del código en este README.