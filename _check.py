"""The free "Uber Eats page check" in English, French and Spanish: check.html, fr/check.html, es/check.html.
Built by _build.py. A restaurant sends its Uber Eats store link and gets, by email within 24 hours, a score for its page
and the 3 fixes that matter most. Free, no login, no card.

The form (site.js, #checkForm) posts to the Google Apps Script web app MenuFix already uses (CHECK_URL at the top of
site.js, the only place the address is written). The script only appends one validated row to the "Page checks" tab.
The consent sentence next to the box is the same text MenuFix keeps with the email (studio/page_check.py CONSENT)."""

PAGES = {
    "en": {
        "name": "check.html",
        "title": "Free Uber Eats Page Check: Your Score and 3 Fixes | MenuFix",
        "desc": "Send us your Uber Eats store link and get a free page check by email within 24 hours: a score for your page and the 3 fixes that matter most. No login, no card.",
        "eyebrow": "Free Uber Eats page check", "h1": "How good is your Uber Eats page? <span class='hl'>Free check.</span>",
        "lead": "Send us your store link. Within 24 hours you get an email with a score for your page and the 3 fixes that matter most. Free, no login, no card.",
        "get": "What you get", "get_h": "Plain answers about your own page.",
        "cards": [("star", "A score out of 100", "Worked out only from what we can see on your page: photos, descriptions, categories, dish names and the cover photo. Every part of the score is shown."),
                  ("pen", "The 3 fixes that matter most", "With the names of your own dishes, so you know exactly where to start. You can make the changes yourself."),
                  ("phone", "By email within 24 hours", "No login, no card and nothing to install. When we have one ready, a Concept mockup of how your page could look comes with it.")],
        "link": "Where to find your store link", "link_h": "Copy your store link first.", "link_steps": [
            "Open your restaurant in the Uber Eats app or on ubereats.com, as a customer would.",
            "In the app, tap Share and then Copy link. On a computer, copy the address at the top of the browser.",
            "Paste it in the form. It looks like ubereats.com, then store, then your restaurant's name."],
        "form_h": "Get my free page check", "form_lead": "Free, no login, no card. By email within 24 hours.",
        "f_url": "Your Uber Eats store link", "p_url": "https://www.ubereats.com/au/store/your-restaurant/...",
        "f_name": "Restaurant name", "p_name": "For example Little Saigon Kitchen",
        "f_email": "Email", "p_email": "you@yourrestaurant.com", "f_first": "Your first name (optional)", "p_first": "",
        "consent": "Send me my page check by email",
        "privacy": "We use your email only for your page check. See our <a href='privacy.html'>privacy policy</a>.",
        "send": "Send me my free check",
        "thanks_h": "Thank you, it's on its way.",
        "thanks": "You'll get your page check by email within 24 hours. If you don't see it, look in your spam folder.",
        "bad_url": "That doesn't look like an Uber Eats store link. Open your restaurant on Uber Eats, copy its link and paste it here.",
        "error": "Sorry, something went wrong. Please try again in a minute, or email us at hello@getmenufix.com.",
        "faq_h": "Questions",
        "faq": [("Is it really free?", "Yes. There is no card, no login and nothing to buy. You get your page check by email."),
                ("Do you need access to my Uber Eats account?", "No. We only look at your public Uber Eats page, the same page your customers see."),
                ("What happens after the check?", "Nothing, unless you want help. If you'd like us to make the fixes for you, just reply to the email. Otherwise you'll get at most one short follow up."),
                ("How is the score worked out?", "Only from facts on your page: how many dishes have a photo and a description, how many categories your menu has, whether any dish name is used twice and whether your page has a cover photo. The email shows each part.")],
    },
    "fr": {
        "name": "fr/check.html",
        "title": "Analyse gratuite de votre page Uber Eats : score et 3 améliorations | MenuFix",
        "desc": "Envoyez le lien de votre restaurant sur Uber Eats et recevez une analyse gratuite par email sous 24 heures : un score pour votre page et les 3 améliorations les plus importantes. Sans compte, sans carte.",
        "eyebrow": "Analyse gratuite de votre page Uber Eats", "h1": "Votre page Uber Eats est elle à la hauteur ? <span class='hl'>Analyse gratuite.</span>",
        "lead": "Envoyez nous le lien de votre restaurant. Sous 24 heures, vous recevez un email avec un score pour votre page et les 3 améliorations les plus importantes. Gratuit, sans compte, sans carte.",
        "get": "Ce que vous recevez", "get_h": "Des réponses claires sur votre propre page.",
        "cards": [("star", "Un score sur 100", "Calculé uniquement à partir de ce que nous voyons sur votre page : photos, descriptions, catégories, noms des plats et photo de couverture. Chaque partie du score est détaillée."),
                  ("pen", "Les 3 améliorations les plus importantes", "Avec les noms de vos propres plats, pour savoir exactement par où commencer. Vous pouvez faire les changements vous même."),
                  ("phone", "Par email sous 24 heures", "Sans compte, sans carte et rien à installer. Quand nous en avons une prête, une Maquette concept de votre page l'accompagne.")],
        "link": "Où trouver le lien de votre restaurant", "link_h": "Copiez d'abord le lien de votre restaurant.", "link_steps": [
            "Ouvrez votre restaurant dans l'application Uber Eats ou sur ubereats.com, comme un client.",
            "Dans l'application, touchez Partager puis Copier le lien. Sur un ordinateur, copiez l'adresse en haut du navigateur.",
            "Collez le dans le formulaire. Il contient ubereats.com, puis store, puis le nom de votre restaurant."],
        "form_h": "Recevoir mon analyse gratuite", "form_lead": "Gratuit, sans compte, sans carte. Par email sous 24 heures.",
        "f_url": "Le lien de votre restaurant sur Uber Eats", "p_url": "https://www.ubereats.com/fr/store/votre-restaurant/...",
        "f_name": "Nom du restaurant", "p_name": "Par exemple Le Petit Bistrot",
        "f_email": "Email", "p_email": "vous@votrerestaurant.fr", "f_first": "Votre prénom (facultatif)", "p_first": "",
        "consent": "Envoyez moi l'analyse de ma page par email",
        "privacy": "Nous utilisons votre email uniquement pour votre analyse. Voir notre <a href='privacy.html'>politique de confidentialité</a>.",
        "send": "Recevoir mon analyse gratuite",
        "thanks_h": "Merci, c'est en route.",
        "thanks": "Vous recevrez l'analyse de votre page par email sous 24 heures. Si vous ne la voyez pas, regardez dans vos courriers indésirables.",
        "bad_url": "Ce lien ne ressemble pas au lien d'un restaurant sur Uber Eats. Ouvrez votre restaurant sur Uber Eats, copiez son lien et collez le ici.",
        "error": "Désolé, une erreur s'est produite. Réessayez dans une minute, ou écrivez nous à hello@getmenufix.com.",
        "faq_h": "Questions fréquentes",
        "faq": [("Est ce vraiment gratuit ?", "Oui. Pas de carte, pas de compte, rien à acheter. Vous recevez l'analyse de votre page par email."),
                ("Avez vous besoin d'accéder à mon compte Uber Eats ?", "Non. Nous regardons seulement votre page publique sur Uber Eats, celle que voient vos clients."),
                ("Que se passe t il après l'analyse ?", "Rien, sauf si vous voulez de l'aide. Si vous souhaitez que nous fassions les améliorations pour vous, répondez simplement à l'email. Sinon, vous recevrez au plus une courte relance."),
                ("Comment le score est il calculé ?", "Uniquement à partir de faits visibles sur votre page : combien de plats ont une photo et une description, combien de catégories compte votre menu, si un nom de plat apparaît deux fois et si votre page a une photo de couverture. L'email détaille chaque partie.")],
    },
    "es": {
        "name": "es/check.html",
        "title": "Análisis gratis de su página de Uber Eats: puntuación y 3 mejoras | MenuFix",
        "desc": "Envíe el enlace de su restaurante en Uber Eats y reciba un análisis gratis por correo en 24 horas: una puntuación para su página y las 3 mejoras que más importan. Sin registro ni tarjeta.",
        "eyebrow": "Análisis gratis de su página de Uber Eats", "h1": "¿Qué tal está su página de Uber Eats? <span class='hl'>Análisis gratis.</span>",
        "lead": "Envíenos el enlace de su restaurante. En 24 horas recibirá un correo con una puntuación para su página y las 3 mejoras que más importan. Gratis, sin registro y sin tarjeta.",
        "get": "Qué recibe", "get_h": "Respuestas claras sobre su propia página.",
        "cards": [("star", "Una puntuación sobre 100", "Calculada solo con lo que vemos en su página: fotos, descripciones, categorías, nombres de los platos y foto de portada. Cada parte de la puntuación aparece detallada."),
                  ("pen", "Las 3 mejoras que más importan", "Con los nombres de sus propios platos, para saber exactamente por dónde empezar. Puede hacer los cambios usted mismo."),
                  ("phone", "Por correo en 24 horas", "Sin registro, sin tarjeta y sin instalar nada. Cuando tenemos una lista, la acompaña una maqueta conceptual de su página.")],
        "link": "Dónde encontrar el enlace de su restaurante", "link_h": "Primero copie el enlace de su restaurante.", "link_steps": [
            "Abra su restaurante en la aplicación de Uber Eats o en ubereats.com, como lo haría un cliente.",
            "En la aplicación, toque Compartir y luego Copiar enlace. En un ordenador, copie la dirección de la parte de arriba del navegador.",
            "Péguelo en el formulario. Contiene ubereats.com, luego store y después el nombre de su restaurante."],
        "form_h": "Quiero mi análisis gratis", "form_lead": "Gratis, sin registro y sin tarjeta. Por correo en 24 horas.",
        "f_url": "El enlace de su restaurante en Uber Eats", "p_url": "https://www.ubereats.com/es/store/su-restaurante/...",
        "f_name": "Nombre del restaurante", "p_name": "Por ejemplo Casa Lola",
        "f_email": "Correo electrónico", "p_email": "usted@surestaurante.es", "f_first": "Su nombre (opcional)", "p_first": "",
        "consent": "Envíenme el análisis de mi página por correo",
        "privacy": "Usamos su correo solo para su análisis. Vea nuestra <a href='privacy.html'>política de privacidad</a>.",
        "send": "Quiero mi análisis gratis",
        "thanks_h": "Gracias, ya está en camino.",
        "thanks": "Recibirá el análisis de su página por correo en 24 horas. Si no lo ve, mire en la carpeta de correo no deseado.",
        "bad_url": "Ese enlace no parece el de un restaurante en Uber Eats. Abra su restaurante en Uber Eats, copie su enlace y péguelo aquí.",
        "error": "Lo sentimos, algo ha fallado. Inténtelo de nuevo en un minuto o escríbanos a hello@getmenufix.com.",
        "faq_h": "Preguntas frecuentes",
        "faq": [("¿Es gratis de verdad?", "Sí. Sin tarjeta, sin registro y sin comprar nada. Recibe el análisis de su página por correo."),
                ("¿Necesitan acceso a mi cuenta de Uber Eats?", "No. Solo miramos su página pública de Uber Eats, la misma que ven sus clientes."),
                ("¿Qué pasa después del análisis?", "Nada, salvo que quiera ayuda. Si quiere que hagamos las mejoras por usted, responda al correo. Si no, recibirá como mucho un breve recordatorio."),
                ("¿Cómo se calcula la puntuación?", "Solo con datos de su página: cuántos platos tienen foto y descripción, cuántas categorías tiene su carta, si algún nombre de plato se repite y si su página tiene foto de portada. El correo muestra cada parte.")],
    },
}

