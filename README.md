# ⚡ SparkFlow — Juego de lógica, rutas y condiciones

**SparkFlow** es un juego educativo interactivo de **13 misiones progresivas** para aprender a interpretar datos JSON, configurar condiciones y observar cómo un dato atraviesa las rutas de un router, igual que en un orquestador como Make. Está diseñado para aprender experimentando, sin conocimientos previos de programación y sin instalar aplicaciones.

**Jugar online:** https://sagitari01.github.io/sparkflow/

## Objetivo del juego

Ordenar el flujo de solicitudes de una oficina. Cada misión muestra uno o varios documentos JSON (las solicitudes) con datos diferentes. Las rutas ya están conectadas: la tarea del jugador es **seleccionar cada ruta que sale del router y definir la condición que decidirá si la solicitud pasa o queda retenida**.

Se practican las comparaciones `>`, `<`, `>=`, `<=`, `==` y `!=`, las condiciones combinadas **AND (Y)** y **OR (O)**, la comparación exacta de texto (respetando mayúsculas y minúsculas), los valores booleanos `true` y `false`, la evaluación de varias rutas en paralelo y la **escritura manual de JSON**.

### Datos que traen las solicitudes

| Campo | Tipo | Qué representa |
|---|---|---|
| `monto` | número | Monto de la solicitud |
| `prioridad` | número | Prioridad de atención |
| `area` | texto | Área a la que pertenece (`"ventas"`, `"soporte"`) |
| `aprobado` | booleano | Si la solicitud está aprobada |
| `completo` | booleano | Si la documentación está completa |
| `urgente` | booleano | Si está marcada como urgente |
| `copia` | booleano | Si se pide copia para Archivo |

### Las 13 misiones

| N.º | Misión | Nivel | Qué se practica |
|---|---|---|---|
| 1 | Primer día en la oficina | Inicial | Comparación numérica: mayor o igual que |
| 2 | Dos áreas, dos bandejas | Inicial | Comparar textos y rutas excluyentes |
| 3 | Una solicitud, dos destinos | Inicial | Un router puede ejecutar dos salidas a la vez |
| 4 | La mesa de prioridades | Inicial | Límites y rangos sin solapamientos |
| 5 | La doble firma | Intermedio | AND: dos condiciones verdaderas a la vez |
| 6 | Original y copia | Intermedio | Filtros de rutas independientes |
| 7 | Cuatro bandejas de atención | Avanzado | AND y OR en cuatro rutas paralelas |
| 8 | Cuatro revisiones independientes | Avanzado | Combinar AND y OR y distinguir umbrales |
| 9 | Cuatro vistos buenos | Avanzado | Cuatro rutas y una firma final que exige todas |
| 10 | El circuito de Gerencia | Final | Dos routers en cascada y cinco rutas |
| 11 | Redacta la solicitud | Creación de JSON | Escribir claves, valores y tipos correctos |
| 12 | JSON de decisiones | Creación de JSON | Leer filtros compuestos ya instalados |
| 13 | El JSON maestro | Desafío final | Diseñar un JSON para un objetivo complejo |

En las misiones **1 a 10** se configuran los filtros de cada ruta. En las misiones **11, 12 y 13** los filtros ya están instalados y bloqueados: el desafío es **escribir desde cero el JSON** que active solo los destinos pedidos. Esas respuestas se validan por el comportamiento del circuito, no por coincidir con un único JSON; si varias combinaciones cumplen el objetivo, todas son válidas.

En las misiones 9 y 10 varios revisores deben dar su visto bueno para que la «Firma final» deje pasar la solicitud a Gerencia. Esa firma es una **mecánica pedagógica del juego**: no representa una unión automática de rutas en Make u otras herramientas.

## Opción A — Jugar desde internet

