"""Builds the getmenufix.com pages (shared header and footer). Run: python3 _build.py"""
from pathlib import Path

ROOT = Path(__file__).parent
NAV = [("services.html", "Services"), ("examples.html", "Examples"), ("how-it-works.html", "How it works"),
       ("pricing.html", "Pricing"), ("about.html", "About"), ("faq.html", "FAQ")]


def page(name, title, desc, body, active=""):
    on = ' class="on"'
    links = "".join(f'<a href="{h}"{on if h == active else ""}>{t}</a>' for h, t in NAV)
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="canonical" href="https://getmenufix.com/{'' if name == 'index.html' else name}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="https://getmenufix.com/img/hero.jpg">
<meta property="og:type" content="website">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,500;0,9..144,600;0,9..144,700;1,9..144,500&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
</head>
<body>
<nav class="nav"><div class="wrap">
  <a class="logo" href="index.html"><img src="img/logo-mark.svg" alt=""><b>menu<span>fix</span></b></a>
  <button class="burger" aria-label="Menu" onclick="document.querySelector('.nav .links').classList.toggle('open')">☰</button>
  <div class="links">{links}<a class="btn primary small" href="contact.html">Free mockup</a></div>
</div></nav>
{body}
<footer><div class="wrap">
  <div class="top">
    <div><a class="logo" href="index.html"><img src="img/logo-mark.svg" alt=""><b>menu<span>fix</span></b></a>
      <p style="max-width:330px">Uber Eats page makeovers for independent restaurants, cafés and small shops. Clear menus, better photos of your real food, done for you.</p></div>
    <div><h4>Services</h4><a href="services.html">Menu rewrite</a><a href="services.html#photos">Photo enhancement</a><a href="services.html#done">Done for you</a><a href="examples.html">Examples</a></div>
    <div><h4>Company</h4><a href="about.html">About</a><a href="how-it-works.html">How it works</a><a href="pricing.html">Pricing</a><a href="faq.html">FAQ</a></div>
    <div><h4>Get started</h4><a href="contact.html">Free mockup</a><a class="mailto" href="#">Email us</a><a href="privacy.html">Privacy</a><a href="terms.html">Terms</a></div>
  </div>
  <div class="bottom"><span>© 2026 MenuFix. All rights reserved.</span><span>MenuFix is independent and not affiliated with Uber or Uber Eats.</span></div>
</div></footer>
<script src="site.js"></script>
</body>
</html>
"""
    (ROOT / name).write_text(html)


def ba(n, before_name, after_name, before_desc, after_desc):
    return f"""<div class="reveal"><div class="ba">
  <img src="img/{n}-before.jpg" alt="Before: a quick phone photo" loading="lazy">
  <img class="after" src="img/{n}-after.jpg" alt="After: a clear, bright photo" loading="lazy">
  <div class="handle"></div><span class="tag l">Before</span><span class="tag r">After</span>
  <input type="range" min="0" max="100" value="50" aria-label="Compare before and after">
</div>
<div class="ba-caption"><div><b><s>{before_name}</s></b>{before_desc}</div><div><b>{after_name}</b>{after_desc}</div></div></div>"""


MOCKS = {"mock1": "Pho Saigon Corner", "mock2": "Nonna Rosa Pizzeria", "mock3": "Seoul Bowl Kitchen"}


def mockpair(key, note=True):
    return f"""<div class="mockpair reveal">
  <figure><div class="device"><img src="img/{key}-before.jpg" alt="{MOCKS[key]} page before" loading="lazy"></div><figcaption><span class="pill">Before</span>Typos, no descriptions, missing photos</figcaption></figure>
  <div class="mockarrow">→</div>
  <figure><div class="device"><img src="img/{key}-after.jpg" alt="{MOCKS[key]} page after" loading="lazy"></div><figcaption><span class="pill on">After</span>Clear names, descriptions that sell, bright photos of the real dishes</figcaption></figure>
