# -*- coding: utf-8 -*-
"""Pagina indice /sectores/: tarjetas de los 8 sectores, bloques comunes,
tabla sector x solucion, FAQ y datos estructurados (ItemList + FAQPage).
Lee los data_*.py, asi que un sector nuevo aparece solo al regenerar.
Uso: python3 tools/sectores/hub_build.py (tambien lo llama build_all.py)."""
import os, sys, json, importlib
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from sector_build import CSS, JS, SITE, SVC, UP, WA, ic, esc, head
from fuentes import faq_precio, faq_datos, faq_zona, AUD

URL = SITE + "/sectores/"
ORDER = ["estetica", "peluquerias", "academias", "inmobiliarias", "tiendas_ecommerce",
         "restaurantes", "gimnasios", "talleres"]
KP = "IA para negocios en Valladolid"
YOAST = {"keyphrase": KP, "title": "%s, por sectores | Verantia" % KP,
         "desc": "%s adaptada a tu sector: estética, peluquerías, academias, restaurantes, talleres y más. Auditoría gratuita." % KP}

# Una frase por sector para la tarjeta (el resto sale de su data_*.py)
BLURB = {
 "centros-de-estetica": "Citas por WhatsApp y teléfono, recordatorios de bonos y tratamientos, y más reseñas en Google.",
 "peluquerias": "Agenda llena sin soltar las tijeras: citas, recordatorios, avisos para volver y reseñas.",
 "academias": "Solicitudes de información atendidas al momento, matrículas, cobros y avisos a familias.",
 "inmobiliarias": "Compradores y propietarios atendidos y clasificados, visitas y documentación en orden.",
 "tiendas-ecommerce": "Dudas de clientes resueltas al momento, pedidos y stock automáticos y fichas de producto con IA.",
 "restaurantes": "Reservas por WhatsApp y teléfono, confirmaciones automáticas y más reseñas en Google.",
 "gimnasios": "Horarios y tarifas a cualquier hora, seguimiento de pruebas y avisos para que ningún socio se pierda.",
 "talleres-mecanicos": "Citas sin soltar la llave, avisos de coche listo, revisión e ITV y reseñas en Google.",
}

# Columnas de la tabla: (clave, titulo, enlace)
COLS = [("wa", "Asistente de WhatsApp y web", "chatbots-asistentes-virtuales"),
        ("tel", "Asistente telefónico", "chatbots-asistentes-virtuales"),
        ("automatizacion-de-procesos", "Automatización y avisos", "automatizacion-de-procesos"),
        ("resenas-automaticas-google", "Reseñas en Google", "resenas-automaticas-google"),
        ("clasificador-de-leads", "Clasificador de contactos", "clasificador-de-leads"),
        ("ia-generativa-contenido-visual", "Contenido con IA", "ia-generativa-contenido-visual")]

BASE = [("chat", "Asistente virtual para WhatsApp y la web", "chatbots-asistentes-virtuales",
         "Responde al momento, a cualquier hora, con tus precios, horarios y tono. Da cita, reserva o recoge el contacto."),
        ("phoneai", "Asistente telefónico con IA", "chatbots-asistentes-virtuales",
         "Atiende las llamadas que no puedes coger con una voz natural. Lo desarrollamos a medida y siempre avisa de que es automático."),
        ("bell", "Automatización de avisos y tareas", "automatizacion-de-procesos",
         "Recordatorios, confirmaciones, cobros, pedidos o renovaciones: lo que hoy haces a mano, funcionando solo."),
        ("star", "Reseñas y reputación en Google", "resenas-automaticas-google",
         "Un mensaje de agradecimiento con el enlace a tu ficha, a todos los clientes por igual y sin incentivos.")]

OTHERS = ["Clínicas dentales", "Fisioterapia", "Clínicas veterinarias", "Asesorías y gestorías",
          "Despachos de abogados", "Hoteles y casas rurales", "Autoescuelas", "Ópticas", "Tiendas de barrio"]

