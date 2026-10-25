"""Builds the getmenufix.com pages (shared header and footer). Run: python3 _build.py"""
import re
from pathlib import Path

ROOT = Path(__file__).parent
NAV = [("services.html", "Services"), ("examples.html", "Examples"), ("how-it-works.html", "How it works"),
       ("pricing.html", "Pricing"), ("guides/index.html", "Guides"), ("about.html", "About"), ("faq.html", "FAQ")]
INSTAGRAM = "https://www.instagram.com/menufix.official/"
FACEBOOK = "https://www.facebook.com/profile.php?id=61584153426184"  # the MenuFix Facebook Page
IG_SVG = ('<svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5" '
          'fill="none" stroke="currentColor" stroke-width="2"/><circle cx="12" cy="12" r="4" fill="none" stroke="currentColor" '
          'stroke-width="2"/><circle cx="17.3" cy="6.7" r="1.3" fill="currentColor"/></svg>')
FB_SVG = ('<svg viewBox="0 0 24 24" width="26" height="26" aria-hidden="true"><path fill="currentColor" d="M13.5 21v-7.5h2.6l.4-3h-3'
          'V8.6c0-.9.3-1.5 1.6-1.5h1.6V4.4c-.3 0-1.2-.1-2.3-.1-2.3 0-3.9 1.4-3.9 4v2.2H7.9v3h2.6V21h3z"/></svg>')


def social():
    """Round brand coloured icons for our Instagram and Facebook Page (footer)."""
    out = f'<a class="ig" href="{INSTAGRAM}" rel="me noopener" target="_blank" aria-label="Instagram @menufix.official" title="Instagram @menufix.official">{IG_SVG}</a>'
    if FACEBOOK:
        out += f'<a class="fb" href="{FACEBOOK}" rel="me noopener" target="_blank" aria-label="Facebook MenuFix" title="Facebook MenuFix">{FB_SVG}</a>'
    return f'<div class="social">{out}</div>'


LOGO = '<a class="logo" href="index.html"><img src="img/logo-mark.png" alt=""><b>menu<span>fix</span></b></a>'


def ic(name, cls="icon3d"):
    return f'<img class="{cls}" src="img/icons/{name}.png" alt="" loading="lazy">'


def floaty(name, style, delay=0):
    return f'<img class="floaty" src="img/icons/{name}.png" alt="" style="{style};animation-delay:-{delay}s">'


def _sized(html, up=""):
    """Give every local image its width and height (no layout jumps) and lazy, async decoding."""
    import re
    import struct

    def dims(path):
        b = (ROOT / path).read_bytes()
        if b[:8] == b"\x89PNG\r\n\x1a\n":
            return struct.unpack(">II", b[16:24])
        i = 2
        while i < len(b):
            marker, size = b[i + 1], struct.unpack(">H", b[i + 2:i + 4])[0]
            if marker in (0xC0, 0xC1, 0xC2):
                h, w = struct.unpack(">HH", b[i + 5:i + 9])
                return w, h
            i += 2 + size
        return None

    def add(m):
        tag, src = m.group(0), m.group(1)
        if "width=" in tag or not (ROOT / src).is_file() or src.endswith(".svg"):
            return tag
        d = dims(src)
        return tag.replace("<img ", f'<img width="{d[0]}" height="{d[1]}" decoding="async" ', 1) if d else tag
    return re.sub(r'<img [^>]*?src="' + re.escape(up) + r'(img/[^"]+)"[^>]*>', add, html)


