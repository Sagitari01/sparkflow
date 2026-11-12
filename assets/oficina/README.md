# Biblioteca de oficina · SparkFlow

Recursos gráficos separados para diseñar una oficina seria con estética pixel-art, sin colores neón predominantes. Los archivos **no se cargan automáticamente en el juego**: esta carpeta es un catálogo para escoger y componer la próxima interfaz sin modificar la lógica.

## Personajes
| Recurso | Uso |
|---|---|
| ![Coordinadora de pie](personajes/coordinadora-pie.png) | Personaje que presenta misiones |
| ![Retrato de coordinadora](personajes/coordinadora-retrato.png) | Cuadro de diálogo de misión |
| ![Operador de pie](personajes/operador-pie.png) | Personaje jugador / oficina |
| ![Retrato de operador](personajes/operador-retrato.png) | Perfil e instrucciones |

## Fondos
| Vista | Recurso |
|---|---|
| Oficina pixel-art diurna | ![Oficina diurna](fondos/oficina-dia.webp) |
| Oficina corporativa neutra | ![Oficina corporativa](fondos/oficina-corporativa.webp) |

## Mobiliario reutilizable
| Escritorio | Silla | Archivador |
|---|---|---|
| ![Escritorio](items/escritorio.webp) | ![Silla](items/silla.webp) | ![Archivador](items/archivador.webp) |

| Cafetera | Planta | Pizarra |
|---|---|---|
| ![Estación de café](items/cafe.webp) | ![Planta](items/planta.webp) | ![Pizarra](items/pizarra.webp) |

## Integración recomendada
- Mantener la zona central del SVG de circuitos y rutas por encima de cualquier fondo.
- Usar los retratos pequeños junto al objetivo y los personajes de pie como decoración lateral.
- No modificar los IDs del juego, el sistema de 13 misiones, las reglas de los routers ni el progreso.
- Los sprites PNG tienen transparencia; los fondos y objetos se entregan en WebP para reducir peso.

**Fecha del catálogo:** 2026-11-12.
