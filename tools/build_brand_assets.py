from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parents[1]
BRAND = ROOT / "assets" / "brand"
LOGOS = BRAND / "logos"
SOCIAL = BRAND / "social"
for directory in (LOGOS, SOCIAL):
    directory.mkdir(parents=True, exist_ok=True)

BLUE = "#2F5BD3"
CORAL = "#EF7C5B"
DAYLIGHT = "#FBFAF5"
INK = "#17212B"
MIST = "#E9EFFC"
SAGE = "#DCE9DE"

SYMBOL = f'''<g aria-label="Clearer Days open horizon symbol">
  <path d="M74 22 A52 52 0 1 0 74 126" fill="none" stroke="{BLUE}" stroke-width="20" stroke-linecap="round"/>
  <path d="M77 74 H132" fill="none" stroke="{BLUE}" stroke-width="8" stroke-linecap="round"/>
  <circle cx="119" cy="62" r="13" fill="{CORAL}"/>
</g>'''

def write(name, content):
    (name).write_text(content, encoding="utf-8")

def svg(width, height, content, bg=None, label="Clearer Days brand asset"):
    background = f'<rect width="{width}" height="{height}" fill="{bg}"/>' if bg else ""
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="{escape(label)}">
{background}{content}
</svg>'''

write(LOGOS / "clearer-days-symbol.svg", svg(148, 148, SYMBOL, label="Clearer Days symbol"))
write(LOGOS / "clearer-days-symbol-on-blue.svg", svg(148, 148, SYMBOL.replace(BLUE, "#FFFFFF"), BLUE, "Clearer Days white symbol"))

horizontal = f'''<g transform="translate(14 14) scale(.72)">{SYMBOL}</g>
<text x="138" y="64" fill="{INK}" font-family="Manrope, Arial, sans-serif" font-size="38" font-weight="700" letter-spacing="-1.5">Clearer Days</text>
<text x="140" y="91" fill="{BLUE}" font-family="Manrope, Arial, sans-serif" font-size="13" font-weight="600" letter-spacing=".4">PRACTICAL SUPPORT FOR BUSY BRAINS.</text>'''
write(LOGOS / "clearer-days-primary.svg", svg(520, 116, horizontal, label="Clearer Days primary logo"))

stacked = f'''<g transform="translate(126 20)">{SYMBOL}</g>
<text x="200" y="199" text-anchor="middle" fill="{INK}" font-family="Manrope, Arial, sans-serif" font-size="38" font-weight="700" letter-spacing="-1.5">Clearer Days</text>
<text x="200" y="229" text-anchor="middle" fill="{BLUE}" font-family="Manrope, Arial, sans-serif" font-size="12" font-weight="600" letter-spacing=".4">PRACTICAL SUPPORT FOR BUSY BRAINS.</text>'''
write(LOGOS / "clearer-days-stacked.svg", svg(400, 260, stacked, label="Clearer Days stacked logo"))

mono_symbol = SYMBOL.replace(BLUE, INK).replace(CORAL, INK)
mono = f'''<g transform="translate(14 14) scale(.72)">{mono_symbol}</g><text x="138" y="72" fill="{INK}" font-family="Manrope, Arial, sans-serif" font-size="38" font-weight="700" letter-spacing="-1.5">Clearer Days</text>'''
write(LOGOS / "clearer-days-mono.svg", svg(500, 116, mono, label="Clearer Days monochrome logo"))

def brand_mark(x, y, scale=1):
    return f'<g transform="translate({x} {y}) scale({scale})">{SYMBOL}</g>'

def social_template(width, height, title, subtitle, kind, accent=SAGE):
    pad = int(width * .075)
    mark_scale = max(.45, width / 2100)
    content = f'''
      <circle cx="{width*.88:.0f}" cy="{height*.18:.0f}" r="{width*.22:.0f}" fill="{MIST}"/>
      <path d="M0 {height*.84:.0f} Q {width*.38:.0f} {height*.7:.0f} {width:.0f} {height*.82:.0f} V {height} H0Z" fill="{accent}"/>
      {brand_mark(pad, pad, mark_scale)}
      <text x="{pad}" y="{height*.45:.0f}" fill="{BLUE}" font-family="Manrope, Arial, sans-serif" font-size="{max(18,width*.022):.0f}" font-weight="700" letter-spacing="1.5">{escape(kind.upper())}</text>
      <text x="{pad}" y="{height*.53:.0f}" fill="{INK}" font-family="Manrope, Arial, sans-serif" font-size="{width*.062:.0f}" font-weight="700" letter-spacing="-2">{escape(title)}</text>
      <text x="{pad}" y="{height*.59:.0f}" fill="#53606B" font-family="Manrope, Arial, sans-serif" font-size="{width*.026:.0f}" font-weight="500">{escape(subtitle)}</text>
      <text x="{pad}" y="{height-pad*.55:.0f}" fill="{INK}" font-family="Manrope, Arial, sans-serif" font-size="{max(16,width*.018):.0f}" font-weight="650">Clearer Days · ADHD coaching with Riya</text>'''
    return svg(width, height, content, DAYLIGHT, f"Clearer Days {kind} template")

templates = {
    "instagram-tip-portrait.svg": (1080, 1350, "One thing first.", "A practical idea goes here.", "Practical tip", SAGE),
    "instagram-quote-square.svg": (1080, 1080, "Your words here.", "Keep it short, warm and human.", "A clearer thought", MIST),
    "instagram-carousel-cover.svg": (1080, 1350, "A useful topic", "Swipe for a calmer way forward →", "Clearer Days guide", "#F4E4C5"),
    "instagram-carousel-slide.svg": (1080, 1350, "01  Start here", "Use one idea per slide and plenty of space.", "Small steps", SAGE),
    "instagram-service.svg": (1080, 1350, "Work with Riya", "ADHD coaching · Abu Dhabi + online", "Coaching", MIST),
    "instagram-story-qa.svg": (1080, 1920, "Ask Riya", "Add a question sticker here.", "Questions are welcome", "#F4E4C5"),
    "instagram-story-availability.svg": (1080, 1920, "Now booking", "Free 20-minute fit conversations", "Availability", SAGE),
}
for filename, values in templates.items():
    write(SOCIAL / filename, social_template(*values))

personal_banner = f'''<circle cx="1390" cy="40" r="310" fill="{MIST}"/><path d="M0 350 Q 650 280 1584 338 V396 H0Z" fill="{SAGE}"/>
<g transform="translate(545 62) scale(.46)">{SYMBOL}</g>
<text x="675" y="155" fill="{INK}" font-family="Manrope, Arial, sans-serif" font-size="45" font-weight="700" letter-spacing="-1.5">Practical support for busy brains.</text>
<text x="677" y="203" fill="#53606B" font-family="Manrope, Arial, sans-serif" font-size="22" font-weight="550">ADHD coaching · Abu Dhabi + online</text>
<text x="677" y="260" fill="{BLUE}" font-family="Manrope, Arial, sans-serif" font-size="18" font-weight="700">CLEARER DAYS WITH RIYA</text>'''
write(SOCIAL / "linkedin-personal-banner.svg", svg(1584, 396, personal_banner, DAYLIGHT, "Clearer Days LinkedIn personal banner"))

company_banner = f'''<circle cx="1040" cy="20" r="190" fill="{MIST}"/><path d="M0 160 Q 420 125 1128 165 V191 H0Z" fill="{SAGE}"/>
<g transform="translate(70 20) scale(.32)">{SYMBOL}</g>
<text x="190" y="80" fill="{INK}" font-family="Manrope, Arial, sans-serif" font-size="28" font-weight="700">Practical support for busy brains.</text>
<text x="191" y="112" fill="#53606B" font-family="Manrope, Arial, sans-serif" font-size="15" font-weight="550">ADHD coaching with Riya · Abu Dhabi + online</text>'''
write(SOCIAL / "linkedin-company-banner.svg", svg(1128, 191, company_banner, DAYLIGHT, "Clearer Days LinkedIn company banner"))

readme = f'''# Clearer Days digital brand kit

