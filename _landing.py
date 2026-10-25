"""Landing pages by type of business and by city (SEO), built by _build.py into uber-eats/*.html.
Rules: practical and honest, no invented numbers, reviews or local claims, Australian English, no dashes or hyphens
between words. We work by email with businesses anywhere: the city pages say so plainly, they don't pretend we have
a local office."""

CUISINES = [
    {
        "slug": "cafes", "icons": ("coffee", "croissant"), "ex": ["breakfast", "cake"],
        "title": "Uber Eats Menu Makeover for Cafés | MenuFix",
        "desc": "We rewrite café menus on Uber Eats and enhance photos of your real breakfasts, lunches, coffee and cakes. A free mockup first, one time prices.",
        "eyebrow": "For cafés", "h1": "Make your café easy to choose on <span class='hl'>Uber Eats.</span>",
        "lead": "Great coffee and a beautiful brunch don't always come across on a delivery app. We make your café's page as inviting as your counter.",
        "problems": [("Breakfast and lunch mixed together", "One long list makes people scroll past your best dishes. We group the menu by time of day and put favourites first."),
                     ("Coffee options that confuse", "Sizes, milks and extra shots set up as clear options, so orders arrive right and nobody has to guess."),
                     ("Photos taken under café lights", "We enhance photos of your real plates and cakes so they look bright and fresh, without changing the food.")],
        "tips": ["Use time based menus so breakfast only shows when you serve it.",
                 "Put your signature brunch dish and best cake near the top.",
                 "Say what comes on the plate: \"Smashed avocado, poached egg and feta on toasted sourdough\".",
                 "List milk alternatives and extra shots as paid options.",
                 "Pause cakes and pastries as soon as they sell out."],
        "faq": [("Do you work with small cafés?", "Yes. Most of the businesses we help are independent cafés, restaurants and bakeries, not chains."),
                ("Can you help with coffee options on Uber Eats?", "Yes. We set out sizes, milks and extras as clear options in the menu we send you, and we set them up for you.")],
        "guides": ["uber-eats-menu-categories", "write-uber-eats-menu-descriptions", "uber-eats-food-photos-phone"],
    },
    {
        "slug": "pizza", "icons": ("pizza", "chef"), "ex": ["pizza"],
        "title": "Uber Eats Menu Makeover for Pizza Shops | MenuFix",
        "desc": "Clear pizza names, descriptions that sell and better photos of your real pizzas on Uber Eats. For independent pizzerias. Free mockup first.",
        "eyebrow": "For pizza shops", "h1": "Pizzas that look as good on the app as they <span class='hl'>taste.</span>",
        "lead": "When every pizza page looks the same, clear names, real toppings and bright photos help yours stand out.",
        "problems": [("Numbered pizzas", "\"Pizza 7\" means nothing to a new customer. We give every pizza a name and list its toppings."),
                     ("Sizes and bases that aren't clear", "Small, large, family, gluten free base: we set them out so people know exactly what they'll get."),
                     ("Dark photos from the oven", "We enhance photos of your real pizzas so the colours of the toppings come through.")],
        "tips": ["Name each pizza and list the main toppings in the description.",
                 "Say the size in a way people understand: \"Large, 8 slices\".",
                 "Put deals and family bundles in their own clear category.",
                 "Shoot pizzas from above, straight out of the oven, in daylight if you can.",
                 "Mark vegetarian options only when they truly are."],
        "faq": [("Can you help with pizza deals and bundles?", "Yes. We write what's included in each bundle clearly and suggest where to place deals in your menu."),
                ("Do you change how my pizzas look in photos?", "No. We improve light, colour and background, but the pizza stays exactly as you make it.")],
        "guides": ["write-uber-eats-menu-descriptions", "price-menu-uber-eats", "uber-eats-banner-photo"],
    },
    {
        "slug": "asian-restaurants", "icons": ("noodles", "dumpling"), "ex": ["laksa", "dumplings", "poke"],
        "title": "Uber Eats Menu Makeover for Asian Restaurants | MenuFix",
        "desc": "Clear dish names, helpful descriptions and better photos for Asian restaurants on Uber Eats: noodles, dumplings, curries, sushi and more. Free mockup first.",
        "eyebrow": "For Asian restaurants", "h1": "Help new customers find their new <span class='hl'>favourite dish.</span>",
        "lead": "Long menus with dish names some customers don't know can be hard to order from. We keep your dishes authentic and make them easy to choose.",
        "problems": [("Long menus with numbers", "We organise big menus into clear categories and put your best sellers first, so people don't give up scrolling."),
                     ("Names some customers don't know", "Keep the real name, and add a few words that say what it is: \"Laksa: coconut curry noodle soup\"."),
                     ("Missing spice levels and portions", "Spice level, number of pieces and what comes with rice: the details that stop people hesitating.")],
        "tips": ["Keep your dish's real name, then explain it in plain words.",
                 "Show the spice level on hot dishes.",
                 "Say how many pieces come in dumplings, rolls and sushi.",
                 "Group noodles, rice dishes, soups and sides so they're easy to scan.",
                 "Photograph soups and noodle bowls from above to show what's inside."],
        "faq": [("Will you change the names of my dishes?", "Only to make them clearer. We keep the names your regulars know and add a short explanation for new customers."),
                ("Can you handle a long menu?", "Yes. Every package covers photos for your whole menu and a new structure for it.")],
        "guides": ["uber-eats-menu-categories", "write-uber-eats-menu-descriptions", "get-more-orders-on-uber-eats"],
    },
    {
        "slug": "takeaways", "icons": ("kebab", "burger"), "ex": ["burger", "shawarma", "tacos"],
        "title": "Uber Eats Menu Makeover for Takeaways | MenuFix",
        "desc": "Better Uber Eats pages for takeaways: burgers, kebabs, fried chicken, tacos and late night food. Clear combos, descriptions and real photos. Free mockup first.",
        "eyebrow": "For takeaways", "h1": "Late night favourites, made easy to <span class='hl'>order.</span>",
        "lead": "Takeaway customers decide fast. Clear combos, simple names and bright photos of your real food help them choose you.",
        "problems": [("Combos that don't say what's in them", "\"Meal deal 2\" becomes \"Cheeseburger, chips and a can of drink\", so there are no surprises."),
                     ("ALL CAPS and short codes", "We fix names, typos and capitals so your page looks as cared for as your food."),
                     ("Photos that don't show the food", "We enhance photos of your real burgers, wraps and boxes so people can see what they're getting.")],
        "tips": ["Write out every item in each combo.",
                 "Shoot burgers and wraps from the side, so the layers show.",
                 "Put extras like cheese, sauces and drinks as paid options.",
                 "Check your late night hours match when you're really cooking.",
                 "Use vented packaging for anything crispy."],
        "faq": [("Can you help with our combos and meal deals?", "Yes. We rewrite them so each one says exactly what's included, and suggest where to place them in your menu."),
                ("We're open late. Does that matter?", "Late night customers want to decide quickly, so a clear, short menu with photos helps even more.")],
        "guides": ["price-menu-uber-eats", "get-more-orders-on-uber-eats", "reply-to-uber-eats-reviews"],
    },
]

