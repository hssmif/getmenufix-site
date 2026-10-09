// Edit these if anything changes.
const CONTACT = "hssmif@gmail.com";
const LINKS = {
  menu_fix: "https://buy.stripe.com/6oU6oI0bi1I4bDWfXY1sQ04",
  menu_photos: "https://buy.stripe.com/5kQaEYf6c5Yk6jCeTU1sQ05",
  full_makeover: "https://buy.stripe.com/3cIdRa5vC1I4dM4dPQ1sQ06",
  done_for_you: "https://buy.stripe.com/cNi28s4ry5Yk8rK6no1sQ07",
};
// What Stripe charges in each currency (other countries see the closest one at checkout).
const PRICES = {
  menu_fix: { aud: 289, gbp: 149, eur: 169, usd: 189 },
  menu_photos: { aud: 579, gbp: 299, eur: 339, usd: 379 },
  full_makeover: { aud: 969, gbp: 499, eur: 569, usd: 629 },
  done_for_you: { aud: 89, gbp: 45, eur: 50, usd: 59 },
};
const SYM = { aud: "A$", gbp: "£", eur: "€", usd: "$" };

function setCur(c) {
  document.querySelectorAll(".cur button").forEach((b) => b.classList.toggle("on", b.dataset.c === c));
  document.querySelectorAll("[data-p]").forEach((el) => {
    el.textContent = (el.dataset.p === "done_for_you" ? "+" : "") + SYM[c] + PRICES[el.dataset.p][c];
  });
  try { localStorage.setItem("cur", c); } catch (e) {}
}
document.querySelectorAll(".cur button").forEach((b) => (b.onclick = () => setCur(b.dataset.c)));
document.querySelectorAll("[data-buy]").forEach((a) => (a.href = LINKS[a.dataset.buy]));

document.querySelectorAll(".mailto").forEach((a) => (a.href = "mailto:" + CONTACT));

// Free mockup form: opens the visitor's email app with everything filled in.
const form = document.getElementById("mockForm");
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

if (document.querySelector(".cur")) {
  const lang = (navigator.language || "").toLowerCase();
  let saved = null; try { saved = localStorage.getItem("cur"); } catch (e) {}
  setCur(saved || (lang.endsWith("-gb") ? "gbp" : lang.endsWith("-us") ? "usd"
    : /-(ie|fr|de|es|it|nl|be|pt|at|fi)$/.test(lang) ? "eur" : "aud"));
}
