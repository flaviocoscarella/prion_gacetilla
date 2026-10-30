from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import Image, PageBreak, Paragraph, Spacer, Table, TableStyle

from ..utils import make_h1, style_data_table


def build_biography_section(styles, assets, content_width, content_height):
    biography_body_style = ParagraphStyle(
        "BiographyBody",
        parent=styles["Body"],
        leading=12.5,
    )
    discography = [
        ["2003", "Time of Plagues", "Larga duración"],
        ["2008", "Impressions", "Larga duración"],
        ["2015", "Uncertain Process", "Larga duración"],
        ["2019", "Aberrant Calamity", "Larga duración"],
        ["2026", "Shadows Swirl", "Adelanto del nuevo disco"],
    ]
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
        Paragraph("BIOGRAFÍA", styles["H1"]),
        Paragraph(
            "<b>Prion</b> es una banda argentina de Death Metal "
            "originaria de Buenos Aires, formada en 1994. "
            "Con más de 30 años (con <b>Gregorio Kochian</b> "
            "como único miembro constante), desarrolló una propuesta "
            "basada en la brutalidad y técnica, con riffs de alta "
            "intensidad dentro del death metal.",
            biography_body_style,
        ),
        Paragraph(
            "Durante su primera y extensa etapa, la batería estuvo a cargo "
            "de <b>Marcelo Russo</b>, quien formó parte desde los "
            "comienzos, con una interrupción entre 2004 y 2006 donde <b>Rodrigo "
            "Robledo</b> ocupó su lugar, y permaneció en la banda hasta fines de "
            "2015. Russo participó en la grabación de los principales trabajos "
            "de estudio de esa etapa, incluyendo <i>Time of Plagues</i> (2003), "
            "<i>Impressions</i> (2008) y <i>Uncertain Process</i> (2015).",
            biography_body_style,
        ),
        Paragraph(
            "Entre los integrantes de la primera etapa de Prion también formaron "
            "parte <b>Diego Braña</b> e <b>Iñaki Meli</b>, quienes estuvieron "
            "en la banda desde su fundación en 1994, participando activamente en la "
            "trayectoria inicial. En el año 2000 Iñaki abandonó la banda y fue "
            "reemplazado por <b>Walter Barrionuevo</b>, y Diego Braña hizo lo propio "
            "en el 2004, quedando la banda conformada como trío.",
            biography_body_style,
        ),
        Paragraph(
            "A fines de 2015, luego de la tercera gira europea de la banda, "
            "Marcelo Russo dejó la banda y fue reemplazado por "
            "<b>Flavio Coscarella</b>, quien se incorporó a la formación en "
            "2016. Desde entonces, Flavio pasó a ocupar la batería y "
            "participó en la siguiente etapa discográfica de la banda, "
            "incluyendo <i>Aberrant Calamity</i> (2019).",
            biography_body_style,
        ),
        Paragraph(
            "La discografía de la banda incluye "
            "<i>Time of Plagues</i> (2003), "
            "<i>Impressions</i> (2008), "
            "<i>Uncertain Process</i> (2015) y "
            "<i>Aberrant Calamity</i> (2019), además de material "
            "previo, splits y participaciones en compilaciones.",
            biography_body_style,
        ),
        Paragraph(
            "<i>Aberrant Calamity</i>, publicado por Comatose Music "
            "en 2019, consolidó el enfoque de Prion hacia un Death "
            "Metal brutal y técnico. Actualmente la banda trabaja "
            "en nuevo material, cuyo primer adelanto es "
            "<i>Shadows Swirl</i>.",
            biography_body_style,
        ),
        Spacer(1, 3 * mm),
        make_h1("DISCOGRAFÍA SELECCIONADA", styles["H1"]),
        Spacer(1, 3 * mm),
        discography_table,
        Spacer(1, 5 * mm),
        make_h1("SONIDO Y PROPUESTA", styles["H1"]),
        Spacer(1, 3 * mm),
        Paragraph(
            "A lo largo de su trayectoria, Prion desarrolló una identidad "
            "sonora en constante evolución, incorporando diferentes matices "
            "dentro del Death Metal extremo. Su álbum debut, "
            "<i>Time of Plagues</i> (2003), presenta un enfoque más cercano "
            "al Death/Thrash, con una combinación de elementos que remite "
            "a la agresividad de Death y Sepultura. En <i>Impressions</i> "
            "(2008), el sonido se volvió más brutal y contundente, con una "
            "orientación marcada hacia la intensidad y la precisión de "
            "Hate Eternal. A partir de <i>Uncertain Process</i> (2015), "
            "la música incorporó cierta afinidad con la oscuridad, "
            "la densidad y el carácter disonante de Immolation, sin "
            "abandonar la brutalidad, la agresividad y la técnica "
            "desarrolladas en la etapa anterior.",
            biography_body_style,
        ),
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
