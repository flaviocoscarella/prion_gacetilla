from reportlab.lib import colors
from reportlab.lib.colors import HexColor
from reportlab.lib.units import mm
from reportlab.graphics.barcode.qr import QrCodeWidget
from reportlab.graphics.shapes import Drawing
from reportlab.platypus import Flowable, Paragraph, Table, TableStyle

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


class TaperedSeparator(Flowable):
    def __init__(
        self,
        width=100 * mm,
        height=1 * mm,
        color=colors.HexColor("#8B1A1A"),
    ):
        super().__init__()
        self.width = width
        self.height = height
        self.color = color
        self.hAlign = "CENTER"

    def draw(self):
        canvas = self.canv
        canvas.setFillColor(self.color)

        path = canvas.beginPath()
        path.moveTo(0, self.height / 2)
        path.lineTo(self.width / 2, self.height)
        path.lineTo(self.width, self.height / 2)
        path.lineTo(self.width / 2, 0)
        path.close()

        canvas.drawPath(path, fill=1, stroke=0)


def make_h1(text, style):
    return _H1Heading(text, style)


class _H1Heading(Flowable):
    def __init__(self, text, style):
        super().__init__()
        self.paragraph = Paragraph(text, style)
        self.separator = TaperedSeparator()
        self.paragraph_height = 0
        self.separator_gap = 6
        self.space_after = max(0, style.spaceAfter - self.separator_gap)

    def wrap(self, avail_width, avail_height):
        self.width = avail_width
        _, self.paragraph_height = self.paragraph.wrap(
            avail_width,
            avail_height,
        )
        self.separator.width = min(self.separator.width, avail_width)
        self.height = (
            self.separator.height
            + self.separator_gap
            + self.paragraph_height
            + self.space_after
        )
        return self.width, self.height

    def draw(self):
        self.separator.drawOn(
            self.canv,
            (self.width - self.separator.width) / 2,
            self.space_after + self.paragraph_height + self.separator_gap,
        )
        self.paragraph.drawOn(
            self.canv,
            0,
            self.space_after,
        )


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
