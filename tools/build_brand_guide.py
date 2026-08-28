from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white
from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib.utils import ImageReader

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output" / "pdf" / "clearer-days-brand-guide.pdf"
OUT.parent.mkdir(parents=True, exist_ok=True)
W, H = landscape(A4)
BLUE, CORAL, DAY, INK, MIST, SAGE, MUTED = map(HexColor, ["#2F5BD3", "#EF7C5B", "#FBFAF5", "#17212B", "#E9EFFC", "#DCE9DE", "#59656E"])

c = canvas.Canvas(str(OUT), pagesize=(W, H))
c.setTitle("Clearer Days Brand Guide")
c.setAuthor("Clearer Days")

def background(color=DAY):
    c.setFillColor(color); c.rect(0, 0, W, H, stroke=0, fill=1)

def footer(page):
    c.setFillColor(MUTED); c.setFont("Helvetica", 8)
    c.drawString(40, 24, "CLEARER DAYS  |  BRAND GUIDE")
    c.drawRightString(W-40, 24, f"{page:02d}")

def title(kicker, heading, intro=None, dark=False):
    fg = white if dark else INK
    c.setFillColor(CORAL if dark else BLUE); c.setFont("Helvetica-Bold", 10); c.drawString(48, H-56, kicker.upper())
    c.setFillColor(fg); c.setFont("Helvetica-Bold", 31); c.drawString(48, H-100, heading)
    if intro:
        c.setFillColor(HexColor("#C9D1D7") if dark else MUTED); c.setFont("Helvetica", 11); c.drawString(48, H-126, intro)

def page_end(n):
    footer(n); c.showPage()

# 1 Cover
background(); c.setFillColor(MIST); c.circle(W-70, H-30, 170, stroke=0, fill=1); c.setFillColor(SAGE); c.rect(0, 0, W, 92, stroke=0, fill=1)
c.drawImage(ImageReader(str(ROOT / "assets/brand/logos/clearer-days-symbol.png")), 55, H-190, 100, 100, mask='auto')
c.setFillColor(INK); c.setFont("Helvetica-Bold", 42); c.drawString(55, H-240, "Clearer Days")
c.setFillColor(BLUE); c.setFont("Helvetica-Bold", 16); c.drawString(58, H-275, "PRACTICAL SUPPORT FOR BUSY BRAINS.")
c.setFillColor(MUTED); c.setFont("Helvetica", 12); c.drawString(58, H-308, "Digital identity and usage guide")
page_end(1)

# 2 Idea and logo
background(); title("01 - Core idea", "An open horizon.", "A mark for clarity, possibility and a new day.")
c.drawImage(ImageReader(str(ROOT / "assets/brand/logos/clearer-days-symbol.png")), 58, 150, 210, 210, mask='auto')
c.setFillColor(INK); c.setFont("Helvetica-Bold", 17); c.drawString(335, 340, "The symbol")
c.setFillColor(MUTED); c.setFont("Helvetica", 11)
for i, line in enumerate(["An open C-shaped arc creates the sky.", "The coral disc is a new day at the horizon.", "The horizontal line gives the mark calm direction.", "Together they feel optimistic without being clinical."]): c.drawString(335, 311-i*25, line)
c.setFillColor(INK); c.setFont("Helvetica-Bold", 17); c.drawString(335, 190, "Clear space")
c.setFillColor(MUTED); c.setFont("Helvetica", 11); c.drawString(335, 163, "Keep space equal to one coral-disc diameter on every side.")
page_end(2)

# 3 Logo system
background(); title("02 - Logo system", "Built to work everywhere.", "Use the simplest version that stays clear at the intended size.")
c.drawImage(ImageReader(str(ROOT / "assets/brand/logos/clearer-days-primary.png")), 52, 305, 470, 106, mask='auto')
c.drawImage(ImageReader(str(ROOT / "assets/brand/logos/clearer-days-stacked.png")), 565, 260, 220, 143, mask='auto')
c.setFillColor(MUTED); c.setFont("Helvetica", 9); c.drawString(55, 282, "PRIMARY HORIZONTAL"); c.drawString(566, 245, "STACKED")
c.drawImage(ImageReader(str(ROOT / "assets/brand/logos/clearer-days-symbol.png")), 70, 88, 120, 120, mask='auto')
c.setFillColor(BLUE); c.roundRect(260, 88, 120, 120, 18, stroke=0, fill=1); c.drawImage(ImageReader(str(ROOT / "assets/brand/logos/clearer-days-symbol-on-blue.png")), 260, 88, 120, 120, mask='auto')
c.drawImage(ImageReader(str(ROOT / "assets/brand/logos/clearer-days-mono.png")), 455, 105, 300, 70, mask='auto')
c.setFillColor(MUTED); c.drawString(70, 70, "SYMBOL"); c.drawString(260, 70, "REVERSED"); c.drawString(455, 70, "ONE COLOR")
page_end(3)

