# -*- coding: utf-8 -*-
"""Generador de paginas de sector de Verantia.
build(S) recibe el diccionario de un sector y devuelve el HTML completo
para pegar en un unico widget HTML de Elementor: CSS acotado bajo .vsx,
marcado, datos estructurados y JS en linea (reveal + contadores)."""
import json, html as H
from sector_css import CSS

SITE = "https://verantiapro.es"
ORG_ID = SITE + "/#organization"
SVC = SITE + "/servicios/"
UP = SITE + "/wp-content/uploads/2026/09/"

SC = 'fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"'
def ic(name):
    return '<svg viewBox="0 0 24 24" %s aria-hidden="true">%s</svg>' % (SC, I[name])

I = {
 "arrow":  '<path d="M5 12h14"/><path d="m12 5 7 7-7 7"/>',
 "check":  '<path d="M20 6 9 17l-5-5"/>',
 "checkc": '<circle cx="12" cy="12" r="9"/><path d="m8.5 12 2.5 2.5 4.5-5"/>',
 "plus":   '<path d="M12 5v14"/><path d="M5 12h14"/>',
 "chat":   '<path d="M21 11.5a8.4 8.4 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.4 8.4 0 0 1-3.8-.9L3 21l1.9-5.7a8.4 8.4 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.4 8.4 0 0 1 3.8-.9h.5a8.5 8.5 0 0 1 8 8z"/>',
 "calx":   '<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/><path d="m10 14 4 4M14 14l-4 4"/>',
 "calok":  '<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/><path d="m9 16 2 2 4-4"/>',
 "bell":   '<path d="M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9"/><path d="M10.3 21a1.9 1.9 0 0 0 3.4 0"/>',
 "star":   '<path d="m12 3 2.7 5.5 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.8 1-6.1L3.2 9.4l6.1-.9z"/>',
 "camera": '<path d="M14.5 4h-5L7 7H4a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2h-3z"/><circle cx="12" cy="13" r="3.5"/>',
 "sparkle":'<path d="M12 3v3M12 18v3M5 12H3M21 12h-2M7 7l1.4 1.4M15.6 15.6 17 17M17 7l-1.4 1.4M8.4 15.6 7 17"/><circle cx="12" cy="12" r="3.2"/>',
 "flower": '<circle cx="12" cy="12" r="3"/><path d="M12 16.5A4.5 4.5 0 1 1 7.5 12 4.5 4.5 0 1 1 12 7.5a4.5 4.5 0 1 1 4.5 4.5 4.5 4.5 0 1 1-4.5 4.5"/><path d="M12 7.5V9M7.5 12H9M16.5 12H15M12 16.5V15"/>',
 "grid":   '<rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><rect x="14" y="14" width="7" height="7" rx="1.5"/>',
 "layers": '<path d="m12 2 10 5-10 5L2 7z"/><path d="m2 17 10 5 10-5"/><path d="m2 12 10 5 10-5"/>',
 "send":   '<path d="m22 2-7 20-4-9-9-4z"/><path d="M22 2 11 13"/>',
 "clip":   '<path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><rect width="8" height="4" x="8" y="2" rx="1"/><path d="m9 13 2 2 4-4"/>',
 "funnel": '<path d="M3 4h18l-7 8v7l-4 2v-9z"/>',
 "app":    '<rect width="18" height="16" x="3" y="4" rx="2"/><path d="M3 9h18"/>',
 "zap":    '<path d="M13 2 3 14h9l-1 8 10-12h-9z"/>',
 "users":  '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.9M16 3.1a4 4 0 0 1 0 7.8"/>',
 "home":   '<path d="m3 10 9-7 9 7v10a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z"/>',
 "cart":   '<circle cx="9" cy="20" r="1.5"/><circle cx="18" cy="20" r="1.5"/><path d="M2 3h3l2.7 12.4a2 2 0 0 0 2 1.6h8.6a2 2 0 0 0 2-1.5L22 7H6"/>',
 "chef":   '<path d="M6 14a4 4 0 1 1 1.6-7.7A5 5 0 0 1 17 6.4 4 4 0 1 1 18 14"/><path d="M6 14v6h12v-6"/><path d="M6 17h12"/>',
 "book":   '<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20V3H6.5A2.5 2.5 0 0 0 4 5.5z"/><path d="M4 19.5A2.5 2.5 0 0 0 6.5 22H20v-5"/>',
 "scissors":'<circle cx="6" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><path d="M20 4 8.1 15.9M14.5 14.5 20 20M8.1 8.1 12 12"/>',
 "dumbbell":'<path d="M6.5 6.5v11M17.5 6.5v11M3 9v6M21 9v6M6.5 12h11"/>',
 "wrench": '<path d="M14.7 6.3a4 4 0 0 0-5.4 5.4L3 18l3 3 6.3-6.3a4 4 0 0 0 5.4-5.4l-2.5 2.5-2.4-.6-.6-2.4z"/>',
 "clock":  '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 "euro":   '<path d="M18 7a7.5 7.5 0 1 0 0 10"/><path d="M3 10h9M3 14h9"/>',
 "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/>',
 "doc":    '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M8 13h8M8 17h5"/>',
 "phone":  '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/>',
 "phoneai":'<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/><path d="M15 2.5a6.5 6.5 0 0 1 6.5 6.5M15 6a3 3 0 0 1 3 3"/>',
 "mail":   '<rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-9 5.7a2 2 0 0 1-2 0L2 7"/>',
 "trend":  '<path d="m22 7-8.5 8.5-5-5L2 17"/><path d="M16 7h6v6"/>',
 "tag":    '<path d="M20.6 13.4 13.4 20.6a2 2 0 0 1-2.8 0L2 12V2h10l8.6 8.6a2 2 0 0 1 0 2.8z"/><circle cx="7" cy="7" r="1.5"/>',
 "box":    '<path d="M21 8 12 3 3 8v8l9 5 9-5z"/><path d="m3 8 9 5 9-5M12 13v8"/>',
 "grad":   '<path d="M22 10 12 5 2 10l10 5z"/><path d="M6 12v5c3 2 9 2 12 0v-5"/>',
 "car":    '<path d="M5 17h14v-5l-2-5H7l-2 5z"/><circle cx="7.5" cy="17" r="2"/><circle cx="16.5" cy="17" r="2"/><path d="M5 12h14"/>',
 "key":    '<circle cx="7.5" cy="15.5" r="4.5"/><path d="m10.7 12.3 9.8-9.8M17 6l3 3M15 8l2 2"/>',
 "utensils":'<path d="M3 2v7a3 3 0 0 0 6 0V2M6 2v20M21 15V2a5 5 0 0 0-5 5v6h5zM21 15v7"/>',
}
WA = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.5 14.4c-.3-.1-1.8-.9-2-1s-.5-.1-.7.1-.8 1-1 1.2-.4.2-.7.1a8.2 8.2 0 0 1-2.4-1.5 9 9 0 0 1-1.7-2.1c-.2-.3 0-.5.1-.6l.5-.5.3-.5a.6.6 0 0 0 0-.5l-.9-2.3c-.3-.6-.5-.5-.7-.5h-.6a1.2 1.2 0 0 0-.9.4 3.6 3.6 0 0 0-1.1 2.7 6.3 6.3 0 0 0 1.3 3.3 14.4 14.4 0 0 0 5.5 4.9c2 .9 2.5.9 3.3.8a2.9 2.9 0 0 0 1.9-1.3 2.4 2.4 0 0 0 .2-1.3c-.1-.2-.3-.3-.6-.4zM12 21.8a9.8 9.8 0 0 1-5-1.4l-.4-.2-3.7 1 1-3.6-.2-.4A9.8 9.8 0 1 1 12 21.8zM20.5 3.5A11.8 11.8 0 0 0 1.7 17.8L0 24l6.3-1.7A11.8 11.8 0 0 0 24 12a11.7 11.7 0 0 0-3.5-8.5z"/></svg>'

