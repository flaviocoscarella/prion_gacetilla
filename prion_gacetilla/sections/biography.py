from reportlab.lib.units import mm
from reportlab.platypus import PageBreak, Paragraph, Spacer, Table

from ..utils import style_data_table


def build_biography_section(styles):
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
                Paragraph(f"<b>{year}</b>", styles["Body"]),
                Paragraph(title, styles["Body"]),
                Paragraph(kind, styles["Body"]),
            ]
            for year, title, kind in discography
        ],
        colWidths=[18 * mm, 55 * mm, 72 * mm],
    )
    style_data_table(discography_table)

    return [
        Paragraph("BIOGRAFÍA", styles["H1"]),
        Paragraph(
            "<b>Prion</b> es una banda argentina de Death Metal "
            "originaria de Buenos Aires, formada en 1994. "
            "A lo largo de más de tres décadas de actividad, "
            "desarrolló una propuesta basada en la brutalidad, "
            "la precisión técnica, riffs de alta intensidad y "
            "una marcada identidad dentro del metal extremo.",
            styles["Body"],
        ),
        Paragraph(
            "Durante su primera y extensa etapa, la batería estuvo a cargo "
            "de <b>Marcelo Russo</b>, quien formó parte desde los "
            "comienzos, con una interrupción entre 2004 y 2006, y permaneció "
            "en la banda hasta fines de 2015. Russo participó en la grabación "
            "de los principales trabajos de estudio de esa etapa, incluyendo "
            "<i>Time of Plagues</i> (2003), <i>Impressions</i> (2008) y "
            "<i>Uncertain Process</i> (2015).",
            styles["Body"],
        ),
        Paragraph(
            "Entre los integrantes de la primera etapa de Prion también se "
            "encontró <b>Diego Braña</b>, quien formó parte de la banda desde "
            "su fundación en 1994 hasta 2006, participando activamente en el "
            "desarrollo de la formación y en la trayectoria inicial.",
            styles["Body"],
        ),
        Paragraph(
            "A fines de 2015, luego de la tercera gira europea de la banda, "
            "Marcelo Russo dejó la banda y fue reemplazado por "
            "<b>Flavio Coscarella</b>, quien se incorporó a la formación en "
            "2016. Desde entonces, Coscarella pasó a ocupar la batería y "
            "participó en la siguiente etapa discográfica de la banda, "
            "incluyendo <i>Aberrant Calamity</i> (2019).",
            styles["Body"],
        ),
        Paragraph(
            "La discografía de la banda incluye "
            "<i>Time of Plagues</i> (2003), "
            "<i>Impressions</i> (2008), "
            "<i>Uncertain Process</i> (2015) y "
            "<i>Aberrant Calamity</i> (2019), además de material "
            "previo, splits y participaciones en compilaciones.",
            styles["Body"],
        ),
        Paragraph(
            "<i>Aberrant Calamity</i>, publicado por Comatose Music "
            "en 2019, consolidó el enfoque de Prion hacia un Death "
            "Metal brutal y técnico. Actualmente la banda trabaja "
            "en nuevo material, cuyo primer adelanto es "
            "<i>Shadows Swirl</i>.",
            styles["Body"],
        ),
        Spacer(1, 3 * mm),
        Paragraph("DISCOGRAFÍA SELECCIONADA", styles["H1"]),
        discography_table,
        Spacer(1, 7 * mm),
        Paragraph("SONIDO Y PROPUESTA", styles["H1"]),
        Paragraph(
            "Death Metal extremo con una combinación de brutalidad, "
            "precisión y pasajes técnicos. La propuesta de Prion se "
            "completa con una puesta en vivo intensa y directa, "
            "construida para escenarios de metal extremo.",
            styles["Body"],
        ),
        PageBreak(),
    ]
