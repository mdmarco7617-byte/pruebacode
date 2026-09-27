# -*- coding: utf-8 -*-
"""Pagina /servicios/: los 7 servicios, auditoria destacada, buscador por
necesidad, por que Verantia, FAQ y datos estructurados
(ItemList de Service + FAQPage). Mismo sistema visual que /sectores/.
Uso: python3 tools/sectores/servicios_build.py (tambien lo llama build_all.py)."""
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import sector_build
from sector_build import CSS, JS, SITE, SVC, WA, ic, esc, head
from hub_build import HUB_CSS, colors
from fuentes import faq_datos, faq_zona, AUD

sector_build.I.update({
 "headset": '<path d="M3 18v-6a9 9 0 0 1 18 0v6"/><path d="M21 19a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2h3zM3 19a2 2 0 0 0 2 2h1a2 2 0 0 0 2-2v-3a2 2 0 0 0-2-2H3z"/>',
 "pin": '<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/>',
 "search": '<circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/>',
})

URL = SITE + "/servicios/"
KP = "servicios de IA y automatización"
YOAST = {"keyphrase": KP, "title": "Servicios de IA y automatización para pymes | Verantia",
         "desc": "Servicios de IA y automatización para pymes de Valladolid: chatbots, procesos, aplicaciones a medida e IA generativa. Auditoría gratuita."}

def pal(s, d, l, so, rgb):
    return {"s": s, "dark": d, "light": l, "soft": so, "rgb": rgb}

# slug, color, icono, categoria, titulo, descripcion, 3 ventajas
SERVICES = [
 ("chatbots-asistentes-virtuales", pal("#3b82f6", "#1d4ed8", "#bfdbfe", "#eff6ff", "59,130,246"), "chat", "Atención al cliente",
  "Chatbots y asistentes virtuales 24/7",
  "Atienden a tus clientes en tu web y en WhatsApp a cualquier hora: responden preguntas, dan cita y recogen los datos de contacto, sin descansos ni festivos.",
  ["Respuestas al momento, con tus precios y horarios", "Citas y reservas directamente en tu agenda", "Asistente telefónico con IA, desarrollado a medida"]),
 ("automatizacion-de-procesos", pal("#f59e0b", "#b45309", "#fde68a", "#fffbeb", "245,158,11"), "zap", "Procesos",
  "Automatización de procesos",
  "Facturas, pedidos, recordatorios y tareas administrativas que hoy haces a mano, funcionando solas. Ahorras tiempo y dinero, y ganas eficacia.",
  ["Conectamos las herramientas que ya usas", "Recordatorios y avisos automáticos a clientes", "Menos errores al pasar datos de un sitio a otro"]),
 ("aplicaciones-personalizadas", pal("#8b5cf6", "#6d28d9", "#ddd6fe", "#f5f3ff", "139,92,246"), "app", "Software a medida",
  "Aplicaciones personalizadas",
  "¿Necesitas controlar tu inventario u otra gestión concreta sin pagar un software genérico? Creamos una aplicación a medida, solo con lo que tu negocio necesita.",
  ["Sin pagar por funciones que no usas", "Pensada para tu forma de trabajar", "Fácil de usar para todo tu equipo"]),
 ("ia-generativa-contenido-visual", pal("#06b6d4", "#0e7490", "#a5f3fc", "#ecfeff", "6,182,212"), "sparkle", "Marketing y contenido",
  "IA generativa para contenido visual",
  "Mejoramos y creamos imágenes y vídeos con IA para que tu negocio destaque, con el tono y el estilo de tu marca.",
  ["Fotos de producto más atractivas", "Contenido para redes listo para publicar", "Vídeos cortos que dan vida a tu web"]),
 ("clasificador-de-leads", pal("#10b981", "#047857", "#a7f3d0", "#ecfdf5", "16,185,129"), "funnel", "Ventas",
  "Clasificador inteligente de leads",
  "¿Te llegan contactos pero no sabes a cuáles dedicar tiempo primero? Clasificamos automáticamente cada consulta según su interés real y su urgencia.",
  ["Todos los contactos en un solo sitio", "Ordenados por interés y urgencia", "Aviso inmediato de los más importantes"]),
 ("resenas-automaticas-google", pal("#14b8a6", "#0f766e", "#99f6e4", "#f0fdfa", "20,184,166"), "star", "Reputación",
  "Reseñas automáticas en Google",
  "Cuando terminas una cita, entregas un pedido o completas un servicio, tu cliente recibe el enlace para dejarte una reseña en Google, sin que tengas que acordarte.",
  ["Se envía en el mejor momento", "A todos tus clientes por igual, como exige Google", "Sin incentivos que pongan en riesgo tu ficha"]),
]
AUDIT = ("auditoria-de-procesos", "Auditoría de procesos gratuita",
         "Analizamos tu negocio de arriba a abajo y te decimos, sin compromiso y sin coste, dónde estás perdiendo tiempo o dinero y qué tareas se pueden automatizar.",
         ["Sin coste y sin compromiso", "Te decimos qué merece la pena y qué no", "Sales con una horquilla de precio realista"])

