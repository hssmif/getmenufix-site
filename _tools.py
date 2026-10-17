"""Free tools for restaurant owners, built by _build.py into tools/ (English), fr/outils/ and es/herramientas/.
Everything runs in the visitor's browser (code in site.js): photos and text are never uploaded or sent anywhere.
Rules: honest, every Uber fact links to Uber's own page for that country, no dashes or hyphens between words."""

MENU_PHOTO = "https://help.uber.com/en/merchants-and-restaurants/article/merchant-submitted-menu-catalog-photo-guidelines?nodeId=6985355b-0426-4523-94f2-89bb9b0566e9"
DESC_ADVICE = "https://www.uber.com/au/en/blog/6-ways-to-optimise-your-uber-eats-menu/"
MENU_PHOTO_FR = "https://help.uber.com/fr-FR/merchants-and-restaurants/article/merchant-submitted-menu-catalog-photo-guidelines?nodeId=6985355b-0426-4523-94f2-89bb9b0566e9"
MENU_INFO_FR = "https://help.uber.com/fr-FR/merchants-and-restaurants/article/quelles-informations-dois-je-fournir-concernant-mon-menu-pour-uber-eats?nodeId=83ae0158-34aa-45d7-9fff-6bab96354072"
MENU_PHOTO_ES = "https://help.uber.com/es-ES/merchants-and-restaurants/article/gu%C3%ADa-para-las-fotos-de-men%C3%BA-enviadas-por-el-restaurante?nodeId=6985355b-0426-4523-94f2-89bb9b0566e9"
MENU_INFO_ES = "https://help.uber.com/es-ES/merchants-and-restaurants/article/qu%C3%A9-informaci%C3%B3n-del-men%C3%BA-debo-proporcionar-para-uber-eats?nodeId=83ae0158-34aa-45d7-9fff-6bab96354072"

# key: the English slug, the same tool in every language
TOOLS = {
    "en": [
        {"key": "uber-eats-photo-checker", "slug": "uber-eats-photo-checker", "name": "Uber Eats photo checker",
         "short": "Check a dish photo against Uber's size rules and fix the shape in one click.",
         "title": "Free Uber Eats Photo Checker: Size, Ratio and File Type | MenuFix",
         "desc": "Check a menu photo against Uber Eats rules in your browser: 5:4 shape, at least 550 × 440 pixels, under 10 MB, JPG or PNG. Crop and resize to 2880 × 2304 in one click.",
         "icon": "camera"},
        {"key": "menu-description-checker", "slug": "menu-description-checker", "name": "Menu description checker",
         "short": "Paste a dish description: length, capitals, vague words and missing ingredients.",
         "title": "Free Uber Eats Menu Description Checker | MenuFix",
         "desc": "Paste an Uber Eats dish description and check it against Uber's 140 to 260 character advice. Flags ALL CAPS, vague words and descriptions that don't name the ingredients.",
         "icon": "pen"},
        {"key": "uber-eats-page-score", "slug": "uber-eats-page-score", "name": "Uber Eats page score",
         "short": "Answer 10 quick questions about your page and get your score and your 3 most important fixes now.",
         "title": "Free Uber Eats Page Score: Check Your Restaurant Page in 2 Minutes | MenuFix",
         "desc": "How good is your Uber Eats page? Answer 10 quick questions about your photos, descriptions, menu order and rating. Get a score out of 100 and your 3 most important fixes at once. Free.",
         "icon": "star"},
    ],
    "fr": [
        {"key": "uber-eats-photo-checker", "slug": "verificateur-photo-uber-eats", "name": "Vérificateur de photo Uber Eats",
         "short": "Vérifiez une photo de plat selon les règles de taille d'Uber et corrigez le format en un clic.",
         "title": "Vérificateur de photo Uber Eats gratuit : taille, format et fichier | MenuFix",
         "desc": "Vérifiez une photo de menu selon les règles Uber Eats, dans votre navigateur : format 5:4, au moins 550 × 440 pixels, moins de 10 Mo, JPG ou PNG. Recadrage en 2880 × 2304 en un clic.",
         "icon": "camera"},
        {"key": "menu-description-checker", "slug": "verificateur-description-menu", "name": "Vérificateur de description de plat",
         "short": "Collez une description : longueur, majuscules, mots vagues et ingrédients manquants.",
         "title": "Vérificateur de description de plat Uber Eats gratuit | MenuFix",
         "desc": "Collez la description d'un plat Uber Eats et vérifiez sa longueur, les mots en MAJUSCULES, les mots vagues et la présence des ingrédients. Gratuit, dans votre navigateur.",
         "icon": "pen"},
        {"key": "uber-eats-page-score", "slug": "score-page-uber-eats", "name": "Score de votre page Uber Eats",
         "short": "Répondez à 10 questions rapides sur votre page : votre score et vos 3 corrections les plus importantes, tout de suite.",
         "title": "Score gratuit de votre page Uber Eats : vérifiez votre restaurant en 2 minutes | MenuFix",
         "desc": "Votre page Uber Eats est efficace ? Répondez à 10 questions rapides sur vos photos, descriptions, l'ordre du menu et votre note. Un score sur 100 et vos 3 corrections prioritaires, tout de suite. Gratuit.",
         "icon": "star"},
    ],
    "es": [
        {"key": "uber-eats-photo-checker", "slug": "comprobador-fotos-uber-eats", "name": "Comprobador de fotos para Uber Eats",
         "short": "Compruebe una foto de un plato con las reglas de tamaño de Uber y corrija el formato con un clic.",
         "title": "Comprobador de fotos para Uber Eats gratis: tamaño, formato y archivo | MenuFix",
         "desc": "Compruebe una foto de la carta con las reglas de Uber Eats en su navegador: formato 5:4, mínimo 550 × 440 píxeles, menos de 10 MB, JPG o PNG. Recorte a 2880 × 2304 con un clic.",
         "icon": "camera"},
        {"key": "menu-description-checker", "slug": "comprobador-descripciones-menu", "name": "Comprobador de descripciones de platos",
         "short": "Pegue una descripción: longitud, mayúsculas, palabras vagas e ingredientes que faltan.",
         "title": "Comprobador de descripciones de platos para Uber Eats gratis | MenuFix",
         "desc": "Pegue la descripción de un plato de Uber Eats y compruebe su longitud, las palabras en MAYÚSCULAS, las palabras vagas y si nombra los ingredientes. Gratis, en su navegador.",
         "icon": "pen"},
        {"key": "uber-eats-page-score", "slug": "puntuacion-pagina-uber-eats", "name": "Puntuación de su página de Uber Eats",
         "short": "Responda 10 preguntas rápidas sobre su página: su puntuación y sus 3 mejoras más importantes, al momento.",
         "title": "Puntuación gratis de su página de Uber Eats: revise su restaurante en 2 minutos | MenuFix",
         "desc": "¿Funciona bien su página de Uber Eats? Responda 10 preguntas rápidas sobre fotos, descripciones, orden de la carta y valoración. Una puntuación sobre 100 y sus 3 mejoras más importantes al momento. Gratis.",
         "icon": "star"},
    ],
}