</div>""" + ('<p class="note" style="text-align:center;margin-top:18px">Concept mockup for a fictional restaurant, made with AI for this website.</p>' if note else "")


def cta(title="See your page improved, free",
        text="Tell us your restaurant or shop on Uber Eats. We'll send you a free mockup of how your page could look. No payment, no obligation.",
        img="delivery"):
    return f"""<section class="tight"><div class="wrap"><div class="cta reveal"><img src="img/{img}.jpg" alt="" loading="lazy"><div>
  <span class="eyebrow" style="color:#f6a184">Free mockup</span><h2>{title}</h2><p class="lead">{text}</p>
  <div class="row"><a class="btn primary" href="contact.html">Get my free mockup <span class="arr">→</span></a><a class="btn" style="border-color:#fff;color:#fff" href="pricing.html">See pricing</a></div>
</div></div></div></section>"""


PLANS = """<div class="plans">
  <div class="plan reveal"><h3>Menu Fix</h3><p class="muted">Clean, clear and ready to sell.</p>
    <div class="price" data-p="menu_fix"></div><small class="muted">one time</small>
    <ul><li>Typos and wording fixed</li><li>Every description rewritten to sell</li><li>Best sellers moved to the top</li><li>Categories in the right order</li></ul>
    <a class="btn dark" data-buy="menu_fix" href="#">Get Menu Fix</a></div>
  <div class="plan feat reveal"><span class="ribbon">Recommended</span><h3>Menu and Photos</h3><p class="muted">Everything in Menu Fix, plus your photos.</p>
    <div class="price" data-p="menu_photos"></div><small class="muted">one time</small>
    <ul><li>Everything in Menu Fix</li><li>Your real photos of 5 dishes enhanced</li><li>Better light and a clean background</li><li>Sized for Uber Eats</li></ul>
    <a class="btn primary" data-buy="menu_photos" href="#">Get Menu and Photos</a></div>
  <div class="plan reveal"><h3>Full Makeover</h3><p class="muted">The complete refresh.</p>
    <div class="price" data-p="full_makeover"></div><small class="muted">one time</small>
    <ul><li>Everything above for up to 15 dishes</li><li>New menu layout and structure</li><li>One month of updates when you change dishes or prices</li></ul>
    <a class="btn dark" data-buy="full_makeover" href="#">Get Full Makeover</a></div>
</div>
<div class="addon reveal"><div class="ic">✓</div>
  <div><h3 style="font-size:22px">Done for you</h3><p class="muted" style="margin:6px 0 0">We make every change on your Uber Eats page ourselves. You don't touch anything: just add us as a user on Uber Eats Manager. Tick the box at checkout.</p></div>
  <div class="price" data-p="done_for_you"></div></div>
