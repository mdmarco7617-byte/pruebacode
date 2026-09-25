# -*- coding: utf-8 -*-
"""Fuentes verificadas en origen y piezas de texto comunes a los sectores."""
def a(url, txt):
    return '<a href="%s" target="_blank" rel="noopener nofollow">%s</a>' % (url, txt)

SQUARE   = a("https://squareup.com/es/es/press/estudio-radiografia-del-consumo-en-espana-realizado-por-square", "Square, Radiografía del consumo en España") + " (más de 1.000 encuestados, 2023)"
ZENDESK  = a("https://cxtrends.zendesk.com/es/", "Zendesk CX Trends 2026")
HUBSPOT  = a("https://www.periodicopublicidad.com/articulo/estudios/whatsapp-gana-peso-relacion-entre-empresas-clientes/20260526101512173926.html", "HubSpot, vía El Periódico de la Publicidad") + " (mayo de 2026)"
INE_IA   = a("https://cotec.es/proyectos-cpt/uso-de-la-ia-en-las-empresas/", "INE, Encuesta de uso de TIC en las empresas, vía Fundación Cotec")
BOOKSY   = a("https://www.distribucionactualidad.com/booksy-atrae-mas-salones-de-belleza-en-2025", "Booksy, vía DA Retail") + " (febrero de 2026)"
HBR      = a("https://hbr.org/2011/03/the-short-life-of-online-sales-leads", "Harvard Business Review, auditoría a 2.241 empresas de EE. UU.") + " (2011)"
LACAIXA  = a("https://mediahub.fundacionlacaixa.org/es/social/programas-sociales/exclusion-social/2026-02-03/estudio-educacion-extraescolares-desigualdad-observatorio-social-7977.html", "Observatorio Social de la Fundación «la Caixa»") + " (2.500 familias, febrero de 2026)"
ESADE    = a("https://www.diariodeleon.es/sociedad/260726/2092354/educacion-sombra-crece-fuerza-castilla-leon.html", "EsadeEcPol a partir de datos del INE, vía Diario de León") + " (julio de 2026)"
INE_VIV  = a("https://www.ine.es/dyngs/Prensa/ETDP1225.htm", "INE, Estadística de Transmisiones de Derechos de la Propiedad, año 2025")
CNMC     = a("https://www.cnmc.es/prensa/comercio-electronico-20260703", "CNMC, datos de comercio electrónico 2025") + " (julio de 2026)"
BAYMARD  = a("https://baymard.com/lists/cart-abandonment-rate", "Baymard Institute, media de 50 estudios") + " (septiembre de 2025)"
COVER    = a("https://www.infohoreca.com/noticias/20260323/62-cita-previa-restaurantes", "CoverManager, estudio «Las Mesas Hablan» 2025, vía InfoHoreca") + " (78,4 millones de mesas analizadas)"
SKEEPERS = a("https://ucex.org/el-83-de-los-consumidores-espanoles-leen-resenas-online-antes-de-comprar-en-tiendas-fisicas/", "Skeepers, 10.000 encuestados en España") + " (febrero de 2025)"
CSD      = a("https://portalhoy.es/aumenta-la-practica-deportiva-en-espana-y-disminuye-su-brecha-de-genero-segun-la-ultima-encuesta-de-habitos-deportivos-del-csd/", "Consejo Superior de Deportes, Encuesta de Hábitos Deportivos 2025")
ANFAC    = a("https://anfac.com/la-mitad-de-los-turismos-que-circulan-en-espana-superan-ya-los-15-anos-de-antiguedad/", "ANFAC, informe de parque de vehículos 2025") + " (agosto de 2026)"

def sources(*xs):
    return " · ".join(xs) + "."

AUD = '<a href="https://verantiapro.es/servicios/auditoria-de-procesos/">auditoría gratuita</a>'

def faq_phone(lugar, que):
    return ("¿Cómo funciona el asistente telefónico?",
     "<p>Se conecta a tu número de teléfono para atender las llamadas que tú no puedes coger: %s, en horas punta o con el negocio cerrado. "
     "Responde con una voz natural, informa de %s y, cuando hace falta, toma el recado para que devuelvas la llamada.</p>"
     "<p>Lo desarrollamos a medida para cada negocio, y antes de activarlo escuchas cómo suena y apruebas lo que dice. Al empezar cada llamada "
     "avisa de que es un asistente automático, como exige la normativa europea de inteligencia artificial.</p>" % (lugar, que))

def faq_datos(quien):
    return ("¿Cómo se protegen los datos de mis %s?" % quien,
     "<p>Trabajamos sobre tus propias cuentas y herramientas, y firmamos contigo el contrato de encargado de tratamiento que exige el RGPD. "
     "Los datos son tuyos y puedes retirarnos el acceso cuando quieras.</p>"
     "<p>Si en algún paso hace falta enviar información a un proveedor de inteligencia artificial, te lo explicamos antes y decides tú.</p>")

def faq_precio(negocio):
    return ("¿Cuánto cuesta para %s?" % negocio,
     "<p>Depende de las soluciones que necesites: un sistema de avisos automáticos no tiene nada que ver con un asistente completo conectado a tus herramientas.</p>"
     "<p>Por eso empezamos con una <strong>auditoría gratuita y sin compromiso</strong>: sales de ella con una horquilla de precio realista y ajustada al tamaño de tu negocio.</p>")

def faq_zona(plural):
    return ("¿Trabajáis solo con %s de Valladolid?" % plural,
     "<p>Somos una agencia de Valladolid y nos gusta conocer los negocios en persona, pero todo lo que hacemos funciona igual en remoto.</p>"
     "<p>Trabajamos con %s de toda Castilla y León y del resto de España.</p>" % plural)

def faq_software(que, herramienta):
    return ("¿Funciona con %s que ya uso?" % que,
     "<p>Depende de la herramienta. Si %s permite conectarse con otras aplicaciones, lo integramos directamente. Si no, te proponemos la "
     "alternativa más sencilla para que no tengas que duplicar trabajo.</p><p>Lo comprobamos en la %s, antes de que decidas nada.</p>" % (herramienta, AUD))

STEPS = lambda negocio, cosas, carga: {
  "eyebrow": "Cómo empezamos",
  "h2": "De la primera conversación a tu %s funcionando" % negocio,
  "items": [
   ("Auditoría gratuita", "Revisamos cómo gestionas hoy %s, y te decimos qué merece la pena automatizar. <strong>Sin coste y sin compromiso.</strong>" % cosas),
   ("Lo configuramos a tu medida", carga),
   ("Lo activamos y te acompañamos", "Te enseñamos a usarlo con tu propio día a día y seguimos ajustándolo contigo siempre que lo necesites."),
  ]}

def yoast(frase, extra):
    return {"keyphrase": frase, "title": "%s | Verantia" % frase,
            "desc": "%s: %s" % (frase, extra)}
