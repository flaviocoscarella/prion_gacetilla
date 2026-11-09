from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import Image, PageBreak, Paragraph, Spacer, Table, TableStyle

from ..translations import TRANSLATIONS
from ..utils import make_h1, style_data_table


def build_biography_section(
    styles,
    assets,
    content_width,
    content_height,
    text=None,
):
    if text is None:
        text = TRANSLATIONS["es"]["biography"]
    biography_body_style = ParagraphStyle(
        "BiographyBody",
        parent=styles["Body"],
        leading=12.5,
    )
    discography = text["discography"]
    discography_table = Table(
        [
            [
                Paragraph(f"<b>{year}</b>", biography_body_style),
                Paragraph(title, biography_body_style),
                Paragraph(kind, biography_body_style),
            ]
            for year, title, kind in discography
        ],
        colWidths=[15 * mm, 39 * mm, 43 * mm],
    )
    style_data_table(
        discography_table,
        horizontal_padding=3,
        vertical_padding=2,
    )

    biography = [
        Paragraph(text["heading"], styles["H1"]),
        *[
            Paragraph(paragraph, biography_body_style)
            for paragraph in text["paragraphs"]
        ],
        Spacer(1, 3 * mm),
        make_h1(text["discography_heading"], styles["H1"]),
        Spacer(1, 3 * mm),
        discography_table,
        Spacer(1, 5 * mm),
        make_h1(text["sound_heading"], styles["H1"]),
        Spacer(1, 3 * mm),
        Paragraph(text["sound"], biography_body_style),
    ]

    column_widths = [content_width * 0.7, content_width * 0.3]
    cover_width = min(48 * mm, column_widths[1])
    album_caption_style = ParagraphStyle(
        "AlbumCaption",
        parent=styles["Small"],
        alignment=TA_CENTER,
        fontSize=7,
        leading=8.5,
    )
    cover_rows = []
    for album in assets.album_covers:
        image_scale = cover_width / max(1, album.ratio)
        cover_rows.append(
            [
                Image(
                    str(album.path),
                    width=image_scale,
                    height=image_scale * album.ratio,
                ),
                Paragraph(
                    f"<b>{album.title}</b> · {album.year}",
                    album_caption_style,
                ),
            ]
        )
    cover_column = Table(
        [[row] for row in cover_rows],
        colWidths=[cover_width],
        rowHeights=[content_height / len(cover_rows)] * len(cover_rows),
    )
    cover_column.setStyle(
        TableStyle(
            [
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ]
        )
    )

    biography_layout = Table(
        [[biography, cover_column]],
        colWidths=column_widths,
        hAlign="LEFT",
    )
    biography_layout.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (0, 0), 3 * mm),
                ("RIGHTPADDING", (1, 0), (1, 0), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ]
        )
    )

    return [
        biography_layout,
        PageBreak(),
    ]
