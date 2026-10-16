"""Checks of the built website (run after _build.py): python3 -m unittest _test_site"""
import re
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).parent
DASH = re.compile(r"[—–]|\w-\w|\w ?/ ?\w")


def text_of(html):
    html = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", html, flags=re.S)
    html = re.sub(r'(href|src)="[^"]*"', "", html)
    return re.sub(r"<[^>]+>", " ", html)


class GuaranteeTests(unittest.TestCase):
    def test_block_on_home_pricing_and_check_in_three_languages(self):
        from _guarantee import CHECK_ON, PLANS_ON, TEXT
        for path in PLANS_ON + CHECK_ON:
            html = (ROOT / path).read_text()
            lang = "fr" if path.startswith("fr/") else "es" if path.startswith("es/") else "en"
            self.assertEqual(html.count("<!--guarantee-->"), 1, path)
            self.assertIn(TEXT[lang][1], html, path)
            if path in PLANS_ON:
                self.assertLess(html.index("<!--guarantee-->"), html.index('<div class="plans">'), path)  # above the prices

    def test_faq_entry_in_three_languages(self):
        self.assertIn("What if I don't like it?", (ROOT / "faq.html").read_text())
        self.assertEqual((ROOT / "fr/faq.html").read_text().count("Et si elle ne me plaît pas ?"), 1)
        self.assertIn("¿Y si no me gusta?", (ROOT / "es/faq.html").read_text())
        self.assertIn('"name": "What if I don', (ROOT / "faq.html").read_text())  # in the FAQ structured data too

    def test_the_rules(self):
        from _guarantee import FAQ, TEXT
        for lang in ("en", "fr", "es"):
            for s in TEXT[lang] + FAQ[lang]:
                self.assertIsNone(DASH.search(s), s)
                self.assertNotRegex(s, r"\d")  # no numbers, no claims
            self.assertRegex(TEXT[lang][2], r"never promise more orders|ne promettons jamais|Nunca prometemos")

    def test_nobody_pays_on_the_website(self):
        js = (ROOT / "site.js").read_text()
        block = js[js.index('document.querySelectorAll("[data-buy]")'):][:400]
        self.assertIn('"contact.html?"', block)
        self.assertNotIn("LINKS[", block)

    def test_rebuild_adds_nothing_twice(self):
        subprocess.run(["python3", "_build.py"], cwd=ROOT, check=True, capture_output=True)
        self.assertEqual((ROOT / "index.html").read_text().count("<!--guarantee-->"), 1)
        self.assertEqual((ROOT / "fr/faq.html").read_text().count("<!--guarantee-faq-->"), 1)


class MenulogGuideTests(unittest.TestCase):
    PAGE = ROOT / "guides/moving-from-menulog-to-uber-eats.html"

    def test_guide_built_linked_from_every_australian_city_and_ends_with_the_check(self):
        from _landing import CITIES
        html = self.PAGE.read_text()
        self.assertIn("<h1", html)
        self.assertIn("Moving from Menulog to Uber Eats", html)
        for c in CITIES:
            self.assertIn("guides/moving-from-menulog-to-uber-eats.html", (ROOT / f"uber-eats/{c['slug']}.html").read_text(), c["slug"])
        article = html[html.index("<article"):html.index("</article>")]
        self.assertIn('href="/check.html"', article[-600:])                  # ends with the free page check
        self.assertIn("guides/moving-from-menulog-to-uber-eats.html", (ROOT / "sitemap.xml").read_text())

    def test_facts_only_from_ubers_own_pages(self):
        from _guides import GUIDES
        g = next(x for x in GUIDES if x["slug"] == "moving-from-menulog-to-uber-eats")
        hosts = {re.match(r"https://([^/]+)", u).group(1) for u in re.findall(r'href="(https://[^"]+)"', g["body"])}
        self.assertEqual(hosts, {"merchants.ubereats.com", "help.uber.com", "www.uber.com"})
        numbers = set(re.findall(r"\d[\d ×]*\d|\d", text_of(g["body"] + g["answer"] + " ".join(a for _, a in g["faq"]))))
        # Uber's own numbers (5:4, 2880 × 2304, 550 × 440, 10 MB) and the section numbers 1 to 6, nothing else
        self.assertLessEqual(numbers, {"2880 × 2304", "550 × 440", "550", "440", "10", "1", "2", "3", "4", "5", "6"})
        for part in [g["title"], g["lead"], g["answer"], text_of(g["body"])] + [q + a for q, a in g["faq"]]:
            self.assertIsNone(DASH.search(part.replace("5:4", "")), part[:80])
        self.assertNotIn("0%", text_of(g["body"]))                         # the fee offer is not from Uber's own page
        self.assertNotRegex(text_of(g["body"]), r"26 November|180 days")


if __name__ == "__main__":
    unittest.main()