TOOLS_TEXT = {
    "en": {"dir": "tools/", "eyebrow": "Free tools", "one": "Free tool", "h2": "Check your page in seconds", "go": "Open the tool",
           "lead": "Simple checks that run in your browser. Nothing you add is uploaded or saved.", "guides": "guides/index.html",
           "cta_h": "Want the whole page done?",
           "cta_p": "We rewrite your menu and enhance photos of your real dishes. Start with a free mockup, no payment and no obligation."},
    "fr": {"dir": "fr/outils/", "eyebrow": "Outils gratuits", "one": "Outil gratuit", "h2": "Vérifiez votre page en quelques secondes", "go": "Ouvrir l'outil",
           "lead": "Des vérifications simples, directement dans votre navigateur. Rien n'est envoyé ni enregistré.", "guides": "fr/guides/index.html",
           "cta_h": "Envie que toute votre page soit refaite ?",
           "cta_p": "Nous réécrivons votre menu et améliorons les photos de vos vrais plats. Commencez par une maquette gratuite, sans paiement et sans engagement."},
    "es": {"dir": "es/herramientas/", "eyebrow": "Herramientas gratis", "one": "Herramienta gratis", "h2": "Revise su página en unos segundos", "go": "Abrir la herramienta",
           "lead": "Comprobaciones sencillas que funcionan en su navegador. No se sube ni se guarda nada.", "guides": "es/guias/index.html",
           "cta_h": "¿Prefiere que mejoremos toda la página?",
           "cta_p": "Reescribimos su carta y mejoramos las fotos de sus platos reales. Empiece con una maqueta gratis, sin pago y sin compromiso."},
}


def tool_cards(lang="en") -> str:
    t = TOOLS_TEXT[lang]
    return "".join(f'<a class="photo-card reveal tool-card" href="/{t["dir"]}{x["slug"]}.html"><div class="body">'
                   f'<img class="icon3d" src="img/icons/{x["icon"]}.png" alt="" loading="lazy"><h3>{x["name"]}</h3>'
                   f'<p>{x["short"]}</p><span class="tool-go">{t["go"]} →</span></div></a>' for x in TOOLS[lang])


def _photo_body(t):
    return f"""
<section style="padding-top:20px"><div class="narrow">
  <div class="tool" id="photoTool">
    <label class="tool-drop" id="ptDrop"><input type="file" id="ptFile" accept="image/*">
      <b>{t["choose"]}</b><span>{t["stays"]}</span></label>
    <div id="ptOut" class="tool-out" aria-live="polite"></div>
    <div class="row hidden" id="ptFixRow" style="margin-top:18px">
      <button class="btn primary" type="button" id="ptFix">{t["fix"]}</button>
      <span class="note" id="ptFixNote"></span></div>
    <canvas id="ptCanvas" class="tool-preview hidden" aria-label="{t["preview"]}"></canvas>
  </div>
  <div class="prose" style="margin-top:40px">
    {t["prose"]}
  </div>
</div></section>"""


