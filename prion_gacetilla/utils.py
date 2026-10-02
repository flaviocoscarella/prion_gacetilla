from reportlab.lib import colors
from reportlab.lib.colors import HexColor
from reportlab.lib.units import mm
from reportlab.graphics.barcode.qr import QrCodeWidget
from reportlab.graphics.shapes import Drawing
from reportlab.platypus import Table, TableStyle

from .styles import DARK


def make_qr(data):
    qr = QrCodeWidget(data)
    qr.barFillColor = HexColor("#FAFAFA")

    x1, y1, x2, y2 = qr.getBounds()
    size = 29 * mm
    scale_x = size / (x2 - x1)
    scale_y = size / (y2 - y1)

    drawing = Drawing(
        size,
        size,
        transform=[scale_x, 0, 0, scale_y, -x1 * scale_x, -y1 * scale_y],
    )
    drawing.add(qr)
    return drawing


def style_data_table(
    table: Table,
    alternating_rows: bool = True,
    horizontal_padding: int = 6,
    vertical_padding: int = 4,
) -> None:
    commands = []
    if alternating_rows:
        commands.append(
            (
                "ROWBACKGROUNDS",
                (0, 0),
                (-1, -1),
                [DARK, colors.HexColor("#111")],
            )
        )
    else:
        commands.append(("BACKGROUND", (0, 0), (-1, -1), DARK))

    commands.extend(
        [
            ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#333")),
            ("INNERGRID", (0, 0), (-1, -1), 0.3, colors.HexColor("#333")),
            (
                "LEFTPADDING",
                (0, 0),
                (-1, -1),
                horizontal_padding,
            ),
            (
                "RIGHTPADDING",
                (0, 0),
                (-1, -1),
                horizontal_padding,
            ),
            ("TOPPADDING", (0, 0), (-1, -1), vertical_padding),
            ("BOTTOMPADDING", (0, 0), (-1, -1), vertical_padding),
        ]
    )
    table.setStyle(TableStyle(commands))
