# Verantia — Landing page

Landing page estática (HTML + CSS + JS, sin dependencias ni build) para
**Verantia**, negocio de automatización e inteligencia artificial para
pymes en Valladolid.

Está pensada como reemplazo ligero y moderno de la home actual en
WordPress/Elementor de [verantiapro.es](https://verantiapro.es/),
conservando su contenido y su identidad de marca (colores azul/negro,
tipografías DM Sans y Manrope).

## Estructura

```
index.html                     Home (hero, cómo funciona, servicios,
                                integraciones, CTA, contacto, footer)
servicios/index.html           Hub con las 6 páginas de servicio
servicios/asistentes-virtuales.html
servicios/gestion-de-citas.html
servicios/automatizacion-de-procesos.html
servicios/aplicaciones-personalizadas.html
servicios/analisis-y-reporting.html
servicios/integracion-de-herramientas.html

assets/css/style.css            Estilos base (home)
assets/css/services.css         Estilos de las páginas de servicio
                                 (hero, problema/solución, estadísticas,
                                 FAQ, enlaces cruzados)
assets/js/script.js             Menú móvil, scroll reveal, botón "volver
                                 arriba" y validación básica del
                                 formulario de contacto
```

### Páginas de servicio

Cada página de servicio sigue la misma estructura, pensada para generar
interés y venta: problema → solución → beneficios → estadísticas del
sector (con su fuente) → para quién es → cómo lo implementamos → FAQ →
CTA final → enlaces a los demás servicios. Las estadísticas citadas son
datos de estudios reales del sector (McKinsey, Aurora Inbox, Software
Advice, etc.), no cifras inventadas ni resultados propios de Verantia.

Se generaron con un script (no versionado) que combina una plantilla
HTML con el contenido de cada servicio, para mantener consistencia
visual entre las seis páginas.

## Ver la página en local

No requiere instalación. Basta con abrir `index.html` en el navegador,
o servirlo con cualquier servidor estático, por ejemplo:

```bash
python3 -m http.server 8000
# luego visita http://localhost:8000
```

## Pendiente de conectar

- **Formulario de contacto**: actualmente es solo interfaz (no envía
  datos a ningún sitio). Hay que conectarlo a un backend, a un servicio
  de formularios o a un webhook propio para recibir los mensajes.
- **Teléfono**: se ha unificado a `+34 601 85 53 47` (el número usado en
  WhatsApp y en el pie de página del sitio original), ya que el CTA de
  cabecera del sitio original mostraba un número distinto.