<p class="note" style="margin-top:18px">One time price, no subscription. Secure payment by Stripe. Prefer to do it yourself? We send everything ready to copy with a simple guide, included in every package.</p>"""

CUR = """<p class="curnote">Prices in <b data-curname>your currency</b>, charged in the same currency at checkout.</p>"""

FAQ = [
    ("Do I need to give you my password?", "No. For Done for you, you add us as a user on your Uber Eats Manager, and you can remove us any time. We never ask for your password."),
    ("Do you use fake food photos?", "Never. We only enhance photos of your real dishes: better light, a clean background and the right size. Customers should get exactly what they see, and Uber Eats requires real photos too. The free mockup is a concept preview only."),
    ("How long does it take?", "Usually two to three working days after we have your photos and, for Done for you, access to your Uber Eats Manager."),
    ("Will this guarantee more orders?", "No one can honestly promise that. What we do is make your page clearer and more appetising, which is what helps people choose you."),
    ("What do I need to send you?", "For Menu Fix, nothing: we work from your current page. For the photo packages, photos of your dishes taken on your phone in good light. Near a window is perfect."),
    ("Do you work with cafés and shops too?", "Yes. Restaurants, cafés, bakeries, dessert places, grocers and other small businesses that sell on Uber Eats. We don't work with big chains."),
    ("Is MenuFix part of Uber?", "No. MenuFix is an independent service and is not affiliated with Uber or Uber Eats."),
    ("Which countries do you work with?", "Australia, New Zealand, the UK, Ireland and more. Prices show in your currency at checkout."),
]


def faq_html(items):
    return '<div class="faq">' + "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in items) + "</div>"


# ------------------------------------------------------------------------------------------------ home
page("index.html", "MenuFix | Uber Eats page makeovers for restaurants, cafés and shops",
     "We make your Uber Eats page show how good your food is: clear names, descriptions that sell, the right order and better photos of your real food. Done for you. Free mockup first.",
f"""<header class="hero"><div class="wrap">
  <div class="reveal">
    <span class="eyebrow">Uber Eats page makeovers</span>
    <h1>Your food is great. Your Uber Eats page should <em>show it.</em></h1>
    <p class="lead">Customers order what they can see and understand. We rewrite your menu, put your best sellers first and make photos of your real food look their best. We can even make every change on your page for you.</p>
    <div class="row"><a class="btn primary" href="contact.html">Get a free mockup <span class="arr">→</span></a><a class="btn" href="examples.html">See examples</a></div>
    <div class="trust"><span><b>Free</b> mockup first</span><span><b>One time</b> price</span><span><b>Real food</b> photos only</span></div>
  </div>
  <div class="hero-visual reveal">
    <div class="hero-photo"><img src="img/hero.jpg" alt="A freshly baked pizza" fetchpriority="high"></div>
    <div class="phone"><div class="screen">
      <div class="app-top"><b>Popular</b><small>Most ordered right now</small></div>
      <div class="app-item"><div><b>Smash Burger and Fries</b><small>Double beef, cheddar, pickles and house sauce on a toasted brioche bun.</small><i>$19.50</i></div><img src="img/burger-after.jpg" alt=""></div>
      <div class="app-item"><div><b>Chicken Laksa</b><small>Rich coconut curry broth, rice noodles, poached chicken and lime.</small><i>$18.00</i></div><img src="img/laksa-after.jpg" alt=""></div>
      <div class="app-item"><div><b>Pork and Chive Dumplings</b><small>Handmade, pan fried, with chilli oil and black vinegar.</small><i>$14.50</i></div><img src="img/dumplings-after.jpg" alt=""></div>
    </div></div>
    <div class="badge-float"><span class="tick">✓</span><div><b>Menu fixed</b><br><span class="muted">12 dishes rewritten</span></div></div>
  </div>
</div></header>

<section class="bg2"><div class="wrap">
  <div class="head reveal"><div><span class="eyebrow">Why it matters</span><h2>People decide in seconds.</h2></div>
    <p class="lead">On a delivery app your page is your shop window. A missing photo, a typo or a dish nobody understands is enough for someone to scroll to the next place.</p></div>
  <div class="grid3">
    <div class="card reveal"><div class="icon">📷</div><h3>Photos that make people hungry</h3><p>Dark or missing photos get skipped. Your best dishes need a bright, clear picture of the real food.</p></div>
    <div class="card reveal"><div class="icon">✍️</div><h3>Words that sell the dish</h3><p>A short line on what's in it and why it's good turns a name into a reason to order, especially at higher prices.</p></div>
    <div class="card reveal"><div class="icon">⭐</div><h3>Best sellers first</h3><p>Your most loved dishes should be the first thing people see, in a menu that's easy to find your way around.</p></div>
  </div>
</div></section>

<section><div class="wrap">
  <div class="head reveal"><div><span class="eyebrow">Before and after</span><h2>Same dish. Same price. More appetising.</h2></div>
    <div><p class="lead">Drag the slider to compare. We turn quick phone snaps and unclear names into a page people want to order from.</p>
    <a class="btn" href="examples.html">See all examples <span class="arr">→</span></a></div></div>
  <div class="grid2">
    {ba("burger", "dbl burgr + chips", "Smash Burger and Fries", "No description.", "Double beef, aged cheddar, pickles and house sauce on a toasted brioche bun.")}
    {ba("laksa", "LAKSA SPECIAL", "Chicken Laksa", "see photo", "Rich coconut curry broth, rice noodles, poached chicken, tofu puffs and lime.")}
  </div>
  <p class="note" style="margin-top:22px">Illustrative examples to show the kind of change we make. Images made with AI for this website.</p>
</div></section>

