"""Free tools for restaurant owners, built by _build.py into tools/*.html. Everything runs in the visitor's browser
(code in site.js): photos and text are never uploaded or sent anywhere.
Rules: Australian English, honest, every Uber fact links to Uber's own page, no dashes or hyphens between words."""

MENU_PHOTO = "https://help.uber.com/en/merchants-and-restaurants/article/merchant-submitted-menu-catalog-photo-guidelines?nodeId=6985355b-0426-4523-94f2-89bb9b0566e9"
DESC_ADVICE = "https://www.uber.com/au/en/blog/6-ways-to-optimise-your-uber-eats-menu/"

TOOLS = [
    {"slug": "uber-eats-photo-checker", "name": "Uber Eats photo checker",
     "short": "Check a dish photo against Uber's size rules and fix the shape in one click.",
     "title": "Free Uber Eats Photo Checker: Size, Ratio and File Type | MenuFix",
     "desc": "Check a menu photo against Uber Eats rules in your browser: 5:4 shape, at least 550 × 440 pixels, under 10 MB, JPG or PNG. Crop and resize to 2880 × 2304 in one click.",
     "icon": "camera"},
    {"slug": "menu-description-checker", "name": "Menu description checker",
     "short": "Paste a dish description: length, capitals, vague words and missing ingredients.",
     "title": "Free Uber Eats Menu Description Checker | MenuFix",
     "desc": "Paste an Uber Eats dish description and check it against Uber's 140 to 260 character advice. Flags ALL CAPS, vague words and descriptions that don't name the ingredients.",
     "icon": "pen"},
]


def tool_cards() -> str:
    return "".join(f'<a class="photo-card reveal tool-card" href="/tools/{t["slug"]}.html"><div class="body">'
                   f'<img class="icon3d" src="img/icons/{t["icon"]}.png" alt="" loading="lazy"><h3>{t["name"]}</h3>'
                   f'<p>{t["short"]}</p><span class="tool-go">Open the tool →</span></div></a>' for t in TOOLS)


PHOTO_BODY = f"""
<section style="padding-top:20px"><div class="narrow">
  <div class="tool" id="photoTool">
    <label class="tool-drop" id="ptDrop"><input type="file" id="ptFile" accept="image/*">
      <b>Choose a dish photo</b><span>or drop it here. It stays on your device: nothing is uploaded.</span></label>
    <div id="ptOut" class="tool-out" aria-live="polite"></div>
    <div class="row hidden" id="ptFixRow" style="margin-top:18px">
      <button class="btn primary" type="button" id="ptFix">Crop to 5:4 and resize to 2880 × 2304</button>
      <span class="note" id="ptFixNote"></span></div>
    <canvas id="ptCanvas" class="tool-preview hidden" aria-label="Preview of the fixed photo"></canvas>
  </div>
  <div class="prose" style="margin-top:40px">
    <h2>What this checks</h2>
    <ul class="ticks"><li><b>Shape:</b> close to 5:4 landscape, the shape Uber recommends.</li>
      <li><b>Size:</b> at least 550 × 440 pixels; 2880 × 2304 is ideal.</li>
      <li><b>File size:</b> under 10 MB.</li><li><b>File type:</b> JPG or PNG.</li></ul>
    <p>These come from Uber's <a href="{MENU_PHOTO}" rel="nofollow">menu photo guidelines</a>. The tool can't check what's in the
      photo: Uber also turns down photos with text, logos, more than one item or faces. See
      <a href="/guides/uber-eats-photo-upload-not-working.html">photo upload not working</a> for every reason and fix.</p>
    <p>The fix button crops the middle of your photo to 5:4 and saves a JPG at 2880 × 2304. If your photo is smaller than
      that, it gets bigger but not sharper, so a larger original is always better.</p>
  </div>
</div></section>"""

DESC_BODY = f"""
<section style="padding-top:20px"><div class="narrow">
  <div class="tool" id="descTool">
    <label class="f" for="dtText" style="font-weight:700">Dish description</label>
    <textarea id="dtText" rows="5" placeholder="For example: Crumbed chicken schnitzel topped with napoli sauce, leg ham and melted mozzarella. Served with chips and a side salad."></textarea>
    <div class="tool-meter"><div class="tool-bar"><i id="dtBar"></i></div><span id="dtCount">0 characters</span></div>
    <div id="dtOut" class="tool-out" aria-live="polite"></div>
  </div>
  <div class="prose" style="margin-top:40px">
    <h2>What this checks</h2>
    <ul class="ticks"><li><b>Length:</b> Uber's advice is 140 to 260 characters, about two short sentences
      (<a href="{DESC_ADVICE}" rel="nofollow">Uber Australia</a>).</li>
      <li><b>ALL CAPS:</b> words in capitals read like shouting and are harder to skim.</li>
      <li><b>Vague words:</b> delicious, amazing, best and similar say nothing about the dish.</li>
      <li><b>Ingredients:</b> whether it names at least two foods or cooking methods.</li></ul>
    <p>These are simple rules, not AI, and your text never leaves your browser. For ideas, see
      <a href="/guides/uber-eats-menu-description-examples.html">30 menu description examples</a> and
      <a href="/guides/write-uber-eats-menu-descriptions.html">how to write menu descriptions</a>.</p>
  </div>
</div></section>"""


def build_tools(page, head, cta) -> list[str]:
    bodies = {"uber-eats-photo-checker": (PHOTO_BODY, "Free Uber Eats <span class='hl'>photo checker.</span>",
                                          "Check a dish photo against Uber's size rules before you upload it, and fix the shape in one click."),
              "menu-description-checker": (DESC_BODY, "Free menu description <span class='hl'>checker.</span>",
                                           "Paste a dish description to check its length and wording against Uber's advice.")}
    out = []
    for t in TOOLS:
        body, h, lead = bodies[t["slug"]]
        name = f"tools/{t['slug']}.html"
        page(name, t["title"], t["desc"], f"""{head("Free tool", h, lead, (t["icon"], "star"))}
{body}
{cta("Want the whole page done?", "We rewrite your menu and enhance photos of your real dishes. Start with a free mockup, no payment and no obligation.")}
""", "guides/index.html", alt=None)
        out.append(name)
    return out