FAQ = [
 ("¿Con qué sectores trabaja Verantia?",
  "<p>Tenemos soluciones preparadas para centros de estética, peluquerías, academias, inmobiliarias, tiendas e-commerce, restaurantes, "
  "gimnasios y talleres mecánicos. Cada sector tiene su propia página con los servicios que mejor le funcionan.</p>"
  "<p>También trabajamos con otros negocios locales, como clínicas, asesorías u hoteles: las soluciones son las mismas y las adaptamos a tu forma de trabajar.</p>"),
 ("Mi sector no aparece en la lista, ¿podéis ayudarme?",
  "<p>Sí. Casi cualquier negocio que atiende clientes por WhatsApp o por teléfono, da citas o repite las mismas tareas cada semana puede aprovechar la inteligencia artificial.</p>"
  "<p>En la " + AUD + " vemos tu caso concreto y te decimos con sinceridad si merece la pena.</p>"),
 ("¿Por qué solución conviene empezar?",
  "<p>Depende de dónde se te va el tiempo. En negocios con mucha cita o reserva suele compensar antes el asistente de WhatsApp o los recordatorios automáticos; "
  "en los que venden por internet, la atención a dudas y la automatización de pedidos.</p>"
  "<p>No hace falta contratarlo todo: puedes empezar por una sola solución y ampliar cuando veas que funciona.</p>"),
 ("¿Qué diferencia hay entre el asistente virtual y el asistente telefónico?",
  "<p>El asistente virtual responde por escrito, en WhatsApp y en el chat de tu web. El asistente telefónico atiende llamadas con una voz natural cuando tú no puedes cogerlas.</p>"
  "<p>Los dos usan la misma información de tu negocio, y el telefónico avisa al empezar de que es un asistente automático, como exige la normativa europea de inteligencia artificial.</p>"),
 ("¿Tengo que cambiar los programas que ya uso?",
  "<p>Normalmente no. Conectamos la inteligencia artificial con tu agenda, tu tienda o tu programa de gestión cuando permiten integrarse. Si no, te proponemos la alternativa más sencilla.</p>"),
 faq_precio("mi negocio"),
 faq_datos("clientes"),
 faq_zona("negocios"),
]


def nw(t):  # evita que "e-commerce" se parta por el guion
    return t.replace("e-commerce", '<span class="vsx-nw">e-commerce</span>')


def load():
    out = []
    for m in ORDER:
        out.append(importlib.import_module("data_" + m).S)
    return out


def colors(c):
    return "--s:%s;--s-dark:%s;--s-light:%s;--s-soft:%s;--s-rgb:%s" % (c["s"], c["dark"], c["light"], c["soft"], c["rgb"])