def _desc_body(t):
    return f"""
<section style="padding-top:20px"><div class="narrow">
  <div class="tool" id="descTool">
    <label class="f" for="dtText" style="font-weight:700">{t["label"]}</label>
    <textarea id="dtText" rows="5" placeholder="{t["placeholder"]}"></textarea>
    <div class="tool-meter"><div class="tool-bar"><i id="dtBar"></i></div><span id="dtCount">{t["count"]}</span></div>
    <div id="dtOut" class="tool-out" aria-live="polite"></div>
  </div>
  <div class="prose" style="margin-top:40px">
    {t["prose"]}
  </div>
</div></section>"""


PHOTO = {
    "en": {"h": "Free Uber Eats <span class='hl'>photo checker.</span>",
           "lead": "Check a dish photo against Uber's size rules before you upload it, and fix the shape in one click.",
           "choose": "Choose a dish photo", "stays": "or drop it here. It stays on your device: nothing is uploaded.",
           "fix": "Crop to 5:4 and resize to 2880 × 2304", "preview": "Preview of the fixed photo",
           "prose": f"""<h2>What this checks</h2>
    <ul class="ticks"><li><b>Shape:</b> close to 5:4 landscape, the shape Uber recommends.</li>
      <li><b>Size:</b> at least 550 × 440 pixels; 2880 × 2304 is ideal.</li>
      <li><b>File size:</b> under 10 MB.</li><li><b>File type:</b> JPG or PNG.</li></ul>
    <p>These come from Uber's <a href="{MENU_PHOTO}" rel="nofollow">menu photo guidelines</a>. The tool can't check what's in the
      photo: Uber also turns down photos with text, logos, more than one item or faces. See
      <a href="/guides/uber-eats-photo-upload-not-working.html">photo upload not working</a> for every reason and fix.</p>
    <p>The fix button crops the middle of your photo to 5:4 and saves a JPG at 2880 × 2304. If your photo is smaller than
      that, it gets bigger but not sharper, so a larger original is always better.</p>"""},
    "fr": {"h": "Vérificateur de <span class='hl'>photo Uber Eats.</span>",
           "lead": "Vérifiez une photo de plat selon les règles de taille d'Uber avant de l'envoyer, et corrigez le format en un clic.",
           "choose": "Choisissez une photo de plat", "stays": "ou déposez la ici. Elle reste sur votre appareil : rien n'est envoyé.",
           "fix": "Recadrer en 5:4 et redimensionner en 2880 × 2304", "preview": "Aperçu de la photo corrigée",
           "prose": f"""<h2>Ce que l'outil vérifie</h2>
    <ul class="ticks"><li><b>Format :</b> proche du 5:4 à l'horizontale, le format recommandé par Uber.</li>
      <li><b>Taille :</b> au moins 550 × 440 pixels ; 2880 × 2304 est idéal.</li>
      <li><b>Poids :</b> moins de 10 Mo.</li><li><b>Type de fichier :</b> JPG ou PNG.</li></ul>
    <p>Ces règles viennent des <a href="{MENU_PHOTO_FR}" rel="nofollow">consignes photo du menu</a> d'Uber. L'outil ne peut pas
      juger le contenu de la photo : Uber refuse aussi les photos avec du texte, un logo, plusieurs articles ou des visages. Toutes
      les causes de refus et leurs solutions sont dans notre guide <a href="/fr/guides/photo-uber-eats-ne-se-charge-pas.html">photo Uber Eats qui ne se charge pas</a>.</p>
    <p>Le bouton de correction recadre le centre de votre photo en 5:4 et enregistre un JPG en 2880 × 2304. Si votre photo est
      plus petite, elle est agrandie mais pas plus nette : partez toujours de la photo d'origine la plus grande possible.</p>"""},
    "es": {"h": "Comprobador de <span class='hl'>fotos para Uber Eats.</span>",
           "lead": "Compruebe una foto de un plato con las reglas de tamaño de Uber antes de subirla y corrija el formato con un clic.",
           "choose": "Elija una foto de un plato", "stays": "o arrástrela aquí. Se queda en su dispositivo: no se sube nada.",
           "fix": "Recortar a 5:4 y ajustar a 2880 × 2304", "preview": "Vista previa de la foto corregida",
           "prose": f"""<h2>Qué comprueba</h2>
    <ul class="ticks"><li><b>Formato:</b> cerca de 5:4 en horizontal, el formato que recomienda Uber.</li>
      <li><b>Tamaño:</b> al menos 550 × 440 píxeles; 2880 × 2304 es lo ideal.</li>
      <li><b>Peso:</b> menos de 10 MB.</li><li><b>Tipo de archivo:</b> JPG o PNG.</li></ul>
    <p>Estas reglas vienen de la <a href="{MENU_PHOTO_ES}" rel="nofollow">guía de fotos del menú</a> de Uber. La herramienta no
      puede valorar lo que sale en la foto: Uber también rechaza fotos con texto, logotipos, más de un producto o caras. Tiene todas
      las causas y soluciones en <a href="/es/guias/foto-uber-eats-no-se-sube.html">la foto de Uber Eats no se sube</a>.</p>
    <p>El botón de corrección recorta el centro de su foto a 5:4 y guarda un JPG de 2880 × 2304. Si su foto es más pequeña, se
      amplía pero no gana nitidez, así que conviene partir siempre de la foto original más grande que tenga.</p>"""},
}

