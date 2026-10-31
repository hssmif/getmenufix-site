"""The free "Uber Eats page check" in English, French and Spanish: check.html, fr/check.html, es/check.html.
Built by _build.py.

31 Oct 2026, Abdel: one free page check (the free mockup and the page check in one), fast, with a wow: a restaurant
pastes its Uber Eats store link and sees a live progress screen while we read their page (about 30 seconds), then its
result right on the page: the score counting up, today against after the fix, what customers see today (their real
dishes with no photo), how the score is made and the 3 fixes. The full report follows by email in about 10 minutes:
the PDF and their page today next to how it will look after we fix it.

The form (site.js, #liveForm) posts to admin.getmenufix.com/api/public/live_check (studio/live_check.py). The consent
sentence next to the box is the same text MenuFix keeps with the email (studio/page_check.py CONSENT). Every word the
script shows is in the page (the #liveText JSON), so the script itself has no language."""

PAGES = {
    "en": {
        "name": "check.html",
        "title": "Free Uber Eats Page Check: Your Score in 30 Seconds | MenuFix",
        "desc": "Paste your Uber Eats store link and see your page score in 30 seconds: photos, descriptions, menu and the 3 fixes that matter most. Then your before and after by email. Free, no login, no card.",
        "eyebrow": "Free Uber Eats page check",
        "h1": "Your Uber Eats page score <span class='hl'>in 30 seconds.</span>",
        "lead": "Paste your Uber Eats link. See your score, what customers see today and what to fix first, right here. Then we email you your page today next to how it will look after we fix it.",
        "trust": ["Free, no card", "No login", "Your real Uber Eats page"],
        "form_h": "Check my page now", "form_lead": "Your score shows on this page in about 30 seconds.",
        "f_url": "Your Uber Eats store link", "p_url": "https://www.ubereats.com/au/store/your-restaurant/...",
        "f_email": "Your email", "p_email": "you@yourrestaurant.com", "f_first": "Your first name (optional)",
        "consent": "Send me my page check by email",
        "privacy": "We use your email only for your page check. See our <a href='privacy.html'>privacy policy</a>.",
        "send": "Check my page now",
        "find": "Where do I find my link?", "find_steps": [
            "Open your restaurant in the Uber Eats app or on ubereats.com, as a customer would.",
            "In the app, tap Share and then Copy link. On a computer, copy the address at the top of the browser.",
            "Paste it above. It looks like ubereats.com, then store, then your restaurant's name."],
        "get": "What you get", "get_h": "A real check of your real page.",
        "cards": [("star", "Your score in 30 seconds", "Counted on your real Uber Eats page: photos, descriptions, categories, dish names and the cover photo. Every part is shown."),
                  ("pen", "The 3 fixes that matter most", "With the names of your own dishes, so you know exactly where to start."),
                  ("phone", "Your before and after by email", "Your page today next to how it will look after we fix it, with a PDF report. Free, no card.")],
        "faq_h": "Questions",
        "faq": [("Is it really free?", "Yes. No card, no login and nothing to buy. You see your score on the page and get the full report by email."),
                ("Do you need access to my Uber Eats account?", "No. We only look at your public Uber Eats page, the same page your customers see."),
                ("How is the score worked out?", "Only from facts on your page: how many dishes have a photo and a description, how many categories your menu has, whether a dish name is used twice and whether your page has a cover photo. Every part is shown."),
                ("Do you use AI photos?", "Never on your menu. Your before and after can show example photos marked Example, so you can see the look. We replace every one with your own food once you send us your photos or order."),
                ("What happens after the check?", "Nothing, unless you want help. If you'd like us to make the fixes for you, just reply to the email. Otherwise you'll get at most one short follow up.")],
        "live": {
            "wait_h": "Checking your Uber Eats page", "wait_p": "About 30 seconds. Keep this page open.",
            "steps": ["Opening your Uber Eats page", "Counting your dish photos", "Reading your descriptions",
                      "Checking your menu and categories", "Working out your score"],
            "eyebrow": "Your Uber Eats page check", "score": "Your page score", "of": "out of 100",
            "levels": {"good": "Strong page", "mid": "Room to grow", "low": "Losing orders"},
            "now": "Today", "then": "After the fix", "could": "Your page could score {p}.", "strong_h": "Your page is in good shape.",
            "hook": "Add a photo and a description that sells to every dish, and your page scores {p} out of 100.",
            "t_photo": "dishes show no photo", "t_desc": "dishes have no real description", "t_goal": "of your dishes meet Uber Eats' goal of {goal}%",
            "of_n": "of {n}", "see": "What your customers see today", "nophoto": "No photo",
            "parts": "How your score is made", "fixes": "The 3 fixes that matter most",
            "next_h": "Your before and after is on its way",
            "next": "In about 10 minutes we email you the full report: your page today next to how it will look after we fix it, and the PDF.",
            "spam": "Not in your inbox? Look in spam or promotions.",
            "yes": "Yes, fix my page", "yes_subject": "Yes, fix my Uber Eats page", "prices": "See prices",
            "strong": "Your page is in good shape. Small things still help: a photo and a short line that sells for every dish.",
            "error": "Sorry, something went wrong. Please try again in a minute, or email us at hello@getmenufix.com.",
            "bad_url": "That doesn't look like an Uber Eats store link. Open your restaurant on Uber Eats, copy its link and paste it here.",
            "again": "Check another page"},
    },
    "fr": {
        "name": "fr/check.html",
        "title": "Analyse gratuite de votre page Uber Eats : votre score en 30 secondes | MenuFix",
        "desc": "Collez le lien de votre restaurant sur Uber Eats et voyez le score de votre page en 30 secondes : photos, descriptions, menu et les 3 améliorations les plus importantes. Puis votre avant et après par email. Gratuit, sans compte, sans carte.",
        "eyebrow": "Analyse gratuite de votre page Uber Eats",
        "h1": "Le score de votre page Uber Eats <span class='hl'>en 30 secondes.</span>",
        "lead": "Collez le lien de votre restaurant sur Uber Eats. Voyez votre score, ce que vos clients voient aujourd'hui et quoi améliorer en premier, ici même. Puis nous vous envoyons votre page aujourd'hui à côté de son rendu après notre travail.",
        "trust": ["Gratuit, sans carte", "Sans compte", "Votre vraie page Uber Eats"],
        "form_h": "Analyser ma page", "form_lead": "Votre score s'affiche sur cette page en 30 secondes environ.",
        "f_url": "Le lien de votre restaurant sur Uber Eats", "p_url": "https://www.ubereats.com/fr/store/votre-restaurant/...",
        "f_email": "Votre email", "p_email": "vous@votrerestaurant.fr", "f_first": "Votre prénom (facultatif)",
        "consent": "Envoyez moi l'analyse de ma page par email",
        "privacy": "Nous utilisons votre email uniquement pour votre analyse. Voir notre <a href='privacy.html'>politique de confidentialité</a>.",
        "send": "Analyser ma page",
        "find": "Où trouver mon lien ?", "find_steps": [
            "Ouvrez votre restaurant dans l'application Uber Eats ou sur ubereats.com, comme un client.",
            "Dans l'application, touchez Partager puis Copier le lien. Sur un ordinateur, copiez l'adresse en haut du navigateur.",
            "Collez le ci dessus. Il contient ubereats.com, puis store, puis le nom de votre restaurant."],
        "get": "Ce que vous recevez", "get_h": "Une vraie analyse de votre vraie page.",
        "cards": [("star", "Votre score en 30 secondes", "Calculé sur votre vraie page Uber Eats : photos, descriptions, catégories, noms des plats et photo de couverture. Chaque partie est détaillée."),
                  ("pen", "Les 3 améliorations les plus importantes", "Avec les noms de vos propres plats, pour savoir exactement par où commencer."),
                  ("phone", "Votre avant et après par email", "Votre page aujourd'hui à côté de son rendu après notre travail, avec un rapport PDF. Gratuit, sans carte.")],
        "faq_h": "Questions fréquentes",
        "faq": [("Est ce vraiment gratuit ?", "Oui. Pas de carte, pas de compte, rien à acheter. Vous voyez votre score sur la page et recevez le rapport complet par email."),
                ("Avez vous besoin d'accéder à mon compte Uber Eats ?", "Non. Nous regardons seulement votre page publique sur Uber Eats, celle que voient vos clients."),
                ("Comment le score est il calculé ?", "Uniquement à partir de faits visibles sur votre page : combien de plats ont une photo et une description, combien de catégories compte votre menu, si un nom de plat apparaît deux fois et si votre page a une photo de couverture. Chaque partie est détaillée."),
                ("Utilisez vous des photos faites par IA ?", "Jamais sur votre menu. Votre avant et après peut montrer des photos d'exemple marquées Example, pour voir le rendu. Nous les remplaçons toutes par vos vrais plats dès que vous nous envoyez vos photos ou commandez."),
                ("Que se passe t il après l'analyse ?", "Rien, sauf si vous voulez de l'aide. Si vous souhaitez que nous fassions les améliorations pour vous, répondez simplement à l'email. Sinon, vous recevrez au plus une courte relance.")],
        "live": {
            "wait_h": "Analyse de votre page Uber Eats", "wait_p": "Environ 30 secondes. Gardez cette page ouverte.",
            "steps": ["Ouverture de votre page Uber Eats", "Comptage des photos de vos plats", "Lecture de vos descriptions",
                      "Vérification de votre menu et des catégories", "Calcul de votre score"],
            "eyebrow": "L'analyse de votre page Uber Eats", "score": "Score de votre page", "of": "sur 100",
            "levels": {"good": "Page solide", "mid": "Marge de progression", "low": "Des commandes perdues"},
            "now": "Aujourd'hui", "then": "Après notre travail", "could": "Votre page pourrait atteindre {p}.", "strong_h": "Votre page est en bon état.",
            "hook": "Une photo et une description qui donne envie pour chaque plat, et votre page passe à {p} sur 100.",
            "t_photo": "plats sans photo", "t_desc": "plats sans vraie description", "t_goal": "de vos plats atteignent l'objectif d'Uber Eats de {goal} %",
            "of_n": "sur {n}", "see": "Ce que vos clients voient aujourd'hui", "nophoto": "Pas de photo",
            "parts": "Comment votre score est calculé", "fixes": "Les 3 améliorations les plus importantes",
            "next_h": "Votre avant et après arrive",
            "next": "Dans 10 minutes environ, nous vous envoyons le rapport complet : votre page aujourd'hui à côté de son rendu après notre travail, et le PDF.",
            "spam": "Pas dans votre boîte de réception ? Regardez dans les courriers indésirables ou promotions.",
            "yes": "Oui, améliorez ma page", "yes_subject": "Oui, améliorez ma page Uber Eats", "prices": "Voir les tarifs",
            "strong": "Votre page est en bon état. Les petites choses aident encore : une photo et une courte description qui donne envie pour chaque plat.",
            "error": "Désolé, une erreur s'est produite. Réessayez dans une minute, ou écrivez nous à hello@getmenufix.com.",
            "bad_url": "Ce lien ne ressemble pas au lien d'un restaurant sur Uber Eats. Ouvrez votre restaurant sur Uber Eats, copiez son lien et collez le ici.",
            "again": "Analyser une autre page"},
    },
    "es": {
        "name": "es/check.html",
        "title": "Análisis gratis de su página de Uber Eats: su puntuación en 30 segundos | MenuFix",
        "desc": "Pegue el enlace de su restaurante en Uber Eats y vea la puntuación de su página en 30 segundos: fotos, descripciones, carta y las 3 mejoras que más importan. Después, su antes y después por correo. Gratis, sin registro ni tarjeta.",
        "eyebrow": "Análisis gratis de su página de Uber Eats",
        "h1": "La puntuación de su página de Uber Eats <span class='hl'>en 30 segundos.</span>",
        "lead": "Pegue el enlace de su restaurante en Uber Eats. Vea su puntuación, lo que ven hoy sus clientes y qué mejorar primero, aquí mismo. Después le enviamos su página hoy junto a cómo quedará después de nuestro trabajo.",
        "trust": ["Gratis, sin tarjeta", "Sin registro", "Su página real de Uber Eats"],
        "form_h": "Analizar mi página", "form_lead": "Su puntuación aparece en esta página en unos 30 segundos.",
        "f_url": "El enlace de su restaurante en Uber Eats", "p_url": "https://www.ubereats.com/es/store/su-restaurante/...",
        "f_email": "Su correo", "p_email": "usted@surestaurante.es", "f_first": "Su nombre (opcional)",
        "consent": "Envíenme el análisis de mi página por correo",
        "privacy": "Usamos su correo solo para su análisis. Vea nuestra <a href='privacy.html'>política de privacidad</a>.",
        "send": "Analizar mi página",
        "find": "¿Dónde encuentro mi enlace?", "find_steps": [
            "Abra su restaurante en la aplicación de Uber Eats o en ubereats.com, como lo haría un cliente.",
            "En la aplicación, toque Compartir y luego Copiar enlace. En un ordenador, copie la dirección de la parte de arriba del navegador.",
            "Péguelo arriba. Contiene ubereats.com, luego store y después el nombre de su restaurante."],
        "get": "Qué recibe", "get_h": "Un análisis real de su página real.",
        "cards": [("star", "Su puntuación en 30 segundos", "Calculada en su página real de Uber Eats: fotos, descripciones, categorías, nombres de los platos y foto de portada. Cada parte aparece detallada."),
                  ("pen", "Las 3 mejoras que más importan", "Con los nombres de sus propios platos, para saber exactamente por dónde empezar."),
                  ("phone", "Su antes y después por correo", "Su página hoy junto a cómo quedará después de nuestro trabajo, con un informe en PDF. Gratis, sin tarjeta.")],
        "faq_h": "Preguntas frecuentes",
        "faq": [("¿Es gratis de verdad?", "Sí. Sin tarjeta, sin registro y sin comprar nada. Ve su puntuación en la página y recibe el informe completo por correo."),
                ("¿Necesitan acceso a mi cuenta de Uber Eats?", "No. Solo miramos su página pública de Uber Eats, la misma que ven sus clientes."),
                ("¿Cómo se calcula la puntuación?", "Solo con datos de su página: cuántos platos tienen foto y descripción, cuántas categorías tiene su carta, si algún nombre de plato se repite y si su página tiene foto de portada. Cada parte aparece detallada."),
                ("¿Usan fotos hechas con IA?", "Nunca en su carta. Su antes y después puede mostrar fotos de ejemplo marcadas Example, para que vea el resultado. Las cambiamos todas por sus platos reales cuando nos envíe sus fotos o haga su pedido."),
                ("¿Qué pasa después del análisis?", "Nada, salvo que quiera ayuda. Si quiere que hagamos las mejoras por usted, responda al correo. Si no, recibirá como mucho un breve recordatorio.")],
        "live": {
            "wait_h": "Analizando su página de Uber Eats", "wait_p": "Unos 30 segundos. Mantenga esta página abierta.",
            "steps": ["Abriendo su página de Uber Eats", "Contando las fotos de sus platos", "Leyendo sus descripciones",
                      "Revisando su carta y sus categorías", "Calculando su puntuación"],
            "eyebrow": "El análisis de su página de Uber Eats", "score": "Puntuación de su página", "of": "de 100",
            "levels": {"good": "Página sólida", "mid": "Margen de mejora", "low": "Pierde pedidos"},
            "now": "Hoy", "then": "Después", "could": "Su página podría llegar a {p}.", "strong_h": "Su página está en buen estado.",
            "hook": "Con una foto y una descripción que vende en cada plato, su página llega a {p} de 100.",
            "t_photo": "platos sin foto", "t_desc": "platos sin una descripción de verdad", "t_goal": "de sus platos cumplen el objetivo de Uber Eats del {goal} %",
            "of_n": "de {n}", "see": "Lo que ven hoy sus clientes", "nophoto": "Sin foto",
            "parts": "Cómo se calcula su puntuación", "fixes": "Las 3 mejoras que más importan",
            "next_h": "Su antes y después está en camino",
            "next": "En unos 10 minutos le enviamos el informe completo: su página hoy junto a cómo quedará después de nuestro trabajo, y el PDF.",
            "spam": "¿No está en su bandeja de entrada? Mire en spam o promociones.",
            "yes": "Sí, mejoren mi página", "yes_subject": "Sí, mejoren mi página de Uber Eats", "prices": "Ver precios",
            "strong": "Su página está en buen estado. Los detalles siguen ayudando: una foto y una frase que vende en cada plato.",
            "error": "Lo sentimos, algo ha fallado. Inténtelo de nuevo en un minuto o escríbanos a hello@getmenufix.com.",
            "bad_url": "Ese enlace no parece el de un restaurante en Uber Eats. Abra su restaurante en Uber Eats, copie su enlace y péguelo aquí.",
            "again": "Analizar otra página"},
    },
}

