"""The public referral program page in English, French and Spanish: referral.html, fr/parrainage.html,
es/referidos.html. Built by _build.py. Honest terms only: the referrer gets 30% of what a restaurant actually paid.
The sign up form posts to MenuFix (site.js, #refForm, /api/public/form), like the contact form."""

PAGES = {
    "en": {
        "name": "referral.html", "active": "",
        "title": "Earn 30% for Every Restaurant You Send Us | MenuFix Referral Program",
        "desc": "Know restaurant or café owners? Share your personal MenuFix link and earn 30% of what each restaurant that comes through it pays. Simple, honest terms.",
        "eyebrow": "Referral program", "h1": "Earn 30% for every restaurant you <span class='hl'>send us.</span>",
        "lead": "Know restaurant, café or bakery owners who sell on Uber Eats? Share your personal link. When a restaurant that came through it pays, you receive 30% of what it paid.",
        "how": "How it works", "how_h": "Three simple steps.",
        "steps": [("gift", "Get your link", "Fill in the form below. We reply with your personal link within one working day."),
                  ("phone", "Share it", "Send it to the restaurant, café and bakery owners you know."),
                  ("star", "Earn 30% when they pay", "When a restaurant that came through your link pays, you receive 30% of what it paid.")],
        "who": "Who it's for", "who_h": "People who know restaurant owners.",
        "who_cards": [("camera", "Food photographers", "You already shoot their dishes."),
                      ("menu", "Bookkeepers and accountants", "You see how much delivery matters to them."),
                      ("bag", "POS and packaging suppliers", "You supply cafés and takeaways every week."),
                      ("chef", "Shared kitchens", "Many of your kitchens sell on Uber Eats."),
                      ("salad", "Anyone who knows restaurant owners", "A friend, a regular or a happy client.")],
        "gets": "The restaurant starts with a free concept of its own Uber Eats page and only pays if it wants our help. It pays the same price as everyone else.",
        "terms": "The terms", "terms_h": "Simple and honest.",
        "terms_list": ["You receive 30% of the amount the restaurant actually paid us. Refunded payments don't count.",
                       "We pay you by bank transfer or PayPal within 7 days after the restaurant's payment.",
                       "Your link counts for 60 days after a restaurant first clicks it.",
                       "No payment for referring yourself or your own business.",
                       "No spam: don't send unsolicited bulk messages using the MenuFix name.",
                       "MenuFix may end the program with notice."],
        "form_h": "Get your personal link", "form_lead": "We reply with your personal link within one working day.",
        "f_name": "Your name", "f_email": "Email", "f_biz": "Business (optional)", "f_how": "How will you share it?",
        "p_name": "First and last name", "p_email": "you@example.com", "p_biz": "For example your studio or company",
        "p_how": "For example: I photograph cafés and will tell my clients about it.",
        "send": "Send", "send_note": "We use your email only to send your link and your payments.",
        "err": "Sorry, something went wrong. Please try again in a minute, or email us at hello@getmenufix.com.",
        "th": "Thank you, we've got your request.", "tp": "We'll email you your personal link within one working day. If you don't see it, look in your spam folder.",
        "faq_h": "Questions",
        "faq": [("Does the restaurant pay more?", "No. It pays the same price as any other restaurant."),
                ("How do you know a restaurant came through my link?", "Your link saves a code in the restaurant's browser for 60 days. When they ask for their free page check from that browser, the code comes with their request and stays with them until they pay. If they write to us another way, tell us and we'll look into it."),
                ("When do I get paid?", "Within 7 days after the restaurant's payment, by bank transfer or PayPal.")],
    },
    "fr": {
        "name": "fr/parrainage.html", "active": "",
        "title": "Parrainage MenuFix : gagnez 30 % pour chaque restaurant recommandé",
        "desc": "Vous connaissez des restaurateurs ? Partagez votre lien MenuFix personnel et recevez 30 % de ce que paie chaque restaurant venu par ce lien. Des conditions simples et claires.",
        "eyebrow": "Parrainage", "h1": "Gagnez 30 % pour chaque restaurant que vous nous <span class='hl'>recommandez.</span>",
        "lead": "Vous connaissez des restaurants, cafés ou boulangeries qui vendent sur Uber Eats ? Partagez votre lien personnel. Quand un restaurant venu par ce lien paie, vous recevez 30 % de ce qu'il a payé.",
        "how": "Comment ça marche", "how_h": "Trois étapes simples.",
        "steps": [("gift", "Recevez votre lien", "Remplissez le formulaire plus bas. Nous vous répondons avec votre lien personnel sous un jour ouvré."),
                  ("phone", "Partagez le", "Envoyez le aux restaurateurs, cafés et boulangeries que vous connaissez."),
                  ("star", "Gagnez 30 % quand ils paient", "Quand un restaurant venu par votre lien paie, vous recevez 30 % de ce qu'il a payé.")],
        "who": "Pour qui", "who_h": "Ceux qui connaissent des restaurateurs.",
        "who_cards": [("camera", "Photographes culinaires", "Vous photographiez déjà leurs plats."),
                      ("menu", "Comptables et experts comptables", "Vous voyez combien la livraison compte pour eux."),
                      ("bag", "Fournisseurs de caisses et d'emballages", "Vous livrez cafés et restaurants chaque semaine."),
                      ("chef", "Cuisines partagées", "Beaucoup de vos cuisines vendent sur Uber Eats."),
                      ("salad", "Tous ceux qui connaissent des restaurateurs", "Un ami, un habitué ou un client satisfait.")],
        "gets": "Le restaurant commence par une analyse gratuite de sa propre page Uber Eats et ne paie que s'il veut notre aide. Il paie le même prix que tout le monde.",
        "terms": "Les conditions", "terms_h": "Simples et honnêtes.",
        "terms_list": ["Vous recevez 30 % du montant réellement payé par le restaurant. Les paiements remboursés ne comptent pas.",
                       "Nous vous payons par virement bancaire ou PayPal dans les 7 jours suivant le paiement du restaurant.",
                       "Votre lien compte pendant 60 jours après le premier clic du restaurant.",
                       "Aucun paiement si vous vous recommandez vous même ou votre propre entreprise.",
                       "Pas de spam : n'envoyez pas de messages en masse non sollicités au nom de MenuFix.",
                       "MenuFix peut mettre fin au programme avec un préavis."],
        "form_h": "Recevez votre lien personnel", "form_lead": "Nous vous répondons avec votre lien personnel sous un jour ouvré.",
        "f_name": "Votre nom", "f_email": "Email", "f_biz": "Entreprise (facultatif)", "f_how": "Comment allez vous le partager ?",
        "p_name": "Prénom et nom", "p_email": "vous@exemple.fr", "p_biz": "Par exemple votre studio ou votre société",
        "p_how": "Par exemple : je photographie des cafés et j'en parlerai à mes clients.",
        "send": "Envoyer", "send_note": "Nous utilisons votre email uniquement pour vous envoyer votre lien et vos paiements.",
        "err": "Désolé, un problème est survenu. Réessayez dans une minute, ou écrivez nous à hello@getmenufix.com.",
        "th": "Merci, nous avons bien reçu votre demande.", "tp": "Nous vous enverrons votre lien personnel par email sous un jour ouvré. Si vous ne le voyez pas, regardez dans vos spams.",
        "faq_h": "Questions fréquentes",
        "faq": [("Le restaurant paie il plus cher ?", "Non. Il paie le même prix que n'importe quel autre restaurant."),
                ("Comment savez vous qu'un restaurant vient de mon lien ?", "Votre lien enregistre un code dans le navigateur du restaurant pendant 60 jours. Quand il demande son analyse gratuite depuis ce navigateur, le code accompagne sa demande et reste lié à lui jusqu'au paiement. S'il nous contacte autrement, prévenez nous et nous vérifierons."),
                ("Quand suis je payé ?", "Dans les 7 jours suivant le paiement du restaurant, par virement bancaire ou PayPal.")],
    },
    "es": {
        "name": "es/referidos.html", "active": "",
        "title": "Programa de referidos MenuFix: gane un 30 % por cada restaurante",
        "desc": "¿Conoce a dueños de restaurantes? Comparta su enlace personal de MenuFix y reciba un 30 % de lo que pague cada restaurante que llegue por él. Condiciones claras.",
        "eyebrow": "Programa de referidos", "h1": "Gane un 30 % por cada restaurante que nos <span class='hl'>recomiende.</span>",
        "lead": "¿Conoce restaurantes, cafeterías o panaderías que venden en Uber Eats? Comparta su enlace personal. Cuando un restaurante que llegue por ese enlace pague, usted recibe un 30 % de lo que pagó.",
        "how": "Cómo funciona", "how_h": "Tres pasos sencillos.",
        "steps": [("gift", "Reciba su enlace", "Rellene el formulario de abajo. Le respondemos con su enlace personal en un día laborable."),
                  ("phone", "Compártalo", "Envíelo a los dueños de restaurantes, cafeterías y panaderías que conozca."),
                  ("star", "Gane un 30 % cuando paguen", "Cuando un restaurante que llegó por su enlace paga, usted recibe un 30 % de lo que pagó.")],
        "who": "Para quién es", "who_h": "Personas que conocen a dueños de restaurantes.",
        "who_cards": [("camera", "Fotógrafos gastronómicos", "Ya fotografía sus platos."),
                      ("menu", "Gestores y asesores contables", "Sabe cuánto les importa el reparto a domicilio."),
                      ("bag", "Proveedores de TPV y envases", "Abastece a cafeterías y locales cada semana."),
                      ("chef", "Cocinas compartidas", "Muchas de sus cocinas venden en Uber Eats."),
                      ("salad", "Cualquiera que conozca a dueños de restaurantes", "Un amigo, un cliente habitual o un cliente contento.")],
        "gets": "El restaurante empieza con un análisis gratis de su propia página de Uber Eats y solo paga si quiere nuestra ayuda. Paga el mismo precio que cualquier otro.",
        "terms": "Las condiciones", "terms_h": "Sencillas y honestas.",
        "terms_list": ["Recibe un 30 % del importe que el restaurante pagó realmente. Los pagos reembolsados no cuentan.",
                       "Le pagamos por transferencia bancaria o PayPal en los 7 días siguientes al pago del restaurante.",
                       "Su enlace cuenta durante 60 días desde el primer clic del restaurante.",
                       "No hay pago por recomendarse a usted mismo ni a su propio negocio.",
                       "Nada de spam: no envíe mensajes masivos no solicitados en nombre de MenuFix.",
                       "MenuFix puede terminar el programa con previo aviso."],
        "form_h": "Reciba su enlace personal", "form_lead": "Le respondemos con su enlace personal en un día laborable.",
        "f_name": "Su nombre", "f_email": "Correo electrónico", "f_biz": "Negocio (opcional)", "f_how": "¿Cómo lo va a compartir?",
        "p_name": "Nombre y apellidos", "p_email": "usted@ejemplo.es", "p_biz": "Por ejemplo, su estudio o su empresa",
        "p_how": "Por ejemplo: fotografío cafeterías y se lo contaré a mis clientes.",
        "send": "Enviar", "send_note": "Usamos su correo solo para enviarle su enlace y sus pagos.",
        "err": "Lo sentimos, algo ha fallado. Inténtelo de nuevo en un minuto o escríbanos a hello@getmenufix.com.",
        "th": "Gracias, hemos recibido su solicitud.", "tp": "Le enviaremos su enlace personal por correo en un día laborable. Si no lo ve, mire en su carpeta de spam.",
        "faq_h": "Preguntas frecuentes",
        "faq": [("¿El restaurante paga más?", "No. Paga el mismo precio que cualquier otro restaurante."),
                ("¿Cómo saben que un restaurante llegó por mi enlace?", "Su enlace guarda un código en el navegador del restaurante durante 60 días. Cuando pide su análisis gratis desde ese navegador, el código va con su solicitud y queda unido a él hasta el pago. Si nos contacta de otra forma, avísenos y lo revisaremos."),
                ("¿Cuándo cobro?", "En los 7 días siguientes al pago del restaurante, por transferencia bancaria o PayPal.")],
    },
}


