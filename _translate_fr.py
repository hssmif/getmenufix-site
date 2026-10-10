"""Builds the French website (website/fr/) from the English pages. Run after _build.py, from menufix/:
.venv/bin/python website/_translate_fr.py [page.html ...]"""
import re
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import config  # noqa: F401  (loads .env)
from openai import OpenAI

ROOT = Path(__file__).parent
OUT = ROOT / "fr"
PAGES = ["index.html", "services.html", "examples.html", "how-it-works.html", "pricing.html", "about.html", "faq.html",
         "contact.html", "privacy.html", "terms.html", "404.html"]

SYSTEM = """You translate a web page of MenuFix (a service that improves restaurants' Uber Eats pages) from English into
natural, warm, professional French for French restaurant owners (use « vous »).
Return the COMPLETE HTML document, identical to the input except for the visible text and these attributes: alt,
title, placeholder, aria-label, content of <meta name="description"> and og:title/og:description. Never change tags,
classes, ids, href, src, data-* attributes, scripts, styles or numbers. Set <html lang="fr">.
Fixed names: "Menu Fix" stays "Menu Fix"; "Menu and Photos" = "Menu et Photos"; "Full Makeover" = "Refonte Complète";
"Done for you" = "Clé en main"; "free mockup" = "maquette gratuite"; "Uber Eats Manager" stays. Keep "MenuFix",
"Uber Eats", "Stripe" and dish names as they are. "one time price, no subscription" = "prix unique, sans abonnement".
Translate EVERY piece of visible English text: badges ("Before and after" = "Avant et après"), card titles and
descriptions, dish names and descriptions in the example cards (e.g. "Smash Burger and Fries" = "Smash Burger et
frites"), buttons, captions and footers. The only exception: strikethrough "before" dish names inside <s> are
deliberately messy menu entries, keep them exactly as written.
Headline of the home page: "Donnez envie aux clients affamés de vous choisir." with the highlighted span kept on
"vous choisir.". Prices like "$18.00" become "18,00 €".
Rules: no dashes (— or –) and never join words with a hyphen, no slash between words; French punctuation (space
before : ; ? !). Keep it honest: do not add claims, numbers or reviews that are not in the English page."""


def fix_paths(html: str) -> str:
    """The French pages live one folder down: point assets at the parent folder."""
    html = re.sub(r'(src|href)="(img/|style\.css|site\.js|favicon\.png|apple-touch-icon\.png)', r'\1="../\2', html)
    html = re.sub(r'<a class="lang" href="fr/([^"]*)" hreflang="fr"[^>]*>[^<]*</a>',
                  r'<a class="lang" href="../\1" hreflang="en" title="English">EN</a>', html)
    html = re.sub(r'<link rel="canonical" href="https://getmenufix.com/([^"]*)">',
                  r'<link rel="canonical" href="https://getmenufix.com/fr/\1">', html)
    return html


def translate(name: str) -> str:
    src = (ROOT / name).read_text()
    r = OpenAI(timeout=600).chat.completions.create(
        model="gpt-5-mini", messages=[{"role": "system", "content": SYSTEM}, {"role": "user", "content": src}])
    html = r.choices[0].message.content.strip()
    html = re.sub(r"^```(?:html)?\s*|\s*```$", "", html)
    if not html.lower().startswith("<!doctype") or src.count("<section") != html.count("<section"):
        raise RuntimeError(f"{name}: translation changed the page structure")
    OUT.mkdir(exist_ok=True)
    (OUT / name).write_text(fix_paths(html))
    return name


if __name__ == "__main__":
    todo = sys.argv[1:] or PAGES
    with ThreadPoolExecutor(4) as ex:
        for f in [ex.submit(translate, n) for n in todo]:
            try:
                print("translated", f.result(), flush=True)
            except Exception as e:
                print("FAILED", e, flush=True)
