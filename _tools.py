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
        txt = PHOTO[lang] if x["icon"] == "camera" else DESC[lang]
        body = _photo_body(txt) if x["icon"] == "camera" else _desc_body(txt)
        name = f"{t['dir']}{x['slug']}.html"
        page(name, x["title"], x["desc"], f"""{head(t["one"], txt["h"], txt["lead"], (x["icon"], "star"))}
{body}
{cta.replace(cta[cta.index("<h2>") + 4:cta.index("</h2>")], t["cta_h"], 1).replace(cta[cta.index('<p class="lead">') + 16:cta.index("</p>", cta.index('<p class="lead">'))], t["cta_p"], 1)}
""", t["guides"], lang=lang)
        out.append((x["key"], name))
    return out