def esc(s):  # para atributos y JSON-LD a partir de texto con marcado
    import re
    return H.unescape(re.sub(r'<[^>]+>', '', s))

def head(eyebrow, h2, sub=None, hid=None):
    o = ['<div class="vsx-head vsx-rv">']
    if eyebrow: o.append('<p class="vsx-eyebrow">%s</p>' % eyebrow)
    o.append('<h2%s>%s</h2>' % (' id="%s"' % hid if hid else '', h2))
    if sub: o.append('<p>%s</p>' % sub)
    o.append('</div>')
    return "\n      ".join(o)

def build(S):
    url = SITE + "/sectores/%s/" % S["slug"]
    style = "--s:%s;--s-dark:%s;--s-light:%s;--s-soft:%s;--s-rgb:%s" % (
        S["color"]["s"], S["color"]["dark"], S["color"]["light"], S["color"]["soft"], S["color"]["rgb"])
    o = []; w = o.append

    w('<!-- ==========================================================\n'
      '     VERANTIA - Pagina de sector: %s\n'
      '     Pegar tal cual en un unico widget HTML de Elementor.\n'
      '     Ajustes de pagina en Elementor: Diseno de pagina =\n'
      '     "Elementor ancho completo", para que el tema no pinte un\n'
      '     segundo H1 con el titulo de la pagina.\n'
      '     Fotos: %s\n'
      '     ========================================================== -->\n' % (S["name"], S["credits"]))
    w(CSS)
    w('\n<div class="vsx" style="%s">\n\n' % style)

    # ---------- HERO ----------
    h = S["hero"]
    w('  <section class="vsx-hero" aria-labelledby="vsx-h1">\n')
    w('    <nav class="vsx-crumb" aria-label="Ruta de navegación"><ol>'
      '<li><a href="%s/">Inicio</a></li><li><a href="%s/sectores/">Sectores</a></li>'
      '<li><span aria-current="page">%s</span></li></ol></nav>\n' % (SITE, SITE, S["name"]))
    w('    <div class="vsx-hero-grid">\n      <div class="vsx-hero-copy">\n')
    w('        <p class="vsx-tag"><i>%s</i>Sector · %s</p>\n' % (ic(S["icon"]), S["name"]))
    w('        <h1 id="vsx-h1">%s</h1>\n' % h["h1"])
    w('        <p class="vsx-lead">%s</p>\n' % h["lead"])
    w('        <div class="vsx-ctas">\n')
    w('          <a class="vsx-btn vsx-btn--p" href="%s/contacto/">Solicitar auditoría gratuita %s</a>\n' % (SITE, ic("arrow")))
    w('          <a class="vsx-btn vsx-btn--g" href="#vsx-servicios">Ver soluciones</a>\n')
    w('        </div>\n        <ul class="vsx-chips">\n')
    for c in h["chips"]:
        w('          <li>%s%s</li>\n' % (ic("check"), c))
    w('        </ul>\n      </div>\n')
    img = S["img1"]
    w('      <div class="vsx-media">\n')
    w('        <img src="%s%s-1200.webp" srcset="%s%s-800.webp 800w, %s%s-1200.webp 1200w" '
      'sizes="(max-width:1080px) 92vw, 540px" width="1200" height="800" '
      'fetchpriority="high" decoding="async" alt="%s">\n' % (UP, img["file"], UP, img["file"], UP, img["file"], img["alt"]))
    w('      </div>\n    </div>\n  </section>\n\n')

    # ---------- DOLORES ----------
    p = S["pains"]
    w('  <section class="vsx-sec vsx-sec--soft" aria-labelledby="vsx-pain-t">\n    <div class="vsx-wrap">\n      ')
    w(head(p["eyebrow"], p["h2"], p["sub"], "vsx-pain-t") + '\n      <div class="vsx-g4">\n')
    for icn, t, d in p["items"]:
        w('        <div class="vsx-pain vsx-rv"><i>%s</i><h3>%s</h3><p>%s</p></div>\n' % (ic(icn), t, d))
    w('      </div>\n      <p class="vsx-summary vsx-rv">%s</p>\n    </div>\n  </section>\n\n' % p["summary"])

    # ---------- 4 SERVICIOS ----------
    v = S["services"]
    w('  <section class="vsx-sec" id="vsx-servicios" aria-labelledby="vsx-svc-t">\n    <div class="vsx-wrap">\n      ')
    w(head(v["eyebrow"], v["h2"], v["sub"], "vsx-svc-t") + '\n      <div class="vsx-svcs">\n')
    for n, it in enumerate(v["items"], 1):
        w('        <article class="vsx-svc vsx-rv">\n')
        w('          <div class="vsx-svc-top"><div class="vsx-svc-ico">%s</div>'
          '<div><span class="vsx-svc-n">Servicio %02d</span><h3>%s</h3></div></div>\n' % (ic(it["icon"]), n, it["title"]))
        w('          <p>%s</p>\n          <ul>\n' % it["desc"])
        for b in it["bullets"]:
            w('            <li>%s<span>%s</span></li>\n' % (ic("checkc"), b))
        w('          </ul>\n')
        w('          <p class="vsx-svc-res"><b>Resultado:</b> %s</p>\n' % it["result"])
        w('          <a class="vsx-svc-link" href="%s%s/">%s %s</a>\n' % (SVC, it["base"], it["link"], ic("arrow")))
        w('        </article>\n')
    w('      </div>\n      <div class="vsx-also vsx-rv">\n        <p>%s</p>\n        <ul>\n' % v["also_intro"])
    for slug, txt in v["also"]:
        w('          <li><a href="%s%s/">%s</a></li>\n' % (SVC, slug, txt))
    w('        </ul>\n      </div>\n    </div>\n  </section>\n\n')

    # ---------- CIFRAS ----------
    st = S["stats"]
    w('  <section class="vsx-dark" aria-labelledby="vsx-stat-t">\n    <div class="vsx-wrap">\n      ')
    w(head(st["eyebrow"], st["h2"], st["sub"], "vsx-stat-t") + '\n      <div class="vsx-g4">\n')
    for tag, val, dec, unit, label, src in st["items"]:
        shown = "{:,.{d}f}".format(float(val), d=dec).replace(",", "X").replace(".", ",").replace("X", ".")
        w('        <div class="vsx-stat vsx-rv"><span class="vsx-stat-t">%s</span>'
          '<p class="vsx-stat-n"><span data-vsx-count="%s" data-vsx-dec="%d">%s</span>'
          '<span class="vsx-stat-u">%s</span></p><p class="vsx-stat-l">%s</p><p class="vsx-stat-s">%s</p></div>\n'
          % (tag, val, dec, shown, unit, label, src))
    w('      </div>\n      <p class="vsx-src vsx-rv">Fuentes: %s</p>\n    </div>\n  </section>\n\n' % st["sources"])

    # ---------- UN DIA CUALQUIERA ----------
    d = S["day"]; img = S["img2"]
    w('  <section class="vsx-sec" aria-labelledby="vsx-day-t">\n    <div class="vsx-wrap">\n      ')
    w(head(d["eyebrow"], d["h2"], d["sub"], "vsx-day-t") + '\n      <div class="vsx-day">\n')
    w('        <figure class="vsx-day-media vsx-rv"><img src="%s%s-800.webp" srcset="%s%s-800.webp 800w, %s%s-1200.webp 1200w" '
      'sizes="(max-width:1080px) 92vw, 460px" width="800" height="1000" loading="lazy" decoding="async" alt="%s">'
      '<figcaption>%s</figcaption></figure>\n' % (UP, img["file"], UP, img["file"], UP, img["file"], img["alt"], d["caption"]))
    w('        <div class="vsx-rv">\n          <ol class="vsx-tl">\n')
    for icn, txt in d["items"]:
        w('            <li><span class="vsx-tl-i" aria-hidden="true">%s</span><div>%s</div></li>\n' % (ic(icn), txt))
    w('          </ol>\n        </div>\n      </div>\n    </div>\n  </section>\n\n')

    # ---------- PASOS ----------
    s = S["steps"]
    w('  <section class="vsx-sec vsx-sec--soft" aria-labelledby="vsx-steps-t">\n    <div class="vsx-wrap">\n      ')
    w(head(s["eyebrow"], s["h2"], s.get("sub"), "vsx-steps-t") + '\n      <div class="vsx-steps">\n')
    for t, txt in s["items"]:
        w('        <div class="vsx-step vsx-rv"><h3>%s</h3><p>%s</p></div>\n' % (t, txt))
    w('      </div>\n    </div>\n  </section>\n\n')

    # ---------- FAQ ----------
    q = S["faq"]
    w('  <section class="vsx-sec" aria-labelledby="vsx-faq-t">\n    <div class="vsx-wrap">\n      ')
    w(head(q["eyebrow"], q["h2"], q["sub"], "vsx-faq-t") + '\n      <div class="vsx-faq">\n')
    for pregunta, resp in q["items"]:
        w('        <details class="vsx-rv"><summary><h3>%s</h3><i aria-hidden="true">%s</i></summary><div class="a">%s</div></details>\n'
          % (pregunta, ic("plus"), resp))
    w('      </div>\n    </div>\n  </section>\n\n')

    # ---------- CTA + RELACIONADOS ----------
    c = S["cta"]
    w('  <section class="vsx-sec" style="padding-top:0" aria-labelledby="vsx-cta-t">\n    <div class="vsx-cta vsx-rv">\n')
    w('      <h2 id="vsx-cta-t">%s</h2>\n      <p>%s</p>\n      <div class="vsx-ctas">\n' % (c["h2"], c["p"]))
    w('        <a class="vsx-btn vsx-btn--w" href="%s/contacto/">Solicitar auditoría gratuita %s</a>\n' % (SITE, ic("arrow")))
    w('        <a class="vsx-btn vsx-btn--o" href="https://wa.me/34601855347" target="_blank" rel="noopener">%s WhatsApp 601 85 53 47</a>\n' % WA)
    w('      </div>\n      <small>O llámanos al <a href="tel:+34983618315">983 61 83 15</a> · '
      '<a href="mailto:info@verantiapro.es">info@verantiapro.es</a></small>\n    </div>\n')
    w('    <div class="vsx-wrap" style="margin-top:70px">\n      ')
    w(head("Sigue explorando", "Más de Verantia", None, "vsx-rel-t") + '\n      <div class="vsx-rel vsx-rv">\n')
    for icn, href, txt in [("grid", SITE + "/sectores/", "Soluciones por sector"),
                           ("layers", SITE + "/servicios/", "Todos los servicios"),
                           ("clip", SVC + "auditoria-de-procesos/", "Auditoría de procesos gratuita")]:
        w('        <a href="%s"><i>%s</i><span>%s</span></a>\n' % (href, ic(icn), txt))
    w('      </div>\n    </div>\n  </section>\n\n')

    # ---------- JSON-LD ----------
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "Service", "@id": url + "#servicio", "name": esc(h["h1"]), "url": url,
         "serviceType": S["schema_type"], "description": S["schema_desc"],
         "provider": {"@id": ORG_ID},
         "areaServed": [{"@type": "City", "name": "Valladolid"},
                        {"@type": "AdministrativeArea", "name": "Castilla y León"},
                        {"@type": "Country", "name": "España"}],
         "audience": {"@type": "BusinessAudience", "audienceType": S["name"]},
         "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Servicios para " + S["name"].lower(),
            "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Service",
                "name": esc(it["title"]), "description": esc(it["desc"]), "url": SVC + it["base"] + "/"}}
                for it in v["items"]]}},
        {"@type": "FAQPage", "@id": url + "#faq", "inLanguage": "es", "isPartOf": {"@id": url},
         "mainEntity": [{"@type": "Question", "name": esc(a),
                         "acceptedAnswer": {"@type": "Answer", "text": esc(b)}} for a, b in q["items"]]}]}
    w('  <script type="application/ld+json">\n%s\n  </script>\n\n' % json.dumps(ld, ensure_ascii=False, indent=2))
    w('</div>\n\n')
    w(JS)
    return "".join(o)

