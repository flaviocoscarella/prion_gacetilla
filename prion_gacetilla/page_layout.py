from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.utils import ImageReader

from .styles import GRAY, PAGE_H, PAGE_W, RED


def draw_album_cover_background(
    canvas,
    image_path,
    image_opacity=0.30,
    black_overlay_opacity=0.45,
):
    canvas.saveState()
    canvas.setFillAlpha(image_opacity)
    canvas.drawImage(
        ImageReader(str(image_path)),
        0,
        0,
        width=PAGE_W,
        height=PAGE_H,
        preserveAspectRatio=False,
        mask="auto",
    )
    canvas.restoreState()

    canvas.saveState()
    canvas.setFillColorRGB(0, 0, 0)
    canvas.setFillAlpha(black_overlay_opacity)
    canvas.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    canvas.restoreState()


def create_page_background(cover_path, body_font):
    def page_background(canvas, doc):
        canvas.saveState()
        width, height = A4

        draw_album_cover_background(
            canvas,
            cover_path,
            image_opacity=0.90,
            black_overlay_opacity=0.8,
        )

        canvas.setFillColor(RED)
        canvas.rect(
            0,
            height - 4.5 * mm,
            width,
            4.5 * mm,
            fill=1,
            stroke=0,
        )

        canvas.setFillColor(colors.HexColor("#151515"))
        canvas.rect(0, 0, 11 * mm, height, fill=1, stroke=0)

        if doc.page > 1:
            canvas.setStrokeColor(colors.HexColor("#303030"))
            canvas.setLineWidth(0.5)
            canvas.line(22 * mm, 15 * mm, width - 15 * mm, 15 * mm)

            canvas.setFont(body_font, 7)
            canvas.setFillColor(GRAY)
            canvas.drawString(
                22 * mm,
                9 * mm,
                "PRION · DEATH METAL · BUENOS AIRES, ARGENTINA",
            )
            canvas.drawRightString(
                width - 15 * mm,
                9 * mm,
                f"{doc.page:02d}",
            )

        canvas.restoreState()

    return page_background