<section class="bg-dark"><div class="wrap">
  <div class="head reveal"><div><span class="eyebrow">Your free mockup</span><h2>See your whole page, before you pay.</h2></div>
    <p class="lead">Every restaurant we talk to gets a free concept mockup of their own page, like this one. You see exactly what we'd change, with no obligation.</p></div>
  {mockpair("mock2")}
  <div class="row" style="justify-content:center;margin-top:34px"><a class="btn primary" href="contact.html">Get my free mockup <span class="arr">→</span></a></div>
</div></section>

<section class="bg2"><div class="wrap">
  <div class="head reveal"><div><span class="eyebrow">What we do</span><h2>Everything your page needs, in one place.</h2></div>
    <p class="lead">Pick what you need. We handle the details, or we send everything ready to copy if you'd rather do it yourself.</p></div>
  <div class="grid3">
    <a class="photo-card reveal" href="services.html" style="text-decoration:none;color:inherit"><img src="img/desk.jpg" alt="" loading="lazy"><div class="body"><span class="num">01</span><h3>Menu rewrite</h3><p>Clear names, descriptions that sell, typos gone and categories in the right order.</p></div></a>
    <a class="photo-card reveal" href="services.html#photos" style="text-decoration:none;color:inherit"><img src="img/phone.jpg" alt="" loading="lazy"><div class="body"><span class="num">02</span><h3>Photo enhancement</h3><p>Your real dishes with better light, a clean background and the right size for Uber Eats.</p></div></a>
    <a class="photo-card reveal" href="services.html#done" style="text-decoration:none;color:inherit"><img src="img/kitchen.jpg" alt="" loading="lazy"><div class="body"><span class="num">03</span><h3>Done for you</h3><p>We make every change on your Uber Eats page ourselves. You keep cooking.</p></div></a>
  </div>
</div></section>

<section><div class="wrap">
  <div class="head center reveal"><span class="eyebrow">How it works</span><h2>Simple, from start to finish.</h2></div>
  <div class="steps">
    <div class="step reveal"><div class="n">1</div><h3>Free mockup</h3><p>We look at your Uber Eats page and show you how it could look. Free.</p></div>
    <div class="step reveal"><div class="n">2</div><h3>Choose a package</h3><p>One time price, paid securely by card. No subscription.</p></div>
    <div class="step reveal"><div class="n">3</div><h3>Send your photos</h3><p>For photo packages, snap your dishes on your phone and email them.</p></div>
    <div class="step reveal"><div class="n">4</div><h3>Your new page</h3><p>We update it for you, or send it ready to copy with a simple guide.</p></div>
  </div>
</div></section>

<section class="bg2"><div class="wrap">
  <div class="head reveal"><div><span class="eyebrow">Pricing</span><h2>Clear prices. No surprises.</h2></div>
    <div><p class="lead">Choose a package. Add Done for you if you'd like us to make every change for you.</p>{CUR}</div></div>
  {PLANS}
</div></section>

<section><div class="narrow">
  <div class="head center reveal" style="margin-bottom:30px"><span class="eyebrow">Questions</span><h2>Good to know</h2></div>
  {faq_html(FAQ[:4])}
  <p style="margin-top:26px;text-align:center"><a href="faq.html">All questions →</a></p>
</div></section>
{cta()}
""")

# ------------------------------------------------------------------------------------------------ services
page("services.html", "Services | MenuFix", "Menu rewrites, photo enhancement of your real food and Done for you updates for your Uber Eats page.",
f"""<header class="page-head"><div class="wrap">
  <span class="eyebrow">Services</span><h1>Everything that makes people order.</h1>
  <p class="lead">We focus on one thing: your delivery app page. Here's exactly what we do and what you get.</p>
</div></header>

<section class="tight" id="menu"><div class="wrap split">
  <div class="reveal"><span class="eyebrow">01 · Menu rewrite</span><h2>Words that sell every dish.</h2>
    <p class="lead" style="margin-top:20px">Most menus on delivery apps were typed in a hurry. We rewrite them so every item is clear, appetising and easy to choose.</p>
    <ul class="ticks"><li>Typos, capitals and confusing names fixed</li><li>A short, tasty description for every item</li><li>Best sellers moved to the top</li><li>Categories in a clear order, without clutter</li><li>Your real dishes and prices only. We never invent anything</li></ul></div>
  <div class="img reveal"><img src="img/desk.jpg" alt="" loading="lazy"></div>