HUB_CSS = r"""<style>
/* ---------- indice de sectores (complementa el CSS comun) ---------- */
.vsx-hub .vsx-mosaic{display:grid;grid-template-columns:1fr 1fr;gap:16px;position:relative}
.vsx-hub .vsx-mosaic a{position:relative;display:block;border-radius:20px;overflow:hidden;box-shadow:var(--sh-m);
  transition:transform .35s var(--ease),box-shadow .35s var(--ease)}
.vsx-hub .vsx-mosaic a:nth-child(2){transform:translateY(28px)}
.vsx-hub .vsx-mosaic a:nth-child(4){transform:translateY(28px)}
.vsx-hub .vsx-mosaic a:hover{box-shadow:var(--sh-l);z-index:1}
.vsx-hub .vsx-mosaic img{aspect-ratio:4/3;object-fit:cover;width:100%;transition:transform .6s var(--ease)}
.vsx-hub .vsx-mosaic a:hover img{transform:scale(1.05)}
.vsx-hub .vsx-mosaic span{position:absolute;left:10px;bottom:10px;display:inline-flex;align-items:center;gap:7px;
  padding:6px 12px 6px 6px;border-radius:999px;background:rgba(255,255,255,.94);font-family:'Manrope',sans-serif;
  font-size:12.5px;font-weight:700;color:var(--ink);box-shadow:var(--sh-s);white-space:nowrap}
.vsx-hub .vsx-mosaic span i{width:24px;height:24px;border-radius:50%;display:grid;place-items:center;color:#fff;
  background:linear-gradient(135deg,var(--s),var(--s-dark))}
.vsx-hub .vsx-mosaic span svg{width:13px;height:13px}
.vsx-hub .vsx-media::before{display:none}
.vsx-count{display:flex;flex-wrap:wrap;gap:28px;margin-top:34px;padding-top:26px;border-top:1px solid var(--border)}
.vsx-count div{font-size:14px;color:var(--muted);line-height:1.35}
.vsx-count b{display:block;font-family:'Manrope',sans-serif;font-size:28px;font-weight:800;letter-spacing:-.03em;color:var(--ink)}
/* tarjetas de sector */
.vsx-secs{display:grid;grid-template-columns:repeat(4,1fr);gap:22px}
.vsx-sc{position:relative;display:flex;flex-direction:column;background:#fff;border:1px solid var(--border);
  border-radius:var(--r-lg);overflow:hidden;box-shadow:var(--sh-s);
  transition:transform .32s var(--ease),box-shadow .32s var(--ease),border-color .32s}
.vsx-sc:hover{transform:translateY(-7px);box-shadow:var(--sh-l);border-color:var(--s-light)}
.vsx-sc-img{position:relative}
.vsx-sc-ph{position:relative;overflow:hidden}
.vsx-sc-ph img{aspect-ratio:3/2;object-fit:cover;width:100%;transition:transform .6s var(--ease)}
.vsx-sc:hover .vsx-sc-ph img{transform:scale(1.06)}
.vsx-sc-ph::after{content:'';position:absolute;inset:0;background:linear-gradient(180deg,transparent 45%,rgba(var(--s-rgb),.55))}
.vsx-sc-ico{position:absolute;z-index:1;left:18px;bottom:-22px;width:48px;height:48px;border-radius:14px;display:grid;
  place-items:center;color:#fff;background:linear-gradient(135deg,var(--s),var(--s-dark));
  box-shadow:0 10px 22px -10px rgba(var(--s-rgb),.9);border:3px solid #fff;transition:transform .3s var(--ease)}
.vsx-sc:hover .vsx-sc-ico{transform:rotate(-6deg) scale(1.06)}
.vsx-sc-ico svg{width:22px;height:22px}
.vsx-sc-body{display:flex;flex-direction:column;flex:1;padding:36px 22px 22px}
.vsx-sc h3{font-size:19px;margin:0 0 8px}
.vsx-sc h3 a::after{content:'';position:absolute;inset:0;z-index:2}
.vsx-sc p{font-size:14.5px;color:var(--muted);margin-bottom:16px}
.vsx-sc ul{display:grid;gap:7px;margin-bottom:18px}
.vsx-sc li{display:flex;gap:8px;font-size:13.5px;line-height:1.4;color:var(--ink)}
.vsx-sc li svg{width:16px;height:16px;flex:0 0 auto;color:var(--s);margin-top:1px}
.vsx-sc-more{margin-top:auto;display:inline-flex;align-items:center;gap:7px;font-family:'Manrope',sans-serif;
  font-size:14px;font-weight:700;color:var(--s-dark)}
.vsx-sc-more svg{width:15px;height:15px;transition:transform .25s var(--ease)}
.vsx-sc:hover .vsx-sc-more svg{transform:translateX(4px)}
/* bloques comunes */
.vsx-base{display:grid;grid-template-columns:repeat(4,1fr);gap:22px}
.vsx-base a{display:flex;flex-direction:column;background:#fff;border:1px solid var(--border);border-radius:var(--r);
  padding:28px 24px;box-shadow:var(--sh-s);transition:transform .28s var(--ease),box-shadow .28s,border-color .28s}
.vsx-base a:hover{transform:translateY(-5px);box-shadow:var(--sh-m);border-color:var(--s-light)}
.vsx-base i{width:50px;height:50px;border-radius:14px;display:grid;place-items:center;margin-bottom:18px;color:#fff;
  background:linear-gradient(135deg,var(--s),var(--s-dark));box-shadow:0 10px 22px -10px rgba(var(--s-rgb),.8)}
.vsx-base i svg{width:24px;height:24px}
.vsx-base h3{font-size:17.5px;margin:0 0 8px}
.vsx-base p{font-size:15px;color:var(--muted);margin-bottom:16px}
.vsx-base span{margin-top:auto;font-family:'Manrope',sans-serif;font-size:14px;font-weight:700;color:var(--s-dark)}
/* tabla sector x solucion */
.vsx-tbl-w{overflow-x:auto;border-radius:var(--r);border:1px solid rgba(255,255,255,.12);background:rgba(255,255,255,.04);
  -webkit-overflow-scrolling:touch}
.vsx-tbl{width:100%;border-collapse:collapse;min-width:760px;font-size:14.5px}
.vsx-tbl caption{caption-side:bottom;padding:14px 18px;text-align:left;font-size:13px;color:rgba(255,255,255,.55)}
.vsx-tbl th,.vsx-tbl td{padding:15px 14px;text-align:center;border-bottom:1px solid rgba(255,255,255,.08)}
.vsx-tbl thead th{font-family:'Manrope',sans-serif;font-size:12.5px;font-weight:700;letter-spacing:.02em;
  color:rgba(255,255,255,.75);vertical-align:bottom;line-height:1.3}
.vsx-tbl thead th a:hover{color:#fff;text-decoration:underline}
.vsx-tbl thead th:first-child{text-align:left;padding-left:22px}
.vsx-tbl tbody th{text-align:left;padding-left:22px;font-weight:600;color:#fff;white-space:nowrap}
.vsx-tbl tbody th a{display:inline-flex;align-items:center;gap:10px}
.vsx-tbl tbody th a:hover{text-decoration:underline;text-underline-offset:3px}
.vsx-tbl tbody th i{width:10px;height:10px;border-radius:50%;background:var(--c);box-shadow:0 0 0 4px rgba(255,255,255,.06)}
.vsx-tbl tbody tr{transition:background .2s}
.vsx-tbl tbody tr:hover{background:rgba(255,255,255,.05)}
.vsx-tbl tbody tr:last-child>*{border-bottom:0}
.vsx-y{display:inline-grid;place-items:center;width:26px;height:26px;border-radius:50%;background:rgba(var(--s-rgb),.6);color:#fff}
.vsx-y svg{width:15px;height:15px}
.vsx-n{color:rgba(255,255,255,.28)}
.vsx-tbl-hint{display:none;margin:0 0 12px;text-align:right;font-size:13px;color:rgba(255,255,255,.6)}
.vsx-dark .vsx-tbl-note{max-width:820px;margin:26px auto 0;text-align:center;font-size:15px;color:rgba(255,255,255,.7)}
/* otros sectores */
.vsx-other{display:grid;grid-template-columns:1.1fr .9fr;gap:48px;align-items:center;background:#fff;
  border:1px solid var(--border);border-radius:var(--r-lg);padding:48px;box-shadow:var(--sh-m)}
.vsx-other h2{font-size:clamp(26px,3.2vw,34px);margin:0 0 14px}
.vsx-other p{color:var(--muted)}
.vsx-other ul{display:flex;flex-wrap:wrap;gap:10px}
.vsx-other li{padding:9px 15px;border-radius:999px;background:var(--s-soft);border:1px solid var(--s-light);
  font-size:14px;font-weight:600;color:var(--s-dark)}
.vsx-nw{white-space:nowrap}
.vsx-other li:last-child{background:#fff;border-style:dashed}
@media (max-width:1080px){
  .vsx-secs,.vsx-base{grid-template-columns:repeat(2,1fr)}
  .vsx-other{grid-template-columns:1fr;gap:30px;padding:38px 30px}
  .vsx-hub .vsx-media{max-width:560px}
}
@media (max-width:860px){
  .vsx-tbl-hint{display:block}
  .vsx-tbl thead th:first-child,.vsx-tbl tbody th{position:sticky;left:0;z-index:1;background:#232323}
}
@media (max-width:560px){
  .vsx-secs,.vsx-base{grid-template-columns:1fr}
  .vsx-hub .vsx-mosaic{gap:10px}
  .vsx-hub .vsx-mosaic a:nth-child(2),.vsx-hub .vsx-mosaic a:nth-child(4){transform:translateY(16px)}
  .vsx-hub .vsx-mosaic span{font-size:11px;left:6px;bottom:6px;padding:4px 9px 4px 4px}
  .vsx-hub .vsx-mosaic span i{width:20px;height:20px}
  .vsx-count{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}
  .vsx-count div{font-size:12.5px}
  .vsx-count b{font-size:23px}
  .vsx-other{padding:30px 20px}
}
</style>
"""


