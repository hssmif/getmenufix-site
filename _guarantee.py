"""Our guarantee on the website: "You only pay once you've seen your finished page and you're happy with it."
We never promise more orders; the owner simply takes no risk. Built by _build.py: a short block on the home pages,
the pricing pages and the free page check pages (EN, FR, ES), and the FAQ entry "What if I don't like it?".
Marked with comments, so a rebuild replaces the block instead of adding a second one. Same rules as every page: no
dashes or slashes between words, no invented numbers or testimonials."""
import os
import re

TEXT = {
    "en": ("No risk for you", "You only pay once you've seen your finished page and you're happy with it.",
           "Not happy? Tell us what to change, or simply say no and you owe nothing. We never promise more orders: we "
           "make your page clearer, and you decide."),
    "fr": ("Aucun risque pour vous", "Vous ne payez qu'après avoir vu votre page terminée, et seulement si elle vous plaît.",
           "Elle ne vous plaît pas ? Dites nous ce qu'il faut changer, ou dites simplement non : vous ne devez rien. Nous ne "
           "promettons jamais plus de commandes : nous rendons votre page plus claire, et c'est vous qui décidez."),
    "es": ("Sin riesgo para usted", "Solo paga cuando haya visto su página terminada y esté contento con ella.",
           "¿No le convence? Díganos qué cambiar, o simplemente diga que no y no nos debe nada. Nunca prometemos más "
           "pedidos: hacemos su página más clara, y usted decide."),
}
FAQ = {
    "en": ("What if I don't like it?", "You don't pay. We make your finished page first and send it to you, before and "
           "after, with every change listed. If you're happy, you pay. If not, tell us what to change, or simply say no "
           "and you owe nothing."),
    "fr": ("Et si elle ne me plaît pas ?", "Vous ne payez pas. Nous préparons d'abord votre page terminée et vous "
           "l'envoyons, avant et après, avec chaque changement listé. Si elle vous plaît, vous payez. Sinon, dites nous ce "
           "qu'il faut changer, ou dites simplement non : vous ne devez rien."),
    "es": ("¿Y si no me gusta?", "No paga. Primero preparamos su página terminada y se la enviamos, antes y después, con "
           "cada cambio indicado. Si le gusta, paga. Si no, díganos qué cambiar, o simplemente diga que no y no nos debe "
           "nada."),
}
# where the block goes: the pricing section of the home pages and the pricing pages (above the plans), and under the
# free page check form
PLANS_ON = ("index.html", "pricing.html", "fr/index.html", "fr/pricing.html", "es/index.html", "es/pricing.html")
CHECK_ON = ("check.html", "fr/check.html", "es/check.html")
_OLD = re.compile(r"\n?<!--guarantee-->.*?<!--/guarantee-->", re.S)
_OLD_FAQ = re.compile(r"<!--guarantee-faq-->.*?<!--/guarantee-faq-->", re.S)


def block(lang, icon):
    t, line, more = TEXT[lang]
    return (f'\n<!--guarantee--><div class="guarantee reveal"><img src="{icon}" alt=""><div><b>{t}</b>'
            f'<p>{line} {more}</p></div></div><!--/guarantee-->')


def faq_item(lang):
    q, a = FAQ[lang]
    return f"<!--guarantee-faq--><details><summary>{q}</summary><p>{a}</p></details><!--/guarantee-faq-->"


def add_guarantee(root, lang_of):
    """Put the block (and the French FAQ entry, the French pages are translated files) into the built pages."""
    for path in PLANS_ON + CHECK_ON:
        f = root / path
        if not f.is_file():
            continue
        html = _OLD.sub("", f.read_text())
        lang = lang_of(path)
        icon = os.path.relpath("img/icons/check.png", os.path.dirname(path) or ".")
        if path in PLANS_ON:
            html = html.replace('<div class="plans">', block(lang, icon).lstrip("\n") + '\n  <div class="plans">', 1)
        else:
            html = re.sub(r'(<form id="checkForm".*?</form>)', lambda m: m.group(1) + block(lang, icon), html, count=1, flags=re.S)
        f.write_text(html)
    f = root / "fr/faq.html"  # English and Spanish have it in their FAQ lists (and their FAQ structured data)
    if f.is_file():
        html = _OLD_FAQ.sub("", f.read_text())
        html = re.sub(r"(<summary>Est ce que cela garantira davantage de commandes \?</summary><p>.*?</p></details>)",
                      lambda m: m.group(1) + faq_item("fr"), html, count=1, flags=re.S)
        f.write_text(html)
