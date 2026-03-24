from Engine import COLORS, Engine


class SVGEngine(Engine):
    def __init__(self, w, h):
        super().__init__(w, h)

    def open(self):
        print(
            f'<svg width="{int(self.w)}" height="{int(self.h)}" xmlns="http://www.w3.org/2000/svg">'
        )

    def close(self):
        print("</svg>")

    def draw_line(self, nx, ny):
        color = COLORS[self.coloridx]
        print(
            f'<line x1="{self.x:.2f}" y1="{self.y:.2f}" x2="{nx:.2f}" y2="{ny:.2f}" '
            f'stroke="{color}" stroke-width="{self.penWidth}" '
            f'stroke-linecap="round" stroke-linejoin="round"/>'
        )
