// Where this visit came from (Google, Instagram, an email...), kept for the visit so the payment page can say it.
try { const r = document.referrer; if (r && !r.includes(location.host) && !sessionStorage.getItem("mf_from")) sessionStorage.setItem("mf_from", r); } catch (e) {}
// Edit these if anything changes.
const CONTACT = "hello@getmenufix.com";
// The free page check form posts here: the Google Apps Script web app MenuFix already uses (MUSE_SHEET_URL in
// MenuFix Settings). Only its public "check" action works without the secret. Empty: the form opens the email app.
const CHECK_URL = "https://script.google.com/macros/s/AKfycbwFvkB2O8HXfjVmtQOFHOlxQskpVEtGRdotAtznV8kDvG4ZrUkL-4jrSCFkt5pEHmz90w/exec";
const LINKS = {
  full_makeover: "https://buy.stripe.com/7sY3cw9LS4Ug7nGaDE1sQ0o",
  makeover_google: "https://buy.stripe.com/aFafZi4rybiEfUc8vw1sQ0p",
  complete: "https://buy.stripe.com/28EeVe8HO9aweQ8aDE1sQ0q",
  growth_plan: "https://buy.stripe.com/cNi9AUaPW9awazSdPQ1sQ0r",
};
// What Stripe charges in each currency (other countries see the closest one at checkout).
const PRICES = {
  full_makeover: { aud: 969, nzd: 1069, gbp: 499, eur: 569, usd: 629 },
  makeover_google: { aud: 1259, nzd: 1389, gbp: 649, eur: 739, usd: 819 },
  complete: { aud: 2290, nzd: 2490, gbp: 1190, eur: 1359, usd: 1499 },
  growth_plan: { aud: 195, nzd: 215, gbp: 99, eur: 115, usd: 129 },
  // founding restaurants: 30% off, paid after they've seen their finished page
  full_makeover_founding: { aud: 678, nzd: 748, gbp: 349, eur: 398, usd: 440 },
  makeover_google_founding: { aud: 881, nzd: 972, gbp: 454, eur: 517, usd: 573 },
  complete_founding: { aud: 1603, nzd: 1743, gbp: 833, eur: 951, usd: 1049 },
};
const SYM = { aud: "A$", nzd: "NZ$", gbp: "£", eur: "€", usd: "US$" };
const NAME = { aud: "Australian dollars", nzd: "New Zealand dollars", gbp: "British pounds", eur: "euros", usd: "US dollars" };

