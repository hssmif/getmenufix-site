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

const mailFree = "mailto:" + CONTACT + "?subject=" + encodeURIComponent("Free mockup for my Uber Eats page") +
  "&body=" + encodeURIComponent("Hi,\n\nMy restaurant or shop on Uber Eats is: \nCity: \n\nThanks");
const free = document.getElementById("mailFree"); if (free) free.href = mailFree;
document.querySelectorAll("#mailFoot, .mailto").forEach((a) => (a.href = "mailto:" + CONTACT));

if (document.querySelector(".cur")) {
  const lang = (navigator.language || "").toLowerCase();
  let saved = null; try { saved = localStorage.getItem("cur"); } catch (e) {}
  setCur(saved || (lang.endsWith("-gb") ? "gbp" : lang.endsWith("-us") ? "usd"
    : /-(ie|fr|de|es|it|nl|be|pt|at|fi)$/.test(lang) ? "eur" : "aud"));
}
