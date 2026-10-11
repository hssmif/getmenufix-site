// Edit these if anything changes.
const CONTACT = "hello@getmenufix.com";
const LINKS = {
  menu_fix: "https://buy.stripe.com/6oU6oI0bi1I4bDWfXY1sQ04",
  menu_photos: "https://buy.stripe.com/5kQaEYf6c5Yk6jCeTU1sQ05",
  full_makeover: "https://buy.stripe.com/3cIdRa5vC1I4dM4dPQ1sQ06",
  done_for_you: "https://buy.stripe.com/cNi28s4ry5Yk8rK6no1sQ07",
  care_plan: "https://buy.stripe.com/eVq5kEe282M8cI0aDE1sQ08",
};
// What Stripe charges in each currency (other countries see the closest one at checkout).
const PRICES = {
  menu_fix: { aud: 289, gbp: 149, eur: 169, usd: 189 },
  menu_photos: { aud: 579, gbp: 299, eur: 339, usd: 379 },
  full_makeover: { aud: 969, gbp: 499, eur: 569, usd: 629 },
  done_for_you: { aud: 89, gbp: 45, eur: 50, usd: 59 },
  care_plan: { aud: 49, gbp: 25, eur: 29, usd: 35 },
};
const SYM = { aud: "A$", gbp: "£", eur: "€", usd: "US$" };
const NAME = { aud: "Australian dollars", gbp: "British pounds", eur: "euros", usd: "US dollars" };

// Show the currency Stripe will charge this visitor. Stripe picks it from the visitor's country:
// Australia AUD, euro countries EUR, United States USD, everyone else the base currency GBP.
const EURO_TZ = /^(Europe\/(Dublin|Paris|Berlin|Madrid|Rome|Amsterdam|Brussels|Vienna|Lisbon|Helsinki|Athens|Riga|Tallinn|Vilnius|Bratislava|Ljubljana|Luxembourg|Malta|Monaco|Zagreb|Nicosia|Andorra|San_Marino|Vatican|Busingen)|Atlantic\/(Madeira|Canary|Azores)|Asia\/(Nicosia|Famagusta))$/;
const US_TZ = /^(America\/(New_York|Chicago|Denver|Los_Angeles|Phoenix|Anchorage|Juneau|Sitka|Yakutat|Nome|Metlakatla|Adak|Boise|Detroit|Menominee|Indiana\/.+|Kentucky\/.+|North_Dakota\/.+)|Pacific\/Honolulu|US\/.+)$/;
const EURO_CC = /^(IE|FR|DE|ES|IT|NL|BE|AT|PT|FI|GR|LV|EE|LT|SK|SI|LU|MT|CY|HR|MC|AD|SM|VA)$/;
function detectCur() {
  let tz = ""; try { tz = Intl.DateTimeFormat().resolvedOptions().timeZone || ""; } catch (e) {}
  if (/^Australia\//.test(tz)) return "aud";
  if (EURO_TZ.test(tz)) return "eur";
  if (US_TZ.test(tz)) return "usd";
  if (tz) return "gbp";
  const cc = ((navigator.language || "").split("-")[1] || "").toUpperCase();
  return cc === "AU" ? "aud" : cc === "US" ? "usd" : EURO_CC.test(cc) ? "eur" : "gbp";
}
const CUR = detectCur();
const FR = document.documentElement.lang === "fr";
const NAME_FR = { aud: "dollars australiens", gbp: "livres sterling", eur: "euros", usd: "dollars américains" };
document.querySelectorAll("[data-p]").forEach((el) => {
  const n = PRICES[el.dataset.p][CUR], plus = el.dataset.p === "done_for_you" ? "+" : "";
  el.textContent = FR ? plus + n + "\u00a0" + (CUR === "eur" ? "€" : SYM[CUR]) : plus + SYM[CUR] + n;
});
document.querySelectorAll("[data-curname]").forEach((el) => (el.textContent = (FR ? NAME_FR : NAME)[CUR]));
// A restaurant arriving from our offer email (?ref=<id>) keeps its id, so its payment is matched to it.
let REF = new URLSearchParams(location.search).get("ref");
try { if (REF) sessionStorage.setItem("ref", REF); else REF = sessionStorage.getItem("ref"); } catch (e) {}
document.querySelectorAll("[data-buy]").forEach((a) => {
  a.href = LINKS[a.dataset.buy] + (REF && /^\d+$/.test(REF) ? "?client_reference_id=" + REF : "");
});

document.querySelectorAll(".mailto").forEach((a) => (a.href = "mailto:" + CONTACT));

// Free mockup form: opens the visitor's email app with everything filled in.
const form = document.getElementById("mockForm");
if (form) { const q = new URLSearchParams(location.search).get("biz"); if (q) document.getElementById("biz").value = q; }
if (form) form.addEventListener("submit", (e) => {
  e.preventDefault();
  const v = (id) => document.getElementById(id).value.trim();
  const body = "Hi,\n\nI'd like a free mockup of my Uber Eats page.\n\nRestaurant or shop: " + v("biz") +
    "\nCity: " + v("city") + "\nUber Eats link: " + v("link") + "\n\n" + v("msg") + "\n\nThanks,\n" + v("name");
  location.href = "mailto:" + CONTACT + "?subject=" + encodeURIComponent("Free mockup for " + v("biz")) +
    "&body=" + encodeURIComponent(body);
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

  // Clicks on pricing links, pay buttons and email links.
  document.addEventListener("click", (e) => {
    const a = e.target.closest && e.target.closest("a");
    if (!a) return;
    const buy = a.getAttribute("data-buy"), href = a.getAttribute("href") || "";
    if (buy && Object.prototype.hasOwnProperty.call(LINKS, buy)) track("click-pay-" + buy);
    else if (/^mailto:/i.test(href) || a.classList.contains("mailto")) track("click-email");
    else if (/(^|\/)pricing\.html(\?|#|$)/.test(href)) track("click-pricing");
  }, true);
})();