## Core identity
- Brand: Clearer Days
- Descriptor: ADHD coaching with Riya
- Tagline: Practical support for busy brains.
- Symbol: open horizon / open C with sunrise disc

## Palette
- Horizon Blue: {BLUE}
- Sunrise Coral: {CORAL}
- Daylight: {DAYLIGHT}
- Deep Ink: {INK}
- Sky Mist: {MIST}
- Soft Sage: {SAGE}

## Typography
Manrope Variable is included under the SIL Open Font License. Use 700 for headings, 600 for labels and 400-500 for body copy.

## Usage
Keep clear space around the logo equal to the diameter of the coral sun. Do not stretch, recolor individual elements, add effects or place the full-color mark on busy photography. SVG templates are editable and can be imported into Canva, Figma or Adobe tools.
'''
write(BRAND / "README.md", readme)
print(f"Built brand SVG assets in {BRAND}")

try:
    import cairosvg
    from xml.etree import ElementTree
    for source in [*LOGOS.glob("*.svg"), *SOCIAL.glob("*.svg")]:
        root = ElementTree.parse(source).getroot()
        width = int(float(root.attrib["width"]))
        height = int(float(root.attrib["height"]))
        if source.parent == LOGOS:
            scale = max(1, 2400 / max(width, height))
            width, height = int(width * scale), int(height * scale)
        cairosvg.svg2png(url=str(source), write_to=str(source.with_suffix(".png")), output_width=width, output_height=height)
    print("Exported transparent PNG logo and social assets")
except ImportError:
    print("CairoSVG not installed; SVG sources were built without PNG exports")