# "Si te pasa esto" -> servicio
NEEDS = [
 ("Pierdo clientes porque no llego a contestar mensajes y llamadas", 0),
 ("Paso horas haciendo facturas, pasando datos o enviando avisos a mano", 1),
 ("Ningún programa del mercado se adapta a cómo trabajo", 2),
 ("No tengo tiempo para crear fotos y contenido para redes", 3),
 ("Me llegan muchos contactos y no sé a cuáles atender primero", 4),
 ("Mis clientes salen contentos, pero casi nadie me deja reseñas", 5),
 ("No sé por dónde empezar", None),
]

VALUES = [
 ("headset", "Hablas con una persona", "Respondemos tus dudas por email, WhatsApp o llamada en menos de 24 horas laborables. Nunca con un contestador automático."),
 ("layers", "Hecho a tu medida", "Nada de plantillas genéricas: cada solución se configura con tus servicios, tus precios y tu forma de hablar."),
 ("shield", "Tus datos, protegidos", "Trabajamos sobre tus propias herramientas y firmamos contigo el contrato de encargado de tratamiento que exige el RGPD."),
 ("euro", "Presupuestos para pymes", "Precios pensados para pymes y negocios locales, no para grandes empresas. Pagas solo por lo que tu negocio necesita."),
]

FAQ = [
 ("¿Qué servicios de IA y automatización ofrece Verantia?",
  "<p>Chatbots y asistentes virtuales para la web, WhatsApp y el teléfono, automatización de procesos, aplicaciones personalizadas, "
  "IA generativa para contenido visual, clasificación inteligente de leads y reseñas automáticas en Google.</p>"
  "<p>Además, hacemos una auditoría de procesos gratuita para decidir contigo por dónde empezar.</p>"),
 ("¿Necesito conocimientos técnicos?",
  "<p>No. Nosotros nos encargamos de toda la parte técnica: configurar, conectar y mantener. Tú solo nos cuentas cómo trabajas.</p>"
  "<p>Cuando está listo, te enseñamos a usarlo con tu propio día a día, y seguimos disponibles para cualquier duda.</p>"),
 ("¿Puedo contratar un solo servicio?",
  "<p>Sí. Puedes empezar por una sola solución, la que más te vaya a ahorrar, y ampliar después si ves que funciona. No tienes que contratarlo todo.</p>"),
 ("¿Funciona con las herramientas que ya uso?",
  "<p>En la mayoría de los casos, sí: agendas, tiendas online, programas de facturación, CRM o WhatsApp. Si una herramienta permite conectarse con otras, "
  "lo integramos directamente. Si no, te proponemos la alternativa más sencilla.</p><p>Lo comprobamos en la " + AUD + ", antes de que decidas nada.</p>"),
 ("¿Cuánto cuestan los servicios?",
  "<p>Depende de lo que necesites: un sistema de avisos automáticos no tiene nada que ver con una aplicación a medida.</p>"
  "<p>Por eso empezamos con una <strong>auditoría gratuita y sin compromiso</strong>: sales de ella con una horquilla de precio realista y ajustada al tamaño de tu negocio.</p>"),
 ("¿Qué incluye la auditoría gratuita?",
  "<p>Revisamos cómo trabajas hoy, qué tareas se repiten y dónde se te va el tiempo. Después te explicamos qué merece la pena automatizar, qué no, y cuánto costaría.</p>"
  "<p>No tiene coste ni compromiso: si no te compensa, te lo diremos igual.</p>"),
 faq_datos("clientes"),
 faq_zona("negocios"),
]