DESC = {
    "en": {"h": "Free menu description <span class='hl'>checker.</span>",
           "lead": "Paste a dish description to check its length and wording against Uber's advice.",
           "label": "Dish description", "count": "0 characters",
           "placeholder": "For example: Crumbed chicken schnitzel topped with napoli sauce, leg ham and melted mozzarella. Served with chips and a side salad.",
           "prose": f"""<h2>What this checks</h2>
    <ul class="ticks"><li><b>Length:</b> Uber's advice is 140 to 260 characters, about two short sentences
      (<a href="{DESC_ADVICE}" rel="nofollow">Uber Australia</a>).</li>
      <li><b>ALL CAPS:</b> words in capitals read like shouting and are harder to skim.</li>
      <li><b>Vague words:</b> delicious, amazing, best and similar say nothing about the dish.</li>
      <li><b>Ingredients:</b> whether it names at least two foods or cooking methods.</li></ul>
    <p>These are simple rules, not AI, and your text never leaves your browser. For ideas, see
      <a href="/guides/uber-eats-menu-description-examples.html">30 menu description examples</a> and
      <a href="/guides/write-uber-eats-menu-descriptions.html">how to write menu descriptions</a>.</p>"""},
    "fr": {"h": "Vérificateur de <span class='hl'>description de plat.</span>",
           "lead": "Collez la description d'un plat pour vérifier sa longueur et ses mots avant de la publier sur Uber Eats.",
           "label": "Description du plat", "count": "0 caractère",
           "placeholder": "Par exemple : Poulet fermier rôti au thym, jus corsé et purée maison au beurre. Servi avec une salade verte de saison.",
           "prose": f"""<h2>Ce que l'outil vérifie</h2>
    <ul class="ticks"><li><b>Longueur :</b> notre repère est de 140 à 260 caractères, soit environ deux phrases courtes. Assez pour
      citer les ingrédients, assez court pour être lu en faisant défiler.</li>
      <li><b>MAJUSCULES :</b> les mots en capitales donnent l'impression de crier et se lisent moins vite.</li>
      <li><b>Mots vagues :</b> délicieux, incroyable, le meilleur et autres ne disent rien du plat.</li>
      <li><b>Ingrédients :</b> si la description cite au moins deux produits ou modes de cuisson.</li></ul>
    <p>Uber recommande d'ajouter une description à vos articles pour aider les clients à choisir (<a href="{MENU_INFO_FR}" rel="nofollow">aide Uber</a>).
      La longueur de 140 à 260 caractères est notre conseil, pas une règle d'Uber. L'outil applique des règles simples, sans IA, et
      votre texte ne quitte jamais votre navigateur. Pour des idées, voyez nos
      <a href="/fr/guides/exemples-descriptions-menu-uber-eats.html">30 exemples de descriptions</a> et notre guide pour
      <a href="/fr/guides/descriptions-menu-uber-eats.html">écrire des descriptions qui donnent envie</a>.</p>"""},
    "es": {"h": "Comprobador de <span class='hl'>descripciones de platos.</span>",
           "lead": "Pegue la descripción de un plato para revisar su longitud y sus palabras antes de publicarla en Uber Eats.",
           "label": "Descripción del plato", "count": "0 caracteres",
           "placeholder": "Por ejemplo: Croquetas caseras de jamón ibérico con bechamel cremosa y rebozado crujiente. Ración de ocho unidades, fritas al momento.",
           "prose": f"""<h2>Qué comprueba</h2>
    <ul class="ticks"><li><b>Longitud:</b> nuestra referencia es de 140 a 260 caracteres, unas dos frases cortas. Suficiente para
      nombrar los ingredientes y lo bastante breve para leerla mientras se desplaza por la carta.</li>
      <li><b>MAYÚSCULAS:</b> las palabras en mayúsculas parecen gritos y cuestan más de leer.</li>
      <li><b>Palabras vagas:</b> delicioso, increíble, el mejor y similares no dicen nada del plato.</li>
      <li><b>Ingredientes:</b> si la descripción nombra al menos dos productos o formas de cocinar.</li></ul>
    <p>Uber recomienda añadir una descripción a sus productos para ayudar a los clientes a elegir (<a href="{MENU_INFO_ES}" rel="nofollow">ayuda de Uber</a>).
      La longitud de 140 a 260 caracteres es nuestro consejo, no una regla de Uber. La herramienta usa reglas sencillas, sin IA, y su
      texto nunca sale de su navegador. Si busca ideas, vea nuestros
      <a href="/es/guias/ejemplos-descripciones-menu-uber-eats.html">30 ejemplos de descripciones</a> y la guía para
      <a href="/es/guias/descripciones-menu-uber-eats.html">escribir descripciones que venden</a>.</p>"""},
}


