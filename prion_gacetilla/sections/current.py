from reportlab.lib.units import mm
from reportlab.platypus import Image, PageBreak, Paragraph, Spacer, Table

from ..utils import style_data_table


def build_current_section(styles, assets):
    members = [
        ["GREGORIO KOCHIAN", "Voz · Guitarra"],
        ["WALTER BARRIONUEVO", "Bajo"],
        ["FLAVIO COSCARELLA", "Batería"],
    ]
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

    return [
        Paragraph("SHADOWS SWIRL", styles["H1"]),
        Paragraph("NUEVO MATERIAL · 2026", styles["H2"]),
        Paragraph(
            "<b>Prion se encuentra actualmente promocionando "
            "<i>Shadows Swirl</i>, adelanto del nuevo disco de la banda.</b> "
            "El lanzamiento representa una nueva etapa y mantiene "
            "la misma alineación: Gregorio Kochian en voz y guitarra, "
            "Walter Barrionuevo en bajo y Flavio Coscarella en batería.",
            styles["Body"],
        ),
        Paragraph(
            "La banda continúa presentando el nuevo material en vivo y "
            "desarrollando su actividad de prensa y difusión alrededor "
            "de este adelanto. Mientras tanto, Prion se encuentra "
            "finalizando en su próximo álbum en vistas de ser lanzado"
            "en el año 2027.",
            styles["Body"],
        ),
        Spacer(1, 4 * mm),
        Paragraph("FORMACIÓN ACTUAL", styles["H1"]),
        member_table,
        Spacer(1, 6 * mm),
        Image(
            str(assets.band_photo),
            width=150 * mm,
            height=150 * mm * assets.band_photo_ratio,
            kind="proportional",
        ),
        Spacer(1, 6 * mm),
        Paragraph("TRAYECTORIA INTERNACIONAL", styles["H1"]),
        Paragraph(
            "Prion desarrolló una importante actividad internacional, "
            "con tres giras europeas realizadas. La primera tuvo lugar "
            "en junio de 2011 e incluyó presentaciones en Italia, "
            "Rep. Checa, Macedonia, Hungría y España",
            styles["Body"],
        ),
        Paragraph(
            "En septiembre de 2012, la banda realizó su segunda gira "
            "europea junto a <b>Ingurgitate</b> (Estados Unidos) y "
            "<b>Merciless Precision</b> (Inglaterra), participando además "
            "en festivales como NRW Deathfest, GrindHoven y Morbide Fest.",
            styles["Body"],
        ),
        Paragraph(
            "En septiembre de 2015 llegó la tercera gira europea, "
            "compartiendo escenario con <b>Avulsed</b> (España) y "
            "<b>Natron</b> (Italia). La gira incluyó fechas en distintos "
            "países europeos y festivales del circuito extremo, consolidando "
            "la presencia de Prion fuera de Argentina.",
            styles["Body"],
        ),
        Paragraph(
            "En Sudamérica, Prion también llevó su música a Uruguay y Chile. "
            "La banda realizó presentaciones en Uruguay durante distintas "
            "etapas de su trayectoria, incluyendo una fecha en Montevideo en "
            "septiembre de 2018. En junio de 2019, Prion se presentó en el Teatro "
            "Cariola de Santiago de Chile como parte de la primera edición "
            "del Santiago Metal Festival, compartiendo cartel con "
            "<b>Nocturnus A.D.</b> (USA) y <b>Nasty Savage</b> (USA), además "
            "de destacadas bandas de la escena chilena.",
            styles["Body"],
        ),
        Paragraph(
            "A nivel local, Prion también ha compartido escenario con algunas "
            "de las bandas más reconocidas del Death y Black Metal internacional, "
            "entre ellas <b>PESTILENCE</b>, <b>IMMOLATION</b>, "
            "<b>MORBID ANGEL</b>, <b>NILE</b>, <b>DEICIDE</b>, "
            "<b>VADER</b>, <b>OBITUARY</b>, <b>BEHEMOTH</b>, "
            "<b>VITAL REMAINS</b> y <b>MAYHEM</b>, formando parte de importantes"
            "fechas de la escena extrema en Buenos Aires.",
            styles["Body"],
        ),
        Spacer(1, 3 * mm),
        Paragraph("ACTIVIDAD EN VIVO ACTUAL", styles["H1"]),
        Paragraph(
            "Durante 2026, Prion continúa llevando su propuesta de "
            "Death Metal extremo a escenarios de Buenos Aires y sumando "
            "material nuevo a su repertorio. Durante el año, la banda se "
            "presentó en tres oportunidades: el 10/07/2026 en Club V, junto "
            "a Ataúdes y Colapso; el 27/08/2026 en Melonio, junto a "
            "Morbosatan, The Satan's Scourge, Blasphemous Command y "
            "Expiration; y el 12/09/2026 nuevamente en Club V, junto a "
            "Axsem, Burden Rage y Aterrada. La próxima presentación será "
            "el 05/12/2026 en Club V, compartiendo escenario con "
            "Fossilization y Ataúdes.",
            styles["Body"],
        ),
        PageBreak(),
    ]
