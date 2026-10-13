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

// Free tools (tools/*.html). Everything runs here in the browser: photos and text are never uploaded or sent.
(() => {
  const $ = (id) => document.getElementById(id);
  const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
  const msg = (kind, label, text) => `<div class="tool-msg ${kind}"><b>${label}</b><span>${text}</span></div>`;

  // ---- Uber Eats photo checker: 5:4, at least 550 x 440, under 10 MB, JPG or PNG
  const file = $("ptFile");
  if (file) {
    const drop = $("ptDrop"), out = $("ptOut"), fixRow = $("ptFixRow"), canvas = $("ptCanvas");
    let img = null, name = "photo";
    const check = (f) => {
      if (!f) return;
      name = (f.name || "photo").replace(/\.[^.]+$/, "");
      const okType = /^image\/(jpeg|png)$/.test(f.type) || /\.(jpe?g|png)$/i.test(f.name || "");
      const mb = f.size / 1048576;
      const sizeText = mb < 0.1 ? Math.max(1, Math.round(f.size / 1024)) + " KB" : mb.toFixed(1) + " MB";
      const url = URL.createObjectURL(f);
      const im = new Image();
      im.onload = () => {
        img = im;
        const w = im.naturalWidth, h = im.naturalHeight, r = w / h, shapeOk = Math.abs(r - 1.25) <= 0.03;
        const rows = [
          okType ? msg("pass", "Pass", "File type: " + (/png/i.test(f.type || f.name) ? "PNG" : "JPG") + ".")
                 : msg("fix", "Fix", "File type: save or export it as a JPG before uploading."),
          mb <= 10 ? msg("pass", "Pass", `File size: ${sizeText}, under 10 MB.`)
                   : msg("fix", "Fix", `File size: ${sizeText}. Uber allows up to 10 MB. The fix button below makes a smaller JPG.`),
          w >= 550 && h >= 440 ? msg(w >= 2880 && h >= 2304 ? "pass" : "info", w >= 2880 && h >= 2304 ? "Pass" : "OK",
              `Size: ${w} × ${h} pixels. ${w >= 2880 && h >= 2304 ? "Big enough for Uber's ideal 2880 × 2304." : "Above Uber's minimum of 550 × 440. 2880 × 2304 is ideal, so use a bigger original if you have one."}`)
            : msg("fix", "Fix", `Size: ${w} × ${h} pixels, smaller than Uber's minimum of 550 × 440. Use the original photo, not a screenshot or a copy from a chat app.`),
          shapeOk ? msg("pass", "Pass", `Shape: ${r.toFixed(2)} to 1, close to 5:4.`)
                  : msg("fix", "Fix", `Shape: ${r.toFixed(2)} to 1. Uber recommends 5:4 (1.25 to 1) landscape. Use the button below to crop it.`),
        ];
        const allOk = okType && mb <= 10 && w >= 550 && h >= 440 && shapeOk;
        out.innerHTML = (allOk ? msg("pass", "Ready", "This photo meets Uber's size rules. Check it shows one real dish with no text or logos.") : "") + rows.join("");
        fixRow.classList.remove("hidden");
        $("ptFixNote").textContent = w < 2880 || h < 2304 ? "Your photo is smaller than 2880 × 2304, so it will be enlarged, not sharpened." : "";
        canvas.classList.add("hidden");
      };
      im.onerror = () => {
        img = null; fixRow.classList.add("hidden");
        out.innerHTML = msg("fix", "Fix", "This browser can't open that file. It may be a HEIC photo from an iPhone: export or share it as a JPG, then try again.");
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
        $("ptFixNote").textContent = `Saved a ${kb < 100 ? Math.max(1, Math.round(kb)) + " KB" : (kb / 1024).toFixed(1) + " MB"} JPG at 2880 × 2304. Check the dish is still centred.`;
      }, "image/jpeg", 0.88);
    });
  }

  // ---- Menu description checker: 140 to 260 characters, ALL CAPS, vague words, ingredients
  const text = $("dtText");
  if (text) {
    const VAGUE = ["delicious", "amazing", "best", "yummy", "tasty", "awesome", "perfect", "incredible", "world famous", "mouth watering", "to die for", "great", "nice", "lovely", "beautiful"];
    const FOOD = ("beef chicken lamb pork fish prawn prawns salmon tuna egg eggs tofu cheese cheddar mozzarella feta haloumi parmesan " +
      "rice noodles noodle pasta bread bun brioche sourdough pita wrap tortilla pastry chips fries potato salad lettuce tomato onion " +
      "garlic chilli ginger lemon lime avocado mushroom mushrooms capsicum spinach basil coriander mint parsley sesame peanut peanuts " +
      "coconut curry sauce gravy mayo aioli butter cream yoghurt honey chocolate caramel vanilla berries banana mango apple oat oats " +
      "milk espresso coffee tea bacon ham sausage chorizo pepperoni olives pickles slaw kimchi soy teriyaki satay tamarind " +
      "grilled chargrilled fried crumbed roasted smoked braised slow baked toasted crispy steamed stir wood fired marinated " +
      "beans lentils chickpeas quinoa edamame cucumber carrot corn pumpkin beetroot dumpling dumplings broth soup patty").split(" ");
    const run = () => {
      const t = text.value.trim(), n = t.length;
      const bar = $("dtBar"), out = $("dtOut");
      $("dtCount").textContent = n + " character" + (n === 1 ? "" : "s");
      bar.style.width = Math.min(100, n / 2.6) + "%";
      bar.classList.toggle("ok", n >= 140 && n <= 260);
      if (!n) { out.innerHTML = ""; return; }
      const rows = [];
      rows.push(n < 140 ? msg("fix", "Short", `${n} characters. Uber's advice is 140 to 260: add the main ingredients or one detail that makes it yours.`)
        : n > 260 ? msg("fix", "Long", `${n} characters. Uber's advice is 140 to 260: cut it to the ingredients people care about.`)
        : msg("pass", "Pass", `${n} characters, inside Uber's 140 to 260 advice.`));
      const caps = (t.match(/\b[A-Z]{3,}\b/g) || []).filter((w) => !["BBQ", "XL", "GF", "VG", "DF"].includes(w));
      rows.push(caps.length ? msg("fix", "Capitals", `Write ${esc(caps.slice(0, 5).join(", "))} in normal capitals. ALL CAPS is harder to read.`)
        : msg("pass", "Pass", "No ALL CAPS words."));
      const low = " " + t.toLowerCase().replace(/[^a-z\s]/g, " ") + " ";
      const vague = VAGUE.filter((v) => low.includes(" " + v + " "));
      rows.push(vague.length ? msg("fix", "Vague", `Swap "${esc(vague.join('", "'))}" for something specific: an ingredient, how it's cooked, or the portion.`)
        : msg("pass", "Pass", "No vague praise words."));
      const foods = [...new Set(FOOD.filter((f) => low.includes(" " + f + " ")))];
      rows.push(foods.length >= 2 ? msg("pass", "Pass", `Names ingredients or cooking: ${esc(foods.slice(0, 6).join(", "))}.`)
        : msg("fix", "Ingredients", "Name at least two main ingredients or how it's cooked, so people know what they're getting."));
      out.innerHTML = rows.join("");
    };
    text.addEventListener("input", run);
    run();
  }
})();
