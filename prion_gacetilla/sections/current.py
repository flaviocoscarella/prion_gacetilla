from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (
    Image,
    PageBreak,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)

from ..styles import RED
from ..translations import TRANSLATIONS
from ..utils import make_h1, style_data_table


def build_current_section(styles, assets, text=None):
    if text is None:
        text = TRANSLATIONS["es"]["current"]
    band_photo_caption_style = ParagraphStyle(
        "BandPhotoCaption",
        parent=styles["Small"],
        fontSize=11,
        alignment=TA_CENTER,
        spaceBefore=2,
    )
    members = text["members"]
    member_table = Table(
        [
            [
                Paragraph(f"<b>{name}</b>", styles["Body"]),
                Paragraph(role, styles["Body"]),
            ]
            for name, role in members
        ],
        colWidths=[75 * mm, 70 * mm],
    )
    style_data_table(member_table, alternating_rows=False)

    band_photo = Image(
        str(assets.band_photo),
        width=150 * mm,
        height=150 * mm * assets.band_photo_ratio,
        kind="proportional",
    )
    band_photo_frame = Table([[band_photo]], colWidths=[150 * mm])
    band_photo_frame.setStyle(
        TableStyle(
            [
                ("BOX", (0, 0), (-1, -1), 1.5, "#8B1A1A"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ]
        )
    )

    return [
        Paragraph(text["title"], styles["H1"]),
        Paragraph(text["subtitle"], styles["H2"]),
        Paragraph(text["intro"], styles["Body"]),
        Paragraph(text["activity"], styles["Body"]),
        Spacer(1, 5 * mm),
        make_h1(text["lineup_heading"], styles["H1"]),
        Spacer(1, 4 * mm),
        member_table,
        Spacer(1, 6 * mm),
        band_photo_frame,
        Paragraph(text["photo_caption"], band_photo_caption_style),
        PageBreak(),
        Spacer(1, 7 * mm),
        Paragraph(text["international_heading"], styles["H1"]),
        Spacer(1, 3 * mm),
        *[
            Paragraph(paragraph, styles["Body"])
            for paragraph in text["international"]
        ],
        Spacer(1, 3 * mm),
        make_h1(text["live_heading"], styles["H1"]),
        Spacer(1, 3 * mm),
        Paragraph(text["live"], styles["Body"]),
        PageBreak(),
    ]
