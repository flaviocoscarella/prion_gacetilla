from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Image, KeepTogether
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import mm
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from PIL import Image as PILImage
import qrcode, os

base_path = "C:\\Users\\flavi\\Desktop\\temas radio\\"
logo_path = fr"{base_path}Prion logo.png"
out = fr"{base_path}PRION_Gacetilla_de_Prensa_2026_FINAL.pdf"

# Read uploaded logo
logo_img = PILImage.open(logo_path)
logo_w, logo_h = logo_img.size
logo_ratio = logo_h / logo_w

try:
    pdfmetrics.registerFont(TTFont("DejaVuSans", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
    pdfmetrics.registerFont(TTFont("DejaVuSans-Bold", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))
    BODY, BOLD = "DejaVuSans", "DejaVuSans-Bold"
except Exception:
    BODY, BOLD = "Helvetica", "Helvetica-Bold"

BLACK = colors.HexColor("#080808")
DARK = colors.HexColor("#151515")
RED = colors.HexColor("#a30d16")
WHITE = colors.white
GRAY = colors.HexColor("#bcbcbc")
LIGHT = colors.HexColor("#dedede")

ss = getSampleStyleSheet()
ss.add(ParagraphStyle(name="CoverTitle", fontName=BOLD, fontSize=35, leading=36,
                       textColor=WHITE, alignment=TA_CENTER))
ss.add(ParagraphStyle(name="CoverSub", fontName=BODY, fontSize=10.5, leading=14,
                       textColor=GRAY, alignment=TA_CENTER))
ss.add(ParagraphStyle(name="H1", fontName=BOLD, fontSize=20, leading=23,
                       textColor=RED, spaceAfter=9))
ss.add(ParagraphStyle(name="H2", fontName=BOLD, fontSize=12.5, leading=15,
                       textColor=WHITE, spaceBefore=5, spaceAfter=5))
ss.add(ParagraphStyle(name="Body", fontName=BODY, fontSize=9.2, leading=13.5,
                       textColor=LIGHT, spaceAfter=7))
ss.add(ParagraphStyle(name="Small", fontName=BODY, fontSize=7.2, leading=9.5,
                       textColor=GRAY))
ss.add(ParagraphStyle(name="Quote", fontName=BOLD, fontSize=11, leading=15,
                       textColor=WHITE, alignment=TA_CENTER,
                       leftIndent=12*mm, rightIndent=12*mm, spaceBefore=7, spaceAfter=11))
ss.add(ParagraphStyle(name="Link", fontName=BODY, fontSize=8, leading=11,
                       textColor=LIGHT))

links = {
    "Facebook": "https://www.facebook.com/Priondeathmetal",
    "Instagram": "https://www.instagram.com/prion_death_metal/",
    "YouTube": "https://www.youtube.com/priondeath",
    "Bandcamp": "https://prion.bandcamp.com/",
    "Spotify": "https://open.spotify.com/intl-es/artist/5FXU7Dmtuv0xN8Ic3FTeW4",
}

def make_qr(data, filename):
    p = fr"{base_path}{filename}.png"
    qrcode.make(data).save(p)
    return p

qrs = {k: make_qr(v, f"prion_final_qr_{k.lower()}") for k, v in links.items()}

class DarkDoc(SimpleDocTemplate):
    pass

doc = DarkDoc(out, pagesize=A4, rightMargin=18*mm, leftMargin=22*mm,
              topMargin=18*mm, bottomMargin=22*mm)

def page_bg(canvas, doc):
    canvas.saveState()
    w, h = A4
    canvas.setFillColor(BLACK)
    canvas.rect(0, 0, w, h, fill=1, stroke=0)
    canvas.setFillColor(RED)
    canvas.rect(0, h-4.5*mm, w, 4.5*mm, fill=1, stroke=0)
    canvas.setFillColor(colors.HexColor("#151515"))
    canvas.rect(0, 0, 11*mm, h, fill=1, stroke=0)
    if doc.page > 1:
        canvas.setStrokeColor(colors.HexColor("#303030"))
        canvas.setLineWidth(.5)
        canvas.line(22*mm, 15*mm, w-15*mm, 15*mm)
        canvas.setFont(BODY, 7)
        canvas.setFillColor(GRAY)
        canvas.drawString(22*mm, 9*mm, "PRION · DEATH METAL · BUENOS AIRES, ARGENTINA")
        canvas.drawRightString(w-15*mm, 9*mm, f"{doc.page:02d}")
    canvas.restoreState()

S = []

# COVER: logo prominently featured
cover_logo_w = 155*mm
cover_logo_h = cover_logo_w * logo_ratio
S += [
    Spacer(1, 20*mm),
    Image(logo_path, width=cover_logo_w, height=cover_logo_h, kind="proportional"),
    Spacer(1, 10*mm),
    Paragraph("DEATH METAL · BUENOS AIRES, ARGENTINA", ss["CoverSub"]),
    Spacer(1, 10*mm),
    Paragraph("GACETILLA DE PRENSA · 2026", ss["CoverSub"]),
    Spacer(1, 23*mm),
    Paragraph("<b>SHADOWS SWIRL</b><br/>Adelanto del nuevo material de Prion", ss["Quote"]),
    Paragraph("Más de tres décadas de Death Metal extremo.", ss["CoverSub"]),
    Spacer(1, 17*mm),
    Table([[Paragraph(x.upper(), ss["Small"]) for x in
            ["Facebook", "Instagram", "YouTube", "Bandcamp", "Spotify"]]],
          colWidths=[29*mm]*5,
          style=TableStyle([("ALIGN",(0,0),(-1,-1),"CENTER")]))
]
S.append(PageBreak())

# Current release
S += [
    Paragraph("SHADOWS SWIRL", ss["H1"]),
    Paragraph("NUEVO MATERIAL · 2026", ss["H2"]),
    Paragraph(
        "<b>Prion se encuentra actualmente promocionando <i>Shadows Swirl</i>, "
        "adelanto del nuevo disco de la banda.</b> El lanzamiento representa una nueva etapa "
        "para Prion y mantiene la misma alineación: Gregorio Kochian en voz y guitarra, "
        "Walter Barrionuevo en bajo y Flavio Coscarella en batería.",
        ss["Body"]),
    Paragraph(
        "La banda continúa presentando el nuevo material en vivo y desarrollando su actividad "
        "de prensa y difusión alrededor de este adelanto.",
        ss["Body"]),
    Spacer(1, 4*mm),
    Paragraph("FORMACIÓN ACTUAL", ss["H1"])
]

members = [
    ["GREGORIO KOCHIAN", "Voz · Guitarra"],
    ["WALTER BARRIONUEVO", "Bajo"],
    ["FLAVIO COSCARELLA", "Batería"]
]
mt = Table([[Paragraph(f"<b>{a}</b>", ss["Body"]), Paragraph(b, ss["Body"])]
           for a,b in members], colWidths=[75*mm,70*mm])
mt.setStyle(TableStyle([
    ("BACKGROUND",(0,0),(-1,-1),DARK),
    ("BOX",(0,0),(-1,-1),.5,colors.HexColor("#333")),
    ("INNERGRID",(0,0),(-1,-1),.3,colors.HexColor("#333")),
    ("LEFTPADDING",(0,0),(-1,-1),6), ("RIGHTPADDING",(0,0),(-1,-1),6),
    ("TOPPADDING",(0,0),(-1,-1),4), ("BOTTOMPADDING",(0,0),(-1,-1),4)
]))
S += [
    mt, Spacer(1, 6*mm),
    Paragraph(
        "Esta es la alineación que actualmente lleva adelante la presentación en vivo "
        "y la promoción del nuevo material.",
        ss["Body"]),
    Spacer(1, 3*mm),
    Paragraph("ACTIVIDAD EN VIVO", ss["H1"]),
    Paragraph(
        "Durante 2026, Prion continúa llevando su propuesta de Death Metal extremo a escenarios "
        "de Buenos Aires, incorporando material nuevo a su repertorio.",
        ss["Body"]),
    PageBreak()
]

# Biography / discography
S += [
    Paragraph("BIOGRAFÍA", ss["H1"]),
    Paragraph(
        "<b>Prion</b> es una banda argentina de Death Metal originaria de Buenos Aires, "
        "formada en 1994. A lo largo de más de tres décadas de actividad, desarrolló una propuesta "
        "basada en la brutalidad, la precisión técnica, riffs de alta intensidad y una marcada identidad "
        "dentro del metal extremo.",
        ss["Body"]),
    Paragraph(
        "La discografía de la banda incluye <i>Time of Plagues</i> (2003), <i>Impressions</i> (2008), "
        "<i>Uncertain Process</i> (2015) y <i>Aberrant Calamity</i> (2019), además de material previo, "
        "splits y participaciones en compilaciones.",
        ss["Body"]),
    Paragraph(
        "<i>Aberrant Calamity</i>, publicado por Comatose Music en 2019, consolidó el enfoque de Prion "
        "hacia un Death Metal brutal y técnico. Actualmente la banda trabaja en nuevo material, cuyo primer "
        "adelanto es <i>Shadows Swirl</i>.",
        ss["Body"]),
    Paragraph("DISCOGRAFÍA SELECCIONADA", ss["H1"])
]

disc = [
    ["2003","Time of Plagues","Larga duración"],
    ["2008","Impressions","Larga duración"],
    ["2015","Uncertain Process","Larga duración"],
    ["2019","Aberrant Calamity","Larga duración"],
    ["2026","Shadows Swirl","Adelanto del nuevo disco"]
]
dt = Table([[Paragraph(f"<b>{y}</b>",ss["Body"]),
             Paragraph(t,ss["Body"]), Paragraph(d,ss["Body"])]
            for y,t,d in disc], colWidths=[18*mm,55*mm,72*mm])
dt.setStyle(TableStyle([
    ("ROWBACKGROUNDS",(0,0),(-1,-1),[DARK,colors.HexColor("#111")]),
    ("BOX",(0,0),(-1,-1),.5,colors.HexColor("#333")),
    ("INNERGRID",(0,0),(-1,-1),.3,colors.HexColor("#333")),
    ("LEFTPADDING",(0,0),(-1,-1),6),("RIGHTPADDING",(0,0),(-1,-1),6),
    ("TOPPADDING",(0,0),(-1,-1),4),("BOTTOMPADDING",(0,0),(-1,-1),4)
]))
S += [
    dt, Spacer(1,7*mm),
    Paragraph("SONIDO Y PROPUESTA", ss["H1"]),
    Paragraph(
        "Death Metal extremo con una combinación de brutalidad, precisión y pasajes técnicos. "
        "La propuesta de Prion se completa con una puesta en vivo intensa y directa, construida "
        "para escenarios de metal extremo.",
        ss["Body"]),
    PageBreak()
]

# Contact / links / QR
S += [
    Paragraph("PRENSA · ESCUCHA · REDES", ss["H1"]),
    Paragraph(
        "Canales oficiales para prensa, contratación, entrevistas, cobertura y escucha del material:",
        ss["Body"])
]
rows = []
for n in ["Facebook","Instagram","YouTube","Bandcamp","Spotify"]:
    rows.append([
        Paragraph(f"<b>{n}</b>", ss["Body"]),
        Paragraph(f'<link href="{links[n]}">{links[n]}</link>', ss["Link"])
    ])
lt = Table(rows, colWidths=[30*mm,105*mm])
lt.setStyle(TableStyle([
    ("ROWBACKGROUNDS",(0,0),(-1,-1),[DARK,colors.HexColor("#111")]),
    ("BOX",(0,0),(-1,-1),.5,colors.HexColor("#333")),
    ("INNERGRID",(0,0),(-1,-1),.3,colors.HexColor("#333")),
    ("LEFTPADDING",(0,0),(-1,-1),7),("RIGHTPADDING",(0,0),(-1,-1),7),
    ("TOPPADDING",(0,0),(-1,-1),5),("BOTTOMPADDING",(0,0),(-1,-1),5)
]))
S += [lt, Spacer(1,7*mm), Paragraph("ACCESO DIRECTO", ss["H1"])]

qr_names = ["Instagram","YouTube","Bandcamp","Spotify"]
qr_rows = []
for i in range(0,4,2):
    row=[]
    for n in qr_names[i:i+2]:
        row += [Image(qrs[n], width=29*mm, height=29*mm),
                Paragraph(n.upper(), ss["Small"])]
    qr_rows.append(row)

qt = Table(qr_rows, colWidths=[35*mm,25*mm,35*mm,25*mm])
qt.setStyle(TableStyle([
    ("ALIGN",(0,0),(-1,-1),"CENTER"), ("VALIGN",(0,0),(-1,-1),"MIDDLE"),
    ("TOPPADDING",(0,0),(-1,-1),4), ("BOTTOMPADDING",(0,0),(-1,-1),4)
]))
S += [
    qt, Spacer(1,6*mm),
    Paragraph("MATERIAL DE PRENSA", ss["H1"]),
    Paragraph(
        "Este documento puede acompañarse con fotografías oficiales en alta resolución, "
        "logo vectorial, portada del nuevo lanzamiento, rider técnico y fechas confirmadas.",
        ss["Body"]),
    Spacer(1,5*mm),
    Image(logo_path, width=75*mm, height=75*mm*logo_ratio, kind="proportional"),
    Spacer(1,4*mm),
    Paragraph("PRION · BUENOS AIRES, ARGENTINA · DEATH METAL", ss["Quote"])
]

doc.build(S, onFirstPage=page_bg, onLaterPages=page_bg)
print(out)