# The button on the home page, the guides and the free tools ("Free Uber Eats page check").
CTA = {
    "en": ("Free Uber Eats page check", "Your page score in 30 seconds, and your before and after by email. No login, no card."),
    "fr": ("Analyse gratuite de votre page Uber Eats", "Le score de votre page en 30 secondes, et votre avant et après par email. Sans compte, sans carte."),
    "es": ("Análisis gratis de su página de Uber Eats", "La puntuación de su página en 30 segundos, y su antes y después por correo. Sin registro ni tarjeta."),
}


def build_check(page, head, ic, faq_html, ctas) -> list[tuple[str, str]]:
    """Write the three pages. Returns (lang, path) pairs."""
    import json
    out = []
    for lang, t in PAGES.items():
        cards = "".join(f'<div class="card reveal">{ic(i)}<h3>{a}</h3><p>{b}</p></div>' for i, a, b in t["cards"])
        steps = "".join(f"<li>{x}</li>" for x in t["find_steps"])
        trust = "".join(f"<li>{x}</li>" for x in t["trust"])
        live = json.dumps(t["live"], ensure_ascii=False).replace("</", "<\\/")
        ld = '\n<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in t["faq"]]}, ensure_ascii=False) + "</script>"
        page(t["name"], t["title"], t["desc"], f"""<section class="lc-hero" id="lcStart"><div class="wrap lc-grid">
  <div class="lc-intro reveal"><span class="eyebrow">{t["eyebrow"]}</span><h1>{t["h1"]}</h1>
    <p class="lead">{t["lead"]}</p><ul class="lc-trust">{trust}</ul></div>
  <div class="card lc-card reveal">
    <h3>{t["form_h"]}</h3><p class="note" style="margin:4px 0 20px">{t["form_lead"]}</p>
    <form id="liveForm" data-lang="{lang}" novalidate>
      <div class="f"><label for="lUrl">{t["f_url"]}</label><input id="lUrl" type="url" inputmode="url" required placeholder="{t["p_url"]}" autocomplete="off"></div>
      <div class="f"><label for="lEmail">{t["f_email"]}</label><input id="lEmail" type="email" required maxlength="120" placeholder="{t["p_email"]}" autocomplete="email"></div>
      <div class="f"><label for="lFirst">{t["f_first"]}</label><input id="lFirst" maxlength="40" autocomplete="given-name"></div>
      <div class="hp" aria-hidden="true"><label for="lSite">Website</label><input id="lSite" tabindex="-1" autocomplete="off"></div>
      <label class="consent"><input id="lConsent" type="checkbox" required> <span>{t["consent"]}</span></label>
      <p class="err" id="lErr" role="alert" hidden></p>
      <button class="btn primary" type="submit" style="width:100%">{t["send"]} <span class="arr">→</span></button>
      <p class="note" style="margin:14px 0 0">{t["privacy"]}</p>
    </form>
    <details class="lc-find"><summary>{t["find"]}</summary><ol>{steps}</ol></details>
  </div>
</div></section>

<section class="lc-wait" id="lcWait" hidden><div class="narrow">
  <div class="lc-wait-in"><div class="lc-pulse"></div><h2 id="lcWaitH"></h2><p class="muted" id="lcWaitP"></p>
    <div class="lc-bar"><i id="lcBar"></i></div><ol class="lc-steps" id="lcSteps"></ol>
    <p class="err" id="lcWaitErr" hidden></p></div>
</div></section>

<section class="lc-result" id="lcResult" hidden></section>
<script type="application/json" id="liveText">{live}</script>

<section class="tight" id="lcGet"><div class="wrap">
  <div class="head center reveal"><span class="eyebrow">{t["get"]}</span><h2>{t["get_h"]}</h2></div>
  <div class="grid3">{cards}</div>
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