</div></section>

<section class="tight bg2" id="photos"><div class="wrap split rev">
  <div class="reveal"><span class="eyebrow">02 · Photo enhancement</span><h2>Your real food, at its best.</h2>
    <p class="lead" style="margin-top:20px">Send us photos of your dishes taken on your phone. We make them bright, sharp and appetising, while keeping the food exactly as it is.</p>
    <ul class="ticks"><li>Better light, colour and sharpness</li><li>A clean, neutral background</li><li>Framed and sized for Uber Eats</li><li>Never fake food, never added ingredients</li></ul></div>
  <div class="reveal">{ba("dumplings", "dumplings 10pc", "Pork and Chive Dumplings", "A quick phone photo.", "The same dumplings, bright and clear.")}</div>
</div></section>

<section class="tight" id="done"><div class="wrap split">
  <div class="reveal"><span class="eyebrow">03 · Done for you</span><h2>You cook. We update your page.</h2>
    <p class="lead" style="margin-top:20px">Don't have time to copy everything in? Add us as a user on your Uber Eats Manager and we make every change ourselves.</p>
    <ul class="ticks"><li>No passwords shared: you add us as a user</li><li>Names, descriptions, categories and photos updated</li><li>You can remove our access any time</li><li>Or do it yourself: we send everything ready to copy with a guide</li></ul>
    <div class="row" style="margin-top:30px"><a class="btn primary" href="pricing.html">See pricing <span class="arr">→</span></a></div></div>
  <div class="img reveal"><img src="img/kitchen.jpg" alt="" loading="lazy"></div>
</div></section>

<section class="bg2"><div class="wrap">
  <div class="head center reveal"><span class="eyebrow">Who it's for</span><h2>Independent places on Uber Eats.</h2></div>
  <div class="grid4">
    <div class="card reveal"><div class="icon">🍕</div><h3>Restaurants</h3><p>Pizza, burgers, Asian, Middle Eastern and everything in between.</p></div>
    <div class="card reveal"><div class="icon">☕</div><h3>Cafés</h3><p>Breakfast, lunch, coffee and cakes.</p></div>
    <div class="card reveal"><div class="icon">🍰</div><h3>Bakeries and desserts</h3><p>Cakes, pastries, gelato and sweet treats.</p></div>
    <div class="card reveal"><div class="icon">🛒</div><h3>Small shops</h3><p>Grocers, delis and specialty stores.</p></div>
  </div>
</div></section>
{cta()}
""", "services.html")

# ------------------------------------------------------------------------------------------------ examples
EX = [("burger", "dbl burgr + chips", "Smash Burger and Fries", "No description.", "Double beef, aged cheddar, pickles and house sauce on a toasted brioche bun."),
      ("laksa", "LAKSA SPECIAL", "Chicken Laksa", "see photo", "Rich coconut curry broth, rice noodles, poached chicken, tofu puffs and lime."),
      ("dumplings", "dumplings 10pc", "Pork and Chive Dumplings", "No description.", "Ten handmade dumplings, pan fried, with chilli oil and black vinegar."),
      ("curry", "chiken curry w rice", "Butter Chicken with Rice", "Typos, no description.", "Slow cooked chicken in a rich, mildly spiced tomato and butter sauce, with steamed basmati."),
      ("pizza", "PIZZA 3", "Garden Pizza", "A number nobody remembers.", "Mozzarella, capsicum, mushroom, olives and fresh basil on a crisp, wood fired base."),
      ("shawarma", "wrap", "Chicken Shawarma Wrap", "Too vague to choose.", "Marinated chicken, garlic sauce, pickles, chips and parsley wrapped in warm flatbread."),
      ("tacos", "taco x3", "Beef Birria Tacos", "Says nothing about the taste.", "Three slow braised beef tacos with onion, coriander, lime and consommé to dip."),
      ("poke", "POKE SALMON REG", "Salmon Poke Bowl", "Capitals, no detail.", "Fresh salmon, sushi rice, avocado, edamame, cucumber and mango with sesame dressing."),
      ("breakfast", "avo toast", "Smashed Avo on Sourdough", "Too short to tempt.", "Smashed avocado, poached egg and crumbled feta on toasted sourdough."),
      ("cake", "choc cake", "Triple Chocolate Layer Cake", "Nothing to make you want it.", "Moist chocolate sponge layered with rich ganache. Baked in house every morning.")]
grid = "".join(f"<div>{ba(*e)}</div>" for e in EX)
page("examples.html", "Examples | MenuFix", "Before and after examples of Uber Eats menu makeovers: clearer names, descriptions that sell and better photos.",
f"""<header class="page-head"><div class="wrap">
  <span class="eyebrow">Examples</span><h1>See the difference.</h1>
  <p class="lead">Drag each slider to compare. Below every photo: the name and description before, and after.</p>
