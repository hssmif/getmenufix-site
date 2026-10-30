"""The Spanish website (es/) for restaurant owners in Spain, built by _build.py with the same chrome as the English pages.
Written in natural Spanish from Spain (usted), not translated word for word. Prices always in euros, the same as the
French pricing page. Same rules as everywhere: honest, no invented numbers, no dashes and no hyphens joining words."""
import json
import re

PHOTO_RULES_ES = "https://help.uber.com/es-ES/merchants-and-restaurants/article/gu%C3%ADa-para-las-fotos-de-men%C3%BA-enviadas-por-el-restaurante?nodeId=6985355b-0426-4523-94f2-89bb9b0566e9"

EX = [("burger", "hamburgesa dbl + patatas", "Smash Burger con patatas", "Sin descripción.", "Doble de ternera, cheddar curado, pepinillos y salsa de la casa en pan brioche tostado, con patatas fritas."),
      ("laksa", "LAKSA ESPECIAL", "Laksa de pollo", "ver foto", "Caldo de curry y coco, fideos de arroz, pollo desmenuzado, tofu frito y lima."),
      ("dumplings", "gyozas 10u", "Gyozas de cerdo y cebollino", "Sin descripción.", "Hechas a mano y doradas a la plancha, con aceite de chile para mojar."),
      ("curry", "pollo curri c arroz", "Pollo a la mantequilla con arroz", "Faltas y sin descripción.", "Pollo cocinado a fuego lento en una salsa suave de tomate y mantequilla, ligeramente especiada, con arroz basmati."),
      ("pizza", "PIZZA 3", "Pizza de la huerta", "Un número que nadie recuerda.", "Mozzarella, pimiento, champiñones, aceitunas y albahaca fresca sobre una base crujiente al horno de leña."),
      ("shawarma", "wrap", "Wrap de shawarma de pollo", "Demasiado vago para elegir.", "Pollo marinado, salsa de ajo, pepinillos y patatas fritas envueltos en pan de pita caliente."),
      ("tacos", "taco x3", "Tacos de birria de ternera", "No dice nada del sabor.", "Tres tacos de ternera guisada a fuego lento con cebolla, cilantro, lima y consomé para mojar."),
      ("poke", "POKE SALMON NORMAL", "Poke de salmón", "Mayúsculas y ningún detalle.", "Salmón fresco, arroz de sushi, aguacate, edamame, pepino y mango con sésamo."),
      ("breakfast", "tosta aguacate", "Tostada de aguacate con huevo", "Demasiado corta para tentar.", "Aguacate machacado, huevo poché y queso feta desmenuzado sobre pan de masa madre tostado."),
      ("cake", "tarta choco", "Tarta de tres chocolates", "Nada que le haga desearla.", "Bizcocho de chocolate jugoso con capas de ganache. Hecha en casa cada mañana.")]
EXD = {e[0]: e for e in EX}
MOCKS = {"mock1": "Pho Saigon Corner", "mock2": "Nonna Rosa Pizzeria", "mock3": "Seoul Bowl Kitchen"}
CATS = [("pizza", "Pizza"), ("burger", "Hamburguesas"), ("sushi", "Sushi"), ("noodles", "Fideos"), ("coffee", "Café"),
        ("cake", "Tartas"), ("taco", "Mexicana"), ("curry", "India"), ("dumpling", "Gyozas"), ("chicken", "Pollo"),
        ("salad", "Saludable"), ("croissant", "Panadería"), ("bubbletea", "Bubble tea"), ("kebab", "Kebabs"),
        ("icecream", "Postres")]

FAQ = [
    ("¿Tengo que darles mi contraseña?", "No. Usted nos añade como usuario en su Uber Eats Manager y puede quitarnos el acceso cuando quiera. Nunca le pediremos su contraseña."),
    ("¿Usan fotos falsas de comida?", "Nunca. Solo mejoramos fotos de sus platos reales: mejor luz, un fondo limpio y el tamaño correcto. El cliente debe recibir exactamente lo que ve. La maqueta gratis es solo una vista previa del concepto."),
    ("¿Cuánto tarda?", "Normalmente dos o tres días laborables desde que tenemos sus fotos y el acceso a su Uber Eats Manager."),
    ("¿Me garantizan más pedidos?", "Nadie puede prometerlo con honestidad. Lo que hacemos es que su página sea más clara y más apetecible, que es lo que ayuda a que la gente le elija."),
    ("¿Y si no me gusta?", "No paga. Primero preparamos su página terminada y se la enviamos, antes y después, con cada cambio indicado. Si le gusta, paga. Si no, díganos qué cambiar, o simplemente diga que no y no nos debe nada."),
    ("¿Qué tengo que enviarles?", "Fotos de sus platos hechas con el móvil y con buena luz (junto a una ventana es perfecto) y acceso como usuario a su Uber Eats Manager. Nosotros hacemos el resto."),
    ("¿Trabajan también con cafeterías y panaderías?", "Sí. Restaurantes, comida para llevar, cafeterías, panaderías y heladerías o pastelerías que venden en Uber Eats. No trabajamos con grandes cadenas ni con tiendas de productos envasados."),
    ("¿MenuFix forma parte de Uber?", "No. MenuFix es un servicio independiente y no está afiliado a Uber ni a Uber Eats."),
    ("¿Trabajan con restaurantes en España?", "Sí. Todo se hace por correo electrónico, así que podemos trabajar con restaurantes de cualquier ciudad de España. En estas páginas los precios aparecen en euros."),
]