# 4 Color
background(); title("03 - Color", "Calm daylight, clear contrast.", "Horizon Blue leads; Sunrise Coral is used sparingly for energy.")
colors=[("Horizon Blue","#2F5BD3",BLUE), ("Sunrise Coral","#EF7C5B",CORAL), ("Daylight","#FBFAF5",DAY), ("Deep Ink","#17212B",INK), ("Sky Mist","#E9EFFC",MIST), ("Soft Sage","#DCE9DE",SAGE)]
for i,(name,hexv,col) in enumerate(colors):
    x=48+(i%3)*255; y=285-(i//3)*145
    c.setFillColor(col); c.roundRect(x,y,220,94,15,stroke=1 if hexv=="#FBFAF5" else 0,fill=1)
    c.setFillColor(INK); c.setFont("Helvetica-Bold",11); c.drawString(x,y-20,name); c.setFont("Helvetica",9); c.drawString(x,y-35,hexv)
page_end(4)

# 5 Typography and voice
background(); title("04 - Type and voice", "Easy to read. Easy to trust.", "Manrope keeps the system modern, warm and direct.")
c.setFillColor(INK); c.setFont("Helvetica-Bold",28); c.drawString(48, 350, "Make life feel more workable.")
c.setFillColor(BLUE); c.setFont("Helvetica-Bold",12); c.drawString(48, 315, "MANROPE 700 - HEADINGS")
c.setFillColor(INK); c.setFont("Helvetica",16); c.drawString(48, 260, "Start with the point of friction, then find one next step.")
c.setFillColor(MUTED); c.setFont("Helvetica",10); c.drawString(48, 235, "MANROPE 400-500 - BODY")
c.setFillColor(MIST); c.roundRect(480, 145, 300, 245, 20,stroke=0,fill=1)
c.setFillColor(INK); c.setFont("Helvetica-Bold",15); c.drawString(505,350,"Voice principles")
c.setFont("Helvetica",11)
for i,line in enumerate(["Warm, never patronizing", "Practical, never prescriptive", "Clear, never clinical", "Encouraging, never overpromising", "Short sentences and concrete actions"]): c.drawString(505,315-i*36,"- "+line)
page_end(5)

# 6 Social system
background(); title("05 - Social", "Useful before impressive.", "One idea per post, generous space and a clear next action.")
tip=ROOT/"assets/brand/social/instagram-tip-portrait.png"; quote=ROOT/"assets/brand/social/instagram-quote-square.png"; banner=ROOT/"assets/brand/social/linkedin-personal-banner.png"
c.drawImage(ImageReader(str(tip)),55,80,180,225); c.drawImage(ImageReader(str(quote)),270,80,225,225); c.drawImage(ImageReader(str(banner)),530,170,270,68)
c.setFillColor(MUTED); c.setFont("Helvetica",9); c.drawCentredString(145,62,"PRACTICAL TIP"); c.drawCentredString(382,62,"QUOTE / THOUGHT"); c.drawCentredString(665,150,"LINKEDIN BANNER")
page_end(6)

# 7 Digital use
background(); title("06 - Digital use", "Navigation is part of the brand.", "Clearer Days should feel calm because the next destination is always obvious.")
items=[("01","Explicit labels","Use Prices, About Riya and Breathe - not clever labels."),("02","Short sections","Keep one purpose per section and paragraphs under 70 words."),("03","Persistent actions","Keep Prices, Breathe and WhatsApp easy to reach on mobile."),("04","Accessible by default","44px touch targets, visible focus and reduced motion.")]
for i,(n,h,b) in enumerate(items):
    x=48+(i%2)*380; y=320-(i//2)*140
    c.setFillColor(MIST if i%2==0 else SAGE); c.roundRect(x,y,340,105,18,stroke=0,fill=1)
    c.setFillColor(CORAL); c.setFont("Helvetica-Bold",10); c.drawString(x+20,y+74,n)
    c.setFillColor(INK); c.setFont("Helvetica-Bold",14); c.drawString(x+58,y+72,h)
    c.setFillColor(MUTED); c.setFont("Helvetica",9); c.drawString(x+20,y+39,b)
page_end(7)

# 8 Do / do not
background(INK); title("07 - Guardrails", "Keep Clearer Days clear.", "Consistency protects recognition and trust.",dark=True)
c.setFillColor(SAGE); c.roundRect(48,115,345,280,20,stroke=0,fill=1); c.setFillColor(MIST); c.roundRect(445,115,345,280,20,stroke=0,fill=1)
c.setFillColor(INK); c.setFont("Helvetica-Bold",16); c.drawString(72,355,"DO"); c.drawString(469,355,"DO NOT")
c.setFont("Helvetica",11)
for i,line in enumerate(["Use approved logo files","Keep generous clear space","Use plain, human language","Lead with one useful idea"]): c.drawString(72,315-i*43,"+ "+line)
for i,line in enumerate(["Stretch or rotate the logo","Add shadows or glossy effects","Use fake testimonials or claims","Crowd a layout with messages"]): c.drawString(469,315-i*43,"- "+line)
c.setFillColor(HexColor("#AEB7BD")); c.setFont("Helvetica",9); c.drawString(48,52,"Questions? Use the editable SVG sources in assets/brand.")
footer(8); c.save()
print(OUT)