</div></header>
<section style="padding-top:20px"><div class="wrap">
  <div class="head reveal"><div><span class="eyebrow">Page mockups</span><h2>Whole page makeovers</h2></div>
    <p class="lead">The free mockup we send shows your full page after the makeover: banner, best sellers first, clear names and descriptions, appetising photos.</p></div>
  {mockpair("mock1", False)}
  <div style="height:70px"></div>
  {mockpair("mock3", False)}
  <div style="height:70px"></div>
  {mockpair("mock2", False)}
  <p class="note" style="text-align:center;margin-top:24px">Concept mockups for fictional restaurants, made with AI for this website.</p>
</div></section>
<section class="bg2"><div class="wrap">
  <div class="head reveal"><div><span class="eyebrow">Dish by dish</span><h2>Photos and descriptions</h2></div>
    <p class="lead">Drag each slider. On the left, a quick phone photo and the old menu text. On the right, the same dish enhanced and rewritten.</p></div>
  <div class="grid2" style="gap:56px 32px">{grid}</div>
  <p class="note" style="margin-top:40px">These are illustrative examples for fictional dishes and places, with images made with AI for this website. For your page we only work from photos of your real dishes.</p>
</div></section>
{cta("Want to see your own page?", "Send us your restaurant or shop on Uber Eats and we'll show you a free mockup of yours.")}
""", "examples.html")

# ------------------------------------------------------------------------------------------------ how it works
page("how-it-works.html", "How it works | MenuFix", "From free mockup to your new Uber Eats page in four simple steps, all by email.",
f"""<header class="page-head"><div class="wrap">
  <span class="eyebrow">How it works</span><h1>Four simple steps.</h1>
  <p class="lead">Everything can be done by email. You see the result before you pay anything.</p>
</div></header>
<section class="tight"><div class="wrap split">
  <div class="reveal"><span class="num" style="font-size:40px">1</span><h2>Your free mockup</h2>
    <p class="lead" style="margin-top:18px">Tell us your restaurant or shop on Uber Eats. We look at your page and send you a mockup of how it could look, with the main things we'd change. No payment, no obligation.</p></div>
  <div class="reveal" style="display:flex;justify-content:center"><div class="device solo"><img src="img/mock1-after.jpg" alt="A concept mockup of a restaurant page" loading="lazy"></div></div>
</div></section>
<section class="tight bg2"><div class="wrap split rev">
  <div class="reveal"><span class="num" style="font-size:40px">2</span><h2>Choose your package</h2>
    <p class="lead" style="margin-top:18px">Pick Menu Fix, Menu and Photos or the Full Makeover. Tick Done for you if you'd like us to make the changes. Pay securely by card through Stripe. One time price, no subscription.</p>
    <a class="btn primary" href="pricing.html" style="margin-top:10px">See pricing <span class="arr">→</span></a></div>
  <div class="img reveal"><img src="img/cafe.jpg" alt="" loading="lazy"></div>
</div></section>
<section class="tight"><div class="wrap split">
  <div class="reveal"><span class="num" style="font-size:40px">3</span><h2>Send your photos</h2>
    <p class="lead" style="margin-top:18px">For photo packages, take photos of your dishes on your phone, in good light, and reply to our email with them. We enhance your real photos. We never use fake food.</p></div>
  <div class="reveal">{ba("curry", "chiken curry w rice", "Butter Chicken with Rice", "A quick phone photo.", "The same dish, bright and clear.")}</div>