SVP_CSS = r"""<style>
/* ---------- pagina de servicios (complementa el CSS comun y el del indice) ---------- */
.vsx-svp .vsx-hero .vsx-hub-h1{font-size:clamp(36px,5.6vw,66px)!important;max-width:1000px;text-wrap:balance}
.vsp-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}
.vsp-card{position:relative;display:flex;flex-direction:column;background:#fff;border:1px solid var(--border);
  border-radius:var(--r-lg);padding:32px 28px 28px;box-shadow:var(--sh-s);overflow:hidden;
  transition:transform .3s var(--ease),box-shadow .3s var(--ease),border-color .3s}
.vsp-card::before{content:'';position:absolute;left:0;right:0;top:0;height:4px;background:linear-gradient(90deg,var(--s-dark),var(--s),var(--s-light))}
.vsp-card::after{content:'';position:absolute;right:-60px;top:-60px;width:180px;height:180px;border-radius:50%;
  background:radial-gradient(circle,rgba(var(--s-rgb),.12),transparent 70%);transition:transform .5s var(--ease)}
.vsp-card:hover{transform:translateY(-7px);box-shadow:var(--sh-l);border-color:var(--s-light)}
.vsp-card:hover::after{transform:scale(1.4)}
.vsp-top{display:flex;align-items:center;justify-content:space-between;margin-bottom:20px}
.vsp-ico{width:56px;height:56px;border-radius:16px;display:grid;place-items:center;color:#fff;
  background:linear-gradient(135deg,var(--s),var(--s-dark));box-shadow:0 12px 24px -12px rgba(var(--s-rgb),.9);
  transition:transform .3s var(--ease)}
.vsp-card:hover .vsp-ico{transform:rotate(-6deg) scale(1.06)}
.vsp-ico svg{width:27px;height:27px}
.vsp-cat{font-family:'Manrope',sans-serif;font-size:11.5px;font-weight:800;letter-spacing:.1em;text-transform:uppercase;
  padding:6px 11px;border-radius:999px;background:var(--s-soft);color:var(--s-dark)}
.vsp-card h3{font-size:21px;margin:0 0 10px;line-height:1.25}
.vsp-card h3 a::after{content:'';position:absolute;inset:0;z-index:1}
.vsp-card>p{font-size:15.5px;color:var(--muted);margin-bottom:18px}
.vsp-card ul{display:grid;gap:9px;margin-bottom:22px}
.vsp-card li{display:flex;gap:9px;font-size:14.5px;line-height:1.45;color:var(--ink)}
.vsp-card li svg{width:17px;height:17px;flex:0 0 auto;margin-top:2px;color:var(--s)}
.vsp-more{margin-top:auto;display:inline-flex;align-items:center;gap:7px;font-family:'Manrope',sans-serif;
  font-size:14.5px;font-weight:700;color:var(--s-dark)}
.vsp-more svg{width:15px;height:15px;transition:transform .25s var(--ease)}
.vsp-card:hover .vsp-more svg{transform:translateX(4px)}
/* auditoria destacada */
.vsp-audit{position:relative;isolation:isolate;overflow:hidden;margin-top:28px;border-radius:var(--r-lg);padding:46px 48px;color:#fff;
  display:grid;grid-template-columns:auto 1fr auto;gap:36px;align-items:center;
  background:linear-gradient(125deg,#0b2a6f 0%,#1d4ed8 60%,#3b82f6 100%);box-shadow:0 30px 60px -30px rgba(29,78,216,.7)}
.vsp-audit::before{content:'';position:absolute;inset:0;z-index:-1;
  background:radial-gradient(420px 260px at 90% 0%,rgba(255,255,255,.2),transparent 70%),
             radial-gradient(360px 240px at 0% 100%,rgba(96,165,250,.35),transparent 70%)}
.vsp-audit .vsp-ico{width:72px;height:72px;border-radius:20px;background:rgba(255,255,255,.14);border:1px solid rgba(255,255,255,.25);box-shadow:none}
.vsp-audit .vsp-ico svg{width:34px;height:34px}
.vsp-badge{display:inline-block;margin-bottom:10px;padding:5px 12px;border-radius:999px;background:#fff;color:#1d4ed8;
  font-family:'Manrope',sans-serif;font-size:11.5px;font-weight:800;letter-spacing:.1em;text-transform:uppercase}
.vsp-audit h3{color:#fff;font-size:clamp(23px,2.6vw,30px);margin:0 0 10px}
.vsp-audit p{color:rgba(255,255,255,.85);font-size:16px;max-width:620px}
.vsp-audit ul{display:flex;flex-wrap:wrap;gap:8px 20px;margin-top:16px}
.vsp-audit li{display:flex;align-items:center;gap:7px;font-size:14.5px;font-weight:600}
.vsp-audit li svg{width:16px;height:16px;color:#93c5fd}
.vsp-audit-ctas{display:grid;gap:12px}
.vsp-audit-ctas a{white-space:nowrap}
.vsp-link-w{display:inline-flex;align-items:center;justify-content:center;gap:7px;font-family:'Manrope',sans-serif;font-size:14.5px;
  font-weight:700;color:#fff;text-decoration:underline;text-underline-offset:4px}
/* buscador por necesidad */
.vsp-needs{max-width:900px;margin:0 auto;display:grid;gap:12px}
.vsp-need{display:grid;grid-template-columns:1fr auto;gap:18px;align-items:center;padding:18px 22px;border-radius:16px;background:#fff;
  border:1px solid var(--border);box-shadow:var(--sh-s);transition:transform .25s var(--ease),box-shadow .25s,border-color .25s}
.vsp-need:hover{transform:translateX(6px);box-shadow:var(--sh-m);border-color:var(--s-light)}
.vsp-need q{quotes:'«' '»';font-size:16px;color:var(--ink);font-weight:500}
.vsp-need span{display:inline-flex;align-items:center;gap:8px;padding:8px 14px;border-radius:999px;background:var(--s-soft);
  font-family:'Manrope',sans-serif;font-size:13.5px;font-weight:700;color:var(--s-dark);white-space:nowrap}
.vsp-need span i{width:22px;height:22px;border-radius:50%;display:grid;place-items:center;color:#fff;
  background:linear-gradient(135deg,var(--s),var(--s-dark))}
.vsp-need span svg{width:12px;height:12px}
/* por que Verantia */
.vsp-vals{display:grid;grid-template-columns:repeat(4,1fr);gap:22px}
.vsp-val{padding:28px 24px;border-radius:var(--r);background:#fff;border:1px solid var(--border);box-shadow:var(--sh-s);
  transition:transform .28s var(--ease),box-shadow .28s}
.vsp-val:hover{transform:translateY(-5px);box-shadow:var(--sh-m)}
.vsp-val i{width:50px;height:50px;border-radius:14px;display:grid;place-items:center;margin-bottom:18px;color:#fff;background:var(--g)}
.vsp-val i svg{width:24px;height:24px}
.vsp-val h3{font-size:18px;margin:0 0 8px}
.vsp-val p{font-size:15px;color:var(--muted)}
@media (max-width:1080px){
  .vsp-grid{grid-template-columns:repeat(2,1fr)}
  .vsp-audit{grid-template-columns:1fr;gap:24px;padding:40px 32px}
  .vsp-audit-ctas{grid-auto-flow:column;justify-content:start}
  .vsp-vals{grid-template-columns:repeat(2,1fr)}
}
@media (max-width:640px){
  .vsp-grid,.vsp-vals{grid-template-columns:1fr}
  .vsp-need{grid-template-columns:1fr;gap:12px}
  .vsp-need span{justify-self:start}
  .vsp-audit{padding:32px 22px}
  .vsp-audit .vsp-ico{display:none}
  .vsp-audit-ctas{grid-auto-flow:row}
  .vsp-audit-ctas a{white-space:normal}
}
</style>
"""