JS = r"""<script>
/* Verantia - pagina de sector: aparicion al hacer scroll y contadores.
   El contenido parte VISIBLE; solo se oculta si este script corre, y lo
   que ya esta en pantalla se marca visible en el mismo ciclo (sin parpadeo
   aunque la cache aplace el script). */
(function () {
  var root = document.querySelector('.vsx'); if (!root) return;
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var canIO = 'IntersectionObserver' in window;
  if (canIO && !reduce) {
    root.classList.add('vsx-js');
    var io = new IntersectionObserver(function (es) {
      for (var i = 0; i < es.length; i++) if (es[i].isIntersecting) { es[i].target.classList.add('vsx-in'); io.unobserve(es[i].target); }
    }, { threshold: 0.08, rootMargin: '0px 0px -8% 0px' });
    var els = root.querySelectorAll('.vsx-rv'), vh = window.innerHeight || 800;
    for (var n = 0; n < els.length; n++) {
      if (els[n].getBoundingClientRect().top < vh * 0.95) els[n].classList.add('vsx-in');
      else { els[n].style.transitionDelay = (Math.min(n % 4, 3) * 80) + 'ms'; io.observe(els[n]); }
    }
  }
  var nums = root.querySelectorAll('[data-vsx-count]'); if (!nums.length) return;
  function fmt(v, d) { return v.toLocaleString('es-ES', { minimumFractionDigits: d, maximumFractionDigits: d }); }
  function run(el) {
    var t = parseFloat(el.getAttribute('data-vsx-count')), d = parseInt(el.getAttribute('data-vsx-dec') || '0', 10);
    if (isNaN(t)) return;
    if (reduce || !window.requestAnimationFrame) { el.textContent = fmt(t, d); return; }
    var start = null;
    function frame(ts) {
      if (start === null) start = ts;
      var p = Math.min((ts - start) / 1300, 1);
      el.textContent = fmt(t * (1 - Math.pow(1 - p, 3)), d);
      if (p < 1) requestAnimationFrame(frame); else el.textContent = fmt(t, d);
    }
    requestAnimationFrame(frame);
  }
  if (!canIO || reduce) { for (var k = 0; k < nums.length; k++) run(nums[k]); return; }
  var io2 = new IntersectionObserver(function (es) {
    for (var j = 0; j < es.length; j++) if (es[j].isIntersecting) { run(es[j].target); io2.unobserve(es[j].target); }
  }, { threshold: 0.45 });
  for (var m = 0; m < nums.length; m++) io2.observe(nums[m]);
})();
</script>
"""