</div></section>
<section class="tight bg2"><div class="wrap split rev">
  <div class="reveal"><span class="num" style="font-size:40px">4</span><h2>Your new page</h2>
    <p class="lead" style="margin-top:18px">Done for you: add us as a user on Uber Eats Manager and we update everything. Do it yourself: we email you every new name, description and photo, ready to copy, with a simple step by step guide. Usually within two to three working days.</p></div>
  <div class="img reveal"><img src="img/delivery.jpg" alt="" loading="lazy"></div>
</div></section>
{cta()}
""", "how-it-works.html")

# ------------------------------------------------------------------------------------------------ pricing
page("pricing.html", "Pricing | MenuFix", "Simple one time prices for Uber Eats menu makeovers. Menu Fix, Menu and Photos, Full Makeover, plus Done for you.",
f"""<header class="page-head"><div class="wrap">
  <span class="eyebrow">Pricing</span><h1>Simple, one time prices.</h1>
  <p class="lead">No subscription, no contract. Start with a free mockup if you'd like to see the idea first.</p>
  <div style="margin-top:30px">{CUR}</div>
</div></header>
<section style="padding-top:0"><div class="wrap">{PLANS}
  <h2 style="margin-top:90px;font-size:36px" class="reveal">Compare packages</h2>
  <table class="compare reveal">
    <tr><th></th><th>Menu Fix</th><th>Menu and Photos</th><th>Full Makeover</th></tr>
    <tr><td>Typos and names fixed</td><td class="y">✓</td><td class="y">✓</td><td class="y">✓</td></tr>
    <tr><td>Descriptions rewritten to sell</td><td class="y">✓</td><td class="y">✓</td><td class="y">✓</td></tr>
    <tr><td>Best sellers and category order</td><td class="y">✓</td><td class="y">✓</td><td class="y">✓</td></tr>
    <tr><td>Photos of your real dishes enhanced</td><td class="n">×</td><td>5 dishes</td><td>15 dishes</td></tr>
    <tr><td>New menu layout and structure</td><td class="n">×</td><td class="n">×</td><td class="y">✓</td></tr>
    <tr><td>One month of updates</td><td class="n">×</td><td class="n">×</td><td class="y">✓</td></tr>
    <tr><td>Ready to copy pack with guide</td><td class="y">✓</td><td class="y">✓</td><td class="y">✓</td></tr>
    <tr><td>Done for you</td><td colspan="3">Optional add on, tick the box at checkout</td></tr>
  </table>
</div></section>
<section class="bg2"><div class="narrow"><div class="head center reveal" style="margin-bottom:30px"><h2>Pricing questions</h2></div>
{faq_html([FAQ[2], FAQ[4], ("How do I pay?", "By card through Stripe, a secure payment provider. You pay in the currency shown on this page."), FAQ[0]])}</div></section>
{cta()}
""", "pricing.html")

# ------------------------------------------------------------------------------------------------ about
page("about.html", "About | MenuFix", "MenuFix is a small independent service that helps restaurants, cafés and shops get more from their Uber Eats page.",
f"""<header class="wrap"><div class="banner reveal"><img src="img/kitchen.jpg" alt=""><div>
  <span class="eyebrow" style="color:#f6a184">About MenuFix</span><h1>Great food deserves a great page.</h1>
  <p class="lead">We help independent restaurants, cafés and small shops look as good on Uber Eats as they really are.</p></div></div></header>
<section><div class="wrap split">
  <div class="reveal"><span class="eyebrow">Our story</span><h2>Small places, real food.</h2>
    <p class="lead" style="margin-top:20px">Some of the best food in any city comes from small, independent kitchens. On delivery apps, though, they often look worse than the big chains: no photos, menus typed in a hurry, best dishes hidden at the bottom.</p>
    <p class="lead">MenuFix is a small independent service run by Sam. We do one thing, delivery app pages, so we know exactly what helps people choose you. No agency fees and no long contracts. You deal with us directly, by email.</p></div>
  <div class="img reveal"><img src="img/deli.jpg" alt="" loading="lazy"></div>