def build():
    hub_c = {"s": "#2563eb", "dark": "#1d4ed8", "light": "#bfdbfe", "soft": "#eff6ff", "rgb": "37,99,235"}
    o = []; w = o.append
    w('<!-- ==========================================================\n'
      '     VERANTIA - Pagina de servicios (/servicios/)\n'
      '     Pegar tal cual en un unico widget HTML de Elementor.\n'
      '     Ajustes de pagina en Elementor: Diseno de pagina =\n'
      '     "Elementor ancho completo", para que el tema no pinte un\n'
      '     segundo H1 con el titulo de la pagina.\n'
      '     Sin fotos nuevas: usa solo iconos.\n'
      '     ========================================================== -->\n')
    w(CSS); w(HUB_CSS); w(SVP_CSS)
    w('\n<div class="vsx vsx-hub vsx-svp" style="%s">\n\n' % colors(hub_c))

    # ---------- HERO ----------
    w('  <section class="vsx-hero" aria-labelledby="vsx-h1">\n')
    w('    <nav class="vsx-crumb" aria-label="Ruta de navegación"><ol><li><a href="%s/">Inicio</a></li>'
      '<li><span aria-current="page">Servicios</span></li></ol></nav>\n' % SITE)
    w('    <h1 id="vsx-h1" class="vsx-hub-h1">Servicios de IA y automatización para pymes</h1>\n')
    w('    <div class="vsx-hub-intro">\n      <div class="vsx-hero-copy">\n')
    w('        <p class="vsx-lead">Nuestros <strong>%s</strong> ayudan a pymes y negocios locales de Valladolid y de toda España '
      'a ahorrar tiempo, reducir costes y atender mejor a sus clientes. Soluciones a medida, sin tecnicismos y con una persona '
      'de verdad al otro lado.</p>\n' % KP)
    w('        <div class="vsx-ctas">\n')
    w('          <a class="vsx-btn vsx-btn--p" href="#vsx-lista">Ver servicios %s</a>\n' % ic("arrow"))
    w('          <a class="vsx-btn vsx-btn--g" href="%s/contacto/">Solicitar auditoría gratuita</a>\n' % SITE)
    w('        </div>\n')
    w('        <div class="vsx-count"><div><b>%d</b>servicios a medida</div>'
      '<div><b>0 €</b>la auditoría de procesos</div><div><b>24 h</b>máximo para responderte (días laborables)</div></div>\n' % (len(SERVICES) + 1))
    w('      </div>\n    </div>\n  </section>\n\n')

    # ---------- SERVICIOS ----------
    w('  <section class="vsx-sec vsx-sec--soft" id="vsx-lista" aria-labelledby="vsx-list-t">\n    <div class="vsx-wrap">\n      ')
    w(head("Qué hacemos", "Soluciones para trabajar menos y vender más", None, "vsx-list-t") + '\n      <div class="vsp-grid">\n')
    for slug, c, icn, cat, t, d, bl in SERVICES:
        w('        <article class="vsp-card vsx-rv" style="%s">\n' % colors(c))
        w('          <div class="vsp-top"><span class="vsp-ico" aria-hidden="true">%s</span><span class="vsp-cat">%s</span></div>\n' % (ic(icn), cat))
        w('          <h3><a href="%s%s/">%s</a></h3>\n          <p>%s</p>\n          <ul>\n' % (SVC, slug, t, d))
        for b in bl:
            w('            <li>%s%s</li>\n' % (ic("checkc"), b))
        w('          </ul>\n          <span class="vsp-more" aria-hidden="true">Ver servicio %s</span>\n        </article>\n' % ic("arrow"))
    w('      </div>\n')
    slug, t, d, bl = AUDIT
    w('      <div class="vsp-audit vsx-rv">\n')
    w('        <span class="vsp-ico" aria-hidden="true">%s</span>\n        <div>\n' % ic("clip"))
    w('          <span class="vsp-badge">Empieza aquí · Gratis</span>\n')
    w('          <h3>%s</h3>\n          <p>%s</p>\n          <ul>\n' % (t, d))
    for b in bl:
        w('            <li>%s%s</li>\n' % (ic("check"), b))
    w('          </ul>\n        </div>\n        <div class="vsp-audit-ctas">\n')
    w('          <a class="vsx-btn vsx-btn--w" href="%s/contacto/">Solicitar auditoría %s</a>\n' % (SITE, ic("arrow")))
    w('          <a class="vsp-link-w" href="%s%s/">Cómo funciona la auditoría</a>\n' % (SVC, slug))
    w('        </div>\n      </div>\n    </div>\n  </section>\n\n')

    # ---------- BUSCADOR POR NECESIDAD ----------
    w('  <section class="vsx-sec" aria-labelledby="vsx-need-t">\n    <div class="vsx-wrap">\n      ')
    w(head("¿Qué necesitas?", "Encuentra tu servicio según lo que te pasa", None, "vsx-need-t") + '\n      <div class="vsp-needs">\n')
    audit_c = pal("#2563eb", "#1d4ed8", "#bfdbfe", "#eff6ff", "37,99,235")
    for txt, idx in NEEDS:
        if idx is None:
            href, c, icn, name = SVC + AUDIT[0] + "/", audit_c, "clip", "Auditoría gratuita"
        else:
            s = SERVICES[idx]; href, c, icn, name = SVC + s[0] + "/", s[1], s[2], s[4]
        w('        <a class="vsp-need vsx-rv" href="%s" style="%s"><q>%s</q><span><i aria-hidden="true">%s</i>%s</span></a>\n'
          % (href, colors(c), txt, ic(icn), name))
    w('      </div>\n    </div>\n  </section>\n\n')

    # ---------- POR QUE VERANTIA ----------
    w('  <section class="vsx-sec vsx-sec--soft" aria-labelledby="vsx-val-t">\n    <div class="vsx-wrap">\n      ')
    w(head("Por qué Verantia", "Tecnología a medida, trato de tú a tú", None, "vsx-val-t") + '\n      <div class="vsp-vals">\n')
    for icn, t, d in VALUES:
        w('        <div class="vsp-val vsx-rv"><i aria-hidden="true">%s</i><h3>%s</h3><p>%s</p></div>\n' % (ic(icn), t, d))
    w('      </div>\n    </div>\n  </section>\n\n')

    # ---------- FAQ ----------
    w('  <section class="vsx-sec" aria-labelledby="vsx-faq-t">\n    <div class="vsx-wrap">\n      ')
    w(head("Preguntas frecuentes", "Preguntas frecuentes sobre nuestros %s" % KP,
           "Respuestas claras, sin tecnicismos. Si te falta alguna, escríbenos.", "vsx-faq-t") + '\n      <div class="vsx-faq">\n')
    for q, a in FAQ:
        w('        <details class="vsx-rv"><summary><h3>%s</h3><i aria-hidden="true">%s</i></summary><div class="a">%s</div></details>\n'
          % (q, ic("plus"), a))
    w('      </div>\n    </div>\n  </section>\n\n')

    # ---------- CTA ----------
    w('  <section class="vsx-sec" aria-labelledby="vsx-cta-t">\n    <div class="vsx-cta vsx-rv">\n')
    w('      <h2 id="vsx-cta-t">¿Hablamos de tu negocio?</h2>\n')
    w('      <p>Empezamos con una auditoría gratuita: vemos cómo trabajas hoy y te decimos qué merece la pena automatizar. '
      'Si no te compensa, te lo diremos igual.</p>\n      <div class="vsx-ctas">\n')
    w('        <a class="vsx-btn vsx-btn--w" href="%s/contacto/">Solicitar auditoría gratuita %s</a>\n' % (SITE, ic("arrow")))
    w('        <a class="vsx-btn vsx-btn--o" href="https://wa.me/34601855347" target="_blank" rel="noopener">%s WhatsApp 601 85 53 47</a>\n' % WA)
    w('      </div>\n      <small>O llámanos al <a href="tel:+34983618315">983 61 83 15</a> · '
      '<a href="mailto:info@verantiapro.es">info@verantiapro.es</a></small>\n    </div>\n  </section>\n\n')

    # ---------- JSON-LD ----------
    area = [{"@type": "City", "name": "Valladolid"}, {"@type": "Country", "name": "España"}]
    items = [(SVC + s[0] + "/", s[4], s[5]) for s in SERVICES] + [(SVC + AUDIT[0] + "/", AUDIT[1], AUDIT[2])]
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "ItemList", "@id": URL + "#servicios", "name": "Servicios de IA y automatización de Verantia",
         "numberOfItems": len(items), "itemListOrder": "https://schema.org/ItemListUnordered",
         "itemListElement": [{"@type": "ListItem", "position": i, "item": {
             "@type": "Service", "name": n, "url": u, "description": esc(d),
             "provider": {"@id": SITE + "/#organization"}, "areaServed": area}}
             for i, (u, n, d) in enumerate(items, 1)]},
        {"@type": "FAQPage", "@id": URL + "#faq", "inLanguage": "es", "isPartOf": {"@id": URL},
         "mainEntity": [{"@type": "Question", "name": esc(a),
                         "acceptedAnswer": {"@type": "Answer", "text": esc(b)}} for a, b in FAQ]}]}
    w('  <script type="application/ld+json">\n%s\n  </script>\n\n' % json.dumps(ld, ensure_ascii=False, indent=2))
    w('</div>\n\n')
    w(JS)
    return "".join(o)


def main():
    path = os.path.join(HERE, "..", "..", "elementor", "servicios-widget-html.html")
    open(path, "w", encoding="utf-8").write(build())
    print("  %-28s %6d bytes" % ("servicios (pagina)", os.path.getsize(path)))

if __name__ == "__main__":
    main()