// Show the currency Stripe will charge this visitor. Stripe picks it from the visitor's country:
// Australia AUD, New Zealand NZD, euro countries EUR, United States USD, everyone else the base currency GBP.
const EURO_TZ = /^(Europe\/(Dublin|Paris|Berlin|Madrid|Rome|Amsterdam|Brussels|Vienna|Lisbon|Helsinki|Athens|Riga|Tallinn|Vilnius|Bratislava|Ljubljana|Luxembourg|Malta|Monaco|Zagreb|Nicosia|Andorra|San_Marino|Vatican|Busingen)|Atlantic\/(Madeira|Canary|Azores)|Asia\/(Nicosia|Famagusta))$/;
const US_TZ = /^(America\/(New_York|Chicago|Denver|Los_Angeles|Phoenix|Anchorage|Juneau|Sitka|Yakutat|Nome|Metlakatla|Adak|Boise|Detroit|Menominee|Indiana\/.+|Kentucky\/.+|North_Dakota\/.+)|Pacific\/Honolulu|US\/.+)$/;
const EURO_CC = /^(IE|FR|DE|ES|IT|NL|BE|AT|PT|FI|GR|LV|EE|LT|SK|SI|LU|MT|CY|HR|MC|AD|SM|VA)$/;
function detectCur() {
  let tz = ""; try { tz = Intl.DateTimeFormat().resolvedOptions().timeZone || ""; } catch (e) {}
  if (/^Australia\//.test(tz)) return "aud";
  if (/^(Pacific\/(Auckland|Chatham)|NZ|NZ-CHAT)$/.test(tz)) return "nzd";
  if (EURO_TZ.test(tz)) return "eur";
  if (US_TZ.test(tz)) return "usd";
  if (tz) return "gbp";
  const cc = ((navigator.language || "").split("-")[1] || "").toUpperCase();
  return cc === "AU" ? "aud" : cc === "NZ" ? "nzd" : cc === "US" ? "usd" : EURO_CC.test(cc) ? "eur" : "gbp";
}
const LANG = document.documentElement.lang;
const FR = LANG === "fr", ES = LANG === "es";
// The Spanish pages are for Spain and always show euros.
const CUR = ES ? "eur" : detectCur();
const NAME_FR = { aud: "dollars australiens", nzd: "dollars néo-zélandais", gbp: "livres sterling", eur: "euros", usd: "dollars américains" };
document.querySelectorAll("[data-p]").forEach((el) => {
  const n = PRICES[el.dataset.p][CUR], plus = el.dataset.p === "done_for_you" ? "+" : "";
  el.textContent = FR || ES ? plus + n + "\u00a0" + (CUR === "eur" ? "€" : SYM[CUR]) : plus + SYM[CUR] + n;
});
document.querySelectorAll("[data-curname]").forEach((el) => (el.textContent = (FR ? NAME_FR : ES ? { eur: "euros" } : NAME)[CUR]));
// A restaurant arriving from our emails (?ref=<id>) keeps its id, so its request is matched to it.
let REF = new URLSearchParams(location.search).get("ref");
try { if (REF) sessionStorage.setItem("ref", REF); else REF = sessionStorage.getItem("ref"); } catch (e) {}
// Referral links (?via=<code>): the code is kept in this browser for 60 days after the first click (the first
// referrer counts). It goes in the plan request (contact form), and on with the payment link we send after the
// finished page, as Stripe client_reference_id "<restaurant id or 0>_<code>".
// Stripe only accepts letters, digits, dashes and underscores there, so the two parts are joined with "_".
const VIA_DAYS = 60;
const VIA_NEW = ((new URLSearchParams(location.search).get("via") || "").toLowerCase().match(/^[a-z0-9]{3,24}$/) || [""])[0];
let VIA = VIA_NEW;
try {
  const saved = JSON.parse(localStorage.getItem("via") || "null");
  if (saved && /^[a-z0-9]{3,24}$/.test(saved.code || "") && Date.now() - saved.at < VIA_DAYS * 864e5) VIA = saved.code;
  else if (VIA_NEW) localStorage.setItem("via", JSON.stringify({ code: VIA_NEW, at: Date.now() }));
  else if (saved) localStorage.removeItem("via");
} catch (e) {}
// Paid ads: ?utm_source=facebook&utm_campaign=riders becomes the key "facebook-riders", kept 30 days so a sign up
// later still counts for the ad (MenuFix, Referrals, Ads). The latest ad wins.
const AD_DAYS = 30;
const AD_NEW = (() => {
  const q = new URLSearchParams(location.search), clean = (v) => (v || "").toLowerCase().replace(/[^a-z0-9]/g, "");
  const src = clean(q.get("utm_source")).slice(0, 20), camp = clean(q.get("utm_campaign")).slice(0, 30);
  return src.length >= 2 && camp.length >= 2 ? src + "-" + camp : "";
})();
let AD = AD_NEW;
try {
  if (AD_NEW) localStorage.setItem("ad", JSON.stringify({ key: AD_NEW, at: Date.now() }));
  else {
    const saved = JSON.parse(localStorage.getItem("ad") || "null");
    if (saved && /^[a-z0-9]{2,20}-[a-z0-9]{2,30}$/.test(saved.key || "") && Date.now() - saved.at < AD_DAYS * 864e5) AD = saved.key;
    else if (saved) localStorage.removeItem("ad");
  }
} catch (e) {}
const RID = REF && /^\d+$/.test(REF) ? REF : "";
// Our guarantee: nobody pays on this website. A plan button starts the work (the contact form, with the plan chosen):
// we make the finished page first, and the payment link comes with it, once they've seen it and are happy.
document.querySelectorAll("[data-buy]").forEach((a) => {
  const q = new URLSearchParams({ plan: a.dataset.buy });
  if (RID) q.set("ref", RID);
  if (VIA) q.set("via", VIA);
  a.href = "contact.html?" + q.toString();
});
if (VIA) document.querySelectorAll('a[href*="pricing.html"]').forEach((a) => {  // also when storage is blocked
  try {
    const u = new URL(a.getAttribute("href"), location.href);
    if (u.origin !== location.origin) return;
    u.searchParams.set("via", VIA);
    a.href = u.pathname + u.search + u.hash;
  } catch (e) {}
});

document.querySelectorAll(".mailto").forEach((a) => (a.href = "mailto:" + CONTACT));

// Free mockup form: a plan button or a link can fill in the restaurant and the plan.
const form = document.getElementById("mockForm");
if (form) { const q = new URLSearchParams(location.search).get("biz"); if (q) document.getElementById("biz").value = q; }
// Arriving from a plan button: the message says which plan, and the guarantee (and a referral code, so it is counted).
const PLAN = new URLSearchParams(location.search).get("plan");
const PLAN_NAMES = {
  en: { full_makeover: "Uber Eats Makeover", makeover_google: "Makeover and Google", complete: "Complete", growth_plan: "Growth Plan" },
  fr: { full_makeover: "Refonte Uber Eats", makeover_google: "Refonte et Google", complete: "Complète", growth_plan: "Plan Croissance" },
  es: { full_makeover: "Renovación Uber Eats", makeover_google: "Renovación y Google", complete: "Completa", growth_plan: "Plan Crecimiento" },
}[FR ? "fr" : ES ? "es" : "en"];
if (form && PLAN && PLAN_NAMES[PLAN]) {
  const msg = document.getElementById("msg");
  const line = FR ? "Je souhaite " + PLAN_NAMES[PLAN] + ". Je ne paie qu'après avoir vu ma page terminée, et seulement si elle me plaît."
    : ES ? "Me interesa " + PLAN_NAMES[PLAN] + ". Solo pago cuando haya visto mi página terminada y esté contento con ella."
    : "I'd like " + PLAN_NAMES[PLAN] + ". I only pay once I've seen my finished page and I'm happy with it.";
  if (msg && !msg.value) msg.value = line + (VIA ? (FR ? "\nCode de parrainage : " : ES ? "\nCódigo de referido: " : "\nReferral code: ") + VIA : "");
}
// The free mockup and referral forms post straight to MenuFix (no email app needed), then say thank you.
const FORM_URL = "https://admin.getmenufix.com/api/public/form";
async function sendForm(f, errId, thanksId, data) {
  const err = document.getElementById(errId);
  const say = (msg) => { err.textContent = msg; err.hidden = !msg; };
  if (!f.checkValidity()) { f.reportValidity(); return; }
  say("");
  const btn = f.querySelector("button"); btn.disabled = true;
  try {  // text/plain keeps it a simple request; the server only answers our own website
    const r = await fetch(FORM_URL, { method: "POST", headers: { "Content-Type": "text/plain;charset=utf-8" }, body: JSON.stringify(data) });
    const out = await r.json().catch(() => ({}));
    if (!r.ok || !out.ok) throw new Error(out.error || r.status);
    f.hidden = true;
    const t = document.getElementById(thanksId); t.hidden = false;
    t.scrollIntoView({ behavior: "smooth", block: "center" });
    try { window.goatcounter && window.goatcounter.count({ path: data.form + "-sent", title: location.pathname, event: true }); } catch (x) {}
  } catch (x) {
    btn.disabled = false;
    say(f.dataset.error);
  }
}
if (form) form.addEventListener("submit", (e) => {
  e.preventDefault();
  const v = (id) => document.getElementById(id).value.trim();
  sendForm(form, "mErr", "mockThanks", { form: "mockup", restaurant: v("biz"), city: v("city"), link: v("link"), email: v("email"),
    name: v("name"), message: v("msg"), plan: PLAN || "", via: VIA || "", ref: RID, lang: form.dataset.lang || "en",
    consent: document.getElementById("mConsent").checked, website: v("mSite") });
});

const riderForm = document.getElementById("riderForm");
if (riderForm) riderForm.addEventListener("submit", async (e) => {
  e.preventDefault();
  const err = document.getElementById("rdErr"), say = (t) => { err.textContent = t; err.hidden = !t; };
  if (!riderForm.checkValidity()) { riderForm.reportValidity(); return; }
  const v = (id) => document.getElementById(id).value.trim();
  say("");
  const btn = riderForm.querySelector("button"); btn.disabled = true;
  try {
    const r = await fetch(FORM_URL, { method: "POST", headers: { "Content-Type": "text/plain;charset=utf-8" }, body: JSON.stringify({
      form: "rider", name: v("rdName"), email: v("rdEmail"), city: v("rdCity"), country: v("rdCountry"), phone: v("rdPhone"),
      rules: document.getElementById("rdRules").checked, website: v("rdSite"), ad: AD, lang: "en" }) });
    const out = await r.json().catch(() => ({}));
    if (!r.ok || !out.ok) throw new Error(out.error || r.status);
    riderForm.hidden = true;
    if (out.card) document.getElementById("riderCard").href = out.card;
    document.getElementById("riderThanks").hidden = false;
  } catch (x) { btn.disabled = false; say(riderForm.dataset.error); }
});

const refForm = document.getElementById("refForm");
if (refForm) refForm.addEventListener("submit", (e) => {
  e.preventDefault();
  const v = (id) => document.getElementById(id).value.trim();
  sendForm(refForm, "rErr", "refThanks", { form: "referral", name: v("rName"), email: v("rEmail"), business: v("rBiz"),
    how: v("rHow"), lang: refForm.dataset.lang || "en", website: v("rSite") });
});

// Free Uber Eats page check (check.html): one row in the sheet's "Page checks" tab, then a thank you.
const checkForm = document.getElementById("checkForm");
if (checkForm) checkForm.addEventListener("submit", async (e) => {
  e.preventDefault();
  const v = (id) => document.getElementById(id).value.trim();
  const err = document.getElementById("cErr");
  const say = (msg) => { err.textContent = msg; err.hidden = !msg; };
  const url = v("cUrl"), lang = checkForm.dataset.lang || "en";
  if (!/^https:\/\/(www\.)?ubereats\.com\/([a-z]{2}(-[a-z]{2})?\/)?store\/[^\/?#\s]+\/[A-Za-z0-9_-]+/.test(url)) return say(checkForm.dataset.bad_url);
  if (!checkForm.checkValidity()) { checkForm.reportValidity(); return; }
  say("");
  const data = { action: "check", store_url: url, restaurant: v("cName"), email: v("cEmail"), first_name: v("cFirst"),
                 lang, consent: document.getElementById("cConsent").checked, website: v("cSite") };
  const btn = checkForm.querySelector("button"); btn.disabled = true;
  try {
    if (CHECK_URL) {  // no-cors: the answer can't be read, the sheet script checks everything again
      await fetch(CHECK_URL, { method: "POST", mode: "no-cors", headers: { "Content-Type": "text/plain;charset=utf-8" }, body: JSON.stringify(data) });
    } else {
      const lines = ["Free Uber Eats page check", "Store link: " + url, "Restaurant: " + data.restaurant, "Email: " + data.email,
                     "First name: " + data.first_name, "Language: " + lang, "Consent: " + document.querySelector(".consent span").textContent];
      location.href = "mailto:" + CONTACT + "?subject=" + encodeURIComponent("Free page check: " + data.restaurant) + "&body=" + encodeURIComponent(lines.join("\n"));
    }
    checkForm.hidden = true;
    document.getElementById("checkThanks").hidden = false;
    try { window.goatcounter && window.goatcounter.count({ path: "check-sent", title: location.pathname, event: true }); } catch (x) {}
  } catch (x) {
    btn.disabled = false;
    say(checkForm.dataset.error);
  }
});

// Before and after sliders.
document.querySelectorAll(".ba").forEach((ba) => {
  const range = ba.querySelector("input"), after = ba.querySelector(".after"), handle = ba.querySelector(".handle");
  const set = () => { after.style.clipPath = "inset(0 0 0 " + range.value + "%)"; handle.style.left = range.value + "%"; };
  range.addEventListener("input", set); set();
});

// Nav border on scroll, close the mobile menu after a tap.
const nav = document.querySelector(".nav");
const onScroll = () => nav && nav.classList.toggle("scrolled", scrollY > 10);
addEventListener("scroll", onScroll, { passive: true }); onScroll();
document.querySelectorAll(".nav .links a").forEach((a) => a.addEventListener("click", () =>
  document.querySelector(".nav .links").classList.remove("open")));

// Fade sections in as they appear.
if ("IntersectionObserver" in window) {
  const io = new IntersectionObserver((es) => es.forEach((e) => { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } }),
    { rootMargin: "0px 0px -8% 0px" });
  document.querySelectorAll(".reveal").forEach((el) => io.observe(el));
} else document.querySelectorAll(".reveal").forEach((el) => el.classList.add("in"));

// Engagement events for GoatCounter: time on page, scroll depth and clicks, each sent once per page view.
// Nothing is stored on the visitor's device. If an adblocker blocks GoatCounter, events are simply dropped.
(() => {
  const sent = {}, waiting = [];
  const gc = () => window.goatcounter && typeof window.goatcounter.count === "function" ? window.goatcounter : null;
  const fire = (name) => { try { gc().count({ path: name, title: location.pathname, event: true }); } catch (e) {} };
  const track = (name) => {
    if (sent[name]) return;
    sent[name] = true;
    if (gc()) fire(name); else waiting.push(name);
  };
  // count.js loads async: send what happened before it was ready, give up after a minute.
  let tries = 0;
  const flush = setInterval(() => {
    if (gc()) { waiting.splice(0).forEach(fire); }
    if (gc() || ++tries > 60) { clearInterval(flush); waiting.length = 0; }
  }, 1000);

  // Time on page, counted only while the tab is visible.
  let seen = 0;
  const steps = [10, 30, 60, 180];
  const timer = setInterval(() => {
    if (document.visibilityState !== "visible") return;
    seen += 1;
    steps.forEach((s) => { if (seen >= s) track("time-" + s + "s"); });
    if (seen >= steps[steps.length - 1]) clearInterval(timer);
  }, 1000);

  // Scroll depth: how far down the page the bottom of the screen got.
  const depth = () => {
    const h = document.documentElement.scrollHeight, v = window.innerHeight;
    if (!h || h <= v) return;  // a page that fits on one screen says nothing about scrolling
    const pct = (window.scrollY + v) / h * 100;
    [25, 50, 75].forEach((d) => { if (pct >= d) track("scroll-" + d); });
    if (pct >= 98) track("scroll-100");
  };
  addEventListener("scroll", depth, { passive: true });

  // A visit through a referral link (?via=<code>), not counted again while they move between our own pages.
  if (VIA_NEW && !(document.referrer || "").startsWith(location.origin)) track("via-" + VIA_NEW);
  // A visit from a paid ad (utm tags), counted once per arrival.
  if (AD_NEW && !(document.referrer || "").startsWith(location.origin)) track("ad-" + AD_NEW);

  // Clicks on pricing links, pay buttons and email links.
  document.addEventListener("click", (e) => {
    const a = e.target.closest && e.target.closest("a");
    if (!a) return;
    const buy = a.getAttribute("data-buy"), href = a.getAttribute("href") || "";
    if (buy && Object.prototype.hasOwnProperty.call(LINKS, buy)) track("click-plan-" + buy);
    else if (/^mailto:/i.test(href) || a.classList.contains("mailto")) track("click-email");
    else if (/(^|\/)pricing\.html(\?|#|$)/.test(href)) track("click-pricing");
  }, true);
})();

// Free tools (tools/*.html, fr/outils, es/herramientas). Everything runs here in the browser: photos and text are never uploaded or sent.
(() => {
  const $ = (id) => document.getElementById(id);
  const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
  const msg = (kind, label, text) => `<div class="tool-msg ${kind}"><b>${label}</b><span>${text}</span></div>`;
  const L = FR ? "fr" : ES ? "es" : "en";
  // Words shown by the tools, in each language. {x} parts are filled in below.
  const T = {
    en: { pass: "Pass", fix: "Fix", ok: "OK", ready: "Ready", kb: "KB", mb: "MB",
      typeOk: "File type: {t}.", typeFix: "File type: save or export it as a JPG before uploading.",
      sizeOk: "File size: {s}, under 10 MB.", sizeFix: "File size: {s}. Uber allows up to 10 MB. The fix button below makes a smaller JPG.",
      dims: "Size: {w} × {h} pixels. ", dimsBig: "Big enough for Uber's ideal 2880 × 2304.",
      dimsMin: "Above Uber's minimum of 550 × 440. 2880 × 2304 is ideal, so use a bigger original if you have one.",
      dimsFix: "Size: {w} × {h} pixels, smaller than Uber's minimum of 550 × 440. Use the original photo, not a screenshot or a copy from a chat app.",
      shapeOk: "Shape: {r} to 1, close to 5:4.", shapeFix: "Shape: {r} to 1. Uber recommends 5:4 (1.25 to 1) landscape. Use the button below to crop it.",
      allOk: "This photo meets Uber's size rules. Check it shows one real dish with no text or logos.",
      small: "Your photo is smaller than 2880 × 2304, so it will be enlarged, not sharpened.",
      heic: "This browser can't open that file. It may be a HEIC photo from an iPhone: export or share it as a JPG, then try again.",
      saved: "Saved a {s} JPG at 2880 × 2304. Check the dish is still centred.", dec: (n, d = 2) => n.toFixed(d),
      chars: (n) => n + " character" + (n === 1 ? "" : "s"),
      short: "Short", long: "Long", caps: "Capitals", vague: "Vague", ingr: "Ingredients",
      lenShort: "{n} characters. Uber's advice is 140 to 260: add the main ingredients or one detail that makes it yours.",
      lenLong: "{n} characters. Uber's advice is 140 to 260: cut it to the ingredients people care about.",
      lenOk: "{n} characters, inside Uber's 140 to 260 advice.",
      capsFix: "Write {w} in normal capitals. ALL CAPS is harder to read.", capsOk: "No ALL CAPS words.",
      vagueFix: "Swap \"{w}\" for something specific: an ingredient, how it's cooked, or the portion.", vagueOk: "No vague praise words.",
      foodOk: "Names ingredients or cooking: {w}.", foodFix: "Name at least two main ingredients or how it's cooked, so people know what they're getting.",
      keep: ["BBQ", "XL", "GF", "VG", "DF"],
      VAGUE: ["delicious", "amazing", "best", "yummy", "tasty", "awesome", "perfect", "incredible", "world famous", "mouth watering", "to die for", "great", "nice", "lovely", "beautiful"],
      FOOD: "beef chicken lamb pork fish prawn prawns salmon tuna egg eggs tofu cheese cheddar mozzarella feta haloumi parmesan " +
        "rice noodles noodle pasta bread bun brioche sourdough pita wrap tortilla pastry chips fries potato salad lettuce tomato onion " +
        "garlic chilli ginger lemon lime avocado mushroom mushrooms capsicum spinach basil coriander mint parsley sesame peanut peanuts " +
        "coconut curry sauce gravy mayo aioli butter cream yoghurt honey chocolate caramel vanilla berries banana mango apple oat oats " +
        "milk espresso coffee tea bacon ham sausage chorizo pepperoni olives pickles slaw kimchi soy teriyaki satay tamarind " +
        "grilled chargrilled fried crumbed roasted smoked braised slow baked toasted crispy steamed stir wood fired marinated " +
        "beans lentils chickpeas quinoa edamame cucumber carrot corn pumpkin beetroot dumpling dumplings broth soup patty" },
    fr: { pass: "OK", fix: "À corriger", ok: "Correct", ready: "Prête", kb: "Ko", mb: "Mo",
      typeOk: "Type de fichier : {t}.", typeFix: "Type de fichier : enregistrez ou exportez la photo en JPG avant de l'envoyer.",
      sizeOk: "Poids : {s}, moins de 10 Mo.", sizeFix: "Poids : {s}. Uber accepte 10 Mo au maximum. Le bouton plus bas crée un JPG plus léger.",
      dims: "Taille : {w} × {h} pixels. ", dimsBig: "Assez grande pour le format idéal d'Uber, 2880 × 2304.",
      dimsMin: "Au dessus du minimum d'Uber, 550 × 440. Le format idéal est 2880 × 2304 : utilisez une photo d'origine plus grande si vous en avez une.",
      dimsFix: "Taille : {w} × {h} pixels, sous le minimum d'Uber de 550 × 440. Utilisez la photo d'origine, pas une capture d'écran ni une copie reçue par messagerie.",
      shapeOk: "Format : {r} pour 1, proche du 5:4.", shapeFix: "Format : {r} pour 1. Uber recommande le 5:4 (1,25 pour 1) à l'horizontale. Utilisez le bouton plus bas pour recadrer.",
      allOk: "Cette photo respecte les règles de taille d'Uber. Vérifiez qu'elle montre un seul vrai plat, sans texte ni logo.",
      small: "Votre photo est plus petite que 2880 × 2304 : elle sera agrandie, pas rendue plus nette.",
      heic: "Ce navigateur ne peut pas ouvrir ce fichier. C'est peut être une photo HEIC d'iPhone : exportez la ou partagez la en JPG, puis réessayez.",
      saved: "JPG de {s} enregistré en 2880 × 2304. Vérifiez que le plat est toujours bien centré.", dec: (n, d = 2) => n.toFixed(d).replace(".", ","),
      chars: (n) => n + " caractère" + (n > 1 ? "s" : ""),
      short: "Trop court", long: "Trop long", caps: "Majuscules", vague: "Mots vagues", ingr: "Ingrédients",
      lenShort: "{n} caractères. Notre repère est de 140 à 260 : ajoutez les ingrédients principaux ou un détail qui vous ressemble.",
      lenLong: "{n} caractères. Notre repère est de 140 à 260 : gardez les ingrédients qui comptent pour le client.",
      lenOk: "{n} caractères, dans notre repère de 140 à 260.",
      capsFix: "Écrivez {w} en minuscules. Les MAJUSCULES se lisent moins bien.", capsOk: "Aucun mot en MAJUSCULES.",
      vagueFix: "Remplacez « {w} » par quelque chose de précis : un ingrédient, une cuisson ou la portion.", vagueOk: "Aucun compliment vague.",
      foodOk: "Ingrédients ou cuissons cités : {w}.", foodFix: "Citez au moins deux ingrédients principaux ou la cuisson, pour que le client sache ce qu'il commande.",
      keep: ["BBQ", "XL", "XXL", "AOP", "AOC", "IGP"],
      VAGUE: ["délicieux", "délicieuse", "délicieuses", "incroyable", "incroyables", "meilleur", "meilleure", "parfait", "parfaite", "génial", "géniale", "top", "super", "extra", "excellent", "excellente", "succulent", "succulente", "exceptionnel", "exceptionnelle", "trop bon", "à tomber"],
      FOOD: "boeuf bœuf poulet agneau porc veau canard poisson saumon thon cabillaud crevettes crevette oeuf œuf oeufs œufs tofu fromage cheddar mozzarella " +
        "burrata feta chèvre comté emmental raclette parmesan riz nouilles pâtes pain brioche baguette wrap tortilla galette crêpe pâte frites pommes " +
        "salade tomate tomates oignon oignons ail piment gingembre citron avocat champignons champignon poivron épinards basilic coriandre menthe persil " +
        "sésame cacahuètes coco curry sauce mayonnaise aïoli beurre crème yaourt miel chocolat caramel vanille fruits fraises framboises banane mangue pomme " +
        "lait espresso café thé lardons jambon saucisse chorizo olives cornichons pickles chou kimchi soja teriyaki citronnelle " +
        "grillé grillée grillés rôti rôtie frit frite frits pané panée fumé fumée braisé braisée mijoté mijotée cuit cuite toasté toastée croustillant croustillante " +
        "vapeur mariné marinée confit confite haricots lentilles pois chiches quinoa edamame concombre carotte maïs potiron betterave raviolis bouillon soupe steak " +
        "amandes noisettes pistache herbes thym romarin vinaigrette moutarde" },
    es: { pass: "Bien", fix: "Corregir", ok: "Correcto", ready: "Lista", kb: "KB", mb: "MB",
      typeOk: "Tipo de archivo: {t}.", typeFix: "Tipo de archivo: guárdela o expórtela como JPG antes de subirla.",
      sizeOk: "Peso: {s}, menos de 10 MB.", sizeFix: "Peso: {s}. Uber admite hasta 10 MB. El botón de abajo crea un JPG más ligero.",
      dims: "Tamaño: {w} × {h} píxeles. ", dimsBig: "Suficiente para el tamaño ideal de Uber, 2880 × 2304.",
      dimsMin: "Por encima del mínimo de Uber, 550 × 440. Lo ideal es 2880 × 2304: use una foto original más grande si la tiene.",
      dimsFix: "Tamaño: {w} × {h} píxeles, por debajo del mínimo de Uber de 550 × 440. Use la foto original, no una captura de pantalla ni una copia recibida por chat.",
      shapeOk: "Formato: {r} a 1, cerca de 5:4.", shapeFix: "Formato: {r} a 1. Uber recomienda 5:4 (1,25 a 1) en horizontal. Use el botón de abajo para recortarla.",
      allOk: "Esta foto cumple las reglas de tamaño de Uber. Compruebe que muestra un solo plato real, sin texto ni logotipos.",
      small: "Su foto es más pequeña que 2880 × 2304, así que se ampliará pero no ganará nitidez.",
      heic: "Este navegador no puede abrir el archivo. Puede ser una foto HEIC de iPhone: expórtela o compártala como JPG y vuelva a intentarlo.",
      saved: "Se ha guardado un JPG de {s} a 2880 × 2304. Compruebe que el plato sigue centrado.", dec: (n, d = 2) => n.toFixed(d).replace(".", ","),
      chars: (n) => n + (n === 1 ? " carácter" : " caracteres"),
      short: "Corta", long: "Larga", caps: "Mayúsculas", vague: "Vaga", ingr: "Ingredientes",
      lenShort: "{n} caracteres. Nuestra referencia es de 140 a 260: añada los ingredientes principales o un detalle propio.",
      lenLong: "{n} caracteres. Nuestra referencia es de 140 a 260: deje solo los ingredientes que importan al cliente.",
      lenOk: "{n} caracteres, dentro de nuestra referencia de 140 a 260.",
      capsFix: "Escriba {w} en minúsculas. Las MAYÚSCULAS se leen peor.", capsOk: "No hay palabras en MAYÚSCULAS.",
      vagueFix: "Cambie «{w}» por algo concreto: un ingrediente, cómo se cocina o la ración.", vagueOk: "No hay elogios vagos.",
      foodOk: "Nombra ingredientes o cocciones: {w}.", foodFix: "Nombre al menos dos ingredientes principales o cómo se cocina, para que el cliente sepa qué pide.",
      keep: ["BBQ", "XL", "XXL", "DOP", "IGP"],
      VAGUE: ["delicioso", "deliciosa", "deliciosos", "deliciosas", "increíble", "increíbles", "mejor", "perfecto", "perfecta", "riquísimo", "riquísima", "buenísimo", "buenísima", "espectacular", "brutal", "top", "excelente", "exquisito", "exquisita", "sabroso", "sabrosa"],
      FOOD: "ternera vaca buey pollo cordero cerdo ibérico pescado salmón atún bacalao merluza gambas langostinos calamares pulpo huevo huevos tofu queso cheddar mozzarella " +
        "burrata feta manchego parmesano arroz fideos pasta pan brioche bocadillo chapata tortilla wrap masa patatas fritas ensalada lechuga tomate cebolla " +
        "ajo guindilla jengibre limón lima aguacate champiñones setas pimiento pimientos espinacas albahaca cilantro menta perejil sésamo cacahuete coco curry " +
        "salsa mayonesa alioli mantequilla nata yogur miel chocolate caramelo vainilla frutos fresas plátano mango manzana leche espresso café té " +
        "jamón chorizo salchicha bacon beicon aceitunas pepinillos kimchi soja teriyaki pimentón azafrán " +
        "plancha brasa frito frita fritos fritas rebozado rebozada asado asada ahumado ahumada guisado guisada horno tostado tostada crujiente crujientes " +
        "vapor marinado marinada confitado confitada garbanzos lentejas alubias quinoa edamame pepino zanahoria maíz calabaza remolacha croquetas caldo sopa " +
        "almendras avellanas pistacho hierbas romero tomillo aceite oliva" },
  }[L];
  const fill = (s, o) => s.replace(/\{(\w)\}/g, (_, k) => o[k]);
  const sizeText = (bytes) => { const mb = bytes / 1048576; return mb < 0.1 ? Math.max(1, Math.round(bytes / 1024)) + " " + T.kb : T.dec(mb, 1) + " " + T.mb; };

  // ---- Uber Eats photo checker: 5:4, at least 550 x 440, under 10 MB, JPG or PNG
  const file = $("ptFile");
  if (file) {
    const drop = $("ptDrop"), out = $("ptOut"), fixRow = $("ptFixRow"), canvas = $("ptCanvas");
    let img = null, name = "photo";
    const check = (f) => {
      if (!f) return;
      name = (f.name || "photo").replace(/\.[^.]+$/, "");
      const okType = /^image\/(jpeg|png)$/.test(f.type) || /\.(jpe?g|png)$/i.test(f.name || "");
      const mb = f.size / 1048576, s = sizeText(f.size);
      const url = URL.createObjectURL(f);
      const im = new Image();
      im.onload = () => {
        img = im;
        const w = im.naturalWidth, h = im.naturalHeight, r = w / h, shapeOk = Math.abs(r - 1.25) <= 0.03, big = w >= 2880 && h >= 2304;
        const rows = [
          okType ? msg("pass", T.pass, fill(T.typeOk, { t: /png/i.test(f.type || f.name) ? "PNG" : "JPG" })) : msg("fix", T.fix, T.typeFix),
          mb <= 10 ? msg("pass", T.pass, fill(T.sizeOk, { s })) : msg("fix", T.fix, fill(T.sizeFix, { s })),
          w >= 550 && h >= 440 ? msg(big ? "pass" : "info", big ? T.pass : T.ok, fill(T.dims, { w, h }) + (big ? T.dimsBig : T.dimsMin))
            : msg("fix", T.fix, fill(T.dimsFix, { w, h })),
          shapeOk ? msg("pass", T.pass, fill(T.shapeOk, { r: T.dec(r) })) : msg("fix", T.fix, fill(T.shapeFix, { r: T.dec(r) })),
        ];
        const allOk = okType && mb <= 10 && w >= 550 && h >= 440 && shapeOk;
        out.innerHTML = (allOk ? msg("pass", T.ready, T.allOk) : "") + rows.join("");
        fixRow.classList.remove("hidden");
        $("ptFixNote").textContent = w < 2880 || h < 2304 ? T.small : "";
        canvas.classList.add("hidden");
      };
      im.onerror = () => {
        img = null; fixRow.classList.add("hidden");
        out.innerHTML = msg("fix", T.fix, T.heic);
      };
      im.src = url;
    };
    file.addEventListener("change", () => check(file.files[0]));
    ["dragover", "dragenter"].forEach((ev) => drop.addEventListener(ev, (e) => { e.preventDefault(); drop.classList.add("over"); }));
    ["dragleave", "drop"].forEach((ev) => drop.addEventListener(ev, () => drop.classList.remove("over")));
    drop.addEventListener("drop", (e) => { e.preventDefault(); check(e.dataTransfer.files[0]); });
    $("ptFix").addEventListener("click", () => {
      if (!img) return;
      const W = 2880, H = 2304, w = img.naturalWidth, h = img.naturalHeight;
      let sw = w, sh = Math.round(w * H / W);
      if (sh > h) { sh = h; sw = Math.round(h * W / H); }
      canvas.width = W; canvas.height = H;
      const ctx = canvas.getContext("2d");
      ctx.imageSmoothingQuality = "high";
      ctx.drawImage(img, Math.round((w - sw) / 2), Math.round((h - sh) / 2), sw, sh, 0, 0, W, H);
      canvas.classList.remove("hidden");
      canvas.toBlob((blob) => {
        if (!blob) return;
        const a = document.createElement("a");
        a.href = URL.createObjectURL(blob);
        a.download = name + "-uber-eats-2880x2304.jpg";
        document.body.appendChild(a); a.click(); a.remove();
        const kb = blob.size / 1024;
        $("ptFixNote").textContent = fill(T.saved, { s: kb < 100 ? Math.max(1, Math.round(kb)) + " " + T.kb : T.dec(kb / 1024, 1) + " " + T.mb });
      }, "image/jpeg", 0.88);
    });
  }

  // ---- Menu description checker: 140 to 260 characters, ALL CAPS, vague words, ingredients
  const text = $("dtText");
  if (text) {
    const FOOD = T.FOOD.split(" ");
    const run = () => {
      const t = text.value.trim(), n = t.length;
      const bar = $("dtBar"), out = $("dtOut");
      $("dtCount").textContent = T.chars(n);
      bar.style.width = Math.min(100, n / 2.6) + "%";
      bar.classList.toggle("ok", n >= 140 && n <= 260);
      if (!n) { out.innerHTML = ""; return; }
      const rows = [];
      rows.push(n < 140 ? msg("fix", T.short, fill(T.lenShort, { n })) : n > 260 ? msg("fix", T.long, fill(T.lenLong, { n }))
        : msg("pass", T.pass, fill(T.lenOk, { n })));
      const caps = (t.match(/(?<![\p{L}])\p{Lu}{3,}(?![\p{L}])/gu) || []).filter((w) => !T.keep.includes(w));
      rows.push(caps.length ? msg("fix", T.caps, fill(T.capsFix, { w: esc(caps.slice(0, 5).join(", ")) })) : msg("pass", T.pass, T.capsOk));
      const low = " " + t.toLowerCase().replace(/[^\p{L}\s]/gu, " ").replace(/\s+/g, " ") + " ";
      const vague = T.VAGUE.filter((v) => low.includes(" " + v + " "));
      rows.push(vague.length ? msg("fix", T.vague, fill(T.vagueFix, { w: esc(vague.join(L === "en" ? '", "' : L === "fr" ? " », « " : "», «")) }))
        : msg("pass", T.pass, T.vagueOk));
      const foods = [...new Set(FOOD.filter((f) => low.includes(" " + f + " ")))];
      rows.push(foods.length >= 2 ? msg("pass", T.pass, fill(T.foodOk, { w: esc(foods.slice(0, 6).join(", ")) })) : msg("fix", T.ingr, T.foodFix));
      out.innerHTML = rows.join("");
    };
    text.addEventListener("input", run);
    run();
  }

  // ---- Uber Eats page score: the owner's own answers, added up here. Nothing is read from Uber Eats or sent anywhere.
  const form = $("scoreTool");
  if (form) {
    const D = JSON.parse($("scoreData").textContent);
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      const out = $("scoreOut"), keys = Object.keys(D.max);
      const got = {};
      keys.forEach((k) => { const r = form.querySelector(`input[name="${k}"]:checked`); if (r) got[k] = +r.value; });
      if (keys.some((k) => !(k in got))) {
        out.innerHTML = msg("fix", "!", esc(D.missing));
        const first = keys.find((k) => !(k in got));
        form.querySelector(`input[name="${first}"]`).closest("fieldset").scrollIntoView({ behavior: "smooth", block: "center" });
        return;
      }
      const score = keys.reduce((n, k) => n + got[k], 0);
      const band = D.bands.find(([min]) => score >= min)[1];
      const lost = keys.map((k) => [k, D.max[k] - got[k]]).filter(([, n]) => n > 0).sort((a, b) => b[1] - a[1]).slice(0, 3);
      const fixes = lost.map(([k]) => `<li>${esc(D.fix[k][0])} <a href="${D.fix[k][1]}">${esc(D.read)} →</a></li>`).join("");
      out.innerHTML = `<div class="score-big ${score >= 65 ? "good" : score >= 40 ? "mid" : "low"}"><b>${score}</b><span>${esc(D.out_of)}</span></div>` +
        msg("info", "", esc(band)) +
        (fixes ? `<div class="score-fixes"><h3>${esc(D.top3)}</h3><ol>${fixes}</ol></div>` : msg("pass", "✓", esc(D.none)));
      $("scoreNext").classList.remove("hidden");
      out.scrollIntoView({ behavior: "smooth", block: "start" });
    });
  }
})();


// Instant page check (check.html#instant): screenshots, made smaller here, then the score and the problems at once.
const instantForm = document.getElementById("instantForm");
if (instantForm) instantForm.addEventListener("submit", async (e) => {
  e.preventDefault();
  const err = document.getElementById("iErr"), say = (t) => { err.textContent = t; err.hidden = !t; };
  say("");
  const files = Array.from(document.getElementById("iShots").files || []).slice(0, 5);
  if (!files.length) return say("Please add at least one screenshot of your Uber Eats page.");
  if (!instantForm.checkValidity()) { instantForm.reportValidity(); return; }
  const small = (f) => new Promise((ok, bad) => {
    const img = new Image(), url = URL.createObjectURL(f);
    img.onload = () => { const k = Math.min(1, 1400 / img.width), c = document.createElement("canvas");
      c.width = Math.round(img.width * k); c.height = Math.round(img.height * k);
      c.getContext("2d").drawImage(img, 0, 0, c.width, c.height); URL.revokeObjectURL(url); ok(c.toDataURL("image/jpeg", 0.82)); };
    img.onerror = () => bad(new Error("not a picture")); img.src = url; });
  instantForm.hidden = true;
  document.getElementById("instantWait").hidden = false;
  try {
    const images = await Promise.all(files.map(small));
    const v = (id) => (document.getElementById(id).value || "").trim();
    const ctl = new AbortController(), stop = setTimeout(() => ctl.abort(), 90000);  // never wait for ever
    const r = await fetch("https://admin.getmenufix.com/api/public/instant_check", { method: "POST", signal: ctl.signal,
      headers: { "Content-Type": "text/plain;charset=utf-8" },
      body: JSON.stringify({ images, via: VIA || "", ad: AD || "", restaurant: v("iName"), email: v("iEmail"), first_name: v("iFirst"), website: v("iSite"),
                             consent: document.getElementById("iConsent").checked }) });
    clearTimeout(stop);
    const d = await r.json().catch(() => ({ error: "" }));
    if (!r.ok) throw new Error(d.error || "We couldn't read your page right now. Please try again in a few minutes.");
    const esc = (t) => String(t).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
    const col = d.score >= 75 ? "#16a35a" : d.score >= 50 ? "#e8a100" : "#d93025";
    const probs = (d.problems || []).map((p, i) => `<li style="margin:10px 0"><b>${i + 1}. ${esc(p.title)}</b><br><span class="note">${esc(p.why)}</span>` +
      (p.examples && p.examples.length ? `<br><span style="color:#c2410c;font-size:14px">On your page: ${p.examples.map(esc).join(", ")}</span>` : "") + "</li>").join("");
    const box = document.getElementById("instantResult");
    box.innerHTML = `<div style="display:flex;gap:18px;align-items:center"><div style="width:96px;height:96px;border-radius:50%;border:10px solid ${col};display:flex;align-items:center;justify-content:center;font-size:28px;font-weight:800;color:${col};flex:none">${d.score}</div>` +
      `<div><h3 style="margin:0">Your score: ${d.score} out of 100</h3><p class="note" style="margin:6px 0 0">${d.stats.photos} of ${d.stats.total} dishes have a photo, ${d.stats.descs} have a description.</p></div></div>` +
      `<h3 style="margin:22px 0 4px">What to fix first</h3><ol style="list-style:none;padding:0;margin:0">${probs || "<li>Your page looks strong.</li>"}</ol>` +
      `<p style="margin:18px 0 0">Your full report is on its way to your email.</p>` +
      `<a class="btn primary" href="contact.html" style="width:100%;margin-top:16px">Get my free mockup <span class="arr">→</span></a>`;
    document.getElementById("instantWait").hidden = true;
    box.hidden = false;
    try { window.goatcounter && window.goatcounter.count({ path: "instant-check", title: location.pathname, event: true }); } catch (x) {}
  } catch (x) {
    document.getElementById("instantWait").hidden = true;
    instantForm.hidden = false;
    say(x && x.name === "AbortError" ? "This is taking too long. Please try again in a few minutes, or email your screenshots to hello@getmenufix.com."
        : (x.message && x.message !== "Failed to fetch" ? x.message : "We couldn't reach our server. Please try again in a few minutes."));
  }
});