</div></section>
<section class="bg2"><div class="wrap">
  <div class="head center reveal"><span class="eyebrow">What we believe</span><h2>How we work</h2></div>
  <div class="grid3">
    <div class="card reveal"><div class="icon">🍽️</div><h3>Real food only</h3><p>We enhance photos of your real dishes. We never use fake food or add ingredients that aren't there.</p></div>
    <div class="card reveal"><div class="icon">🤝</div><h3>Honest</h3><p>Clear prices, no hidden fees, and no promises we can't keep. A free mockup first, so you know what you're getting.</p></div>
    <div class="card reveal"><div class="icon">⚡</div><h3>Simple</h3><p>Everything by email, in a few days. Or Done for you, so you don't have to touch anything.</p></div>
  </div>
</div></section>
{cta()}
""", "about.html")

# ------------------------------------------------------------------------------------------------ faq
page("faq.html", "FAQ | MenuFix", "Answers to common questions about MenuFix Uber Eats page makeovers.",
f"""<header class="page-head"><div class="narrow">
  <span class="eyebrow">FAQ</span><h1>Questions and answers.</h1>
  <p class="lead">Can't find what you're looking for? <a class="mailto" href="#">Email us</a> and we'll get back to you.</p>
</div></header>
<section style="padding-top:0"><div class="narrow">{faq_html(FAQ)}</div></section>
{cta()}
""", "faq.html")

# ------------------------------------------------------------------------------------------------ contact
page("contact.html", "Free mockup | MenuFix", "Get a free mockup of your Uber Eats page. No payment, no obligation.",
"""<header class="page-head"><div class="wrap split" style="align-items:start">
  <div><span class="eyebrow">Free mockup</span><h1>See your page improved, free.</h1>
    <p class="lead">Tell us where to find you on Uber Eats. We'll email you a mockup of how your page could look and the main things we'd change. No payment, no obligation.</p>
    <ul class="ticks"><li>Usually within one or two working days</li><li>No payment details needed</li><li>Reply "no" any time and we won't email again</li></ul>
    <div class="img reveal" style="margin-top:40px"><img src="img/phone.jpg" alt="" loading="lazy"></div></div>
  <div class="card reveal" style="padding:40px">
    <form id="mockForm">
      <div class="f"><label for="biz">Restaurant or shop name</label><input id="biz" required placeholder="e.g. Sunny Thai Kitchen"></div>
      <div class="f"><label for="city">City</label><input id="city" required placeholder="e.g. Sydney"></div>
      <div class="f"><label for="link">Your Uber Eats page link (optional)</label><input id="link" placeholder="https://www.ubereats.com/..."></div>
      <div class="f"><label for="name">Your name</label><input id="name" placeholder="First name"></div>
      <div class="f"><label for="msg">Anything we should know? (optional)</label><textarea id="msg" rows="4" placeholder="e.g. we just opened, our best seller is..."></textarea></div>
      <button class="btn primary" type="submit" style="width:100%">Send my request <span class="arr">→</span></button>
      <p class="note" style="margin:14px 0 0">This opens your email app with everything filled in. Just press send.</p>
    </form>
  </div>
</div></header>
""")
# ------------------------------------------------------------------------------------------------ legal + 404
import re
for name, title in (("privacy.html", "Privacy"), ("terms.html", "Terms")):
    inner = re.search(r"<main[^>]*>(.*?)</main>", (ROOT / name).read_text(), re.S).group(1)
    inner = re.sub(r'<h1[^>]*>.*?</h1>\s*', "", inner, count=1, flags=re.S).strip()
    page(name, f"{title} | MenuFix", f"MenuFix {title.lower()}.",
         f'<header class="page-head"><div class="narrow"><span class="eyebrow">Legal</span><h1>{title}</h1></div></header>\n'
         f'<main class="narrow legal" style="padding-bottom:100px">\n{inner}\n</main>')
page("404.html", "Page not found | MenuFix", "This page does not exist.",
     """<header class="page-head" style="text-align:center;padding:140px 0"><div class="narrow">
  <span class="eyebrow">404</span><h1>This page isn't on the menu.</h1>
  <p class="lead">The page you're looking for doesn't exist or has moved.</p>
  <div class="row" style="justify-content:center;margin-top:30px"><a class="btn primary" href="index.html">Back to home</a></div>
</div></header>""")
print("built pages")
