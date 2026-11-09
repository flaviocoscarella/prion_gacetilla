from reportlab.lib.units import mm
from reportlab.platypus import Image, Paragraph, Spacer, Table, TableStyle

from ..translations import TRANSLATIONS
from ..utils import make_h1, make_qr, style_data_table


QR_NAMES = ["Instagram", "YouTube", "Bandcamp", "Spotify"]


def build_press_section(styles, assets, links, text=None):
    if text is None:
        text = TRANSLATIONS["es"]["press"]
    link_rows = [
        [
            Paragraph(f"<b>{name}</b>", styles["Body"]),
            Paragraph(
                f'<link href="{url}">{url}</link>',
                styles["Link"],
            ),
        ]
        for name, url in links.items()
    ]
    links_table = Table(link_rows, colWidths=[30 * mm, 105 * mm])
    style_data_table(
        links_table,
        horizontal_padding=7,
        vertical_padding=5,
    )

    qr_rows = []
    for index in range(0, len(QR_NAMES), 2):
        row = []
        for name in QR_NAMES[index:index + 2]:
            row.extend(
                [
                    make_qr(links[name]),
                    Paragraph(name.upper(), styles["Small"]),
                ]
            )
        qr_rows.append(row)

    qr_table = Table(
        qr_rows,
        colWidths=[35 * mm, 25 * mm, 35 * mm, 25 * mm],
    )
    qr_table.setStyle(
        TableStyle(
            [
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]
        )
    )

    return [
        Paragraph(text["heading"], styles["H1"]),
        Paragraph(text["intro"], styles["Body"]),
        links_table,
        Spacer(1, 7 * mm),
        make_h1(text["direct_heading"], styles["H1"]),
        Spacer(1, 4 * mm),
        qr_table,
        Spacer(1, 6 * mm),
        make_h1(text["materials_heading"], styles["H1"]),
        Spacer(1, 4 * mm),
        Paragraph(
            text["materials"],
            styles["Body"],
        ),
        Spacer(1, 5 * mm),
        Image(
            str(assets.logo),
            width=75 * mm,
            height=75 * mm * assets.logo_ratio,
            kind="proportional",
        ),
        Spacer(1, 4 * mm),
        Paragraph(
            "PRION · BUENOS AIRES, ARGENTINA · DEATH METAL",
            styles["Quote"],
        ),
    ]
