"""Rider partners (22 Oct 2026): delivery riders who see restaurants every day introduce them to MenuFix and earn 30%
of what a restaurant pays. rider.html (sign up, the rules) and rider-card.html (their personal QR card, made in the
browser from ?c=<code>&n=<first name>, to show on the phone or print). Built by _build.py. English for now.

The rules protect the rider's own account: Uber's community guidelines end contact with customers after a delivery,
so riders never use the delivery app, never act during a delivery and never say they are from Uber."""

RULES = ["On your own time only: never during a delivery, never with the delivery bag or in delivery gear.",
         "Never say you are from Uber or Uber Eats. MenuFix is independent.",
         "Never use anything from the delivery app, and never contact customers.",
         "No promises of orders or prices: just show your card. Our website does the rest.",
         "No spam: talk to people, don't send bulk messages with the MenuFix name."]
FAQ = [("How can delivery drivers make extra money?", "Introduce restaurants you already know to MenuFix. Show them your "
        "free QR card on your own time; the owner checks their Uber Eats page for free. If they buy a makeover, you earn a "
        "30% commission. It is a side hustle that fits around your delivery shifts."),
       ("Do I need to sell anything?", "No. You show your card to restaurants you know, at a quiet moment. The owner scans it "
        "and checks their own Uber Eats page with us for free. If they buy a makeover later, you earn."),
       ("How much can I earn per referral?", "30% of what the restaurant pays us. The Uber Eats Makeover is around 970 Australian "
        "dollars, so about 290 dollars for you from one restaurant, and more for the bigger packages. Refunded payments don't count."),
       ("When do I get paid?", "Within 7 days after the restaurant's payment, by bank transfer or PayPal."),
       ("Can Uber Eats, DoorDash, Deliveroo and Menulog riders join?", "Yes. Any delivery rider or driver can join: Uber Eats, "
        "DoorDash, Deliveroo, Menulog, Just Eat or a cycling courier. MenuFix is independent and not linked to any delivery app."),
       ("Can this cause problems with my rider account?", "Follow the rules on this page: never during a delivery, never in "
        "delivery gear, never say you are from Uber, never use the app or contact customers. You talk to restaurants on "
        "your own time, as yourself."),
       ("Which cities?", "Anywhere restaurants sell on Uber Eats: Sydney, Melbourne, Brisbane, London, Manchester, Dublin, "
        "New York and more, in Australia, the UK, Ireland, the USA and New Zealand.")]


