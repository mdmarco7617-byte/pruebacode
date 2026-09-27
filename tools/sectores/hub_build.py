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
.vsx-hub-intro{max-width:800px;margin:0 auto;text-align:center}
.vsx-hub-intro .vsx-lead{max-width:none}
.vsx-hub-intro .vsx-ctas{justify-content:center}
.vsx-hub-intro .vsx-count{justify-content:center}
.vsx-count{display:grid;grid-template-columns:repeat(3,auto);justify-content:start;gap:36px;margin-top:34px;padding-top:26px;border-top:1px solid var(--border)}
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
/* azul Verantia en degradado (solo elementos generales, no las tarjetas de sector) */
.vsx-hub{--g:linear-gradient(120deg,#0b2a6f 0%,#1d4ed8 50%,#60a5fa 100%);
  --g-soft:linear-gradient(135deg,#e6efff,#f5f9ff)}
.vsx-hub .vsx-hero .vsx-hub-h1{max-width:var(--max);margin:0 auto 64px;text-align:center;font-size:clamp(44px,7.4vw,86px)!important;
  line-height:1.02!important;letter-spacing:-.035em!important;font-weight:800!important;padding-bottom:.06em;
  background:var(--g);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;color:transparent;
  animation:vsxUp .8s var(--ease) both}
.vsx-hub .vsx-hub-h2{font-size:clamp(28px,3.4vw,40px);margin:0 0 20px;text-wrap:balance}
.vsx-hub .vsx-hub-h2 em{font-style:normal;background:var(--g);-webkit-background-clip:text;background-clip:text;
  -webkit-text-fill-color:transparent;color:transparent}
.vsx-hub .vsx-btn--p{background:var(--g);background-size:140% 100%;background-position:0 0;
  box-shadow:0 12px 26px -12px rgba(29,78,216,.75);transition:transform .25s var(--ease),box-shadow .25s var(--ease),background-position .4s var(--ease)}
.vsx-hub .vsx-btn--p:hover{background-position:100% 0}
.vsx-hub .vsx-eyebrow{color:#1d4ed8}
.vsx-hub .vsx-eyebrow::before{background:var(--g)}
.vsx-count b{background:var(--g);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;color:transparent}
.vsx-hub .vsx-sec--soft{background:var(--g-soft)}
.vsx-hub .vsx-step::before{background:var(--g);-webkit-background-clip:text;background-clip:text}
.vsx-hub .vsx-faq summary i{background:var(--g-soft);color:#1d4ed8}
.vsx-hub .vsx-faq details[open] summary i{background:var(--g);color:#fff}
.vsx-hub .vsx-faq details:hover,.vsx-hub .vsx-faq details[open]{border-color:#bfdbfe}
.vsx-hub .vsx-rel i{background:var(--g);color:#fff}
.vsx-hub .vsx-rel a::after{color:#1d4ed8}
.vsx-hub .vsx-crumb a:hover{color:#1d4ed8}
.vsx-hub .vsx-cta{background:linear-gradient(125deg,#0b2a6f 0%,#1d4ed8 55%,#3b82f6 100%)!important}
/* otros sectores */
.vsx-other{display:grid;grid-template-columns:1.1fr .9fr;gap:48px;align-items:center;background:#fff;
  border:1px solid var(--border);border-radius:var(--r-lg);padding:48px;box-shadow:var(--sh-m)}
.vsx-other h2{font-size:clamp(26px,3.2vw,34px);margin:0 0 14px}
.vsx-other p{color:var(--muted)}
.vsx-other ul{display:flex;flex-wrap:wrap;gap:10px}
.vsx-other li{padding:9px 15px;border-radius:999px;background:var(--g-soft);border:1px solid #bfdbfe;
  font-size:14px;font-weight:600;color:#1d4ed8}
.vsx-nw{white-space:nowrap}
.vsx-other li:last-child{background:#fff;border-style:dashed}
@media (max-width:1080px){
  .vsx-secs{grid-template-columns:repeat(2,1fr)}
  .vsx-other{grid-template-columns:1fr;gap:30px;padding:38px 30px}
  .vsx-hub .vsx-hero .vsx-hub-h1{margin-bottom:44px}
}
@media (max-width:560px){
  .vsx-secs{grid-template-columns:1fr}
  .vsx-count{grid-template-columns:repeat(3,1fr);gap:12px}
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
    w('    <h1 id="vsx-h1" class="vsx-hub-h1">Soluciones por sector</h1>\n')
    w('    <div class="vsx-hub-intro">\n      <div class="vsx-hero-copy">\n')
    w('        <h2 class="vsx-hub-h2">Inteligencia artificial para <em>cada tipo de negocio</em></h2>\n')
    w('        <p class="vsx-lead">Cada tipo de negocio tiene sus propias características y necesidades: no se atiende igual a los clientes '
      'de una peluquería que a los de un taller o una tienda e-commerce. Somos especialistas en <strong>%s</strong> y en toda España, '
      'y adaptamos cada solución a tu sector para que ahorres tiempo, reduzcas costes y hagas crecer tu negocio.</p>\n' % KP)
    w('        <div class="vsx-ctas">\n')
    w('          <a class="vsx-btn vsx-btn--p" href="#vsx-lista">Buscar mi sector %s</a>\n' % ic("arrow"))
    w('          <a class="vsx-btn vsx-btn--g" href="%s/contacto/">Solicitar auditoría gratuita</a>\n' % SITE)
    w('        </div>\n')
    w('        <div class="vsx-count"><div><b>%d</b>sectores con soluciones propias</div>'
      '<div><b>24/7</b>atención por WhatsApp, web y teléfono</div><div><b>0 €</b>la auditoría de procesos</div></div>\n' % len(SS))
    w('      </div>\n    </div>\n  </section>\n\n')

    # ---------- LISTA DE SECTORES ----------
    w('  <section class="vsx-sec vsx-sec--soft" id="vsx-lista" aria-labelledby="vsx-list-t">\n    <div class="vsx-wrap">\n      ')
    w(head("Elige tu sector", "Encuentra la solución para tu negocio", None, "vsx-list-t") + '\n      <div class="vsx-secs">\n')
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
    w('  <section class="vsx-sec" style="padding-top:0" aria-labelledby="vsx-cta-t">\n    <div class="vsx-cta vsx-rv">\n')
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