CITIES = [
    {"slug": "sydney", "name": "Sydney", "icons": ("sushi", "coffee"),
     "intro": "Sydney has a huge range of independent restaurants, cafés and takeaways on Uber Eats, so customers have plenty of choice. A clear page with real photos helps yours get noticed."},
    {"slug": "melbourne", "name": "Melbourne", "icons": ("coffee", "croissant"),
     "intro": "Melbourne is known for its cafés and its food, and plenty of great independent places are on Uber Eats. We help your page show what makes your food worth ordering."},
    {"slug": "brisbane", "name": "Brisbane", "icons": ("taco", "burger"),
     "intro": "Whether you run a café, a takeaway or a family restaurant in Brisbane, a clear Uber Eats page helps hungry customers choose you."},
    {"slug": "perth", "name": "Perth", "icons": ("pizza", "salad"),
     "intro": "Perth restaurants, cafés and takeaways can look their best on Uber Eats too. We work by email, so being on the other side of the country from Sydney makes no difference."},
    {"slug": "adelaide", "name": "Adelaide", "icons": ("noodles", "cake"),
     "intro": "From cafés to late night takeaways, independent places in Adelaide deserve an Uber Eats page that does their food justice."},
]


def build_landing(page, head, cta, faq_html, guide_card, guides, ba, exd, ic):
    by_slug = {g["slug"]: g for g in guides}

    def guide_row(slugs):
        return '<div class="grid3">' + "".join(guide_card(by_slug[s]) for s in slugs if s in by_slug) + "</div>"

    def others(current, items, label):
        return f'<div class="chips" aria-label="{label}">' + "".join(
            f'<a href="uber-eats/{x["slug"]}.html">{x["name"] if "name" in x else x["eyebrow"].replace("For ", "").capitalize()}</a>' for x in items if x["slug"] != current) + "</div>"

    for c in CUISINES:
        problems = "".join(f'<div class="card reveal">{ic("check")}<h3>{t}</h3><p>{d}</p></div>' for t, d in c["problems"])
        examples = "".join(ba(*exd[k]) for k in c["ex"])
        tips = "".join(f"<li>{t}</li>" for t in c["tips"])
        page(f"uber-eats/{c['slug']}.html", c["title"], c["desc"], f"""{head(c['eyebrow'], c['h1'], c['lead'], c['icons'],
     '<div class="row" style="margin-top:28px"><a class="btn primary" href="contact.html">Get my free mockup <span class="arr">→</span></a><a class="btn ghost" href="pricing.html">See pricing</a></div>')}
<section class="tight"><div class="wrap">
  <div class="head reveal"><div><span class="eyebrow">What we fix</span><h2>Common problems, sorted.</h2></div></div>
  <div class="grid3">{problems}</div>
</div></section>
<section class="tight bg-cream"><div class="wrap">
  <div class="head reveal"><div><span class="eyebrow">Before and after</span><h2>Same dish, easier to choose.</h2></div>
    <p class="lead">Illustrative examples with images made with AI for this website. For your page we only work from photos of your real dishes.</p></div>
  <div class="grid2">{examples}</div>
</div></section>
<section class="tight"><div class="narrow prose">
  <h2 style="margin-top:0">Quick tips you can use today</h2>
  <ul class="ticks">{tips}</ul>
</div></section>
<section class="tight bg-cream"><div class="narrow">
  <div class="head center reveal" style="margin-bottom:30px"><h2>Questions</h2></div>
  {faq_html(c["faq"])}
  {others(c["slug"], CUISINES, "Other businesses we help")}
</div></section>
<section class="tight"><div class="wrap">
  <div class="head reveal" style="margin-bottom:30px"><div><span class="eyebrow">Guides</span><h2>Do it yourself</h2></div></div>
  {guide_row(c["guides"])}
</div></section>
{cta()}
""", "")

    city_faq = lambda n: [  # noqa: E731
        (f"Do you meet restaurants in person in {n}?", "No. We work entirely by email, which keeps our prices simple. You send your Uber Eats link and photos, we send back your new menu and photos, or make the changes for you."),
        ("Do I need to give you my Uber Eats password?", "No. You add us as a user with menu access in Uber Eats Manager, and you can remove us any time."),
        ("How long does it take?", "Usually two to three working days after we have your photos and access to your Uber Eats Manager."),
    ]
    cards = "".join(f'<div class="card reveal">{ic(c["icons"][0])}<h3><a href="uber-eats/{c["slug"]}.html" style="color:inherit">{c["eyebrow"].replace("For ", "").capitalize()}</a></h3><p>{c["lead"]}</p></div>' for c in CUISINES)
    for c in CITIES:
        n = c["name"]
        page(f"uber-eats/{c['slug']}.html", f"Uber Eats Menu Makeover in {n} | MenuFix",
             f"Uber Eats menu rewrites and photo enhancement for independent restaurants, cafés and takeaways in {n}. Done by email, free mockup first, one time prices.",
             f"""{head(n, f"Better Uber Eats pages for {n} <span class='hl'>restaurants.</span>", c["intro"], c["icons"],
     '<div class="row" style="margin-top:28px"><a class="btn primary" href="contact.html">Get my free mockup <span class="arr">→</span></a><a class="btn ghost" href="how-it-works.html">How it works</a></div>')}
<section class="tight"><div class="narrow prose">
  <h2 style="margin-top:0">What we do for {n} businesses</h2>
  <ul class="ticks"><li>Rewrite every dish name and description so it's clear and appetising.</li><li>Put your best sellers first and tidy your categories.</li><li>Enhance photos of your real dishes: better light, a clean background, sized for Uber Eats.</li><li>Make every change on your Uber Eats page for you.</li></ul>
  <h2>How it works from {n}</h2>
  <p>Everything happens by email, so it works the same wherever you are. You send us your restaurant's name or Uber Eats link, and we send a free mockup of how your page could look. If you like it, you choose a package, send photos of your dishes taken on your phone, and we do the rest.</p>
  <p>Prices are shown in Australian dollars for visitors in Australia. See <a href="/pricing.html">pricing</a>.</p>
  <h2>Moving from Menulog?</h2>
  <p>If you're moving your restaurant from Menulog to Uber Eats, our guide <a href="/guides/moving-from-menulog-to-uber-eats.html">Moving from Menulog to Uber Eats: set up your page right</a> goes through what Uber asks for and how to set up your new page, from Uber's own merchant pages.</p>
  <h2>Honest about what we are</h2>
  <p>MenuFix is a small independent service, not a local agency and not part of Uber. We can't promise more orders, and nobody honestly can. What we do is make your page clearer and more appetising, which is what helps people choose you.</p>
</div></section>
<section class="tight bg-cream"><div class="wrap">
  <div class="head reveal"><div><span class="eyebrow">Who we help</span><h2>Independent places of every kind.</h2></div></div>
  <div class="grid4">{cards}</div>
</div></section>
<section class="tight"><div class="narrow">
  <div class="head center reveal" style="margin-bottom:30px"><h2>Questions</h2></div>
  {faq_html(city_faq(n))}
  {others(c["slug"], CITIES, "Other cities")}
</div></section>
{cta(f"See your {n} page improved, free.")}
""", "")

    city_links = "".join(f'<a href="uber-eats/{c["slug"]}.html">{c["name"]}</a>' for c in CITIES)
    page("uber-eats/index.html", "Who We Help: Restaurants, Cafés and Takeaways on Uber Eats | MenuFix",
         "MenuFix helps independent cafés, pizza shops, Asian restaurants and takeaways across Australia and beyond make their Uber Eats page clearer and more appetising.",
         f"""{head("Who we help", "Independent restaurants, cafés and <span class='hl'>takeaways.</span>", "We work by email with independent businesses across Australia, New Zealand, the UK and Ireland. Pick your type of business or your city.", ("chef", "bag"))}
<section class="tight" style="padding-top:30px"><div class="wrap">
  <div class="grid4">{cards}</div>
  <h2 style="margin-top:70px;font-size:30px" class="reveal">Cities in Australia</h2>
  <div class="chips">{city_links}</div>
  <p class="muted" style="margin-top:18px">Not on the list? It doesn't matter: everything is done by email, wherever you are.</p>
</div></section>
{cta()}
""", "uber-eats/index.html")
    return [f"uber-eats/{x['slug']}.html" for x in CUISINES + CITIES] + ["uber-eats/index.html"]
