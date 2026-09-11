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
index.html            Página única (hero, cómo funciona, servicios,
                       integraciones, CTA, contacto, footer)
assets/css/style.css   Estilos
assets/js/script.js    Menú móvil, scroll reveal, botón "volver arriba"
                       y validación básica del formulario de contacto
```

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
