from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


BLACK = colors.HexColor("#080808")
DARK = colors.HexColor("#151515")
RED = colors.HexColor("#a30d16")
WHITE = colors.white
GRAY = colors.HexColor("#bcbcbc")
LIGHT = colors.HexColor("#dedede")
PAGE_W, PAGE_H = A4


def _register_fonts():
    regular_font = Path(
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    )
    bold_font = Path(
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    )
    if not regular_font.is_file() or not bold_font.is_file():
        return "Helvetica", "Helvetica-Bold"

    pdfmetrics.registerFont(
        TTFont("DejaVuSans", str(regular_font))
    )
    pdfmetrics.registerFont(
        TTFont("DejaVuSans-Bold", str(bold_font))
    )
    return "DejaVuSans", "DejaVuSans-Bold"


def create_styles():
    body_font, bold_font = _register_fonts()
    styles = getSampleStyleSheet()

    styles.add(
        ParagraphStyle(
            name="CoverTitle",
            fontName=bold_font,
            fontSize=35,
            leading=36,
            textColor=WHITE,
            alignment=TA_CENTER,
        )
    )
    styles.add(
        ParagraphStyle(
            name="CoverSub",
            fontName=body_font,
            fontSize=10.5,
            leading=14,
            textColor=GRAY,
            alignment=TA_CENTER,
        )
    )
    styles.add(
        ParagraphStyle(
            name="H1",
            fontName=bold_font,
            fontSize=20,
            leading=23,
            textColor=RED,
            spaceAfter=9,
        )
    )
    styles.add(
        ParagraphStyle(
            name="H2",
            fontName=bold_font,
            fontSize=12.5,
            leading=15,
            textColor=WHITE,
            spaceBefore=5,
            spaceAfter=5,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Body",
            fontName=body_font,
            fontSize=9.2,
            leading=13.5,
            textColor=LIGHT,
            spaceAfter=7,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Small",
            fontName=body_font,
            fontSize=7.2,
            leading=9.5,
            textColor=GRAY,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Quote",
            fontName=bold_font,
            fontSize=11,
            leading=15,
            textColor=WHITE,
            alignment=TA_CENTER,
            leftIndent=12 * mm,
            rightIndent=12 * mm,
            spaceBefore=7,
            spaceAfter=11,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Link",
            fontName=body_font,
            fontSize=8,
            leading=11,
            textColor=LIGHT,
        )
    )
    return styles