def build_tools(page, head, cta, lang="en") -> list[tuple[str, str]]:
    """Write the tool pages for one language. Returns (key, path) pairs, the key being the same in every language."""
    t = TOOLS_TEXT[lang]
    out = []
    for x in TOOLS[lang]:
        txt = {"camera": PHOTO, "pen": DESC, "star": SCORE}[x["icon"]][lang]
        body = {"camera": _photo_body, "pen": _desc_body, "star": _score_body}[x["icon"]](txt)
        name = f"{t['dir']}{x['slug']}.html"
        page(name, x["title"], x["desc"], f"""{head(t["one"], txt["h"], txt["lead"], (x["icon"], "star"))}
{body}
{cta.replace(cta[cta.index("<h2>") + 4:cta.index("</h2>")], t["cta_h"], 1).replace(cta[cta.index('<p class="lead">') + 16:cta.index("</p>", cta.index('<p class="lead">'))], t["cta_p"], 1)}
""", t["guides"], lang=lang)
        out.append((x["key"], name))
    return out


# ---- Uber Eats page score: 10 questions the owner answers about their own page. Nothing is read from Uber Eats and
# nothing is sent: the score is added up in the browser (site.js). Points add up to 100. The weights are our own
# judgement, said so on the page; the Uber facts link to Uber.
def _q(key, max_, opts, fix, link):
    return {"key": key, "max": max_, "opts": opts, "fix": fix, "link": link}


