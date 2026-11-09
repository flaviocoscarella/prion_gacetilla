from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate

from .assets import prepare_assets
from .config import PROJECT_DIR, OUTPUT_PATH, SOCIAL_LINKS
from .page_layout import create_page_background
from .sections.biography import build_biography_section
from .sections.cover import build_cover
from .sections.current import build_current_section
from .sections.press import build_press_section
from .styles import create_styles
from .translations import TRANSLATIONS


DEFAULT_FRAME_PADDING = 6


def build_story(
    styles,
    assets,
    links,
    content_width,
    content_height,
    language="es",
):
    text = TRANSLATIONS[language]
    return (
        build_cover(styles, assets, links, text["cover"])
        + build_current_section(styles, assets, text["current"])
        + build_biography_section(
            styles,
            assets,
            content_width,
            content_height,
            text["biography"],
        )
        + build_press_section(styles, assets, links, text["press"])
    )


def generate_pdf(output_path=None, language="es"):
    if language not in TRANSLATIONS:
        raise ValueError(f"Idioma no soportado: {language}")
    if output_path is None:
        output_path = (
            OUTPUT_PATH
            if language == "es"
            else PROJECT_DIR / "PRION_Press_Kit_2026.pdf"
        )
    assets = prepare_assets()
    styles = create_styles()
    document = SimpleDocTemplate(
        str(output_path),
        pagesize=A4,
        rightMargin=18 * mm,
        leftMargin=22 * mm,
        topMargin=18 * mm,
        bottomMargin=22 * mm,
    )
    # SimpleDocTemplate's default frame adds 6 points of padding on every side.
    content_width = document.width - 2 * DEFAULT_FRAME_PADDING
    content_height = document.height - 2 * DEFAULT_FRAME_PADDING
    story = build_story(
        styles,
        assets,
        SOCIAL_LINKS,
        content_width,
        content_height,
        language,
    )
    page_background = create_page_background(
        assets.cover,
        styles["Body"].fontName,
    )
    document.build(
        story,
        onFirstPage=page_background,
        onLaterPages=page_background,
    )
    return output_path


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Genera la gacetilla de Prion.")
    parser.add_argument(
        "--language",
        choices=tuple(TRANSLATIONS),
        default="es",
        help="Idioma del documento (predeterminado: es).",
    )
    arguments = parser.parse_args()
    output_path = generate_pdf(language=arguments.language)
    print(f"PDF creado: {output_path}")
