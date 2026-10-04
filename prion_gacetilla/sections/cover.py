from reportlab.lib.units import mm
from reportlab.platypus import Image, PageBreak, Paragraph, Spacer, Table, TableStyle


def build_cover(styles, assets, links):
    cover_logo_width = 155 * mm
    story = [
        Spacer(1, 20 * mm),
        Image(
            str(assets.logo),
            width=cover_logo_width,
            height=cover_logo_width * assets.logo_ratio,
            kind="proportional",
        ),
        Spacer(1, 10 * mm),
        Paragraph(
            "DEATH METAL · BUENOS AIRES, ARGENTINA",
            styles["CoverSub"],
        ),
        Spacer(1, 10 * mm),
        Paragraph("GACETILLA DE PRENSA · 2026", styles["CoverSub"]),
        Spacer(1, 23 * mm),
        # Paragraph(
        #     "<b>SHADOWS SWIRL</b><br/>"
        #     "Adelanto del nuevo material de Prion",
        #     styles["Quote"],
        # ),
        Paragraph(
            "Más de tres décadas de Death Metal extremo.",
            styles["CoverSub"],
        ),
        Spacer(1, 17 * mm),
        PageBreak(),
    ]
    return story