SCORE = {
    "en": {"h": "Free Uber Eats <span class='hl'>page score.</span>",
           "lead": "Open your restaurant on Uber Eats as a customer would, answer 10 quick questions, and get your score and your 3 most important fixes at once.",
           "go": "See my score", "missing": "Please answer every question to see your score.",
           "out_of": "out of 100", "top3": "Your 3 most important fixes", "read": "How to fix it",
           "bands": [(85, "Your page is in great shape. Small details are all that is left."),
                     (65, "A good page with clear room to grow. The fixes below are where to start."),
                     (40, "Customers are probably scrolling past dishes they would love. The fixes below matter most."),
                     (0, "Your page is holding your food back. Start with the first fix below this week.")],
           "none": "Nothing important to fix. Keep your photos and prices up to date.",
           "next_h": "Want a real person to check your actual page?",
           "next_p": "Send us your Uber Eats link and we email you a free page check with your real dish names, plus a free mockup of your new page. No login, no card.",
           "next_btn": "Get my free page check", "next_href": "/check.html",
           "q": [
               _q("photos", 20, [("All or almost all", 20), ("About half", 10), ("Only a few or none", 0)],
                  "Add photos to your dishes, starting with your 10 best sellers. Uber advises a photo for as many items as possible.",
                  "/guides/how-to-add-photos-to-uber-eats-menu.html"),
               _q("quality", 7, [("Yes", 7), ("Some of them", 3), ("No", 0)],
                  "Retake or enhance your photos: daylight, one dish per photo, a clean background, no text.",
                  "/guides/uber-eats-food-photos-phone.html"),
               _q("desc", 15, [("Yes, almost all", 15), ("Some of them", 7), ("Few or none", 0)],
                  "Give every dish a description of 140 to 260 characters that names the main ingredients, as Uber advises.",
                  "/guides/write-uber-eats-menu-descriptions.html"),
               _q("names", 10, [("Yes", 10), ("No", 0)],
                  "Clean up your dish names: no typos, no ALL CAPS and no codes like A1 or #12.",
                  "/guides/uber-eats-menu-description-examples.html"),
               _q("best", 10, [("Yes", 10), ("No", 0), ("Not sure", 0)],
                  "Put your best sellers in the first category customers see.",
                  "/guides/best-sellers-uber-eats-menu-order.html"),
               _q("cats", 8, [("Yes", 8), ("No", 0)],
                  "Sort your menu into clear categories in the order people eat: starters, mains, sides, drinks, desserts.",
                  "/guides/uber-eats-menu-categories.html"),
               _q("banner", 8, [("Yes", 8), ("No", 0)],
                  "Add a cover photo of your best dish. It is the first thing customers see.",
                  "/guides/uber-eats-banner-photo.html"),
               _q("logo", 4, [("Yes", 4), ("No", 0)],
                  "Add your logo so customers recognise you in search results.",
                  "/guides/new-on-uber-eats-checklist.html"),
               _q("extras", 8, [("Yes", 8), ("No", 0)],
                  "Add drinks, sides and extras. Uber suggests more drink options and add ons before checkout.",
                  "/guides/get-more-orders-on-uber-eats.html"),
               _q("rating", 10, [("4.5 or higher", 10), ("4.0 to 4.4", 5), ("Below 4.0", 0), ("New, no rating yet", 5)],
                  "Work on your rating: reply to reviews and fix what customers mention most.",
                  "/guides/improve-uber-eats-rating-restaurant.html"),
           ],
           "labels": {"photos": "How many of your dishes have a photo?",
                      "quality": "Are your photos bright and sharp, with one dish per photo and no text?",
                      "desc": "Do your dishes have a description that names the main ingredients?",
                      "names": "Are your dish names clear, with no typos, no ALL CAPS and no codes like A1?",
                      "best": "Are your best sellers in the first category customers see?",
                      "cats": "Is your menu in clear categories, in the order people eat?",
                      "banner": "Does your page have a cover photo of your food?",
                      "logo": "Does your page show your logo?",
                      "extras": "Can customers add drinks, sides or extras?",
                      "rating": "What is your Uber Eats rating?"},
           "prose": f"""<h2>How the score works</h2>
    <p>Each answer gives points, 100 in all. Photos and descriptions count the most, because they are what customers look at
      when they choose. The weights are our own judgement from checking Uber Eats pages, not an Uber formula. Uber's own advice
      on photos, descriptions of 140 to 260 characters and drinks is on its <a href="{DESC_ADVICE}" rel="nofollow">menu tips page</a>.</p>
    <p>Your answers stay in your browser: nothing is sent or saved. For a check of your real page by a person, use our
      <a href="/check.html">free page check</a>.</p>"""},
    "fr": {"h": "Score gratuit de votre <span class='hl'>page Uber Eats.</span>",
           "lead": "Ouvrez votre restaurant sur Uber Eats comme un client, répondez à 10 questions rapides, et obtenez votre score et vos 3 corrections les plus importantes tout de suite.",
           "go": "Voir mon score", "missing": "Répondez à toutes les questions pour voir votre score.",
           "out_of": "sur 100", "top3": "Vos 3 corrections les plus importantes", "read": "Comment faire",
           "bands": [(85, "Votre page est en très bonne forme. Il ne reste que des détails."),
                     (65, "Une bonne page, avec une vraie marge de progrès. Commencez par les corrections ci dessous."),
                     (40, "Les clients passent sans doute à côté de plats qu'ils adoreraient. Les corrections ci dessous comptent le plus."),
                     (0, "Votre page dessert votre cuisine. Commencez cette semaine par la première correction ci dessous.")],
           "none": "Rien d'important à corriger. Gardez vos photos et vos prix à jour.",
           "next_h": "Envie qu'une vraie personne vérifie votre page ?",
           "next_p": "Envoyez nous le lien de votre page Uber Eats : nous vous envoyons par email une analyse gratuite avec vos vrais plats, et une maquette gratuite de votre nouvelle page. Sans connexion, sans carte.",
           "next_btn": "Recevoir mon analyse gratuite", "next_href": "/fr/check.html",
           "q": [
               _q("photos", 20, [("Tous ou presque", 20), ("Environ la moitié", 10), ("Peu ou aucun", 0)],
                  "Ajoutez des photos à vos plats, en commençant par vos 10 meilleures ventes. Uber conseille une photo pour un maximum d'articles.",
                  "/fr/guides/ajouter-photos-menu-uber-eats.html"),
               _q("quality", 7, [("Oui", 7), ("Certaines", 3), ("Non", 0)],
                  "Refaites ou améliorez vos photos : lumière du jour, un plat par photo, fond propre, aucun texte.",
                  "/fr/guides/photos-plats-telephone.html"),
               _q("desc", 15, [("Oui, presque tous", 15), ("Certains", 7), ("Peu ou aucun", 0)],
                  "Donnez à chaque plat une description de 140 à 260 caractères qui cite les ingrédients principaux.",
                  "/fr/guides/descriptions-menu-uber-eats.html"),
               _q("names", 10, [("Oui", 10), ("Non", 0)],
                  "Nettoyez les noms de vos plats : pas de fautes, pas de MAJUSCULES, pas de codes comme A1 ou n°12.",
                  "/fr/guides/exemples-descriptions-menu-uber-eats.html"),
               _q("best", 10, [("Oui", 10), ("Non", 0), ("Je ne sais pas", 0)],
                  "Placez vos meilleures ventes dans la première catégorie que voient les clients.",
                  "/fr/guides/meilleures-ventes-ordre-menu-uber-eats.html"),
               _q("cats", 8, [("Oui", 8), ("Non", 0)],
                  "Rangez votre menu en catégories claires, dans l'ordre du repas : entrées, plats, accompagnements, boissons, desserts.",
                  "/fr/guides/categories-menu-uber-eats.html"),
               _q("banner", 8, [("Oui", 8), ("Non", 0)],
                  "Ajoutez une photo de bannière avec votre meilleur plat. C'est la première chose que voient les clients.",
                  "/fr/guides/photo-banniere-uber-eats.html"),
               _q("logo", 4, [("Oui", 4), ("Non", 0)],
                  "Ajoutez votre logo pour que les clients vous reconnaissent dans les résultats.",
                  "/fr/guides/debuter-sur-uber-eats.html"),
               _q("extras", 8, [("Oui", 8), ("Non", 0)],
                  "Ajoutez boissons, accompagnements et suppléments. Uber conseille de proposer plus de boissons et des ajouts avant de commander.",
                  "/fr/guides/plus-de-commandes-uber-eats.html"),
               _q("rating", 10, [("4,5 ou plus", 10), ("De 4,0 à 4,4", 5), ("Moins de 4,0", 0), ("Nouveau, pas encore de note", 5)],
                  "Travaillez votre note : répondez aux avis et corrigez ce que les clients citent le plus.",
                  "/fr/guides/ameliorer-note-uber-eats.html"),
           ],
           "labels": {"photos": "Combien de vos plats ont une photo ?",
                      "quality": "Vos photos sont lumineuses et nettes, avec un plat par photo et sans texte ?",
                      "desc": "Vos plats ont une description qui cite les ingrédients principaux ?",
                      "names": "Les noms de vos plats sont clairs, sans fautes, sans MAJUSCULES et sans codes comme A1 ?",
                      "best": "Vos meilleures ventes sont dans la première catégorie que voient les clients ?",
                      "cats": "Votre menu est rangé en catégories claires, dans l'ordre du repas ?",
                      "banner": "Votre page a une photo de bannière avec vos plats ?",
                      "logo": "Votre page affiche votre logo ?",
                      "extras": "Les clients peuvent ajouter boissons, accompagnements ou suppléments ?",
                      "rating": "Quelle est votre note sur Uber Eats ?"},
           "prose": f"""<h2>Comment le score est calculé</h2>
    <p>Chaque réponse donne des points, 100 au total. Les photos et les descriptions comptent le plus, car c'est ce que regardent
      les clients pour choisir. Les poids sont notre propre jugement, tiré de l'analyse de pages Uber Eats, pas une formule d'Uber.
      Uber recommande d'ajouter une description à vos articles (<a href="{MENU_INFO_FR}" rel="nofollow">aide Uber</a>).</p>
    <p>Vos réponses restent dans votre navigateur : rien n'est envoyé ni enregistré. Pour une vérification de votre vraie page par
      une personne, utilisez notre <a href="/fr/check.html">analyse gratuite</a>.</p>"""},
    "es": {"h": "Puntuación gratis de su <span class='hl'>página de Uber Eats.</span>",
           "lead": "Abra su restaurante en Uber Eats como un cliente, responda 10 preguntas rápidas y obtenga su puntuación y sus 3 mejoras más importantes al momento.",
           "go": "Ver mi puntuación", "missing": "Responda todas las preguntas para ver su puntuación.",
           "out_of": "sobre 100", "top3": "Sus 3 mejoras más importantes", "read": "Cómo hacerlo",
           "bands": [(85, "Su página está en muy buena forma. Solo quedan detalles."),
                     (65, "Una buena página con margen claro para crecer. Empiece por las mejoras de abajo."),
                     (40, "Es probable que los clientes pasen de largo platos que les encantarían. Las mejoras de abajo son las que más cuentan."),
                     (0, "Su página está frenando su cocina. Empiece esta semana por la primera mejora de abajo.")],
           "none": "Nada importante que mejorar. Mantenga sus fotos y precios al día.",
           "next_h": "¿Quiere que una persona revise su página real?",
           "next_p": "Envíenos el enlace de su página de Uber Eats y le mandamos por correo un análisis gratis con sus platos reales, y una maqueta gratis de su nueva página. Sin acceso a su cuenta, sin tarjeta.",
           "next_btn": "Quiero mi análisis gratis", "next_href": "/es/check.html",
           "q": [
               _q("photos", 20, [("Todos o casi todos", 20), ("Más o menos la mitad", 10), ("Pocos o ninguno", 0)],
                  "Añada fotos a sus platos, empezando por los 10 más vendidos. Uber aconseja una foto para el mayor número de productos posible.",
                  "/es/guias/fotos-comida-movil.html"),
               _q("quality", 7, [("Sí", 7), ("Algunas", 3), ("No", 0)],
                  "Repita o mejore sus fotos: luz de día, un plato por foto, fondo limpio y sin texto.",
                  "/es/guias/fotos-comida-movil.html"),
               _q("desc", 15, [("Sí, casi todos", 15), ("Algunos", 7), ("Pocos o ninguno", 0)],
                  "Dé a cada plato una descripción de 140 a 260 caracteres que nombre los ingredientes principales.",
                  "/es/guias/descripciones-menu-uber-eats.html"),
               _q("names", 10, [("Sí", 10), ("No", 0)],
                  "Limpie los nombres de sus platos: sin faltas, sin MAYÚSCULAS y sin códigos como A1 o n.º 12.",
                  "/es/guias/descripciones-menu-uber-eats.html"),
               _q("best", 10, [("Sí", 10), ("No", 0), ("No lo sé", 0)],
                  "Ponga sus platos más vendidos en la primera categoría que ven los clientes.",
                  "/es/guias/mas-pedidos-uber-eats.html"),
               _q("cats", 8, [("Sí", 8), ("No", 0)],
                  "Ordene su carta en categorías claras, en el orden de la comida: entrantes, principales, acompañamientos, bebidas y postres.",
                  "/es/guias/editar-menu-uber-eats-manager.html"),
               _q("banner", 8, [("Sí", 8), ("No", 0)],
                  "Añada una foto de portada con su mejor plato. Es lo primero que ven los clientes.",
                  "/es/guias/empezar-en-uber-eats.html"),
               _q("logo", 4, [("Sí", 4), ("No", 0)],
                  "Añada su logotipo para que los clientes le reconozcan en los resultados.",
                  "/es/guias/empezar-en-uber-eats.html"),
               _q("extras", 8, [("Sí", 8), ("No", 0)],
                  "Añada bebidas, acompañamientos y extras. Uber aconseja más opciones de bebida y extras antes de pagar.",
                  "/es/guias/mas-pedidos-uber-eats.html"),
               _q("rating", 10, [("4,5 o más", 10), ("De 4,0 a 4,4", 5), ("Menos de 4,0", 0), ("Nuevo, sin valoración aún", 5)],
                  "Trabaje su valoración: responda a las reseñas y corrija lo que más mencionan los clientes.",
                  "/es/guias/mas-pedidos-uber-eats.html"),
           ],
           "labels": {"photos": "¿Cuántos de sus platos tienen foto?",
                      "quality": "¿Sus fotos son luminosas y nítidas, con un plato por foto y sin texto?",
                      "desc": "¿Sus platos tienen una descripción que nombra los ingredientes principales?",
                      "names": "¿Los nombres de sus platos son claros, sin faltas, sin MAYÚSCULAS y sin códigos como A1?",
                      "best": "¿Sus platos más vendidos están en la primera categoría que ven los clientes?",
                      "cats": "¿Su carta está en categorías claras, en el orden de la comida?",
                      "banner": "¿Su página tiene una foto de portada con su comida?",
                      "logo": "¿Su página muestra su logotipo?",
                      "extras": "¿Los clientes pueden añadir bebidas, acompañamientos o extras?",
                      "rating": "¿Cuál es su valoración en Uber Eats?"},
           "prose": f"""<h2>Cómo se calcula la puntuación</h2>
    <p>Cada respuesta suma puntos, 100 en total. Las fotos y las descripciones cuentan más, porque es lo que miran los clientes para
      elegir. Los pesos son nuestro propio criterio tras revisar páginas de Uber Eats, no una fórmula de Uber. Uber recomienda añadir
      una descripción a sus productos (<a href="{MENU_INFO_ES}" rel="nofollow">ayuda de Uber</a>).</p>
    <p>Sus respuestas se quedan en su navegador: no se envía ni se guarda nada. Para una revisión de su página real hecha por una
      persona, use nuestro <a href="/es/check.html">análisis gratis</a>.</p>"""},
}