def build_referral(page, head, ic, faq_html, ctas) -> list[tuple[str, str]]:
    """Write the three pages. Returns (lang, path) pairs. ctas: {lang: CTA section html}."""
    import json
    out = []
    for lang, t in PAGES.items():
        steps = "".join(f'<div class="card reveal">{ic(i)}<span class="eyebrow" style="display:block;margin:0 0 6px">{n}</span>'
                        f'<h3>{h}</h3><p>{p}</p></div>' for n, (i, h, p) in enumerate(t["steps"], 1))
        who = "".join(f'<div class="card reveal">{ic(i)}<h3>{h}</h3><p>{p}</p></div>' for i, h, p in t["who_cards"])
        terms = "".join(f"<li>{x}</li>" for x in t["terms_list"])
        ld = '\n<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in t["faq"]]}, ensure_ascii=False) + "</script>"
        page(t["name"], t["title"], t["desc"], f"""{head(t["eyebrow"], t["h1"], t["lead"], ("gift", "star"),
            f'<div class="row" style="margin-top:26px"><a class="btn primary" href="#join">{t["form_h"]} <span class="arr">→</span></a></div>')}

<section class="tight"><div class="wrap">
  <div class="head reveal"><div><span class="eyebrow">{t["how"]}</span><h2>{t["how_h"]}</h2></div><p class="lead">{t["gets"]}</p></div>
  <div class="grid3">{steps}</div>
</div></section>

<section class="bg-butter"><div class="wrap">
  <div class="head center reveal"><span class="eyebrow">{t["who"]}</span><h2>{t["who_h"]}</h2></div>
  <div class="grid3">{who}</div>
</div></section>

<section class="tight" id="join"><div class="wrap split" style="align-items:start">
  <div class="reveal"><span class="eyebrow">{t["terms"]}</span><h2>{t["terms_h"]}</h2>
    <ul class="ticks">{terms}</ul></div>
  <div class="card reveal" style="padding:40px">
    <h3 style="margin-bottom:6px">{t["form_h"]}</h3><p class="note" style="margin:0 0 20px">{t["form_lead"]}</p>
    <form id="refForm" data-lang="{lang}" data-error="{t["err"]}" novalidate>
      <div class="f"><label for="rName">{t["f_name"]}</label><input id="rName" required maxlength="60" placeholder="{t["p_name"]}"></div>
      <div class="f"><label for="rEmail">{t["f_email"]}</label><input id="rEmail" type="email" required maxlength="120" placeholder="{t["p_email"]}"></div>
      <div class="f"><label for="rBiz">{t["f_biz"]}</label><input id="rBiz" maxlength="100" placeholder="{t["p_biz"]}"></div>
      <div class="f"><label for="rHow">{t["f_how"]}</label><textarea id="rHow" rows="3" required maxlength="1000" placeholder="{t["p_how"]}"></textarea></div>
      <div class="hp" aria-hidden="true"><label for="rSite">Website</label><input id="rSite" tabindex="-1" autocomplete="off"></div>
      <p class="err" id="rErr" role="alert" hidden></p>
      <button class="btn primary" type="submit" style="width:100%">{t["send"]} <span class="arr">→</span></button>
      <p class="note" style="margin:14px 0 0">{t["send_note"]}</p>
    </form>
    <div id="refThanks" class="thanks" hidden><h3>{t["th"]}</h3><p>{t["tp"]}</p></div>
  </div>
</div></section>

<section class="bg-cream"><div class="narrow">
  <div class="head center reveal" style="margin-bottom:30px"><h2>{t["faq_h"]}</h2></div>
  {faq_html(t["faq"])}
</div></section>
{ctas[lang]}
""", t["active"], lang=lang, ld_extra=ld)
        out.append((lang, t["name"]))
    return out
