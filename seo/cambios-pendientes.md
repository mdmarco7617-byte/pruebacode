# Verantia — todos los cambios de SEO pendientes, de una vez

Estado comprobado en vivo el 23/09/2026.

## Ya hecho, no lo toques

- Titulo del sitio = `Verantia`
- Las 10 entradas de relleno en latin, borradas
- Las 3 categorias de la plantilla, borradas
- Archivos de autor, desactivados
- Un solo H1 en 9 de las 10 paginas
- Los 8 enlaces de /servicios/ apuntan bien
- La foto del hero se sirve en WebP

---

## 1. Yoast: las 10 paginas

En cada pagina: **Paginas > Editar** (no Elementor) > recuadro de Yoast.
Orden de los campos: frase clave, titulo SEO, meta descripcion.

### Inicio — `/`

**Frase clave**
```
automatización e IA para pymes
```
**Titulo SEO** (55)
```
Automatización e IA para pymes en Valladolid | Verantia
```
**Meta descripcion** (141)
```
Automatización e IA para pymes y negocios locales. Agencia de Valladolid: chatbots, procesos y apps a medida. Auditoría de procesos gratuita.
```

### Servicios — `/servicios/`

**Frase clave**
```
servicios de IA y automatización
```
**Titulo SEO** (54)
```
Servicios de IA y automatización para pymes | Verantia
```
**Meta descripcion** (137)
```
Servicios de IA y automatización para pymes de Valladolid: chatbots, procesos, aplicaciones a medida e IA generativa. Auditoría gratuita.
```

### Chatbots — `/servicios/chatbots-asistentes-virtuales/`

**Frase clave**
```
chatbots y asistentes virtuales
```
**Titulo SEO** (58)
```
Chatbots y asistentes virtuales 24/7 | Verantia Valladolid
```
**Meta descripcion** (137)
```
Chatbots y asistentes virtuales que atienden tu web y tu WhatsApp a cualquier hora, resuelven dudas y agendan citas. Pymes de Valladolid.
```

### Automatización — `/servicios/automatizacion-de-procesos/`

**Frase clave**
```
automatización de procesos
```
**Titulo SEO** (51)
```
Automatización de procesos en Valladolid | Verantia
```
**Meta descripcion** (136)
```
Automatización de procesos para pymes de Valladolid: conectamos las herramientas que ya usas para que los datos dejen de moverse a mano.
```

### Aplicaciones — `/servicios/aplicaciones-personalizadas/`

**Frase clave**
```
aplicaciones personalizadas
```
**Titulo SEO** (52)
```
Aplicaciones personalizadas en Valladolid | Verantia
```
**Meta descripcion** (139)
```
Aplicaciones personalizadas para tu negocio cuando ninguna herramienta del mercado encaja. Software a medida en Valladolid, precio de pyme.
```

### IA Generativa — `/servicios/ia-generativa-contenido-visual/`

**Frase clave**
```
IA generativa
```
**Titulo SEO** (54)
```
IA generativa y contenido visual | Verantia Valladolid
```
**Meta descripcion** (136)
```
IA generativa para tu marca: textos, imágenes y fichas de producto con tu tono y tu estilo. Para pymes y negocios locales de Valladolid.
```

### Clasificador — `/servicios/clasificador-de-leads/`

**Frase clave**
```
clasificador de leads
```
**Titulo SEO** (50)
```
Clasificador de leads con IA | Verantia Valladolid
```
**Meta descripcion** (137)
```
Clasificador de leads con IA: ordena y prioriza los contactos que entran para que dediques tu tiempo a los que van a comprar. Valladolid.
```

### Reseñas — `/servicios/resenas-automaticas-google/`

**Frase clave**
```
reseñas automáticas en Google
```
**Titulo SEO** (51)
```
Reseñas automáticas en Google | Verantia Valladolid
```
**Meta descripcion** (143)
```
Reseñas automáticas en Google pedidas en el momento adecuado y respetando sus normas, para reforzar la ficha local de tu negocio en Valladolid.
```

### Auditoría — `/servicios/auditoria-de-procesos/`

**Frase clave**
```
auditoría de procesos
```
**Titulo SEO** (55)
```
Auditoría de procesos gratuita en Valladolid | Verantia
```
**Meta descripcion** (135)
```
Auditoría de procesos gratuita: medimos qué tareas repetitivas te cuestan tiempo y dinero y qué merece la pena automatizar. Valladolid.
```

### Contacto — `/contacto/`

**Frase clave**
```
(dejar vacía)
```
**Titulo SEO** (54)
```
Contacto | Verantia, automatización e IA en Valladolid
```
**Meta descripcion** (133)
```
Escríbenos por WhatsApp, llámanos o usa el formulario. Auditoría de procesos gratuita y sin compromiso para pymes y negocios locales.
```

---

## 2. Pagina de contacto

- Anadir un H1: es la unica pagina que sigue sin ninguno.
  Texto sugerido: **Contacta con Verantia**
- Corregir tres erratas visibles:
  - `¡Llamanos!` -> `¡Llamanos!` con tilde: **¡Llámanos!**
  - `¡Escribenos!` -> **¡Escribenos!** con tilde: **¡Escríbenos!**
  - `Valladolid- sin oficina fisica,nuestro` -> **Valladolid: sin oficina fisica, nuestro**

## 3. La pagina /novedades/

Sigue publicada y es la portada del blog, ahora vacia porque se borraron
las entradas de relleno. Decide una de las dos:

- Vas a escribir blog: dejala, pero ponla en noindex mientras este vacia
  (Yoast, dentro de la pagina, pestana Avanzado, "Permitir que los
  buscadores muestren esta pagina" = No).
- No vas a escribir blog: borrala y quitala del menu.

## 4. Al terminar

- LiteSpeed Cache > Purge All
- Google Search Console: dar de alta el sitio y enviar sitemap_index.xml
- Google Business Profile: crear la ficha como negocio de area de servicio