def build_site_es(page, head, ic, floaty, faq_html, guide_card, guides):
    def ba(n, before_name, after_name, before_desc, after_desc):
        return f"""<div class="reveal"><div class="ba">
  <img src="img/{n}-before.jpg" alt="Antes: una foto oscura y borrosa hecha con el móvil" loading="lazy">
  <img class="after" src="img/{n}-after.jpg" alt="Después: una foto luminosa y nítida del mismo plato" loading="lazy">
  <div class="handle"></div><span class="tag l">Antes</span><span class="tag r">Después</span>
  <input type="range" min="0" max="100" value="50" aria-label="Comparar antes y después">
</div>
<div class="ba-caption"><div><b><s>{before_name}</s></b>{before_desc}</div><div><b>{after_name}</b>{after_desc}</div></div></div>"""

    def mockpair(key, note=True):
        return f"""<div class="mockpair reveal">
  <figure><div class="device"><img src="img/{key}-before.jpg" alt="Página de {MOCKS[key]} antes" loading="lazy"></div><figcaption><span class="pill">Antes</span>Faltas, sin descripciones y sin fotos</figcaption></figure>
  <div class="mockarrow">→</div>
  <figure><div class="device"><img src="img/{key}-after.jpg" alt="Página de {MOCKS[key]} después" loading="lazy"></div><figcaption><span class="pill on">Después</span>Nombres claros, descripciones que venden y fotos luminosas</figcaption></figure>
</div>""" + ('<p class="note" style="text-align:center;margin-top:18px">Maqueta conceptual de un restaurante ficticio, hecha con IA para esta web.</p>' if note else "")

    def cta(title="Vea su página mejorada, gratis.",
            text="Díganos el nombre de su restaurante, cafetería o panadería en Uber Eats y le enviaremos una maqueta gratuita de cómo podría quedar su página. Sin pago y sin compromiso.",
            img="delivery"):
        return f"""<section class="tight"><div class="wrap"><div class="cta reveal">
  <div class="txt"><span class="eyebrow">Maqueta gratis</span><h2>{title}</h2><p class="lead">{text}</p>
    <div class="row"><a class="btn" href="es/contact.html">Quiero mi maqueta gratis <span class="arr">→</span></a><a class="btn ghost" href="es/pricing.html">Ver precios</a></div></div>
  <div class="pic"><img class="bg" src="img/{img}.jpg" alt="" loading="lazy">
    {floaty("burger", "left:-34px;top:40px")}{floaty("bubbletea", "right:24px;bottom:24px", 3)}</div>
</div></div></section>"""

    plans = f"""<div class="plans">
  <div class="plan reveal">{ic("chef")}<h3>Renovación Uber Eats</h3><p class="muted" style="margin:6px 0 0">Toda su página de Uber Eats, hecha por nosotros.</p>
    <div class="price" data-p="full_makeover">569&nbsp;€</div><small class="once">Precio único, sin suscripción</small>
    <ul><li>Cada plato reescrito para vender</li><li>Sus fotos reales mejoradas, toda la carta</li><li>Lo más vendido arriba y una carta clara</li><li>Revisión de precios y menús combinados</li><li class="dfy">Hacemos todos los cambios en su página. Usted no toca nada</li><li>Un mes de actualizaciones</li></ul>
    <a class="btn dark" data-buy="full_makeover" href="#">Quiero la Renovación</a></div>
  <div class="plan feat reveal"><span class="ribbon">El más elegido</span>{ic("star")}<h3>Renovación Plus</h3><p class="muted" style="margin:6px 0 0">Su página, más los extras que traen pedidos.</p>
    <div class="price" data-p="makeover_google">739&nbsp;€</div><small class="once">Precio único, sin suscripción</small>
    <ul><li>Todo lo de la Renovación Uber Eats</li><li>Un banner de portada hecho con sus propias fotos</li><li>Combos y menús creados para usted</li><li>Una oferta de Uber Eats preparada</li><li>Respuestas automáticas a sus reseñas preparadas</li><li>Una segunda revisión de su página a los 30 días</li></ul>
    <a class="btn primary" data-buy="makeover_google" href="#">Quiero Renovación Plus</a></div>
  <div class="plan reveal"><span class="ribbon green">El mejor precio</span>{ic("gift")}<h3>Renovación y Web</h3><p class="muted" style="margin:6px 0 0">Su página de Uber Eats y su propia web.</p>
    <div class="price" data-p="complete">1359&nbsp;€</div><small class="once">Precio único, primer año de alojamiento incluido</small>
    <ul><li>Todo lo de Renovación Plus</li><li>Una web nueva hecha para usted, o su web antigua renovada</li><li>Carta con fotos y precios, y un botón para pedir</li><li>Horario, mapa, reseñas y su Instagram</li><li>Su dominio conectado</li></ul>
    <a class="btn dark" data-buy="complete" href="#">Quiero Renovación y Web</a></div>
</div>
<p class="note reveal" style="text-align:center;margin-top:18px">Los tres están hechos por nosotros, y solo paga cuando haya visto su página terminada y esté contento.</p>"""
    cur = '<p class="curnote">Precios en <b data-curname>euros</b>. Se paga con tarjeta a través de Stripe.</p>'
    cats = '<div class="cats">' + "".join(f'<div class="cat"><div class="ic"><img src="img/icons/{k}.png" alt="" loading="lazy"></div>{t}</div>' for k, t in CATS) + "</div>"
    feat = "".join(f"""<a class="fcard reveal" href="es/examples.html"><div class="ph"><img src="img/{k}-after.jpg" alt="" loading="lazy"><span class="badge">Antes y después</span></div>
  <h3>{EXD[k][2]}</h3><p>{m}</p></a>""" for k, m in [
        ("burger", "Nuevo nombre, descripción y foto"), ("poke", "Reescrito para vender, foto mejorada"),
        ("dumplings", "De una foto oscura a una foto luminosa"), ("cake", "Un postre que nadie quiere saltarse")])
    faq_ld = lambda items: '\n<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [  # noqa: E731
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", a)}} for q, a in items]}, ensure_ascii=False) + "</script>"

    # ------------------------------------------------------------------------------------------------ home
    page("es/index.html", "Mejoramos su página de Uber Eats: carta y fotos | MenuFix",
         "Hacemos que su página de Uber Eats muestre lo bueno que es su plato: nombres claros, descripciones que venden, el orden correcto y mejores fotos de su comida real. Maqueta gratis primero.",
         f"""<header class="hero">
  {floaty("pizza", "left:45%;bottom:4%", 1)}{floaty("sushi", "left:44%;top:6%", 4)}{floaty("coffee", "right:2%;bottom:4%", 2)}
  <div class="wrap">
  <div class="reveal">
    <span class="chip"><img src="img/icons/bag.png" alt="">Para restaurantes, cafeterías y panaderías en Uber Eats</span>
    <h1>Que los clientes con hambre le elijan a <span class="hl">usted.</span></h1>
    <p class="lead">El cliente pide lo que le entra por los ojos. Reescribimos su carta, ponemos arriba lo que más vende y hacemos que las fotos de su comida real den hambre. Incluso podemos hacer todos los cambios en su página por usted.</p>
    <form class="search" action="es/contact.html" method="get">
      <img src="img/icons/menu.png" alt=""><input name="biz" placeholder="Nombre de su restaurante o cafetería" aria-label="Nombre de su restaurante o cafetería">
      <button class="btn primary" type="submit">Quiero mi maqueta gratis <span class="arr">→</span></button>
    </form>
    <div class="trust"><span>Maqueta gratis primero</span><span>Precio único</span><span>Solo comida real</span></div>
  </div>
  <div class="hero-visual reveal">
    <div class="hero-photo"><img src="img/spread.jpg" alt="Una mesa llena de platos para llevar" fetchpriority="high"></div>
    <div class="food-card b"><img src="img/laksa-after.jpg" alt=""><b>Laksa de pollo</b><small>Caldo de curry y coco, fideos de arroz y lima.</small><div class="tagline">18,00 €<i>Foto nueva</i></div></div>
    <div class="food-card a"><img src="img/burger-after.jpg" alt=""><b>Smash Burger con patatas</b><small>Doble de ternera, cheddar, pepinillos y salsa de la casa.</small><div class="tagline">19,50 €<i>Reescrito</i></div></div>
  </div>
</div></header>

<section class="tight"><div class="wrap">
  <div class="head reveal" style="margin-bottom:28px"><div><span class="eyebrow">Para todo tipo de cocina</span><h2>Cocine lo que cocine, lo hacemos apetecible.</h2></div>
    <p class="lead">Restaurantes independientes, comida para llevar, cafeterías, panaderías y pastelerías. Sin grandes cadenas.</p></div>
  <div class="reveal">{cats}</div>
</div></section>

<section class="bg-cream"><div class="wrap">
  <div class="head reveal"><div><span class="eyebrow">Renovaciones destacadas</span><h2>El mismo plato. El mismo precio. Mucho más apetecible.</h2></div>
    <div><p class="lead">Pequeños cambios hacen que la gente deje de desplazarse: un nombre claro, una línea sabrosa sobre el plato y una foto luminosa.</p>
    <a class="btn" href="es/examples.html">Ver todos los ejemplos <span class="arr">→</span></a></div></div>
  <div class="feat-row">{feat}</div>
</div></section>

<section><div class="wrap">
  <div class="head center reveal"><span class="eyebrow">Deslice para comparar</span><h2>De una foto rápida a una que <span class="hl">abre el apetito.</span></h2>
    <p class="lead">Deslice cada foto. A la izquierda, una foto oscura hecha con el móvil y el texto antiguo de la carta. A la derecha, el mismo plato después de nuestra renovación.</p></div>
  <div class="grid2">
    {ba(*EXD["burger"])}
    {ba(*EXD["laksa"])}
  </div>
  <p class="note" style="margin-top:22px;text-align:center">Ejemplos ilustrativos para mostrar el tipo de cambio que hacemos. Imágenes hechas con IA para esta web.</p>
</div></section>

<section class="bg-peach"><div class="wrap">
  <div class="head reveal"><div><span class="eyebrow">Su maqueta gratis</span><h2>Vea su página entera antes de pagar.</h2></div>
    <p class="lead">Cada restaurante con el que hablamos recibe gratis una maqueta conceptual de su propia página, como esta. Verá exactamente qué cambiaríamos, sin ningún compromiso.</p></div>
  {mockpair("mock2")}
  <div class="row" style="justify-content:center;margin-top:34px"><a class="btn primary" href="es/contact.html">Quiero mi maqueta gratis <span class="arr">→</span></a></div>
</div></section>

<section><div class="wrap">
  <div class="head reveal"><div><span class="eyebrow">Qué hacemos</span><h2>Todo lo que su página necesita.</h2></div>
    <p class="lead">Elija lo que necesite. Nosotros nos ocupamos de los detalles, o le enviamos todo listo para copiar si prefiere hacerlo usted.</p></div>
  <div class="grid3">
    <a class="photo-card reveal" href="es/services.html"><div class="ph"><img class="bg" src="img/desk.jpg" alt="" loading="lazy">{ic("pen")}</div><div class="body"><h3>Reescritura de la carta</h3><p>Nombres claros, descripciones que venden, sin faltas y con las categorías en el orden correcto.</p></div></a>
    <a class="photo-card reveal" href="es/services.html#photos"><div class="ph"><img class="bg" src="img/phone.jpg" alt="" loading="lazy">{ic("camera")}</div><div class="body"><h3>Mejora de fotos</h3><p>Sus platos reales con mejor luz, un fondo limpio y el tamaño adecuado para Uber Eats.</p></div></a>
    <a class="photo-card reveal" href="es/services.html#done"><div class="ph"><img class="bg" src="img/kitchen.jpg" alt="" loading="lazy">{ic("chef")}</div><div class="body"><h3>Hecho por nosotros</h3><p>Con todos nuestros paquetes hacemos nosotros todos los cambios en su página de Uber Eats. Usted sigue cocinando.</p></div></a>
  </div>
</div></section>

<section class="bg-butter"><div class="wrap">
  <div class="head center reveal"><span class="eyebrow">Cómo funciona</span><h2>Sencillo, de principio a fin.</h2></div>
  <div class="steps">
    <div class="step reveal"><span class="n">1</span>{ic("gift")}<h3>Maqueta gratis</h3><p>Miramos su página de Uber Eats y le enseñamos cómo podría quedar. Gratis.</p></div>
    <div class="step reveal"><span class="n">2</span>{ic("menu")}<h3>Elija un paquete</h3><p>Precio único, con pago seguro con tarjeta. Sin suscripción.</p></div>
    <div class="step reveal"><span class="n">3</span>{ic("phone")}<h3>Envíe sus fotos</h3><p>Para los paquetes con fotos, haga fotos de sus platos con el móvil y envíenoslas por correo.</p></div>
    <div class="step reveal"><span class="n">4</span>{ic("rocket")}<h3>Su nueva página</h3><p>La actualizamos por usted, o se la enviamos lista para copiar con una guía sencilla.</p></div>
  </div>
</div></section>

<section><div class="wrap">
  <div class="head reveal"><div><span class="eyebrow">Precios</span><h2>Precios claros. Sin sorpresas.</h2></div>
    <div><p class="lead">Tres paquetes, todo hecho por nosotros: la Renovación Uber Eats, Renovación Plus, o Renovación y Web.</p>{cur}</div></div>
  {plans}
</div></section>

<section class="bg-cream"><div class="narrow">
  <div class="head center reveal" style="margin-bottom:30px"><span class="eyebrow">Preguntas</span><h2>Conviene saber</h2></div>
  {faq_html(FAQ[:4])}
  <p style="margin-top:26px;text-align:center"><a class="btn" href="es/faq.html">Todas las preguntas <span class="arr">→</span></a></p>
</div></section>
{cta()}
""", "", lang="es", ld_extra=faq_ld(FAQ[:4]))

    # ------------------------------------------------------------------------------------------------ services
    page("es/services.html", "Reescritura de cartas, fotos de comida y gestión de Uber Eats | MenuFix",
         "Reescribimos su carta de Uber Eats, mejoramos las fotos de sus platos reales y podemos actualizar su página por usted. Para restaurantes, cafeterías y panaderías.",
         f"""{head("Servicios", "Todo lo que hace que la gente <span class='hl'>pida.</span>", "Nos centramos en una sola cosa: su página en la aplicación de reparto. Esto es exactamente lo que hacemos y lo que recibe.", ("pizza", "sushi"))}

<section class="tight" id="menu"><div class="wrap split">
  <div class="reveal">{ic("pen")}<span class="eyebrow" style="display:block">Reescritura de la carta</span><h2>Palabras que venden cada plato.</h2>
    <p class="lead" style="margin-top:20px">La mayoría de las cartas en las aplicaciones de reparto se escribieron con prisa. Las reescribimos para que cada producto sea claro, apetecible y fácil de elegir.</p>
    <ul class="ticks"><li>Faltas, mayúsculas y nombres confusos corregidos</li><li>Una descripción corta y sabrosa para cada producto</li><li>Los más vendidos, arriba</li><li>Categorías en un orden claro, sin desorden</li><li>Solo sus platos y precios reales. Nunca inventamos nada</li></ul></div>
  <div class="reveal">{ba(*EXD["tacos"])}</div>
</div></section>

<section class="tight bg-cream" id="photos"><div class="wrap split rev">
  <div class="reveal">{ic("camera")}<span class="eyebrow" style="display:block">Mejora de fotos</span><h2>Su comida real, en su mejor versión.</h2>
    <p class="lead" style="margin-top:20px">Envíenos fotos de sus platos hechas con el móvil. Las dejamos luminosas, nítidas y apetecibles, sin cambiar la comida.</p>
    <ul class="ticks"><li>Mejor luz, color y nitidez</li><li>Un fondo limpio y cálido</li><li>Encuadradas y con el tamaño para Uber Eats</li><li>Nunca comida falsa ni ingredientes añadidos</li></ul></div>
  <div class="reveal">{ba(*EXD["dumplings"])}</div>
</div></section>

<section class="tight" id="done"><div class="wrap split">
  <div class="reveal">{ic("chef")}<span class="eyebrow" style="display:block">Hecho por nosotros</span><h2>Usted cocina. Nosotros actualizamos su página.</h2>
    <p class="lead" style="margin-top:20px">Incluido en todos los paquetes. Añádanos como usuario en su Uber Eats Manager y hacemos nosotros todos los cambios.</p>
    <ul class="ticks"><li>Sin compartir contraseñas: usted nos añade como usuario</li><li>Nombres, descripciones, categorías y fotos actualizados</li><li>Puede quitarnos el acceso cuando quiera</li><li>Primero ve su página terminada, y solo paga si le gusta</li></ul>
    <div class="row" style="margin-top:30px"><a class="btn primary" href="es/pricing.html">Ver precios <span class="arr">→</span></a></div></div>
  <div class="img reveal"><img src="img/kitchen.jpg" alt="" loading="lazy"></div>
</div></section>

<section class="bg-butter"><div class="wrap">
  <div class="head center reveal"><span class="eyebrow">Para quién es</span><h2>Negocios independientes en Uber Eats.</h2></div>
  <div class="grid4">
    <div class="card reveal">{ic("pizza")}<h3>Restaurantes</h3><p>Pizza, hamburguesas, cocina asiática, de Oriente Medio y todo lo que hay entre medias.</p></div>
    <div class="card reveal">{ic("coffee")}<h3>Cafeterías</h3><p>Desayunos, almuerzos, café y tartas.</p></div>
    <div class="card reveal">{ic("croissant")}<h3>Panaderías y postres</h3><p>Tartas, bollería, helados y dulces.</p></div>
    <div class="card reveal">{ic("kebab")}<h3>Comida para llevar</h3><p>Kebabs, hamburguesas, pollo frito y los favoritos de la noche.</p></div>
  </div>
</div></section>
{cta()}
""", "es/services.html", lang="es")

    # ------------------------------------------------------------------------------------------------ examples
    grid = "".join(f"<div>{ba(*e)}</div>" for e in EX)
    page("es/examples.html", "Ejemplos de cartas de Uber Eats antes y después | MenuFix",
         "Ejemplos de antes y después de cartas de Uber Eats renovadas: nombres más claros, descripciones que venden y mejores fotos.",
         f"""{head("Ejemplos", "Vea la <span class='hl'>diferencia.</span>", "Primero, páginas completas. Después, plato a plato. Deslice cada control para comparar.", ("taco", "cake"))}
<section style="padding-top:30px"><div class="wrap">
  <div class="head reveal"><div><span class="eyebrow">Maquetas de página</span><h2>Renovaciones de la página completa</h2></div>
    <p class="lead">La maqueta gratis que enviamos muestra su página entera después de la renovación: portada, lo más vendido primero, nombres y descripciones claros y fotos apetecibles.</p></div>
  {mockpair("mock1", False)}
  <div style="height:70px"></div>
  {mockpair("mock3", False)}
  <div style="height:70px"></div>
  {mockpair("mock2", False)}
  <p class="note" style="text-align:center;margin-top:24px">Maquetas conceptuales de restaurantes ficticios, hechas con IA para esta web.</p>
</div></section>
<section class="bg-cream"><div class="wrap">
  <div class="head reveal"><div><span class="eyebrow">Plato a plato</span><h2>Fotos y descripciones</h2></div>
    <p class="lead">A la izquierda, una foto rápida con el móvil y el texto antiguo. A la derecha, el mismo plato mejorado y reescrito.</p></div>
  <div class="grid2" style="gap:56px 32px">{grid}</div>
  <p class="note" style="margin-top:40px">Ejemplos ilustrativos de platos y locales ficticios, con imágenes hechas con IA para esta web. Para su página solo trabajamos con fotos de sus platos reales.</p>
</div></section>
{cta("¿Quiere ver su propia página?", "Envíenos el nombre de su restaurante o cafetería en Uber Eats y le enseñaremos gratis una maqueta de la suya.")}
""", "es/examples.html", lang="es")

    # ------------------------------------------------------------------------------------------------ how it works
    page("es/how-it-works.html", "Cómo funciona la renovación de su carta de Uber Eats | MenuFix",
         "De la maqueta gratis a su nueva página de Uber Eats en cuatro pasos sencillos, todo por correo electrónico.",
         f"""{head("Cómo funciona", "Cuatro pasos <span class='hl'>sencillos.</span>", "Todo se puede hacer por correo electrónico. Verá la idea antes de pagar nada.", ("noodles", "croissant"))}
<section class="tight"><div class="wrap split">
  <div class="reveal">{ic("gift")}<span class="eyebrow" style="display:block">Paso 1</span><h2>Su maqueta gratis</h2>
    <p class="lead" style="margin-top:18px">Díganos cuál es su restaurante o cafetería en Uber Eats. Miramos su página y le enviamos una maqueta de cómo podría quedar, con los cambios principales que haríamos. Sin pago y sin compromiso.</p></div>
  <div class="reveal" style="display:flex;justify-content:center"><div class="device solo"><img src="img/mock1-after.jpg" alt="Maqueta conceptual de la página de un restaurante" loading="lazy"></div></div>
</div></section>
<section class="tight bg-cream"><div class="wrap split rev">
  <div class="reveal">{ic("menu")}<span class="eyebrow" style="display:block">Paso 2</span><h2>Elija su paquete</h2>
    <p class="lead" style="margin-top:18px">Elija la Renovación Uber Eats, Renovación Plus, o Renovación y Web. Hacemos nosotros todos los cambios. Pago seguro con tarjeta a través de Stripe, cuando haya visto su página terminada. Precio único, sin suscripción.</p>
    <a class="btn primary" href="es/pricing.html" style="margin-top:10px">Ver precios <span class="arr">→</span></a></div>
  <div class="img reveal"><img src="img/counter.jpg" alt="" loading="lazy"></div>
</div></section>
<section class="tight"><div class="wrap split">
  <div class="reveal">{ic("phone")}<span class="eyebrow" style="display:block">Paso 3</span><h2>Envíe sus fotos</h2>
    <p class="lead" style="margin-top:18px">Para los paquetes con fotos, haga fotos de sus platos con el móvil, con buena luz, y respóndanos al correo con ellas. Mejoramos sus fotos reales. Nunca usamos comida falsa.</p></div>
  <div class="reveal">{ba(*EXD["curry"])}</div>
</div></section>
<section class="tight bg-cream"><div class="wrap split rev">
  <div class="reveal">{ic("rocket")}<span class="eyebrow" style="display:block">Paso 4</span><h2>Su nueva página</h2>
    <p class="lead" style="margin-top:18px">Añádanos como usuario en Uber Eats Manager y lo actualizamos todo: cada nombre, descripción y foto. Normalmente en dos o tres días laborables.</p></div>
  <div class="img reveal"><img src="img/delivery.jpg" alt="" loading="lazy"></div>
</div></section>
{cta()}
""", "es/how-it-works.html", lang="es")

    # ------------------------------------------------------------------------------------------------ pricing
    pricing_faq = [FAQ[2], FAQ[5], FAQ[4], ("¿Cómo se paga?", "Con tarjeta a través de Stripe, un proveedor de pagos seguro, cuando haya visto su página terminada y esté contento con ella. Los precios de esta página están en euros."), FAQ[0]]
    page("es/pricing.html", "Precios para renovar su carta de Uber Eats | MenuFix",
         "Tres paquetes hechos por nosotros, en euros, para su página de Uber Eats: la Renovación Uber Eats, Renovación Plus, y Renovación y Web (una web nueva o su web antigua renovada).",
         f"""{head("Precios", "Tres paquetes, todo <span class='hl'>hecho por nosotros.</span>", "Sin permanencia. Primero preparamos su página terminada, y solo paga cuando la haya visto y esté contento.", ("star", "bag"), cur)}
<section style="padding-top:40px"><div class="wrap">{plans}
  <h2 style="margin-top:90px;font-size:36px" class="reveal">Compare los paquetes</h2>
  <div class="table-scroll reveal"><table class="compare">
    <tr><th></th><th>Renovación Uber Eats</th><th>Renovación Plus</th><th>Renovación y Web</th></tr>
    <tr><td>Cada plato reescrito para vender</td><td class="y">✓</td><td class="y">✓</td><td class="y">✓</td></tr>
    <tr><td>Sus fotos reales mejoradas, toda la carta</td><td class="y">✓</td><td class="y">✓</td><td class="y">✓</td></tr>
    <tr><td>Lo más vendido arriba y orden de la carta</td><td class="y">✓</td><td class="y">✓</td><td class="y">✓</td></tr>
    <tr><td>Revisión de precios y menús combinados</td><td class="y">✓</td><td class="y">✓</td><td class="y">✓</td></tr>
    <tr><td>Hecho por nosotros: todos los cambios</td><td class="y">✓</td><td class="y">✓</td><td class="y">✓</td></tr>
    <tr><td>Un mes de actualizaciones</td><td class="y">✓</td><td class="y">✓</td><td class="y">✓</td></tr>
    <tr><td>Banner de portada con sus propias fotos</td><td class="n">×</td><td class="y">✓</td><td class="y">✓</td></tr>
    <tr><td>Combos, menús y una oferta de Uber Eats preparados</td><td class="n">×</td><td class="y">✓</td><td class="y">✓</td></tr>
    <tr><td>Respuestas a reseñas y revisión a los 30 días</td><td class="n">×</td><td class="y">✓</td><td class="y">✓</td></tr>
    <tr><td>Su propia web, nueva o renovada, primer año de alojamiento</td><td class="n">×</td><td class="n">×</td><td class="y">✓</td></tr>
  </table></div>
  <p class="note reveal" style="margin-top:24px">El pago lo gestiona Stripe. Si paga con una tarjeta de fuera de la zona euro, Stripe puede mostrarle el importe en otra moneda al pagar.</p>
</div></section>
<section class="bg-cream"><div class="narrow"><div class="head center reveal" style="margin-bottom:30px"><h2>Preguntas sobre los precios</h2></div>
{faq_html(pricing_faq)}</div></section>
{cta()}
""", "es/pricing.html", lang="es")

    # ------------------------------------------------------------------------------------------------ about
    page("es/about.html", "Quiénes somos | MenuFix",
         "MenuFix es un pequeño servicio independiente que ayuda a restaurantes, cafeterías y panaderías a sacar más partido a su página de Uber Eats.",
         f"""<header class="page-head" style="padding-top:40px"><div class="wrap"><div class="banner reveal"><img src="img/counter.jpg" alt=""><div>
  <span class="eyebrow">Sobre MenuFix</span><h1>Una gran cocina merece una gran página.</h1>
  <p class="lead">Ayudamos a restaurantes independientes, cafeterías y panaderías a lucir en Uber Eats tan bien como son en realidad.</p></div></div></div></header>
<section style="padding-top:40px"><div class="wrap split">
  <div class="reveal"><span class="eyebrow">Nuestra historia</span><h2>Negocios pequeños, comida de verdad.</h2>
    <p class="lead" style="margin-top:20px">Parte de la mejor comida de cualquier ciudad sale de cocinas pequeñas e independientes. Pero en las aplicaciones de reparto suelen verse peor que las grandes cadenas: sin fotos, con cartas escritas con prisa y con sus mejores platos escondidos al final.</p>
    <p class="lead">MenuFix es un pequeño servicio independiente. Hacemos una sola cosa, páginas de aplicaciones de reparto, así que sabemos qué ayuda a que le elijan. Sin comisiones de agencia ni contratos largos. Trata directamente con nosotros, por correo electrónico.</p></div>
  <div class="img reveal"><img src="img/kitchen.jpg" alt="" loading="lazy"></div>
</div></section>
<section class="bg-butter"><div class="wrap">
  <div class="head center reveal"><span class="eyebrow">En qué creemos</span><h2>Cómo trabajamos</h2></div>
  <div class="grid3">
    <div class="card reveal">{ic("salad")}<h3>Solo comida real</h3><p>Mejoramos fotos de sus platos reales. Nunca usamos comida falsa ni añadimos ingredientes que no están.</p></div>
    <div class="card reveal">{ic("check")}<h3>Honestidad</h3><p>Precios claros, sin costes ocultos y sin promesas que no podemos cumplir. Primero una maqueta gratis, para que sepa lo que recibe.</p></div>
    <div class="card reveal">{ic("rocket")}<h3>Sencillez</h3><p>Todo por correo electrónico, en pocos días. Todo hecho por nosotros, para que usted no tenga que tocar nada.</p></div>
  </div>
  <p class="lead reveal" style="text-align:center;margin:40px auto 0">¿Conoce a dueños de restaurantes? <a href="es/referidos.html">Gane un 30 % por cada restaurante que nos recomiende</a>.</p>
</div></section>
{cta()}
""", "es/about.html", lang="es")

    # ------------------------------------------------------------------------------------------------ faq
    page("es/faq.html", "Preguntas frecuentes sobre la renovación de su página de Uber Eats | MenuFix",
         "Respuestas a las preguntas más habituales sobre cómo MenuFix renueva páginas de Uber Eats para restaurantes en España.",
         f"""{head("Preguntas frecuentes", "Preguntas y <span class='hl'>respuestas.</span>", "¿No encuentra lo que busca? <a class='mailto' href='#'>Escríbanos</a> y le responderemos.", ("icecream", "dumpling"))}
<section style="padding-top:30px"><div class="narrow">{faq_html(FAQ)}</div></section>
{cta()}
""", "es/faq.html", lang="es", ld_extra=faq_ld(FAQ))

    # ------------------------------------------------------------------------------------------------ contact (email only)
    page("es/contact.html", "Maqueta gratis de su página de Uber Eats | MenuFix",
         "Reciba gratis una maqueta de su página de Uber Eats. Sin pago y sin compromiso.",
         f"""<header class="page-head">{floaty("gift", "left:3%;bottom:6%", 2)}<div class="wrap split" style="align-items:start">
  <div><span class="eyebrow">Maqueta gratis</span><h1>Vea su página mejorada, <span class="hl">gratis.</span></h1>
    <p class="lead">Díganos dónde encontrarle en Uber Eats. Le enviaremos por correo una maqueta de cómo podría quedar su página y los cambios principales que haríamos. Sin pago y sin compromiso.</p>
    <ul class="ticks"><li>Normalmente en uno o dos días laborables</li><li>No necesitamos datos de pago</li><li>Solo paga cuando esté contento</li></ul>
    <div class="img reveal" style="margin-top:40px"><img src="img/spread.jpg" alt="" loading="lazy"></div></div>
  <div class="card reveal" style="padding:40px">
    <form id="mockForm" data-lang="es" data-error="Lo sentimos, algo ha fallado. Inténtelo de nuevo en un minuto o escríbanos a hello@getmenufix.com." novalidate>
      <div class="f"><label for="biz">Nombre del restaurante o cafetería</label><input id="biz" required maxlength="100" autocomplete="organization" placeholder="Por ejemplo: Casa Lola"></div>
      <div class="f"><label for="city">Ciudad</label><input id="city" required maxlength="60" placeholder="Por ejemplo: Valencia"></div>
      <div class="f"><label for="link">Enlace de su página de Uber Eats (opcional)</label><input id="link" inputmode="url" maxlength="300" autocomplete="off" placeholder="https://www.ubereats.com/..."></div>
      <div class="f"><label for="email">Su correo</label><input id="email" type="email" required maxlength="120" placeholder="usted@surestaurante.es" autocomplete="email"></div>
      <div class="f"><label for="name">Su nombre</label><input id="name" maxlength="60" autocomplete="given-name" placeholder="Nombre"></div>
      <div class="f"><label for="msg">¿Algo que debamos saber? (opcional)</label><textarea id="msg" maxlength="1500" rows="4" placeholder="Por ejemplo: acabamos de abrir, nuestro plato estrella es..."></textarea></div>
      <div class="hp" aria-hidden="true"><label for="mSite">Website</label><input id="mSite" tabindex="-1" autocomplete="off"></div>
      <label class="consent"><input id="mConsent" type="checkbox" required> <span>Envíenme mi maqueta gratis por correo</span></label>
      <p class="err" id="mErr" role="alert" hidden></p>
      <button class="btn primary" type="submit" style="width:100%">Enviar mi solicitud <span class="arr">→</span></button>
      <p class="note" style="margin:14px 0 0">Usamos su correo solo para su maqueta. Consulte nuestra <a href='privacy.html'>política de privacidad</a>.</p>
    </form>
    <div id="mockThanks" class="thanks" hidden><h3>Gracias, hemos recibido su solicitud.</h3><p>Le enviaremos su maqueta gratis por correo, normalmente en uno o dos días laborables. Si no la ve, mire en su carpeta de spam.</p></div>
  </div>
</div></header>
""", "", lang="es")

    # ------------------------------------------------------------------------------------------------ legal + 404
    legal = {
        "es/privacy.html": ("Privacidad", "Política de privacidad de MenuFix: qué datos recogemos, para qué los usamos y cómo puede pedirnos que los corrijamos o los borremos.", """<p>Última actualización: octubre de 2026</p>

  <h2>Quiénes somos</h2>
  <p>MenuFix es un pequeño servicio independiente que mejora páginas de Uber Eats de restaurantes, cafeterías y pequeños comercios. Puede escribirnos cuando quiera a <a class="mailto" href="#">nuestro correo</a>.</p>

  <h2>Qué datos recogemos</h2>
  <ul>
    <li><b>Datos del negocio que ya son públicos:</b> el nombre de su negocio, su página de Uber Eats y los datos de contacto que su negocio publica (por ejemplo en su web o en redes sociales), para poder enviarle una maqueta gratis.</li>
    <li><b>Lo que nos envía:</b> correos, mensajes, fotos de sus platos y todo lo que comparta con nosotros para poder hacer el trabajo.</li>
    <li><b>Datos de pago:</b> los pagos los gestiona Stripe. Vemos su nombre, su correo y lo que ha comprado, pero nunca el número completo de su tarjeta.</li>
    <li><b>Llamadas:</b> si nos pide que le llamemos, la llamada puede grabarse para no equivocarnos con los detalles. Se lo diremos al principio de la llamada.</li>
  </ul>

  <h2>Para qué los usamos</h2>
  <ul>
    <li>Para contactar con su negocio sobre cómo mejorar su página de Uber Eats y para responderle.</li>
    <li>Para hacer el trabajo que ha pagado y enviárselo.</li>
    <li>Para guardar los registros de pagos que exige la ley.</li>
  </ul>
  <p>No vendemos sus datos ni los compartimos con nadie, salvo con los servicios que usamos para que MenuFix funcione (por ejemplo correo electrónico, pagos, llamadas y las herramientas de IA que nos ayudan a escribir y editar cartas y fotos).</p>

  <h2>¿No le interesa?</h2>
  <p>Responda «no» a cualquiera de nuestros correos o mensajes, o díganoslo en una llamada, y dejaremos de contactarle.</p>

  <h2>Sus opciones</h2>
  <p>Puede preguntarnos qué datos tenemos sobre usted, pedirnos que los corrijamos o pedirnos que los borremos. Solo tiene que escribirnos.</p>

  <h2>Cambios</h2>
  <p>Si cambiamos esta página, actualizaremos la fecha de arriba.</p>"""),
        "es/terms.html": ("Condiciones", "Condiciones de MenuFix: qué hacemos, la maqueta gratis, el pago, la entrega, su contenido y por qué no prometemos resultados.", """<p>Última actualización: octubre de 2026</p>

  <h2>Qué hacemos</h2>
  <p>MenuFix mejora el contenido de su página de Uber Eats: los nombres de los productos, las descripciones, el orden de su carta y las fotos de sus platos reales. Lo que incluye cada paquete se describe en nuestra web y al pagar.</p>

  <h2>Maqueta gratis</h2>
  <p>La maqueta gratis es una vista previa del concepto para enseñarle la idea. No es un diseño final y nunca se usa en su página sin su acuerdo.</p>

  <h2>Pago</h2>
  <p>Los precios son precios únicos que se muestran al pagar. El pago lo cobra Stripe de forma segura cuando hace el pedido.</p>

  <h2>Qué necesitamos de usted</h2>
  <ul>
    <li>Para los paquetes con fotos: fotos de sus platos reales, enviadas por correo.</li>
    <li>Para que lo hagamos todo por usted: acceso como usuario a su Uber Eats Manager. Puede quitarnos el acceso cuando quiera.</li>
  </ul>

  <h2>Entrega</h2>
  <p>Normalmente entregamos en dos o tres días laborables desde que tenemos lo que necesitamos de usted. Si lo hace usted: le enviamos por correo todo listo para copiar, con una guía. Si lo hacemos nosotros: hacemos los cambios en su página de Uber Eats y le avisamos cuando esté listo.</p>

  <h2>Su contenido</h2>
  <p>Su carta, sus fotos y los textos nuevos que escribimos para usted son suyos y puede usarlos en Uber Eats y en cualquier otro sitio. Solo mejoramos fotos de su comida real y nunca añadimos platos ni ingredientes que no estén en su carta.</p>

  <h2>Sin garantía de resultados</h2>
  <p>Hacemos que su página sea más clara y más apetecible, pero no podemos prometer un número concreto de pedidos, valoraciones o ventas, porque dependen de muchas cosas que no controlamos.</p>

  <h2>Preguntas o problemas</h2>
  <p>Si algo no está bien, escríbanos y haremos todo lo posible por solucionarlo con usted.</p>

  <h2>Uber</h2>
  <p>MenuFix es independiente y no está afiliado a Uber ni a Uber Eats, ni cuenta con su respaldo, ni forma parte de ellos. Uber Eats es una marca de su propietario.</p>"""),
    }
    for name, (title, desc, inner) in legal.items():
        page(name, f"{title} | MenuFix", desc,
             f'<header class="page-head"><div class="narrow"><span class="eyebrow">Legal</span><h1>{title}</h1></div></header>\n'
             f'<main class="narrow legal" style="padding-bottom:100px">\n{inner}\n</main>', lang="es")
    page("es/404.html", "Página no encontrada | MenuFix", "Esta página no existe.",
         f"""<header class="page-head" style="text-align:center;padding:140px 0">{floaty("icecream", "left:12%;top:30%")}{floaty("pizza", "right:12%;top:40%", 3)}<div class="narrow">
  <span class="eyebrow">404</span><h1>Esta página no está en la carta.</h1>
  <p class="lead" style="margin-left:auto;margin-right:auto">La página que busca no existe o ha cambiado de sitio.</p>
  <div class="row" style="justify-content:center;margin-top:30px"><a class="btn primary" href="es/index.html">Volver al inicio</a></div>
</div></header>""", lang="es")