def build_rider(page, head, ic, faq_html, cta) -> list[str]:
    import json
    rules = "".join(f"<li>{r}</li>" for r in RULES)
    faq_ld = json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}, ensure_ascii=False)
    page("rider.html", "Side Hustle for Delivery Drivers: Earn 30% Commission | MenuFix",
         "Extra income for Uber Eats, DoorDash, Deliveroo and Menulog drivers. Refer restaurants you know and earn 30% "
         "commission, about 290 dollars each. No selling, your own time, paid in 7 days.",
         f"""{head("Side hustle for delivery drivers", "Extra income for delivery riders. <span class='hl'>Earn 30%</span> commission.",
             "You walk into restaurants every day. Show them your personal MenuFix card on your own time. When one of them "
             "buys a makeover of its Uber Eats page, you get 30% of what it pays: about 290 dollars per restaurant.", ("bag", "star"),
             '<div class="row" style="margin-top:26px"><a class="btn primary" href="#join">Get my card <span class="arr">→</span></a></div>')}

<section class="tight"><div class="wrap">
  <div class="head center reveal"><span class="eyebrow">How it works</span><h2>Three steps, no selling.</h2></div>
  <div class="grid3">
    <div class="card reveal">{ic("phone")}<h3>1. Get your card</h3><p>Sign up below. Your personal QR card comes by email in a minute: on your phone, or printed.</p></div>
    <div class="card reveal">{ic("chef")}<h3>2. Show it</h3><p>At a quiet moment, on your own time, show it to restaurants you know. They scan it and check their page for free.</p></div>
    <div class="card reveal">{ic("star")}<h3>3. Earn 30%</h3><p>When a restaurant that scanned your card pays us, you get 30% of what it paid, within 7 days.</p></div>
  </div>
</div></section>

<section class="bg-cream"><div class="narrow reveal">
  <h2>A side hustle that fits around your delivery shifts</h2>
  <p class="lead" style="margin-top:14px">Uber Eats, DoorDash, Deliveroo and Menulog drivers already know which restaurants
  struggle online: bad photos, no descriptions, few orders. MenuFix fixes their Uber Eats page. Our restaurant referral program
  pays you a 30% commission for every restaurant you introduce, so the restaurants you visit every day become extra income
  for you. No selling, no fees, no targets.</p>
</div></section>

<section class="bg-butter"><div class="wrap split" style="align-items:start">
  <div class="reveal"><span class="eyebrow">The rules</span><h2>Keep your rider account safe.</h2>
    <p class="lead" style="margin-top:14px">These rules matter. Follow them and this never touches your deliveries.</p></div>
  <div class="card reveal" style="padding:32px"><ol class="ticks">{rules}</ol></div>
</div></section>

<section class="tight" id="join"><div class="wrap split" style="align-items:start">
  <div class="reveal"><span class="eyebrow">Join</span><h2>Get your personal card.</h2>
    <p class="lead" style="margin-top:14px">Free. Your card and your code come by email right away.</p></div>
  <div class="card reveal" style="padding:36px">
    <form id="riderForm" data-error="Sorry, something went wrong. Please try again in a minute, or email hello@getmenufix.com." novalidate>
      <div class="f"><label for="rdName">Your name</label><input id="rdName" required maxlength="60" autocomplete="name"></div>
      <div class="f"><label for="rdEmail">Your email</label><input id="rdEmail" type="email" required maxlength="120" autocomplete="email"></div>
      <div class="f"><label for="rdCity">City</label><input id="rdCity" required maxlength="60" placeholder="For example Sydney"></div>
      <div class="f"><label for="rdCountry">Country</label><select id="rdCountry"><option value="AU">Australia</option>
        <option value="GB">United Kingdom</option><option value="IE">Ireland</option><option value="US">United States</option>
        <option value="NZ">New Zealand</option><option value="">Other</option></select></div>
      <div class="f"><label for="rdPhone">Phone or WhatsApp (optional)</label><input id="rdPhone" maxlength="30" autocomplete="tel"></div>
      <div class="hp" aria-hidden="true"><label for="rdSite">Website</label><input id="rdSite" tabindex="-1" autocomplete="off"></div>
      <label class="consent"><input id="rdRules" type="checkbox" required> <span>I have read the rules and I will follow them</span></label>
      <p class="err" id="rdErr" role="alert" hidden></p>
      <button class="btn primary" type="submit" style="width:100%">Get my card <span class="arr">→</span></button>
    </form>
    <div id="riderThanks" class="thanks" hidden><h3>Your card is on its way.</h3><p>Check your email in a minute. You can also open it now:</p>
      <a id="riderCard" class="btn primary" href="rider-card.html" style="width:100%;margin-top:12px">Open my card <span class="arr">→</span></a></div>
  </div>
</div></section>

<section class="bg-cream"><div class="narrow">
  <div class="head center reveal" style="margin-bottom:30px"><h2>Delivery driver side hustle: questions</h2></div>
  {faq_html(FAQ)}
</div></section>
""", "", ld_extra=f'\n<script type="application/ld+json">{faq_ld}</script>')
    card_page()
    return ["rider.html"]