1. Abre https://sagitari01.github.io/sparkflow/ desde un navegador moderno (Chrome, Edge, Firefox o Safari).
2. Indica si jugarás **individualmente** o **en grupo** y escribe los nombres de los participantes.
3. Lee el objetivo y los resultados esperados para cada JSON de la misión.
4. **Selecciona una ruta** pulsando su botón o su línea en la pizarra. Al entrar ninguna ruta está preseleccionada.
5. En el editor elige el dato del JSON, el operador y escribe el valor; añade otra condición y elige AND u OR cuando corresponda.
6. En las misiones **11, 12 y 13** no se editan filtros: léelos en el panel derecho y escribe el objeto JSON solicitado. La comprobación valida llaves, comillas dobles, claves, valores, tipos (`number`, `boolean`, `string`) y que la entrada active los destinos correctos. Un JSON inválido detiene la simulación y muestra un error explicativo.
7. Ejecuta la simulación, observa el recorrido de **cada JSON** y revisa la respuesta de cada ruta. Corrige hasta activar solo los destinos solicitados.
8. Completa misiones para desbloquear las siguientes. Al terminar, descarga o imprime tu informe con nombres, misiones y resultados.

En celulares, utiliza las pestañas **Circuito**, **Filtros** y **JSON**. En pantallas pequeñas, desplaza el circuito horizontalmente para explorar todas las rutas.

## Opción B — Descargar y jugar sin conexión desde tu computador

1. Desde la página web del juego, baja hasta el pie de página y pulsa **«descarga el archivo index.html»**. También puedes abrir el repositorio y descargar el archivo `index.html` de la rama `main`.
2. Guarda el archivo como **`index.html`**, por ejemplo en una carpeta nueva llamada `SparkFlow` en tu Escritorio o Documentos.
3. Haz doble clic en **`index.html`**. Se abrirá en tu navegador predeterminado. Si no se abre, haz clic derecho → **Abrir con** → Chrome, Edge, Firefox o Safari.
4. Completa el registro inicial y juega normalmente. No hace falta usar terminal, instalar Node.js, tener una cuenta de GitHub ni ejecutar un servidor.
5. Al finalizar, pulsa **Descargar reporte cifrado** o **Vista previa / imprimir**; puedes guardar una copia en PDF desde el diálogo de impresión del navegador.

**Importante:** debes abrir el archivo `.html` en un navegador, **no** en un editor de texto. El archivo contiene HTML, CSS, JavaScript, las imágenes y las fuentes, por lo que no necesita otros archivos ni conexión a internet para funcionar.

## Progreso y privacidad

- El progreso y los nombres se guardan en el **almacenamiento local del navegador** (`localStorage`) del dispositivo donde juegas.
- **No** se envían los nombres ni las respuestas a GitHub: GitHub Pages solamente entrega el archivo estático.
- No hay cuentas, ranking online, servidor de resultados ni sincronización automática entre dispositivos.
- Si cambias de navegador, computadora, perfil o borras los datos del sitio, puedes perder el progreso. **Descarga tu informe** al terminar.
- La versión online y el archivo local pueden guardar progresos separados, porque utilizan orígenes distintos.
- El progreso guardado con la temática anterior (central energética) se conserva: al abrir esta versión, los nombres de campo antiguos se convierten solos a los nuevos.

## Diseño y recursos gráficos

La interfaz usa una estética de oficina de día con personajes pixel-art. Los recursos están en `assets/`:

- `assets/oficina/` — fondos, mobiliario y personajes (catálogo en `assets/oficina/README.md`).
- `assets/oficina/personajes/animacion/` — tiras de caminata (4 cuadros) y celebración (2 cuadros) de cada personaje, con sus originales y los scripts que las procesan y verifican.
- `assets/fuentes/` — Fredoka y Pixelify Sans (licencia SIL Open Font License).

Como el juego se distribuye en un solo archivo, las imágenes y fuentes van **incrustadas** dentro de `index.html`, en el bloque marcado `sparkflow-assets`. Ese bloque no se edita a mano: si cambias una imagen, vuelve a generarlo con

```bash
python3 scripts/incrustar-assets.py
```

Los estilos del tema están en el bloque `<style id="sparkflow-oficina">` de `index.html`.

## Publicación y actualización

El proyecto utiliza GitHub Pages desde la rama `main` y la carpeta `/(root)`. El archivo `index.html` es la página de entrada. Para publicar cambios, actualiza `index.html` en `main` y comprueba el despliegue en la pestaña **Actions** del repositorio.

## Licencia y autoría

Proyecto personal independiente. No está asociado ni patrocinado por una institución educativa. No se declara una licencia de reutilización del código en este README.