# The button on the home page, the guides and the free tools ("Free Uber Eats page check").
CTA = {
    "en": ("Free Uber Eats page check", "A score for your page and the 3 fixes that matter most, by email within 24 hours. No login, no card."),
    "fr": ("Analyse gratuite de votre page Uber Eats", "Un score pour votre page et les 3 améliorations les plus importantes, par email sous 24 heures. Sans compte, sans carte."),
    "es": ("Análisis gratis de su página de Uber Eats", "Una puntuación para su página y las 3 mejoras que más importan, por correo en 24 horas. Sin registro ni tarjeta."),
}


# The instant check (22 Oct 2026): screenshots in, the score and the biggest problems out in about a minute
# (admin.getmenufix.com/api/public/instant_check, studio/instant_check.py), and the PDF report by email.
INSTANT = """<section class="tight" id="instant"><div class="wrap split" style="align-items:start">
  <div class="reveal"><span class="eyebrow">New · in about a minute</span><h2>Get your score now</h2>
    <p class="lead" style="margin-top:14px">Send us 2 to 5 screenshots of your Uber Eats page and see your score and what to fix first, right here.
    The full report comes by email.</p>
    <ol class="ticks"><li>Open your restaurant in the Uber Eats app, as a customer would</li>
      <li>Take a screenshot at the top, then scroll and take 1 to 4 more down your menu</li>
      <li>Add them here, with your name and email</li></ol></div>
  <div class="card reveal" style="padding:36px">
    <form id="instantForm" novalidate>
      <div class="f"><label for="iShots">Your screenshots (2 to 5)</label><input id="iShots" type="file" accept="image/*" multiple required></div>
      <div class="f"><label for="iName">Restaurant name</label><input id="iName" required maxlength="100" autocomplete="organization"></div>
      <div class="f"><label for="iEmail">Your email</label><input id="iEmail" type="email" required maxlength="120" autocomplete="email"></div>
      <div class="f"><label for="iFirst">Your first name (optional)</label><input id="iFirst" maxlength="40" autocomplete="given-name"></div>
      <div class="hp" aria-hidden="true"><label for="iSite">Website</label><input id="iSite" tabindex="-1" autocomplete="off"></div>
      <label class="consent"><input id="iConsent" type="checkbox" required> <span>Email me my page check and the free mockup offer</span></label>
      <p class="err" id="iErr" role="alert" hidden></p>
      <button class="btn primary" type="submit" style="width:100%">Check my page now <span class="arr">→</span></button>
      <p class="note" style="margin:14px 0 0">Your screenshots are only used for your report. No login, no card.</p>
    </form>
    <div id="instantWait" class="thanks" hidden><h3>Reading your page…</h3><p>About 30 seconds. Don't close this page.</p></div>
    <div id="instantResult" hidden></div>
  </div>
</div></section>"""