def card_page() -> None:
    """rider-card.html: the rider's QR card, drawn in the browser (no server needed), for the phone or to print."""
    from pathlib import Path
    root = Path(__file__).parent
    (root / "rider-card.html").write_text("""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex">
<title>Your MenuFix card</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;700;800&display=swap" rel="stylesheet">
<style>
:root{--brand:#ff5a1f;--ink:#1b1b1f;--cream:#fff8f0}
*{box-sizing:border-box}body{margin:0;background:var(--cream);font-family:'Plus Jakarta Sans',-apple-system,sans-serif;color:var(--ink)}
.wrap{max-width:460px;margin:0 auto;padding:24px 16px 40px;text-align:center}
.card{background:#fff;border-radius:24px;box-shadow:0 10px 40px rgba(0,0,0,.08);padding:26px 22px;margin-top:10px}
.logo{font-weight:800;font-size:22px}.logo b{color:var(--brand)}
h1{font-size:24px;line-height:1.2;margin:14px 0 6px}.sub{color:#555;margin:0 0 16px;font-size:15px}
#qr{display:inline-block;padding:12px;background:#fff;border:3px solid var(--brand);border-radius:18px}
.url{margin-top:10px;font-size:13px;color:#777}.by{margin-top:14px;font-size:14px;color:#555}
.btns{display:flex;gap:10px;margin-top:18px}.btns button{flex:1;border:0;border-radius:14px;padding:14px;font:700 15px inherit;font-family:inherit;cursor:pointer}
.p{background:var(--brand);color:#fff}.s{background:#fff;color:var(--ink);border:2px solid #eee}
.rules{text-align:left;font-size:13px;color:#555;margin-top:18px;line-height:1.5}
.sheet{display:none}
@media print{@page{size:A4;margin:10mm}body{background:#fff}.wrap{display:none}
 .sheet{display:grid;grid-template-columns:repeat(2,85mm);gap:6mm 8mm;justify-content:center}
 .mini{width:85mm;height:55mm;border:1px dashed #bbb;border-radius:4mm;padding:4mm;display:flex;gap:4mm;align-items:center;break-inside:avoid}
 .mini .t{flex:1;text-align:left}.mini .t b{display:block;font-size:12pt;line-height:1.15}.mini .t span{font-size:8pt;color:#555}
 .mini .l{font-weight:800;font-size:10pt;margin-bottom:2mm}.mini .l i{color:var(--brand);font-style:normal}}
</style></head><body>
<div class="wrap">
  <div class="logo">menu<b>fix</b></div>
  <div class="card">
    <h1>Free check of your<br>Uber Eats page</h1>
    <p class="sub">Scan to see your score and what to fix, then get a free mockup of your page.</p>
    <div id="qr"></div>
    <div class="url" id="url"></div>
    <div class="by" id="by"></div>
  </div>
  <div class="btns"><button class="p" onclick="window.print()">Print cards</button><button class="s" id="save">Save image</button></div>
  <div class="rules"><b>Your rules:</b> on your own time only, never during a delivery or in delivery gear, never say
    you are from Uber, never use the delivery app or contact customers.</div>
</div>
<div class="sheet" id="sheet"></div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js"></script>
<script>
const q = new URLSearchParams(location.search);
const code = ((q.get("c") || "").toLowerCase().match(/^[a-z0-9]{3,24}$/) || [""])[0];
const name = (q.get("n") || "").replace(/[^\\p{L} '.]/gu, "").slice(0, 30);
const link = "https://getmenufix.com/check.html" + (code ? "?via=" + code : "");
document.getElementById("url").textContent = "getmenufix.com/check.html";
document.getElementById("by").textContent = name ? "Introduced by " + name : "";
new QRCode(document.getElementById("qr"), { text: link, width: 220, height: 220, correctLevel: QRCode.CorrectLevel.M });
const sheet = document.getElementById("sheet");
setTimeout(() => {
  const img = document.querySelector("#qr img, #qr canvas");
  const src = img && (img.tagName === "CANVAS" ? img.toDataURL() : img.src);
  for (let i = 0; i < 8; i++) sheet.insertAdjacentHTML("beforeend",
    `<div class="mini"><img src="${src}" style="width:36mm;height:36mm"><div class="t"><div class="l">menu<i>fix</i></div>
     <b>Free check of your Uber Eats page</b><span>Scan: your score and a free mockup.${name ? " Introduced by " + name : ""}</span></div></div>`);
}, 300);
document.getElementById("save").onclick = () => {
  const qr = document.querySelector("#qr canvas"); if (!qr) return;
  const c = document.createElement("canvas"); c.width = 720; c.height = 960; const x = c.getContext("2d");
  x.fillStyle = "#fff8f0"; x.fillRect(0, 0, 720, 960); x.fillStyle = "#ffffff"; x.fillRect(40, 40, 640, 880);
  x.fillStyle = "#1b1b1f"; x.font = "800 40px sans-serif"; x.textAlign = "center"; x.fillText("menufix", 360, 120);
  x.font = "800 38px sans-serif"; x.fillText("Free check of your", 360, 210); x.fillText("Uber Eats page", 360, 258);
  x.drawImage(qr, 160, 310, 400, 400); x.fillStyle = "#555"; x.font = "500 26px sans-serif";
  x.fillText("Scan: your score and a free mockup", 360, 780); if (name) x.fillText("Introduced by " + name, 360, 830);
  const a = document.createElement("a"); a.download = "menufix-card.png"; a.href = c.toDataURL("image/png"); a.click();
};
</script></body></html>""")