def build():
    SS = load()
    hub_c = {"s": "#2563eb", "dark": "#1d4ed8", "light": "#bfdbfe", "soft": "#eff6ff", "rgb": "37,99,235"}
    o = []; w = o.append
    w('<!-- ==========================================================\n'
      '     VERANTIA - Pagina indice de sectores (/sectores/)\n'
      '     Pegar tal cual en un unico widget HTML de Elementor.\n'
      '     Ajustes de pagina en Elementor: Diseno de pagina =\n'
      '     "Elementor ancho completo", para que el tema no pinte un\n'
      '     segundo H1 con el titulo de la pagina.\n'
      '     Usa las fotos ya subidas de cada sector (no hay fotos nuevas).\n'
      '     ========================================================== -->\n')
    w(CSS); w(HUB_CSS)
    w('\n<div class="vsx vsx-hub" style="%s">\n\n' % colors(hub_c))

    # ---------- HERO ----------
    w('  <section class="vsx-hero" aria-labelledby="vsx-h1">\n')
    w('    <nav class="vsx-crumb" aria-label="Ruta de navegación"><ol><li><a href="%s/">Inicio</a></li>'
      '<li><span aria-current="page">Sectores</span></li></ol></nav>\n' % SITE)
    w('    <div class="vsx-hero-grid">\n      <div class="vsx-hero-copy">\n')
    w('        <p class="vsx-tag"><i>%s</i>Soluciones por sector</p>\n' % ic("grid"))
    w('        <h1 id="vsx-h1">Inteligencia artificial para <em>cada tipo de negocio</em></h1>\n')
    w('        <p class="vsx-lead">Cada negocio pierde el tiempo en sitios distintos: la peluquería, en el teléfono; la tienda e-commerce, '
      'en las mismas dudas; el taller, en los avisos. Somos especialistas en <strong>%s</strong> y en toda España, '
      'y adaptamos la IA a lo que de verdad necesita tu sector.</p>\n' % KP)
    w('        <div class="vsx-ctas">\n')
    w('          <a class="vsx-btn vsx-btn--p" href="#vsx-lista">Buscar mi sector %s</a>\n' % ic("arrow"))
    w('          <a class="vsx-btn vsx-btn--g" href="%s/contacto/">Solicitar auditoría gratuita</a>\n' % SITE)
    w('        </div>\n')
    w('        <div class="vsx-count"><div><b>%d</b>sectores con soluciones propias</div>'
      '<div><b>24/7</b>atención por WhatsApp, web y teléfono</div><div><b>0 €</b>la auditoría de procesos</div></div>\n' % len(SS))
    w('      </div>\n      <div class="vsx-media">\n        <div class="vsx-mosaic">\n')
    for S in [SS[i] for i in (0, 5, 7, 4)]:
        w('          <a href="%s%s/" style="%s"><img src="%s%s-800.webp" width="800" height="533" decoding="async" alt="%s">'
          '<span><i>%s</i>%s</span></a>\n' % (URL, S["slug"], colors(S["color"]), UP, S["img1"]["file"],
                                              S["img1"]["alt"], ic(S["icon"]), S["name"]))
    w('        </div>\n      </div>\n    </div>\n  </section>\n\n')

    # ---------- LISTA DE SECTORES ----------
    w('  <section class="vsx-sec vsx-sec--soft" id="vsx-lista" aria-labelledby="vsx-list-t">\n    <div class="vsx-wrap">\n      ')
    w(head("Elige tu sector", "Soluciones de IA pensadas para tu sector",
           "Cada página explica los problemas típicos del sector, las cuatro soluciones que mejor funcionan y datos públicos con su fuente.",
           "vsx-list-t") + '\n      <div class="vsx-secs">\n')
    for S in SS:
        w('        <article class="vsx-sc vsx-rv" style="%s">\n' % colors(S["color"]))
        w('          <div class="vsx-sc-img"><div class="vsx-sc-ph"><img src="%s%s-800.webp" width="800" height="533" loading="lazy" decoding="async" alt="%s"></div>'
          '<span class="vsx-sc-ico" aria-hidden="true">%s</span></div>\n' % (UP, S["img1"]["file"], S["img1"]["alt"], ic(S["icon"])))
        w('          <div class="vsx-sc-body">\n')
        w('            <h3><a href="%s%s/">IA para %s</a></h3>\n' % (URL, S["slug"], nw(S["name"].lower())))
        w('            <p>%s</p>\n            <ul>\n' % BLURB[S["slug"]])
        for c in S["hero"]["chips"]:
            w('              <li>%s%s</li>\n' % (ic("check"), c))
        w('            </ul>\n            <span class="vsx-sc-more" aria-hidden="true">Ver soluciones %s</span>\n' % ic("arrow"))
        w('          </div>\n        </article>\n')
    w('      </div>\n    </div>\n  </section>\n\n')

    # ---------- BLOQUES COMUNES ----------
    w('  <section class="vsx-sec" aria-labelledby="vsx-base-t">\n    <div class="vsx-wrap">\n      ')
    w(head("La base de todo", "Cuatro soluciones que funcionan en casi cualquier negocio",
           "Cambian los detalles de cada sector, pero la mayoría del tiempo perdido está en los mismos sitios: mensajes, llamadas, tareas repetidas y reputación.",
           "vsx-base-t") + '\n      <div class="vsx-base">\n')
    for icn, t, base, d in BASE:
        w('        <a class="vsx-rv" href="%s%s/"><i>%s</i><h3>%s</h3><p>%s</p><span>Ver servicio →</span></a>\n'
          % (SVC, base, ic(icn), t, d))
    w('      </div>\n    </div>\n  </section>\n\n')

    # ---------- TABLA SECTOR x SOLUCION ----------
    w('  <section class="vsx-dark" aria-labelledby="vsx-tbl-t">\n    <div class="vsx-wrap">\n      ')
    w(head("De un vistazo", "Qué solución de IA encaja en cada sector",
           "Las cuatro soluciones más populares en cada página de sector. Todas se pueden combinar y adaptar a tu caso.",
           "vsx-tbl-t") + '\n')
    w('      <p class="vsx-tbl-hint" aria-hidden="true">Desliza para ver todas las soluciones →</p>\n')
    w('      <div class="vsx-tbl-w vsx-rv">\n        <table class="vsx-tbl">\n')
    w('          <caption>✓ = una de las 4 soluciones más populares del sector. El resto también se puede aplicar si tu negocio lo necesita.</caption>\n')
    w('          <thead><tr><th scope="col">Sector</th>')
    for _, t, base in COLS:
        w('<th scope="col"><a href="%s%s/">%s</a></th>' % (SVC, base, t))
    w('</tr></thead>\n          <tbody>\n')
    for S in SS:
        bases = [it["base"] for it in S["services"]["items"]]
        have = {"wa": True, "tel": True}
        for b in bases:
            have[b] = True
        w('            <tr><th scope="row"><a href="%s%s/"><i style="--c:%s" aria-hidden="true"></i>%s</a></th>'
          % (URL, S["slug"], S["color"]["s"], S["name"]))
        for k, t, _ in COLS:
            if have.get(k):
                w('<td><span class="vsx-y" role="img" aria-label="Sí">%s</span></td>' % ic("check"))
            else:
                w('<td><span class="vsx-n" role="img" aria-label="No incluida">–</span></td>')
        w('</tr>\n')
    w('          </tbody>\n        </table>\n      </div>\n')
    w('      <p class="vsx-tbl-note vsx-rv">Los asistentes de WhatsApp, web y teléfono aparecen en todos los sectores porque '
      'atender a tiempo es el problema más repetido en cualquier negocio local.</p>\n')
    w('    </div>\n  </section>\n\n')

    # ---------- OTROS SECTORES ----------
    w('  <section class="vsx-sec" aria-labelledby="vsx-other-t">\n    <div class="vsx-wrap">\n')
    w('      <div class="vsx-other vsx-rv">\n        <div>\n')
    w('          <p class="vsx-eyebrow">¿No encuentras el tuyo?</p>\n')
    w('          <h2 id="vsx-other-t">Trabajamos con cualquier negocio que atienda clientes</h2>\n')
    w('          <p>Si tu negocio da citas, recibe mensajes y llamadas o repite las mismas tareas cada semana, la IA te puede ayudar '
      'aunque tu sector no tenga página propia. Lo vemos juntos en una auditoría gratuita.</p>\n')
    w('          <div class="vsx-ctas"><a class="vsx-btn vsx-btn--p" href="%s/contacto/">Cuéntanos tu caso %s</a></div>\n' % (SITE, ic("arrow")))
    w('        </div>\n        <ul aria-label="Otros negocios con los que trabajamos">\n')
    for x in OTHERS:
        w('          <li>%s</li>\n' % x)
    w('          <li>Y muchos más</li>\n        </ul>\n      </div>\n    </div>\n  </section>\n\n')

    # ---------- PASOS ----------
    w('  <section class="vsx-sec vsx-sec--soft" aria-labelledby="vsx-steps-t">\n    <div class="vsx-wrap">\n      ')
    w(head("Cómo empezamos", "Tres pasos, sea cual sea tu sector", None, "vsx-steps-t") + '\n      <div class="vsx-steps">\n')
    for t, txt in [("Auditoría gratuita", "Revisamos cómo trabajas hoy y en qué se te va el tiempo, y te decimos qué merece la pena automatizar. <strong>Sin coste y sin compromiso.</strong>"),
                   ("Lo adaptamos a tu negocio", "Configuramos la solución con tus servicios, precios, horarios y forma de hablar, y la conectamos con las herramientas que ya usas."),
                   ("Lo activamos y te acompañamos", "Te enseñamos a usarlo con tu propio día a día y seguimos ajustándolo contigo siempre que lo necesites.")]:
        w('        <div class="vsx-step vsx-rv"><h3>%s</h3><p>%s</p></div>\n' % (t, txt))
    w('      </div>\n    </div>\n  </section>\n\n')

    # ---------- FAQ ----------
    w('  <section class="vsx-sec" aria-labelledby="vsx-faq-t">\n    <div class="vsx-wrap">\n      ')
    w(head("Preguntas frecuentes", "Preguntas frecuentes sobre %s" % KP,
           "Respuestas claras, sin tecnicismos. Si te falta alguna, escríbenos.", "vsx-faq-t") + '\n      <div class="vsx-faq">\n')
    for q, a in FAQ:
        w('        <details class="vsx-rv"><summary><h3>%s</h3><i aria-hidden="true">%s</i></summary><div class="a">%s</div></details>\n'
          % (q, ic("plus"), a))
    w('      </div>\n    </div>\n  </section>\n\n')

    # ---------- CTA ----------
    w('  <section class="vsx-sec" style="padding-top:0" aria-labelledby="vsx-cta-t">\n    <div class="vsx-cta vsx-rv" '
      'style="background:linear-gradient(135deg,#1d4ed8,#0b1b4d 120%)">\n')
    w('      <h2 id="vsx-cta-t">Dedica tu tiempo a tus clientes, no a tareas repetidas</h2>\n')
    w('      <p>Empezamos con una auditoría gratuita de tu negocio: vemos cómo trabajas hoy y te decimos qué merece la pena automatizar. '
      'Si no te compensa, te lo diremos igual.</p>\n      <div class="vsx-ctas">\n')
    w('        <a class="vsx-btn vsx-btn--w" href="%s/contacto/">Solicitar auditoría gratuita %s</a>\n' % (SITE, ic("arrow")))
    w('        <a class="vsx-btn vsx-btn--o" href="https://wa.me/34601855347" target="_blank" rel="noopener">%s WhatsApp 601 85 53 47</a>\n' % WA)
    w('      </div>\n      <small>O llámanos al <a href="tel:+34983618315">983 61 83 15</a> · '
      '<a href="mailto:info@verantiapro.es">info@verantiapro.es</a></small>\n    </div>\n')
    w('    <div class="vsx-wrap" style="margin-top:70px">\n      ')
    w(head("Sigue explorando", "Más de Verantia", None, "vsx-rel-t") + '\n      <div class="vsx-rel vsx-rv">\n')
    for icn, href, txt in [("layers", SITE + "/servicios/", "Todos los servicios"),
                           ("clip", SVC + "auditoria-de-procesos/", "Auditoría de procesos gratuita"),
                           ("mail", SITE + "/contacto/", "Contacto")]:
        w('        <a href="%s"><i>%s</i><span>%s</span></a>\n' % (href, ic(icn), txt))
    w('      </div>\n    </div>\n  </section>\n\n')

    # ---------- JSON-LD ----------
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "ItemList", "@id": URL + "#sectores", "name": "Inteligencia artificial por sectores",
         "description": YOAST["desc"], "numberOfItems": len(SS), "itemListOrder": "https://schema.org/ItemListUnordered",
         "itemListElement": [{"@type": "ListItem", "position": i, "name": "IA para " + S["name"].lower(),
                              "url": URL + S["slug"] + "/"} for i, S in enumerate(SS, 1)]},
        {"@type": "FAQPage", "@id": URL + "#faq", "inLanguage": "es", "isPartOf": {"@id": URL},
         "mainEntity": [{"@type": "Question", "name": esc(a),
                         "acceptedAnswer": {"@type": "Answer", "text": esc(b)}} for a, b in FAQ]}]}
    w('  <script type="application/ld+json">\n%s\n  </script>\n\n' % json.dumps(ld, ensure_ascii=False, indent=2))
    w('</div>\n\n')
    w(JS)
    return "".join(o)


def main():
    path = os.path.join(HERE, "..", "..", "elementor", "sectores-widget-html.html")
    open(path, "w", encoding="utf-8").write(build())
    print("  %-28s %6d bytes" % ("sectores (indice)", os.path.getsize(path)))

if __name__ == "__main__":
    main()