def build_check(page, head, ic, faq_html, ctas) -> list[tuple[str, str]]:
    """Write the three pages. Returns (lang, path) pairs."""
    import html as h
    import json
    out = []
    for lang, t in PAGES.items():
        cards = "".join(f'<div class="card reveal">{ic(i)}<h3>{a}</h3><p>{b}</p></div>' for i, a, b in t["cards"])
        steps = "".join(f"<li>{x}</li>" for x in t["link_steps"])
        msgs = " ".join(f'data-{k}="{h.escape(t[k], quote=True)}"' for k in ("bad_url", "error"))
        ld = '\n<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in t["faq"]]}, ensure_ascii=False) + "</script>"
        page(t["name"], t["title"], t["desc"], f"""{head(t["eyebrow"], t["h1"], t["lead"], ("star", "menu"),
            f'<div class="row" style="margin-top:26px"><a class="btn primary" href="#check">{t["form_h"]} <span class="arr">→</span></a></div>')}

<section class="tight"><div class="wrap">
  <div class="head center reveal"><span class="eyebrow">{t["get"]}</span><h2>{t["get_h"]}</h2></div>
  <div class="grid3">{cards}</div>
</div></section>

{INSTANT if lang == "en" else ""}
<section class="bg-butter" id="check"><div class="wrap split" style="align-items:start">
  <div class="reveal"><span class="eyebrow">{t["link"]}</span><h2>{t["link_h"]}</h2>
    <ol class="ticks">{steps}</ol></div>
  <div class="card reveal" style="padding:40px">
    <h3 style="margin-bottom:6px">{t["form_h"]}</h3><p class="note" style="margin:0 0 20px">{t["form_lead"]}</p>
    <form id="checkForm" data-lang="{lang}" {msgs} novalidate>
      <div class="f"><label for="cUrl">{t["f_url"]}</label><input id="cUrl" type="url" inputmode="url" required placeholder="{t["p_url"]}" autocomplete="off"></div>
      <div class="f"><label for="cName">{t["f_name"]}</label><input id="cName" required maxlength="100" placeholder="{t["p_name"]}" autocomplete="organization"></div>
      <div class="f"><label for="cEmail">{t["f_email"]}</label><input id="cEmail" type="email" required maxlength="120" placeholder="{t["p_email"]}" autocomplete="email"></div>
      <div class="f"><label for="cFirst">{t["f_first"]}</label><input id="cFirst" maxlength="40" autocomplete="given-name"></div>
      <div class="hp" aria-hidden="true"><label for="cSite">Website</label><input id="cSite" tabindex="-1" autocomplete="off"></div>
      <label class="consent"><input id="cConsent" type="checkbox" required> <span>{t["consent"]}</span></label>
      <p class="err" id="cErr" role="alert" hidden></p>
      <button class="btn primary" type="submit" style="width:100%">{t["send"]} <span class="arr">→</span></button>
      <p class="note" style="margin:14px 0 0">{t["privacy"]}</p>
    </form>
    <div id="checkThanks" class="thanks" hidden><h3>{t["thanks_h"]}</h3><p>{t["thanks"]}</p></div>
  </div>
</div></section>

<section class="bg-cream"><div class="narrow">
  <div class="head center reveal" style="margin-bottom:30px"><h2>{t["faq_h"]}</h2></div>
  {faq_html(t["faq"])}
</div></section>
{ctas[lang]}
""", "", lang=lang, ld_extra=ld)
        out.append((lang, t["name"]))
    return out


def cta_strip(lang: str, href: str) -> str:
    """The "Free Uber Eats page check" button under the first header of a page (marked, so a rebuild replaces it)."""
    title, text = CTA[lang]
    return (f'<!--check-cta--><section class="checkcta"><div class="wrap"><div class="checkcta-in reveal">'
            f'<div><b>{title}</b><span>{text}</span></div>'
            f'<a class="btn primary" href="{href}">{title} <span class="arr">→</span></a></div></div></section><!--/check-cta-->')