def ld(name):
    """Structured data so Google understands who we are, what we sell and our FAQs."""
    import json
    org = {"@type": "Organization", "@id": "https://getmenufix.com/#org", "name": "MenuFix", "url": "https://getmenufix.com/",
           "logo": "https://getmenufix.com/img/logo-mark.png", "email": "hello@getmenufix.com",
           "alternateName": ["MenuFix (getmenufix.com)", "getmenufix"],
           "description": "MenuFix is an independent done for you Uber Eats menu optimisation service: menu rewrite, photo enhancement of real dishes and Uber Eats page set up, with a free mockup first.",
           "disambiguatingDescription": "MenuFix at getmenufix.com, an Uber Eats page makeover service. Not menufix.com and not affiliated with Uber.",
           "knowsAbout": ["Uber Eats menu optimisation", "Uber Eats menu descriptions", "Uber Eats food photos", "Delivery app menus",
                          "Uber Eats account management", "Uber Eats error charge disputes", "Uber Eats review replies"],
           "sameAs": [u for u in (INSTAGRAM, FACEBOOK, "https://www.crunchbase.com/organization/menufix",
                                  "https://www.trustpilot.com/review/getmenufix.com") if u]}
    graph = [org, {"@type": "WebSite", "@id": "https://getmenufix.com/#site", "url": "https://getmenufix.com/",
                   "name": "MenuFix", "publisher": {"@id": "https://getmenufix.com/#org"}, "inLanguage": "en"}]
    if name in ("index.html", "services.html", "pricing.html"):
        graph.append({"@type": "Service", "name": "Uber Eats menu optimisation and food photo enhancement",
                      "serviceType": "Delivery app menu makeover", "provider": {"@id": "https://getmenufix.com/#org"},
                      "areaServed": ["AU", "NZ", "GB", "IE"],
                      "offers": [{"@type": "Offer", "name": n, "price": str(pr), "priceCurrency": "AUD",
                                  "url": "https://getmenufix.com/pricing.html"}
                                 for n, pr in (("Uber Eats Makeover", 969), ("Makeover and Google", 1259),
                                               ("Complete: Makeover, Google and Website", 2290))]
                      + [{"@type": "Offer", "name": "Growth Plan (monthly Uber Eats account management)", "price": "195",
                          "priceCurrency": "AUD", "url": "https://getmenufix.com/pricing.html#growth",
                          "priceSpecification": {"@type": "UnitPriceSpecification", "price": "195", "priceCurrency": "AUD",
                                                 "unitCode": "MON"}}]})
    if name in ("faq.html", "index.html"):
        items = FAQ if name == "faq.html" else FAQ[:4]
        graph.append({"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q,
                      "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]})
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False)


NAV_FR = [("fr/services.html", "Services"), ("fr/examples.html", "Exemples"), ("fr/how-it-works.html", "Comment ça marche"),
          ("fr/pricing.html", "Tarifs"), ("fr/guides/index.html", "Guides"), ("fr/about.html", "À propos"), ("fr/faq.html", "FAQ")]
NAV_ES = [("es/services.html", "Servicios"), ("es/examples.html", "Ejemplos"), ("es/how-it-works.html", "Cómo funciona"),
          ("es/pricing.html", "Precios"), ("es/guias/index.html", "Guías"), ("es/about.html", "Nosotros"), ("es/faq.html", "Preguntas")]
CHROME = {
    "en": {"home": "index.html", "nav": NAV, "cta_href": "contact.html", "cta": "Free mockup",
           "blurb": "Uber Eats page makeovers for independent restaurants, cafés and bakeries. Clear menus, better photos of your real food, done for you.",
           "cols": [("Services", [("services.html", "Menu rewrite"), ("services.html#photos", "Photo enhancement"), ("uber-eats-menu-makeover-service.html", "Done for you"), ("examples.html", "Examples")]),
                    ("Company", [("about.html", "About"), ("guides/index.html", "Guides"), ("how-it-works.html", "How it works"), ("pricing.html", "Pricing"), ("faq.html", "FAQ"), ("referral.html", "Earn 20%"), ("rider.html", "Delivery riders: earn 20%")]),
                    ("Who we help", [("uber-eats/cafes.html", "Cafés"), ("uber-eats/pizza.html", "Pizza shops"), ("uber-eats/asian-restaurants.html", "Asian restaurants"), ("uber-eats/takeaways.html", "Takeaways"), ("uber-eats/index.html", "Cities we work with")]),
                    ("Free tools", [("tools/uber-eats-photo-checker.html", "Photo checker"), ("tools/menu-description-checker.html", "Description checker"), ("tools/uber-eats-page-score.html", "Page score")]),
                    ("Get started", [("contact.html", "Free mockup"), ("mailto", "hello@getmenufix.com"), ("privacy.html", "Privacy"), ("terms.html", "Terms")])],
           "promo": ("referral.html", "Know restaurant owners? <b>Earn 20%</b> for every restaurant you send us.", "See how"),
           "follow": "Follow us",
           "rights": "© 2026 MenuFix. All rights reserved.", "indep": "MenuFix is independent and not affiliated with Uber or Uber Eats."},
    "fr": {"home": "fr/index.html", "nav": NAV_FR, "cta_href": "fr/contact.html", "cta": "Maquette gratuite",
           "blurb": "Refonte des pages Uber Eats pour restaurants indépendants, cafés et boulangeries. Menus clairs, meilleures photos de vos vrais plats, tout pris en charge.",
           "cols": [("Services", [("fr/services.html", "Réécriture du menu"), ("fr/services.html#photos", "Amélioration des photos"), ("fr/services.html#done", "Clé en main"), ("fr/examples.html", "Exemples")]),
                    ("Entreprise", [("fr/about.html", "À propos"), ("fr/guides/index.html", "Guides"), ("fr/how-it-works.html", "Comment ça marche"), ("fr/pricing.html", "Tarifs"), ("fr/faq.html", "FAQ"), ("fr/parrainage.html", "Gagnez 20 %")]),
                    ("Outils gratuits", [("fr/outils/verificateur-photo-uber-eats.html", "Vérificateur de photo"), ("fr/outils/verificateur-description-menu.html", "Vérificateur de description"), ("fr/outils/score-page-uber-eats.html", "Score de page")]),
                    ("Commencer", [("fr/contact.html", "Maquette gratuite"), ("mailto", "hello@getmenufix.com"), ("fr/privacy.html", "Confidentialité"), ("fr/terms.html", "Conditions")])],
           "promo": ("fr/parrainage.html", "Vous connaissez des restaurateurs ? <b>Gagnez 20 %</b> pour chaque restaurant recommandé.", "En savoir plus"),
           "follow": "Suivez nous",
           "rights": "© 2026 MenuFix. Tous droits réservés.", "indep": "MenuFix est indépendant et n'est pas affilié à Uber ni à Uber Eats."},
    "es": {"home": "es/index.html", "nav": NAV_ES, "cta_href": "es/contact.html", "cta": "Maqueta gratis",
           "blurb": "Mejoramos páginas de Uber Eats para restaurantes independientes, cafeterías y panaderías. Cartas claras, mejores fotos de sus platos reales y todo hecho por nosotros.",
           "cols": [("Servicios", [("es/services.html", "Reescritura de la carta"), ("es/services.html#photos", "Mejora de fotos"), ("es/services.html#done", "Hecho por nosotros"), ("es/examples.html", "Ejemplos")]),
                    ("Empresa", [("es/about.html", "Quiénes somos"), ("es/guias/index.html", "Guías"), ("es/how-it-works.html", "Cómo funciona"), ("es/pricing.html", "Precios"), ("es/faq.html", "Preguntas frecuentes"), ("es/referidos.html", "Gane un 20 %")]),
                    ("Herramientas gratis", [("es/herramientas/comprobador-fotos-uber-eats.html", "Comprobador de fotos"), ("es/herramientas/comprobador-descripciones-menu.html", "Comprobador de descripciones"), ("es/herramientas/puntuacion-pagina-uber-eats.html", "Puntuación de página")]),
                    ("Empezar", [("es/contact.html", "Maqueta gratis"), ("mailto", "hello@getmenufix.com"), ("es/privacy.html", "Privacidad"), ("es/terms.html", "Condiciones")])],
           "promo": ("es/referidos.html", "¿Conoce a dueños de restaurantes? <b>Gane un 20 %</b> por cada restaurante que nos recomiende.", "Ver cómo"),
           "follow": "Síganos",
           "rights": "© 2026 MenuFix. Todos los derechos reservados.", "indep": "MenuFix es independiente y no está afiliado a Uber ni a Uber Eats."},
}


# Changes when site.js changes, so browsers fetch the new file instead of an old cached copy.
SITE_JS_V = __import__("hashlib").md5((ROOT / "site.js").read_bytes()).hexdigest()[:8]
STYLE_V = __import__("hashlib").md5((ROOT / "style.css").read_bytes()).hexdigest()[:8]


def _url(path):
    return "https://getmenufix.com/" + (path[:-10] if path in ("index.html", "fr/index.html", "es/index.html") else path)


def page(name, title, desc, body, active="", lang="en", ld_extra=""):
    """Write one page. name and every link in the chrome are relative to the site root; pages in folders get ../ prefixes.
    The language switch and the hreflang links are added later by add_languages(), once every page exists."""
    c = CHROME[lang]
    on = ' class="on"'
    links = "".join(f'<a href="{h}"{on if h == active else ""}>{t}</a>' for h, t in c["nav"])
    logo = LOGO.replace('href="index.html"', f'href="{c["home"]}"')
    cols = "".join(f'<div><h4>{h}</h4>' + "".join(f'<a class="mailto" href="#">{t}</a>' if u == "mailto" else f'<a href="{u}">{t}</a>' for u, t in items) + "</div>"
                   for h, items in c["cols"])
    html = f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="msvalidate.01" content="F0DCDD1209340D5FCE9148B6F4762CB7">
<meta name="theme-color" content="#ffffff">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="/favicon.ico" sizes="48x48"><link rel="icon" href="/favicon-192.png" type="image/png" sizes="192x192"><link rel="apple-touch-icon" href="/apple-touch-icon.png"><script>window.goatcounter={{filter:function(){{if(navigator.webdriver)return "automation";try{{if(localStorage.getItem("skipgc")==="t")return "skip";}}catch(e){{}}if("visibilityState" in document&&document.visibilityState==="prerender")return "prerender";return false;}}}};</script><script data-goatcounter="https://menufix.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>
<link rel="canonical" href="{_url(name)}">
<script type="application/ld+json">{ld(name) if lang == "en" else LD_OTHER}</script>{ld_extra}
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="https://getmenufix.com/img/spread.jpg">
<meta property="og:type" content="website">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
</head>
<body>
<a class="promo" href="{c["promo"][0]}"><span>{c["promo"][1]}</span> <u>{c["promo"][2]} →</u></a>
<nav class="nav"><div class="wrap">
  {logo}
  <button class="burger" aria-label="Menu" onclick="document.querySelector('.nav .links').classList.toggle('open')">☰</button>
  <div class="links">{links}<a class="btn primary small" href="{c["cta_href"]}">{c["cta"]}</a></div>
</div></nav>
{body}
<footer><div class="wrap">
  <div class="top">
    <div>{logo}
      <p class="muted" style="max-width:340px">{c["blurb"]}</p>
      <div class="icons"><img src="img/icons/pizza.png" alt=""><img src="img/icons/burger.png" alt=""><img src="img/icons/sushi.png" alt=""><img src="img/icons/coffee.png" alt=""><img src="img/icons/taco.png" alt=""><img src="img/icons/cake.png" alt=""></div>
      <h4 class="follow">{c["follow"]}</h4>{social()}</div>
    {cols}
  </div>
  <div class="bottom"><span>{c["rights"]}</span><span>{c["indep"]}</span></div>
</div></footer>
<script src="site.js?v={SITE_JS_V}"></script>
</body>
</html>
"""
    up = "../" * name.count("/")
    if up:  # a page in a folder: point root relative links and assets at the site root
        html = re.sub(r'(src|href)="(?!https?:|#|mailto:|/|\.\./|data:)([^"]+)"', lambda m: f'{m.group(1)}="{up}{m.group(2)}"', html)
        (ROOT / name).parent.mkdir(parents=True, exist_ok=True)
    (ROOT / name).write_text(_sized(html, up))


# ------------------------------------------------------------------------------------------------ languages
# Pages that are the same page in another language, by topic: {topic: {lang: root relative path}}.
# A page with no group (the Australian city pages and Australian guides) stays in its own language only.
SAME = {}
LANGS = [("en", "EN", "English"), ("fr", "FR", "Français"), ("es", "ES", "Español")]
HOMES = {"en": "index.html", "fr": "fr/index.html", "es": "es/index.html"}
GUIDE_HOMES = {"en": "guides/index.html", "fr": "fr/guides/index.html", "es": "es/guias/index.html"}


def same_page(topic, lang, path):
    SAME.setdefault(topic, {})[lang] = path


def _href(path):
    return "/" + (path[:-10] if path in HOMES.values() else path)


def _lang_of(path):
    return path.split("/")[0] if path.split("/")[0] in ("fr", "es") else "en"



GC_PLAIN = '<script data-goatcounter="https://menufix.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>'
GC_FILTERED = '<script>window.goatcounter={filter:function(){if(navigator.webdriver)return "automation";try{if(localStorage.getItem("skipgc")==="t")return "skip";}catch(e){}if("visibilityState" in document&&document.visibilityState==="prerender")return "prerender";return false;}};</script><script data-goatcounter="https://menufix.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>'


def add_chrome_extras():
    """The referral bar and the social icons on pages that are not built by page() (the translated French pages)."""
    for f in sorted(ROOT.rglob("*.html")):
        path = f.relative_to(ROOT).as_posix()
        if path.startswith((".", "_", "for/")):
            continue
        html = f.read_text()
        if '<nav class="nav">' not in html:
            continue
        html = re.sub(r'href="((?:\.\./)*)style\.css(?:\?v=\w+)?"', rf'href="\1style.css?v={STYLE_V}"', html)  # new design: no old cached copy
        html = html.replace(GC_PLAIN, GC_FILTERED) if GC_FILTERED not in html else html  # our own browsers don't count
        html = re.sub(r'<a class="promo".*?</a>\n', "", html)  # an earlier version: put the current one back
        html = re.sub(r'\n      <h4 class="follow">.*?</div>(</div>)', r"\1", html, flags=re.S)
        c, up = CHROME[_lang_of(path)], "../" * path.count("/")
        bar = f'<a class="promo" href="{up}{c["promo"][0]}"><span>{c["promo"][1]}</span> <u>{c["promo"][2]} →</u></a>\n'
        if path != "rider.html":  # riders from our ads: no referral bar above their own offer
            html = html.replace('<nav class="nav">', bar + '<nav class="nav">', 1)
        html = re.sub(r'(<div class="icons">.*?</div>)</div>', lambda m: m.group(1) + f'\n      <h4 class="follow">{c["follow"]}</h4>{social()}</div>', html, count=1, flags=re.S)
        f.write_text(html)

def add_languages():
    """Give every page the EN FR ES switch, and hreflang links (plus x-default, the English page) to the same page in
    the other languages. Runs over every page on the site, including the French pages that are not built here."""
    group_of = {path: g for g in SAME.values() if len(g) > 1 for path in g.values()}
    for f in sorted(ROOT.rglob("*.html")):
        path = f.relative_to(ROOT).as_posix()
        if path.startswith((".", "_")):
            continue
        html = f.read_text()
        if "<nav class=\"nav\">" not in html:
            continue
        lang, group = _lang_of(path), group_of.get(path, {})
        html = re.sub(r'<link rel="alternate" hreflang="[^"]*" href="[^"]*">\n', "", html)
        html = re.sub(r'<span class="langs">.*?</span>|<a class="lang"[^>]*>[^<]*</a>', "", html)
        if group and not path.endswith("404.html"):
            alts = "".join(f'<link rel="alternate" hreflang="{l}" href="{_url(group[l])}">\n' for l, _, _ in LANGS if l in group)
            if "en" in group:
                alts += f'<link rel="alternate" hreflang="x-default" href="{_url(group["en"])}">\n'
            html = re.sub(r'(<link rel="canonical" href="[^"]*">\n)', lambda m: m.group(1) + alts, html, count=1)
        links = []
        for l, short, full in LANGS:
            if l == lang:
                links.append(f'<a class="lang on" href="{_href(path)}" lang="{l}" title="{full}" aria-current="true">{short}</a>')
            elif l in group:
                links.append(f'<a class="lang" href="{_href(group[l])}" hreflang="{l}" lang="{l}" title="{full}">{short}</a>')
            else:  # no copy in that language: its guides or its home page
                target = GUIDE_HOMES[l] if "/" in path and path.split("/")[-2] in ("guides", "guias", "tools", "outils", "herramientas") else HOMES[l]
                links.append(f'<a class="lang" href="{_href(target)}" lang="{l}" title="{full}">{short}</a>')
        switch = f'<span class="langs">{"".join(links)}</span>'
        html = html.replace('<a class="btn primary small"', switch + '<a class="btn primary small"', 1)
        if lang == "fr" and path.count("/") == 1:  # the French pages written by _translate_fr.py
            html = _fr_static(html)
        f.write_text(html)


def _fr_static(html):
    """Keep the hand translated French pages in step with the built ones: free tools in the footer, current site.js."""
    html = html.replace("<h4>Company</h4>", "<h4>Entreprise</h4>").replace("<h4>Société</h4>", "<h4>Entreprise</h4>").replace("<h4>Get started</h4>", "<h4>Commencer</h4>")
    if "parrainage.html" not in html:  # the referral program, in the Entreprise column
        html = re.sub(r'(<div><h4>Entreprise</h4>.*?)</div>', lambda m: m.group(1) + '<a href="parrainage.html">Gagnez 20 %</a></div>', html, count=1, flags=re.S)
    if "outils/" not in html:
        html = html.replace('<div><h4>Commencer</h4>', '<div><h4>Outils gratuits</h4><a href="outils/verificateur-photo-uber-eats.html">Vérificateur de photo</a>'
                            '<a href="outils/verificateur-description-menu.html">Vérificateur de description</a></div>\n    <div><h4>Commencer</h4>', 1)
    if "outils/score-page-uber-eats.html" not in html:
        html = html.replace('<a href="outils/verificateur-description-menu.html">Vérificateur de description</a>',
                            '<a href="outils/verificateur-description-menu.html">Vérificateur de description</a>'
                            '<a href="outils/score-page-uber-eats.html">Score de page</a>', 1)
    return re.sub(r'src="\.\./site\.js(\?v=[0-9a-f]+)?"', f'src="../site.js?v={SITE_JS_V}"', html)


LD_OTHER = '{"@context": "https://schema.org", "@type": "Organization", "@id": "https://getmenufix.com/#org", "name": "MenuFix", "url": "https://getmenufix.com/"}'


def ba(n, before_name, after_name, before_desc, after_desc):
    return f"""<div class="reveal"><div class="ba">
  <img src="img/{n}-before.jpg" alt="Before: a dark, blurry phone photo" loading="lazy">
  <img class="after" src="img/{n}-after.jpg" alt="After: a bright, clear photo of the same dish" loading="lazy">
  <div class="handle"></div><span class="tag l">Before</span><span class="tag r">After</span>
  <input type="range" min="0" max="100" value="50" aria-label="Compare before and after">
</div>
<div class="ba-caption"><div><b><s>{before_name}</s></b>{before_desc}</div><div><b>{after_name}</b>{after_desc}</div></div></div>"""


MOCKS = {"mock1": "Pho Saigon Corner", "mock2": "Nonna Rosa Pizzeria", "mock3": "Seoul Bowl Kitchen"}


def mockpair(key, note=True):
    return f"""<div class="mockpair reveal">
  <figure><div class="device"><img src="img/{key}-before.jpg" alt="{MOCKS[key]} page before" loading="lazy"></div><figcaption><span class="pill">Before</span>Typos, no descriptions, missing photos</figcaption></figure>
  <div class="mockarrow">→</div>
  <figure><div class="device"><img src="img/{key}-after.jpg" alt="{MOCKS[key]} page after" loading="lazy"></div><figcaption><span class="pill on">After</span>Clear names, descriptions that sell, bright photos</figcaption></figure>
</div>""" + ('<p class="note" style="text-align:center;margin-top:18px">Concept mockup for a fictional restaurant, made with AI for this website.</p>' if note else "")


def cta(title="See your page improved, free.",
        text="Tell us your restaurant, café or bakery on Uber Eats. We'll send you a free mockup of how your page could look. No payment, no obligation.",
        img="delivery"):
    return f"""<section class="tight"><div class="wrap"><div class="cta reveal">
  <div class="txt"><span class="eyebrow">Free mockup</span><h2>{title}</h2><p class="lead">{text}</p>
    <div class="row"><a class="btn" href="contact.html">Get my free mockup <span class="arr">→</span></a><a class="btn ghost" href="pricing.html">See pricing</a></div></div>
  <div class="pic"><img class="bg" src="img/{img}.jpg" alt="" loading="lazy">
    {floaty("burger", "left:-34px;top:40px")}{floaty("bubbletea", "right:24px;bottom:24px", 3)}</div>
</div></div></section>"""


PLANS = f"""<div class="plans">
  <div class="plan reveal">{ic("chef")}<h3>Uber Eats Makeover</h3><p class="muted" style="margin:6px 0 0">Your whole Uber Eats page, done for you.</p>
    <div class="price" data-p="full_makeover"></div><small class="once">One time price, no subscription</small>
    <ul><li>Every dish name and description rewritten to sell</li><li>Your real photos enhanced, for your whole menu</li><li>Best sellers first and a clear menu order</li><li>A prices and combos check after the fees</li><li class="dfy">We make every change on your page. You don't touch anything</li><li>One month of updates</li></ul>
    <a class="btn dark" data-buy="full_makeover" href="#">Get the Makeover</a></div>
  <div class="plan feat reveal"><span class="ribbon">Most popular</span>{ic("star")}<h3>Makeover and Google</h3><p class="muted" style="margin:6px 0 0">Found on Uber Eats and on Google.</p>
    <div class="price" data-p="makeover_google"></div><small class="once">One time price, no subscription</small>
    <ul><li>Everything in the Uber Eats Makeover</li><li>Your Google Business Profile set up: categories, hours and menu</li><li>Your best real photos on Google</li><li>An order button on Google</li><li>Google review auto replies, first month included</li></ul>
    <a class="btn primary" data-buy="makeover_google" href="#">Get Makeover and Google</a></div>
  <div class="plan reveal"><span class="ribbon green">Best value</span>{ic("gift")}<h3>Complete</h3><p class="muted" style="margin:6px 0 0">Uber Eats, Google and your own website.</p>
    <div class="price" data-p="complete"></div><small class="once">One time price, first year of hosting included</small>
    <ul><li>Everything in Makeover and Google</li><li>Your own website, designed in your style</li><li>Menu with photos and prices, and a big order button</li><li>Hours, map, reviews and your Instagram</li><li>Your own web address connected</li><li>The same photos and words everywhere</li></ul>
    <a class="btn dark" data-buy="complete" href="#">Get Complete</a></div>
</div>
<p class="note reveal" style="text-align:center;margin-top:18px">All three are done for you, and you only pay once you've seen your finished page and you're happy with it.</p>"""

CUR = """<p class="curnote">Prices in <b data-curname>your currency</b>, charged in the same currency at checkout.</p>"""

FAQ = [
    ("Do I need to give you my password?", "No. You add us as a user on your Uber Eats Manager, and you can remove us any time. We never ask for your password."),
    ("Do you use fake food photos?", "Never. We only enhance photos of your real dishes: better light, a clean background and the right size. Customers should get exactly what they see, and Uber Eats requires real photos too. The free mockup is a concept preview only."),
    ("How long does it take?", "Usually two to three working days after we have your photos and access to your Uber Eats Manager. A website takes a few days more."),
    ("Will this guarantee more orders?", "No one can honestly promise that. What we do is make your page clearer and more appetising, which is what helps people choose you."),
    ("What if I don't like it?", "You don't pay. We make your finished page first and send it to you, before and after, with every change listed. If you're happy, you pay. If not, tell us what to change, or simply say no and you owe nothing."),
    ("What do I need to send you?", "Photos of your dishes taken on your phone in good light (near a window is perfect), and access as a user to your Uber Eats Manager. We do everything else."),
    ("Do you work with cafés and bakeries too?", "Yes. Restaurants, takeaways, cafés, bakeries and dessert places that sell on Uber Eats. We don't work with big chains, or with shops that sell packaged products."),
    ("Is MenuFix part of Uber?", "No. MenuFix is an independent service and is not affiliated with Uber or Uber Eats."),
    ("Which countries do you work with?", "Australia, New Zealand, the UK, Ireland and more. Prices show in your currency."),
]


def faq_html(items):
    return '<div class="faq">' + "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in items) + "</div>"


CATS = [("pizza", "Pizza"), ("burger", "Burgers"), ("sushi", "Sushi"), ("noodles", "Noodles"), ("coffee", "Coffee"),
        ("cake", "Cakes"), ("taco", "Mexican"), ("curry", "Indian"), ("dumpling", "Dumplings"), ("chicken", "Chicken"),
        ("salad", "Healthy"), ("croissant", "Bakery"), ("bubbletea", "Bubble tea"), ("kebab", "Kebabs"),
        ("icecream", "Desserts")]
cats = '<div class="cats">' + "".join(f'<div class="cat"><div class="ic"><img src="img/icons/{k}.png" alt="" loading="lazy"></div>{t}</div>' for k, t in CATS) + "</div>"

EX = [("burger", "dbl burgr + chips", "Smash Burger and Fries", "No description.", "Double beef, aged cheddar, pickles and house sauce on a toasted brioche bun, with fries."),
      ("laksa", "LAKSA SPECIAL", "Chicken Laksa", "see photo", "Rich coconut curry broth, rice noodles, shredded chicken, tofu puffs and lime."),
      ("dumplings", "dumplings 10pc", "Pork and Chive Dumplings", "No description.", "Handmade and pan fried until golden, with chilli oil for dipping."),
      ("curry", "chiken curry w rice", "Butter Chicken with Rice", "Typos, no description.", "Slow cooked chicken in a rich, mildly spiced tomato and butter sauce, with steamed basmati."),
      ("pizza", "PIZZA 3", "Garden Pizza", "A number nobody remembers.", "Mozzarella, capsicum, mushroom, olives and fresh basil on a crisp, wood fired base."),
      ("shawarma", "wrap", "Chicken Shawarma Wrap", "Too vague to choose.", "Marinated chicken, garlic sauce, pickles and chips wrapped in warm flatbread."),
      ("tacos", "taco x3", "Beef Birria Tacos", "Says nothing about the taste.", "Three slow braised beef tacos with onion, coriander, lime and consommé to dip."),
      ("poke", "POKE SALMON REG", "Salmon Poke Bowl", "Capitals, no detail.", "Fresh salmon, sushi rice, avocado, edamame, cucumber and mango with sesame."),
      ("breakfast", "avo toast", "Smashed Avo on Sourdough", "Too short to tempt.", "Smashed avocado, poached egg and crumbled feta on toasted sourdough."),
      ("cake", "choc cake", "Triple Chocolate Layer Cake", "Nothing to make you want it.", "Moist chocolate sponge layered with rich ganache. Baked in house every morning.")]
EXD = {e[0]: e for e in EX}

FEAT = "".join(f"""<a class="fcard reveal" href="examples.html"><div class="ph"><img src="img/{k}-after.jpg" alt="" loading="lazy"><span class="badge">{b}</span></div>
  <h3>{EXD[k][2]}</h3><p>{m}</p></a>""" for k, b, m in [
    ("burger", "Before and after", "New name, description and photo"),
    ("poke", "Before and after", "Rewritten to sell, photo enhanced"),
    ("dumplings", "Before and after", "From a dark snap to a bright photo"),
    ("cake", "Before and after", "A dessert people can't skip")])

# ------------------------------------------------------------------------------------------------ home
page("index.html", "Uber Eats Menu Optimisation and Food Photos | MenuFix",
     "We make your Uber Eats page show how good your food is: clear names, descriptions that sell, the right order and better photos of your real food. Done for you. Free mockup first.",
f"""<header class="hero">
  {floaty("pizza", "left:45%;bottom:4%", 1)}{floaty("sushi", "left:44%;top:6%", 4)}{floaty("coffee", "right:2%;bottom:4%", 2)}
  <div class="wrap">
  <div class="reveal">
    <span class="chip"><img src="img/icons/bag.png" alt="">For restaurants, cafés and bakeries on Uber Eats</span>
    <h1>Make hungry people choose <span class="hl">you.</span></h1>
    <p class="lead">Customers order what looks good. We rewrite your menu, put your best sellers first and make photos of your real food look delicious. We can even make every change on your page for you.</p>
    <form class="search" action="contact.html" method="get">
      <img src="img/icons/menu.png" alt=""><input name="biz" placeholder="Your restaurant or café name" aria-label="Your restaurant or café name">
      <button class="btn primary" type="submit">Get my free mockup <span class="arr">→</span></button>
    </form>
    <div class="trust"><span>Free mockup first</span><span>One time price</span><span>Real food only</span></div>
  </div>
  <div class="hero-visual reveal">
    <div class="hero-photo"><img src="img/spread.jpg" alt="A table full of takeaway dishes" fetchpriority="high"></div>
    <div class="food-card b"><img src="img/laksa-after.jpg" alt=""><b>Chicken Laksa</b><small>Rich coconut curry broth, rice noodles and lime.</small><div class="tagline">$18.00<i>New photo</i></div></div>
    <div class="food-card a"><img src="img/burger-after.jpg" alt=""><b>Smash Burger and Fries</b><small>Double beef, cheddar, pickles and house sauce.</small><div class="tagline">$19.50<i>Rewritten</i></div></div>
  </div>
</div></header>

<section class="tight"><div class="wrap">
  <div class="head reveal" style="margin-bottom:28px"><div><span class="eyebrow">Made for every kitchen</span><h2>Whatever you cook, we make it look delicious.</h2></div>
    <p class="lead">Independent restaurants, takeaways, cafés, bakeries and dessert spots. No big chains.</p></div>
  <div class="reveal">{cats}</div>
</div></section>

<section class="bg-cream"><div class="wrap">
  <div class="head reveal"><div><span class="eyebrow">Featured makeovers</span><h2>Same dish. Same price. Way more tempting.</h2></div>
    <div><p class="lead">Small changes make people stop scrolling: a clear name, a tasty line about the dish and a bright photo.</p>
    <a class="btn" href="examples.html">See all examples <span class="arr">→</span></a></div></div>
  <div class="feat-row">{FEAT}</div>
</div></section>

<section><div class="wrap">
  <div class="head center reveal"><span class="eyebrow">Drag to compare</span><h2>From a quick snap to <span class="hl">mouth watering.</span></h2>
    <p class="lead">Slide each photo. On the left, a dark phone photo and the old menu text. On the right, the same dish after our makeover.</p></div>
  <div class="grid2">
    {ba(*EXD["burger"])}
    {ba(*EXD["laksa"])}
  </div>
  <p class="note" style="margin-top:22px;text-align:center">Illustrative examples to show the kind of change we make. Images made with AI for this website.</p>
</div></section>

<section class="bg-peach"><div class="wrap">
  <div class="head reveal"><div><span class="eyebrow">Your free mockup</span><h2>See your whole page, before you pay.</h2></div>
    <p class="lead">Every restaurant we talk to gets a free concept mockup of its own page, like this one. You see exactly what we'd change, with no obligation.</p></div>
  {mockpair("mock2")}
  <div class="row" style="justify-content:center;margin-top:34px"><a class="btn primary" href="contact.html">Get my free mockup <span class="arr">→</span></a></div>
</div></section>

<section><div class="wrap">
  <div class="head reveal"><div><span class="eyebrow">What we do</span><h2>Everything your page needs.</h2></div>
    <p class="lead">Pick what you need. We handle the details, or we send everything ready to copy if you'd rather do it yourself.</p></div>
  <div class="grid3">
    <a class="photo-card reveal" href="services.html"><div class="ph"><img class="bg" src="img/desk.jpg" alt="" loading="lazy">{ic("pen")}</div><div class="body"><h3>Menu rewrite</h3><p>Clear names, descriptions that sell, typos gone and categories in the right order.</p></div></a>
    <a class="photo-card reveal" href="services.html#photos"><div class="ph"><img class="bg" src="img/phone.jpg" alt="" loading="lazy">{ic("camera")}</div><div class="body"><h3>Photo enhancement</h3><p>Your real dishes with better light, a clean background and the right size for Uber Eats.</p></div></a>
    <a class="photo-card reveal" href="services.html#done"><div class="ph"><img class="bg" src="img/kitchen.jpg" alt="" loading="lazy">{ic("chef")}</div><div class="body"><h3>Done for you</h3><p>With every package we make every change on your Uber Eats page ourselves. You keep cooking.</p></div></a>
  </div>
</div></section>

<section class="bg-butter"><div class="wrap">
  <div class="head center reveal"><span class="eyebrow">How it works</span><h2>Simple, from start to finish.</h2></div>
  <div class="steps">
    <div class="step reveal"><span class="n">1</span>{ic("gift")}<h3>Free mockup</h3><p>We look at your Uber Eats page and show you how it could look. Free.</p></div>
    <div class="step reveal"><span class="n">2</span>{ic("menu")}<h3>Choose a package</h3><p>One time price, paid securely by card. No subscription.</p></div>
    <div class="step reveal"><span class="n">3</span>{ic("phone")}<h3>Send your photos</h3><p>For photo packages, snap your dishes on your phone and email them.</p></div>
    <div class="step reveal"><span class="n">4</span>{ic("rocket")}<h3>Your new page</h3><p>We update it for you, or send it ready to copy with a simple guide.</p></div>
  </div>
</div></section>

<section><div class="wrap">
  <div class="head reveal"><div><span class="eyebrow">Pricing</span><h2>Clear prices. No surprises.</h2></div>
    <div><p class="lead">Three packages, all done for you: the Uber Eats Makeover, Makeover and Google, or Complete with your own website.</p>{CUR}</div></div>
  {PLANS}
</div></section>

<section class="bg-cream"><div class="narrow">
  <div class="head center reveal" style="margin-bottom:30px"><span class="eyebrow">Questions</span><h2>Good to know</h2></div>
  {faq_html(FAQ[:4])}
  <p style="margin-top:26px;text-align:center"><a class="btn" href="faq.html">All questions <span class="arr">→</span></a></p>
</div></section>
{cta()}
""")


def head(eyebrow, title, lead, icons=("burger", "coffee"), extra=""):
    a, b = icons
    return f"""<header class="page-head">{floaty(a, "right:6%;top:22%")}{floaty(b, "right:20%;bottom:8%", 3)}<div class="wrap">
  <span class="eyebrow">{eyebrow}</span><h1 style="max-width:820px">{title}</h1>
  <p class="lead">{lead}</p>{extra}
</div></header>"""


# ------------------------------------------------------------------------------------------------ services
page("services.html", "Uber Eats Menu Writing, Food Photo Enhancement and Setup | MenuFix", "We rewrite your Uber Eats menu, enhance photos of your real dishes and can update your Uber Eats page for you. For restaurants, cafés and bakeries.",
f"""{head("Services", "Everything that makes people <span class='hl'>order.</span>", "We focus on one thing: your delivery app page. Here's exactly what we do and what you get.", ("pizza", "sushi"))}

<section class="tight" id="menu"><div class="wrap split">
  <div class="reveal">{ic("pen")}<span class="eyebrow" style="display:block">Menu rewrite</span><h2>Words that sell every dish.</h2>
    <p class="lead" style="margin-top:20px">Most menus on delivery apps were typed in a hurry. We rewrite them so every item is clear, appetising and easy to choose.</p>
    <ul class="ticks"><li>Typos, capitals and confusing names fixed</li><li>A short, tasty description for every item</li><li>Best sellers moved to the top</li><li>Categories in a clear order, without clutter</li><li>Your real dishes and prices only. We never invent anything</li></ul></div>
  <div class="reveal">{ba(*EXD["tacos"])}</div>
</div></section>

<section class="tight bg-cream" id="photos"><div class="wrap split rev">
  <div class="reveal">{ic("camera")}<span class="eyebrow" style="display:block">Photo enhancement</span><h2>Your real food, at its best.</h2>
    <p class="lead" style="margin-top:20px">Send us photos of your dishes taken on your phone. We make them bright, sharp and appetising, while keeping the food exactly as it is.</p>
    <ul class="ticks"><li>Better light, colour and sharpness</li><li>A clean, warm background</li><li>Framed and sized for Uber Eats</li><li>Never fake food, never added ingredients</li></ul></div>
  <div class="reveal">{ba(*EXD["dumplings"])}</div>
</div></section>

<section class="tight" id="done"><div class="wrap split">
  <div class="reveal">{ic("chef")}<span class="eyebrow" style="display:block">Done for you</span><h2>You cook. We update your page.</h2>
    <p class="lead" style="margin-top:20px">Included in every package. Add us as a user on your Uber Eats Manager and we make every change ourselves.</p>
    <ul class="ticks"><li>No passwords shared: you add us as a user</li><li>Names, descriptions, categories and photos updated</li><li>You can remove our access any time</li><li>You see your finished page first, and you only pay if you're happy</li></ul>
    <div class="row" style="margin-top:30px"><a class="btn primary" href="pricing.html">See pricing <span class="arr">→</span></a><a class="btn ghost" href="uber-eats-menu-makeover-service.html">The done for you service</a></div></div>
  <div class="img reveal"><img src="img/kitchen.jpg" alt="" loading="lazy"></div>
</div></section>

<section class="bg-butter"><div class="wrap">
  <div class="head center reveal"><span class="eyebrow">Who it's for</span><h2>Independent places on Uber Eats.</h2></div>
  <div class="grid4">
    <div class="card reveal">{ic("pizza")}<h3>Restaurants</h3><p><a href="uber-eats/pizza.html">Pizza</a>, burgers, <a href="uber-eats/asian-restaurants.html">Asian</a>, Middle Eastern and everything in between.</p></div>
    <div class="card reveal">{ic("coffee")}<h3><a href="uber-eats/cafes.html" style="color:inherit">Cafés</a></h3><p>Breakfast, lunch, coffee and cakes.</p></div>
    <div class="card reveal">{ic("croissant")}<h3>Bakeries and desserts</h3><p>Cakes, pastries, gelato and sweet treats.</p></div>
    <div class="card reveal">{ic("kebab")}<h3><a href="uber-eats/takeaways.html" style="color:inherit">Takeaways</a></h3><p>Kebabs, burgers, fried chicken and late night favourites.</p></div>
  </div>
</div></section>
{cta()}
""", "services.html")

# ------------------------------------------------------------------------------------------------ the service page
# 22 Oct 2026: one page that answers exactly "a done for you Uber Eats menu makeover service", for search engines and
# AI assistants (ChatGPT, Perplexity) that look for a company doing the whole job, not tips.
SERVICE_FAQ = [
    ("Is there a service that optimises my Uber Eats menu for me?",
     "Yes. MenuFix (getmenufix.com) rewrites your Uber Eats menu, enhances photos of your real dishes and makes every change on your Uber Eats page for you. You see a free mockup first."),
    ("How is MenuFix different from doing it myself in Uber Eats Manager?",
     "Uber Eats Manager lets you edit your page, but you still have to write every description, fix every photo and choose the order. MenuFix does that work for you and hands it back ready, or updates the page itself."),
    ("Do you need my Uber Eats password?",
     "No. You add us as a user in Uber Eats Manager and you can remove us any time."),
    ("Is MenuFix part of Uber Eats?",
     "No. MenuFix is an independent service at getmenufix.com. It is not affiliated with Uber or Uber Eats, and it is not the same company as menufix.com."),
    ("How long does it take?",
     "Usually two to three working days after we have your photos and access to your Uber Eats Manager."),
]
page("uber-eats-menu-makeover-service.html", "Done for You Uber Eats Menu Makeover Service | MenuFix",
     "MenuFix is a done for you Uber Eats menu optimisation service: we rewrite your menu, enhance photos of your real dishes and update your Uber Eats page for you. Free mockup first.",
f"""{head("Uber Eats menu makeover service", "We fix your Uber Eats page <span class='hl'>for you.</span>",
        "MenuFix is a done for you service for restaurants, cafés and bakeries on Uber Eats. We rewrite the menu, enhance photos of your real dishes and make the changes on your page ourselves. You see a free mockup before you pay anything.", ("burger", "sushi"))}

<section class="tight"><div class="wrap">{mockpair("mock2")}</div></section>

<section class="tight bg-cream"><div class="wrap">
  <div class="head center reveal"><span class="eyebrow">What you get</span><h2>The whole job, not a list of tips.</h2></div>
  <div class="grid4">
    <div class="card reveal">{ic("pen")}<h3>Menu rewrite</h3><p>Clear dish names and a short description that sells for every item. Your real dishes and prices only.</p></div>
    <div class="card reveal">{ic("camera")}<h3>Photo enhancement</h3><p>Photos of your real food made bright and sharp, sized to Uber Eats rules (5:4, at least 550 × 440 pixels).</p></div>
    <div class="card reveal">{ic("chef")}<h3>Page set up</h3><p>Best sellers first, categories in a clear order, and the changes made on your Uber Eats page for you.</p></div>
    <div class="card reveal">{ic("coffee")}<h3>Free mockup first</h3><p>See your page improved before you decide. No payment, no obligation.</p></div>
  </div>
</div></section>

<section class="tight"><div class="wrap">
  <div class="head center reveal"><span class="eyebrow">Your options</span><h2>Ways to improve an Uber Eats page.</h2></div>
  <div class="table-scroll reveal"><table class="compare">
    <tr><th></th><th>Do it yourself</th><th>Food photographer</th><th>MenuFix</th></tr>
    <tr><td>Menu descriptions written</td><td>You write them</td><td>No</td><td>Yes, every dish</td></tr>
    <tr><td>Photos of your dishes</td><td>Your phone photos</td><td>New shoot at your venue</td><td>Your photos, enhanced</td></tr>
    <tr><td>Menu order and categories</td><td>You decide</td><td>No</td><td>Yes</td></tr>
    <tr><td>Changes made on Uber Eats</td><td>You make them</td><td>No</td><td>Yes, we make every change</td></tr>
    <tr><td>Preview before paying</td><td>No</td><td>No</td><td>Free mockup</td></tr>
    <tr><td>Price</td><td>Your time</td><td>Often several hundred a shoot</td><td>From <span data-p="full_makeover"></span>, one time</td></tr>
  </table></div>
  <p class="note" style="text-align:center;margin-top:14px">Compare all our prices on the <a href="pricing.html">pricing page</a>. Uber Eats Makeover <span data-p="full_makeover"></span>, one time, no subscription.</p>
</div></section>

<section class="tight bg-butter"><div class="wrap">
  <div class="head center reveal"><span class="eyebrow">How it works</span><h2>Three steps.</h2></div>
  <div class="grid3">
    <div class="card reveal"><h3>1. Send your Uber Eats page</h3><p>Your store link or name is enough. We send a free mockup, usually within one or two working days.</p></div>
    <div class="card reveal"><h3>2. Say yes and choose a plan</h3><p>The Uber Eats Makeover, Makeover and Google, or Complete with your own website. All done for you.</p></div>
    <div class="card reveal"><h3>3. Your page goes live</h3><p>You check everything first. Nothing changes on your page until you say ok.</p></div>
  </div>
</div></section>

<section style="padding-top:30px"><div class="narrow">
  <div class="head center reveal"><span class="eyebrow">Questions</span><h2>About the service.</h2></div>
  {faq_html(SERVICE_FAQ)}
  <p class="note" style="margin-top:20px">MenuFix works with restaurants in Australia, the United Kingdom, Ireland, the United States and France. Read more in our guides, for example <a href="guides/optimize-uber-eats-page-options.html">5 ways to optimise an Uber Eats page</a>.</p>
</div></section>
{cta()}
""", "services.html", ld_extra='\n<script type="application/ld+json">' + __import__("json").dumps({"@context": "https://schema.org", "@graph": [
    {"@type": "Service", "name": "Done for you Uber Eats menu makeover", "serviceType": "Uber Eats menu optimisation",
     "provider": {"@id": "https://getmenufix.com/#org"}, "areaServed": ["AU", "GB", "IE", "US", "FR", "NZ"],
     "url": "https://getmenufix.com/uber-eats-menu-makeover-service.html",
     "description": "Menu rewrite, photo enhancement of real dishes and Uber Eats page set up, done for the restaurant. Free mockup first."},
    {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in SERVICE_FAQ]}]},
    ensure_ascii=False) + "</script>")

# ------------------------------------------------------------------------------------------------ examples
grid = "".join(f"<div>{ba(*e)}</div>" for e in EX)
page("examples.html", "Uber Eats Menu Before and After Examples | MenuFix", "Before and after examples of Uber Eats menu makeovers: clearer names, descriptions that sell and better photos.",
f"""{head("Examples", "See the <span class='hl'>difference.</span>", "Whole page mockups first, then dish by dish. Drag each slider to compare.", ("taco", "cake"))}
<section style="padding-top:30px"><div class="wrap">
  <div class="head reveal"><div><span class="eyebrow">Page mockups</span><h2>Whole page makeovers</h2></div>
    <p class="lead">The free mockup we send shows your full page after the makeover: banner, best sellers first, clear names and descriptions, appetising photos.</p></div>
  {mockpair("mock1", False)}
  <div style="height:70px"></div>
  {mockpair("mock3", False)}
  <div style="height:70px"></div>
  {mockpair("mock2", False)}
  <p class="note" style="text-align:center;margin-top:24px">Concept mockups for fictional restaurants, made with AI for this website.</p>
</div></section>
<section class="bg-cream"><div class="wrap">
  <div class="head reveal"><div><span class="eyebrow">Dish by dish</span><h2>Photos and descriptions</h2></div>
    <p class="lead">On the left, a quick phone photo and the old menu text. On the right, the same dish enhanced and rewritten.</p></div>
  <div class="grid2" style="gap:56px 32px">{grid}</div>
  <p class="note" style="margin-top:40px">Illustrative examples for fictional dishes and places, with images made with AI for this website. For your page we only work from photos of your real dishes.</p>
</div></section>
{cta("Want to see your own page?", "Send us your restaurant or café on Uber Eats and we'll show you a free mockup of yours.")}
""", "examples.html")

# ------------------------------------------------------------------------------------------------ how it works
page("how-it-works.html", "How Our Uber Eats Menu Makeover Works | MenuFix", "From free mockup to your new Uber Eats page in four simple steps, all by email.",
f"""{head("How it works", "Four simple <span class='hl'>steps.</span>", "Everything can be done by email. You see the idea before you pay anything.", ("noodles", "croissant"))}
<section class="tight"><div class="wrap split">
  <div class="reveal">{ic("gift")}<span class="eyebrow" style="display:block">Step 1</span><h2>Your free mockup</h2>
    <p class="lead" style="margin-top:18px">Tell us your restaurant or café on Uber Eats. We look at your page and send you a mockup of how it could look, with the main things we'd change. No payment, no obligation.</p></div>
  <div class="reveal" style="display:flex;justify-content:center"><div class="device solo"><img src="img/mock1-after.jpg" alt="A concept mockup of a restaurant page" loading="lazy"></div></div>
</div></section>
<section class="tight bg-cream"><div class="wrap split rev">
  <div class="reveal">{ic("menu")}<span class="eyebrow" style="display:block">Step 2</span><h2>Choose your package</h2>
    <p class="lead" style="margin-top:18px">Pick the Uber Eats Makeover, Makeover and Google, or Complete with your own website. We make every change for you. Pay securely by card through Stripe, once you've seen your finished page. One time price, no subscription.</p>
    <a class="btn primary" href="pricing.html" style="margin-top:10px">See pricing <span class="arr">→</span></a></div>
  <div class="img reveal"><img src="img/counter.jpg" alt="" loading="lazy"></div>
</div></section>
<section class="tight"><div class="wrap split">
  <div class="reveal">{ic("phone")}<span class="eyebrow" style="display:block">Step 3</span><h2>Send your photos</h2>
    <p class="lead" style="margin-top:18px">For photo packages, take photos of your dishes on your phone, in good light, and reply to our email with them. We enhance your real photos. We never use fake food.</p></div>
  <div class="reveal">{ba(*EXD["curry"])}</div>
</div></section>
<section class="tight bg-cream"><div class="wrap split rev">
  <div class="reveal">{ic("rocket")}<span class="eyebrow" style="display:block">Step 4</span><h2>Your new page</h2>
    <p class="lead" style="margin-top:18px">Add us as a user on Uber Eats Manager and we update everything: every name, description and photo. Usually within two to three working days.</p></div>
  <div class="img reveal"><img src="img/delivery.jpg" alt="" loading="lazy"></div>
</div></section>
{cta()}
""", "how-it-works.html")

# ------------------------------------------------------------------------------------------------ pricing
page("pricing.html", "Uber Eats Makeover Prices: 3 Done for You Packages | MenuFix", "Three done for you packages for your Uber Eats page: the Uber Eats Makeover, Makeover and Google, and Complete with your own website. Plus the monthly Growth Plan.",
f"""{head("Pricing", "Three packages, all <span class='hl'>done for you.</span>", "No contract. We make your finished page first, and you only pay once you've seen it and you're happy.", ("star", "bag"), CUR)}
<section style="padding-top:40px"><div class="wrap"><div class="head center reveal" style="margin:0 0 40px"><h2 style="font-size:40px">Uber Eats makeover packages</h2></div>{PLANS}
  <div class="head center reveal" id="growth" style="margin:100px 0 40px"><h2 style="font-size:40px">Monthly plan, after your project</h2>
    <p class="muted" style="margin:12px auto 0;max-width:640px">Optional. We look after your Uber Eats page, your Google profile and your website every month. Cancel any time.</p></div>
  <div class="plans" style="grid-template-columns:minmax(300px,460px);justify-content:center">
  <div class="plan feat reveal"><span class="ribbon">Growth Plan</span><img width="160" height="160" decoding="async" class="icon3d" src="img/icons/rocket.png" alt="" loading="lazy"><h3>Growth Plan</h3><p class="muted" style="margin:6px 0 0">Everything kept fresh and working, every month.</p>
    <div class="price" data-p="growth_plan"></div><small class="once">A month, cancel any time</small>
    <ul><li>Menu, prices and photos kept up to date</li><li>Replies to your Uber Eats and Google reviews</li><li>Wrong refunds and error charges disputed for you</li><li>Your offers and ads checked</li><li>Your website kept online and up to date</li><li>A monthly report with your page score</li></ul>
    <a class="btn primary" href="contact.html?topic=growth_plan">Ask about the Growth Plan</a></div>
  </div>
  <h2 style="margin-top:90px;font-size:36px" class="reveal">Compare packages</h2>
  <div class="table-scroll reveal"><table class="compare">
    <tr><th></th><th>Uber Eats Makeover</th><th>Makeover and Google</th><th>Complete</th></tr>
    <tr><td>Every dish rewritten to sell</td><td class="y">✓</td><td class="y">✓</td><td class="y">✓</td></tr>
    <tr><td>Your real photos enhanced, whole menu</td><td class="y">✓</td><td class="y">✓</td><td class="y">✓</td></tr>
    <tr><td>Best sellers first and menu order</td><td class="y">✓</td><td class="y">✓</td><td class="y">✓</td></tr>
    <tr><td>Prices and combos check</td><td class="y">✓</td><td class="y">✓</td><td class="y">✓</td></tr>
    <tr><td>Done for you: we make every change</td><td class="y">✓</td><td class="y">✓</td><td class="y">✓</td></tr>
    <tr><td>One month of updates</td><td class="y">✓</td><td class="y">✓</td><td class="y">✓</td></tr>
    <tr><td>Google Business Profile set up</td><td class="n">×</td><td class="y">✓</td><td class="y">✓</td></tr>
    <tr><td>Google review auto replies, first month</td><td class="n">×</td><td class="y">✓</td><td class="y">✓</td></tr>
    <tr><td>Your own website, first year of hosting</td><td class="n">×</td><td class="n">×</td><td class="y">✓</td></tr>
  </table></div>
</div></section>
<section class="bg-cream"><div class="narrow"><div class="head center reveal" style="margin-bottom:30px"><h2>Pricing questions</h2></div>
{faq_html([FAQ[2], FAQ[5], FAQ[4], ("How do I pay?", "By card through Stripe, a secure payment provider, once you've seen your finished page and you're happy with it. You pay in the currency shown on this page."), FAQ[0]])}</div></section>
{cta()}
""", "pricing.html")

# ------------------------------------------------------------------------------------------------ about
page("about.html", "About | MenuFix", "MenuFix is a small independent service that helps restaurants, cafés and bakeries get more from their Uber Eats page.",
f"""<header class="page-head" style="padding-top:40px"><div class="wrap"><div class="banner reveal"><img src="img/counter.jpg" alt=""><div>
  <span class="eyebrow">About MenuFix</span><h1>Great food deserves a great page.</h1>
  <p class="lead">We help independent restaurants, cafés and bakeries look as good on Uber Eats as they really are.</p></div></div></div></header>
<section style="padding-top:40px"><div class="wrap split">
  <div class="reveal"><span class="eyebrow">Our story</span><h2>Small places, real food.</h2>
    <p class="lead" style="margin-top:20px">Some of the best food in any city comes from small, independent kitchens. On delivery apps, though, they often look worse than the big chains: no photos, menus typed in a hurry, best dishes hidden at the bottom.</p>
    <p class="lead">MenuFix is a small independent service. We do one thing, delivery app pages, so we know exactly what helps people choose you. No agency fees and no long contracts. You deal with us directly, by email.</p></div>
  <div class="img reveal"><img src="img/kitchen.jpg" alt="" loading="lazy"></div>
</div></section>
<section class="bg-butter"><div class="wrap">
  <div class="head center reveal"><span class="eyebrow">What we believe</span><h2>How we work</h2></div>
  <div class="grid3">
    <div class="card reveal">{ic("salad")}<h3>Real food only</h3><p>We enhance photos of your real dishes. We never use fake food or add ingredients that aren't there.</p></div>
    <div class="card reveal">{ic("check")}<h3>Honest</h3><p>Clear prices, no hidden fees, and no promises we can't keep. A free mockup first, so you know what you're getting.</p></div>
    <div class="card reveal">{ic("rocket")}<h3>Simple</h3><p>Everything done for you in a few days, so you don't have to touch anything.</p></div>
  </div>
  <p class="lead reveal" style="text-align:center;margin:40px auto 0">Know restaurant owners? <a href="referral.html">Earn 20% for every restaurant you send us</a>.</p>
</div></section>
{cta()}
""", "about.html")

# ------------------------------------------------------------------------------------------------ faq
page("faq.html", "Uber Eats Menu Makeover Questions | MenuFix", "Answers to common questions about MenuFix Uber Eats page makeovers.",
f"""{head("FAQ", "Questions and <span class='hl'>answers.</span>", "Can't find what you're looking for? <a class='mailto' href='#'>Email us</a> and we'll get back to you.", ("icecream", "dumpling"))}
<section style="padding-top:30px"><div class="narrow">{faq_html(FAQ)}</div></section>
{cta()}
""", "faq.html")

# ------------------------------------------------------------------------------------------------ contact
page("contact.html", "Free Uber Eats Page Mockup | MenuFix", "Get a free mockup of your Uber Eats page. No payment, no obligation.",
f"""<header class="page-head">{floaty("gift", "left:3%;bottom:6%", 2)}<div class="wrap split" style="align-items:start">
  <div><span class="eyebrow">Free mockup</span><h1>See your page improved, <span class="hl">free.</span></h1>
    <p class="lead">Tell us where to find you on Uber Eats. We'll email you a mockup of how your page could look and the main things we'd change. No payment, no obligation.</p>
    <ul class="ticks"><li>Usually within one or two working days</li><li>No payment details needed</li><li>You only pay once you're happy</li></ul>
    <div class="img reveal" style="margin-top:40px"><img src="img/spread.jpg" alt="" loading="lazy"></div></div>
  <div class="card reveal" style="padding:40px">
    <form id="mockForm" data-lang="en" data-error="Sorry, something went wrong. Please try again in a minute, or email us at hello@getmenufix.com." novalidate>
      <div class="f"><label for="biz">Restaurant or café name</label><input id="biz" required maxlength="100" autocomplete="organization" placeholder="e.g. Sunny Thai Kitchen"></div>
      <div class="f"><label for="city">City</label><input id="city" required maxlength="60" placeholder="e.g. Sydney"></div>
      <div class="f"><label for="link">Your Uber Eats page link (optional)</label><input id="link" inputmode="url" maxlength="300" autocomplete="off" placeholder="https://www.ubereats.com/..."></div>
      <div class="f"><label for="email">Your email</label><input id="email" type="email" required maxlength="120" placeholder="you@yourrestaurant.com" autocomplete="email"></div>
      <div class="f"><label for="name">Your name</label><input id="name" maxlength="60" autocomplete="given-name" placeholder="First name"></div>
      <div class="f"><label for="msg">Anything we should know? (optional)</label><textarea id="msg" maxlength="1500" rows="4" placeholder="e.g. we just opened, our best seller is..."></textarea></div>
      <div class="hp" aria-hidden="true"><label for="mSite">Website</label><input id="mSite" tabindex="-1" autocomplete="off"></div>
      <label class="consent"><input id="mConsent" type="checkbox" required> <span>Email me my free mockup</span></label>
      <p class="err" id="mErr" role="alert" hidden></p>
      <button class="btn primary" type="submit" style="width:100%">Send my request <span class="arr">→</span></button>
      <p class="note" style="margin:14px 0 0">We use your email only for your mockup. See our <a href='privacy.html'>privacy policy</a>.</p>
    </form>
    <div id="mockThanks" class="thanks" hidden><h3>Thank you, we've got your request.</h3><p>We'll email you your free mockup, usually within one or two working days. If you don't see it, look in your spam folder.</p></div>
  </div>
</div></header>
""")

# ------------------------------------------------------------------------------------------------ legal + 404
for name, title in (("privacy.html", "Privacy"), ("terms.html", "Terms")):
    inner = re.search(r"<main[^>]*>(.*?)</main>", (ROOT / name).read_text(), re.S).group(1)
    inner = re.sub(r'<h1[^>]*>.*?</h1>\s*', "", inner, count=1, flags=re.S).strip()
    page(name, f"{title} | MenuFix", f"MenuFix {title.lower()}.",
         f'<header class="page-head"><div class="narrow"><span class="eyebrow">Legal</span><h1>{title}</h1></div></header>\n'
         f'<main class="narrow legal" style="padding-bottom:100px">\n{inner}\n</main>')
page("404.html", "Page not found | MenuFix", "This page does not exist.",
     f"""<header class="page-head" style="text-align:center;padding:140px 0">{floaty("icecream", "left:12%;top:30%")}{floaty("pizza", "right:12%;top:40%", 3)}<div class="narrow">
  <span class="eyebrow">404</span><h1>This page isn't on the menu.</h1>
  <p class="lead" style="margin-left:auto;margin-right:auto">The page you're looking for doesn't exist or has moved.</p>
  <div class="row" style="justify-content:center;margin-top:30px"><a class="btn primary" href="index.html">Back to home</a></div>
</div></header>""")
# ------------------------------------------------------------------------------------------------ guides
import json as _json

from _guides import GUIDES
from _guides_es import GUIDES_ES
from _guides_fr import GUIDES_FR

GT = {
    "en": {"dir": "guides/", "eyebrow": "Guides", "updated": "Updated 10 October 2026",
           "answer": "Quick answer", "toc": "In this guide", "faq": "Questions", "more": "More guides", "more_h": "Keep improving your page",
           "index_title": "Uber Eats Guides for Restaurants and Cafés | MenuFix",
           "index_desc": "Free practical guides for restaurant and café owners: getting more Uber Eats orders, pricing, menu descriptions, food photos on your phone and editing your menu.",
           "index_h": "Free guides to a better <span class='hl'>Uber Eats page.</span>",
           "index_lead": "Practical, honest advice for independent restaurants, cafés and bakeries. Use it yourself, or let us do it for you."},
    "fr": {"dir": "fr/guides/", "eyebrow": "Guides", "updated": "Mis à jour le 10 octobre 2026",
           "answer": "En bref", "toc": "Dans ce guide", "faq": "Questions fréquentes", "more": "Autres guides", "more_h": "Continuez à améliorer votre page",
           "index_title": "Guides Uber Eats pour restaurants et cafés | MenuFix",
           "index_desc": "Guides pratiques et gratuits pour restaurateurs : plus de commandes sur Uber Eats, prix, descriptions de plats, photos au téléphone et modification du menu.",
           "index_h": "Des guides gratuits pour une meilleure <span class='hl'>page Uber Eats.</span>",
           "index_lead": "Des conseils pratiques et honnêtes pour les restaurants indépendants, cafés et boulangeries. À suivre seul, ou à nous confier."},
    "es": {"dir": "es/guias/", "eyebrow": "Guías", "updated": "Actualizado el 13 de octubre de 2026",
           "date": "2026-10-13",
           "answer": "Respuesta rápida", "toc": "En esta guía", "faq": "Preguntas frecuentes", "more": "Más guías", "more_h": "Siga mejorando su página",
           "index_title": "Guías de Uber Eats para restaurantes y cafeterías | MenuFix",
           "index_desc": "Guías prácticas y gratuitas para dueños de restaurantes en España: más pedidos en Uber Eats, comisiones, precios, descripciones de platos y fotos con el móvil.",
           "index_h": "Guías gratuitas para una mejor <span class='hl'>página de Uber Eats.</span>",
           "index_lead": "Consejos prácticos y honestos para restaurantes independientes, cafeterías y panaderías. Aplíquelos usted mismo o déjelo en nuestras manos."},
}


def guide_card(g, lang="en"):
    return (f'<a class="photo-card reveal" href="/{GT[lang]["dir"]}{g["slug"]}.html"><div class="ph"><img class="bg" src="img/{g["img"]}.jpg" '
            f'alt="" loading="lazy"></div><div class="body" style="padding-top:26px"><h3>{g["short"]}</h3>'
            f'<p>{g["desc"]}</p></div></a>')


def _slugify(text):
    text = re.sub(r"<[^>]+>", "", text).lower()
    for a, b in (("àâä", "a"), ("éèêë", "e"), ("îï", "i"), ("ôö", "o"), ("ùûü", "u"), ("ç", "c")):
        text = re.sub(f"[{a}]", b, text)
    return re.sub(r"[^a-z0-9]+", "-", text).strip("-")


def with_toc(body):
    """Give every h2 an id and return (body, contents list)."""
    items = []

    def add(m):
        hid = _slugify(m.group(1))
        items.append((hid, re.sub(r"^\d+\.\s*", "", m.group(1))))
        return f'<h2 id="{hid}">{m.group(1)}</h2>'
    body = re.sub(r"<h2>(.*?)</h2>", add, body)
    return body, items


from _tools import TOOLS_TEXT, build_tools, tool_cards


def tools_section(lang):
    t = TOOLS_TEXT[lang]
    return f"""<section class="tight bg-cream" id="tools"><div class="wrap">
  <div class="head reveal" style="margin-bottom:30px"><div><span class="eyebrow">{t["eyebrow"]}</span><h2>{t["h2"]}</h2></div>
    <p class="lead">{t["lead"]}</p></div>
  <div class="grid3">{tool_cards(lang)}</div>
</div></section>"""


def build_guides(guides, lang, cta_html):
    t = GT[lang]
    date = t.get("date", "2026-10-10")
    by_slug = {g["slug"]: g for g in guides}
    out = []
    for g in guides:
        url = f"https://getmenufix.com/{t['dir']}{g['slug']}.html"
        art = {"@context": "https://schema.org", "@type": "Article", "headline": g["title"], "description": g["desc"],
               "image": f"https://getmenufix.com/img/{g['img']}.jpg", "inLanguage": lang,
               "author": {"@type": "Organization", "name": "MenuFix", "url": "https://getmenufix.com/"},
               "publisher": {"@type": "Organization", "name": "MenuFix", "logo": {"@type": "ImageObject",
                             "url": "https://getmenufix.com/img/logo-mark.png"}},
               "mainEntityOfPage": url, "datePublished": date, "dateModified": date}
        faq_ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in g.get("faq", [])]}
        ld_extra = f'\n<script type="application/ld+json">{_json.dumps(art, ensure_ascii=False)}</script>'
        if g.get("faq"):
            ld_extra += f'\n<script type="application/ld+json">{_json.dumps(faq_ld, ensure_ascii=False)}</script>'
        body, toc = with_toc(g["body"].replace('<table class="compare">', '<div class="table-scroll"><table class="compare">').replace("</table>", "</table></div>"))
        toc_html = (f'<nav class="toc" aria-label="{t["toc"]}"><b>{t["toc"]}</b><ol>' +
                    "".join(f'<li><a href="#{i}">{h}</a></li>' for i, h in toc) + "</ol></nav>") if len(toc) >= 4 else ""
        faq_block = (f'<section class="narrow guide-faq" style="padding:10px 0 60px"><h2>{t["faq"]}</h2>{faq_html(g["faq"])}</section>'
                     if g.get("faq") else "")
        related = [by_slug[s] for s in g.get("related", []) if s in by_slug]
        related += [o for o in guides if o is not g and o not in related]
        others = "".join(guide_card(o, lang) for o in related[:3])
        name = f"{t['dir']}{g['slug']}.html"
        # The same topic in each language: English slug, or a shared key for the France and Spain only guides.
        same_page("guide:" + (g.get("key") or (g["slug"] if lang == "en" else g.get("alt")) or name), lang, name)
        page(name, f"{g['title']} | MenuFix", g["desc"], f"""
<header class="page-head" style="padding-bottom:40px"><div class="narrow">
  <span class="eyebrow"><a href="/{t['dir']}index.html" style="color:inherit;text-decoration:none">{t['eyebrow']}</a></span>
  <h1 style="font-size:clamp(32px,4.6vw,54px)">{g['title']}</h1>
  <p class="lead">{g['lead']}</p>
  <p class="byline">{t['updated']}</p>
  {f'<div class="answer"><b>{t["answer"]}</b><p>{g["answer"]}</p></div>' if g.get("answer") else ""}
</div></header>
<div class="narrow"><div class="split" style="display:block"><div class="img" style="aspect-ratio:16/8">
  <img src="img/{g['img']}.jpg" alt="{g['short']}"></div></div></div>
<article class="narrow prose" style="padding:40px 0 30px">{toc_html}{body}</article>
{faq_block}
<section class="tight bg-cream"><div class="wrap">
  <div class="head reveal" style="margin-bottom:30px"><div><span class="eyebrow">{t['more']}</span><h2>{t['more_h']}</h2></div></div>
  <div class="grid3">{others}</div>
</div></section>
{cta_html}
""", f"{t['dir']}index.html", lang=lang, ld_extra=ld_extra)
        out.append(name)

    same_page("guides", lang, f"{t['dir']}index.html")
    page(f"{t['dir']}index.html", t["index_title"], t["index_desc"],
         f"""{head(t['eyebrow'], t['index_h'], t['index_lead'], ("menu", "camera"))}
<section style="padding-top:30px"><div class="wrap"><div class="grid3">{"".join(guide_card(g, lang) for g in guides)}</div></div></section>
{tools_section(lang)}
{cta_html}
""", f"{t['dir']}index.html", lang=lang)
    return [f"{t['dir']}index.html"] + out


CTA_FR = cta("Voyez votre page améliorée, gratuitement.",
             "Envoyez le nom de votre restaurant, café ou boulangerie sur Uber Eats : vous recevez une maquette gratuite de votre future page. Sans paiement, sans engagement.").replace(
    "Free mockup", "Maquette gratuite").replace("Get my free mockup", "Recevoir ma maquette gratuite").replace(
    "See pricing", "Voir les tarifs").replace('href="contact.html"', 'href="fr/contact.html"').replace('href="pricing.html"', 'href="fr/pricing.html"')
CTA_ES = cta("Vea su página mejorada, gratis.",
             "Díganos el nombre de su restaurante, cafetería o panadería en Uber Eats y le enviaremos una maqueta gratuita de cómo podría quedar su página. Sin pago y sin compromiso.").replace(
    "Free mockup", "Maqueta gratis").replace("Get my free mockup", "Quiero mi maqueta gratis").replace(
    "See pricing", "Ver precios").replace('href="contact.html"', 'href="es/contact.html"').replace('href="pricing.html"', 'href="es/pricing.html"')
GUIDE_PAGES = build_guides(GUIDES, "en", cta()) + build_guides(GUIDES_FR, "fr", CTA_FR) + build_guides(GUIDES_ES, "es", CTA_ES)

# ------------------------------------------------------------------------------------------------ landing pages
from _landing import build_landing
LANDING = build_landing(page, head, cta, faq_html, guide_card, GUIDES, ba, EXD, ic)  # Australia: English only
TOOL_PAGES = []
for _lang, _cta in (("en", cta()), ("fr", CTA_FR), ("es", CTA_ES)):
    for _key, _name in build_tools(page, head, _cta, _lang):
        same_page("tool:" + _key, _lang, _name)
        TOOL_PAGES.append(_name)
# ------------------------------------------------------------------------------------------------ Spanish site pages
from _site_es import build_site_es
build_site_es(page, head, ic, floaty, faq_html, guide_card, GUIDES_ES)
# ------------------------------------------------------------------------------------------------ referral program
from _referral import build_referral
REFERRAL_PAGES = []
for _lang, _name in build_referral(page, head, ic, faq_html, {"en": cta(), "fr": CTA_FR, "es": CTA_ES}):
    same_page("referral", _lang, _name)
    REFERRAL_PAGES.append(_name)
# ------------------------------------------------------------------------------------------------ rider partners
from _rider import build_rider
RIDER_PAGES = build_rider(page, head, ic, faq_html, cta())
# ------------------------------------------------------------------------------------------------ free page check
from _check import CTA as CHECK_CTA, build_check, cta_strip
CHECK_PAGES = []
for _lang, _name in build_check(page, head, ic, faq_html, {"en": cta(), "fr": CTA_FR, "es": CTA_ES}):
    same_page("check", _lang, _name)
    CHECK_PAGES.append(_name)
CHECK_HOME = {"en": "check.html", "fr": "fr/check.html", "es": "es/check.html"}
CHECK_ON = ("index.html", "fr/index.html", "es/index.html", "guides/", "fr/guides/", "es/guias/", "tools/", "fr/outils/",
            "es/herramientas/")


def add_check_cta():
    """The "Free Uber Eats page check" button on the home pages, every guide and both free tools, in each language,
    right under the page's first header. Marked, so a rebuild replaces it instead of adding a second one."""
    import os
    for f in sorted(ROOT.rglob("*.html")):
        path = f.relative_to(ROOT).as_posix()
        if not (path in CHECK_ON[:3] or path.startswith(CHECK_ON[3:])):
            continue
        html = re.sub(r"\n?<!--check-cta-->.*?<!--/check-cta-->", "", f.read_text(), flags=re.S)
        lang = _lang_of(path)
        href = os.path.relpath(CHECK_HOME[lang], os.path.dirname(path) or ".")
        html = html.replace("</header>", "</header>\n" + cta_strip(lang, href), 1)
        f.write_text(html)


TOP = ["index.html", "services.html", "examples.html", "how-it-works.html", "pricing.html", "about.html", "faq.html",
       "contact.html", "privacy.html", "terms.html"]
for _name in TOP + ["404.html"]:
    for _lang, _pre in (("en", ""), ("fr", "fr/"), ("es", "es/")):
        same_page("top:" + _name, _lang, _pre + _name)
# ------------------------------------------------------------------------------------------------ languages
add_check_cta()
from _guarantee import add_guarantee
add_guarantee(ROOT, _lang_of)
add_chrome_extras()
add_languages()
# ------------------------------------------------------------------------------------------------ payment pages
# Our own payment page: the order summary, and Stripe's card form inside our page (Checkout embedded). The server
# (admin.getmenufix.com/api/public/pay) makes the Checkout Session; without the publishable key it sends to Stripe.
NOINDEX = '\n<meta name="robots" content="noindex">'
page("pay.html", "Secure payment | MenuFix", "Pay for your MenuFix order securely.",
"""<section style="padding-top:50px"><div class="wrap pay">
  <div class="pay-sum reveal in">
    <span class="eyebrow">Your order</span>
    <h1 id="payName" style="font-size:40px;margin-top:10px">MenuFix</h1>
    <p class="muted" id="payLine" style="margin-top:8px"></p>
    <div class="pay-price"><span id="payPrice"></span><small id="payOnce" class="muted"></small></div>
    <ul id="payList"></ul>
    <div class="pay-trust"><div><img src="img/icons/check.png" alt=""><span>Secure card payment by Stripe. We never see your card.</span></div>
      <div><img src="img/icons/star.png" alt=""><span>An invoice by email for your accounts.</span></div>
      <div><img src="img/icons/phone.png" alt=""><span>Questions? Reply to our email or write to <a class="mailto" href="#">hello@getmenufix.com</a>.</span></div></div>
  </div>
  <div class="pay-box"><div id="checkout"><div class="pay-wait"><span class="spin"></span> Loading the secure payment form…</div></div></div>
</div></section>
<script src="https://js.stripe.com/endive/stripe.js"></script>
<script>
const PAY_API = "https://admin.getmenufix.com/api/public/pay";
const PAY_INFO = {
  full_makeover: ["Uber Eats Makeover", "Your whole Uber Eats page, done for you.", ["Every dish rewritten to sell", "Your real photos enhanced, whole menu", "Best sellers first and a clear menu order", "A prices and combos check", "We make every change for you", "One month of updates"]],
  makeover_google: ["Makeover and Google", "Found on Uber Eats and on Google.", ["Everything in the Uber Eats Makeover", "Your Google Business Profile set up", "Your best real photos on Google", "An order button on Google", "Google review auto replies, first month"]],
  complete: ["Complete", "Uber Eats, Google and your own website.", ["Everything in Makeover and Google", "Your own website in your style", "Menu with photos and an order button", "Your web address connected", "First year of hosting included"]],
  growth_plan: ["Growth Plan", "Everything kept fresh and working, every month.", ["Menu, prices and photos kept up to date", "Replies to your Uber Eats and Google reviews", "Wrong refunds disputed for you", "Offers and ads checked", "Your website kept up to date", "A monthly report"]],
};
const MONTHLY = ["growth_plan"];
window.addEventListener("load", async () => {
  const q = new URLSearchParams(location.search), key = q.get("p") || "", ref = q.get("ref") || "";
  const founding = key.endsWith("_founding"), base = key.replace(/_founding$/, "");
  const info = PAY_INFO[base] && (founding ? [PAY_INFO[base][0] + ", founding price", "30% off as one of our founding restaurants.", PAY_INFO[base][2]] : PAY_INFO[base]);
  const box = document.getElementById("checkout");
  if (!info) { box.innerHTML = '<p class="muted">This payment link is not valid. Please reply to our email and we will send you a new one.</p>'; return; }
  document.getElementById("payName").textContent = info[0];
  document.getElementById("payLine").textContent = info[1];
  document.getElementById("payList").innerHTML = info[2].map((x) => "<li>" + x + "</li>").join("");
  const n = (PRICES[key] || PRICES[base])[CUR];
  document.getElementById("payPrice").textContent = SYM[CUR] + n;
  document.getElementById("payOnce").textContent = MONTHLY.includes(key) ? " a month, cancel any time" : " one time, no subscription";
  try {
    const r = await fetch(PAY_API, { method: "POST", headers: { "Content-Type": "text/plain;charset=utf-8" }, body: JSON.stringify({ p: key, ref, from: (() => { try { return sessionStorage.getItem("mf_from") || document.referrer || ""; } catch (e) { return document.referrer || ""; } })() }) });
    const d = await r.json();
    if (d.url) { box.innerHTML = '<a class="btn primary" style="width:100%" href="' + d.url + '">Pay securely with Stripe <span class="arr">→</span></a>'; return; }
    if (!d.clientSecret) throw new Error(d.error || "no session");
    const stripe = Stripe(d.publishableKey);
    box.innerHTML = "";
    const checkout = await stripe.createEmbeddedCheckoutPage({ fetchClientSecret: async () => d.clientSecret });
    checkout.mount("#checkout");
  } catch (e) {
    box.innerHTML = '<p class="muted">The payment form could not load. Please refresh the page, or reply to our email and we will help.</p>';
  }
});
</script>""", ld_extra=NOINDEX)
page("paid.html", "Thank you | MenuFix", "Your payment is confirmed.",
"""<section style="padding-top:70px"><div class="narrow" style="text-align:center">
  <img src="img/icons/check.png" alt="" style="width:110px;margin:0 auto">
  <h1 id="paidTitle" style="margin-top:18px">Thank you</h1>
  <p class="lead" id="paidText" style="margin:14px auto 0">Checking your payment…</p>
  <p class="muted" style="margin-top:22px">Your invoice is on its way by email. Questions? Write to <a class="mailto" href="#">hello@getmenufix.com</a>.</p>
</div></section>
<script>
window.addEventListener("load", async () => {
  const s = new URLSearchParams(location.search).get("s") || "";
  const t = document.getElementById("paidText");
  try {
    const r = await fetch("https://admin.getmenufix.com/api/public/paid", { method: "POST", headers: { "Content-Type": "text/plain;charset=utf-8" }, body: JSON.stringify({ s }) });
    const d = await r.json();
    if (d.status === "complete") t.textContent = "Your payment for " + (d.package || "your order") + " is confirmed. Sam will email you within one working day to get started.";
    else { t.textContent = "Your payment was not finished. You can try again."; history.length > 1 && setTimeout(() => history.back(), 2500); }
  } catch (e) { t.textContent = "Thank you. Sam will email you within one working day to get started."; }
});
</script>""", ld_extra=NOINDEX)


# ------------------------------------------------------------------------------------------------ sitemap
URLS = (TOP + ["uber-eats-menu-makeover-service.html"] + RIDER_PAGES + ["fr/" + p for p in TOP] + ["es/" + p for p in TOP] + REFERRAL_PAGES + CHECK_PAGES + GUIDE_PAGES + TOOL_PAGES + LANDING)
(ROOT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
    "".join(f"  <url><loc>{_url(u)}</loc><lastmod>2026-10-13</lastmod></url>\n" for u in URLS) + "</urlset>\n")
print("built pages")


# ------------------------------------------------------------------------------------------------ clean addresses
def clean_index_links():
    """Links and addresses never end in index.html (getmenufix.com/, getmenufix.com/guides/): GitHub Pages serves
    the folder's index.html by itself. Run last, over every page any step above wrote (and the sitemap)."""
    def fix(s):
        s = re.sub(r'((?:href|content)=")index\.html(?=["#?])', r'\1./', s)   # the page next to it: "./"
        return re.sub(r'(?<=/)index\.html(?=["#?<])', "", s)                  # "guides/index.html" -> "guides/"
    for f in list(ROOT.rglob("*.html")) + [ROOT / "sitemap.xml"]:
        if any(part.startswith((".", "_")) for part in f.relative_to(ROOT).parts) or not f.is_file():
            continue
        s = f.read_text()
        n = fix(s)
        if n != s:
            f.write_text(n)


clean_index_links()