def _score_body(t):
    import json as _j
    qs = "".join(
        f'<fieldset class="sq"><legend>{i}. {t["labels"][q["key"]]}</legend><div class="sq-opts">' +
        "".join(f'<label><input type="radio" name="{q["key"]}" value="{p}"><span>{lab}</span></label>' for lab, p in q["opts"]) +
        "</div></fieldset>" for i, q in enumerate(t["q"], 1))
    data = {"max": {q["key"]: q["max"] for q in t["q"]}, "fix": {q["key"]: [q["fix"], q["link"]] for q in t["q"]},
            "bands": t["bands"], "out_of": t["out_of"], "top3": t["top3"], "read": t["read"], "none": t["none"],
            "missing": t["missing"]}
    blob = _j.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    assert sum(q["max"] for q in t["q"]) == 100 and all(max(p for _, p in q["opts"]) == q["max"] for q in t["q"])
    return f"""
<section style="padding-top:20px"><div class="narrow">
  <form class="tool" id="scoreTool" novalidate>
    {qs}
    <button class="btn primary" type="submit" style="margin-top:8px">{t["go"]}</button>
    <div id="scoreOut" class="tool-out" aria-live="polite"></div>
    <div id="scoreNext" class="score-next hidden"><h3>{t["next_h"]}</h3><p>{t["next_p"]}</p>
      <a class="btn primary" href="{t["next_href"]}">{t["next_btn"]}</a></div>
  </form>
  <script type="application/json" id="scoreData">{blob}</script>
  <div class="prose" style="margin-top:40px">
    {t["prose"]}
  </div>
</div></section>"""
