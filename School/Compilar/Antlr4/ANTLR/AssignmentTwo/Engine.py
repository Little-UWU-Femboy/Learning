import math

COLORS = [
    "black",
    "red",
    "green",
    "blue",
    "yellow",
    "cyan",
    "magenta",
    "coral",
    "gray",
    "orange",
    "purple",
    "brown",
    "pink",
    "lime",
    "navy",
    "teal",
]


class Engine:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.home()

    def home(self):
        self.x = self.w / 2.0
        self.y = self.h / 2.0
        self.headingDeg = 0.0
        self.penIsDown = True
        self.coloridx = 0
        self.penWidth = 2  # Default width

    def penDown(self):
        self.penIsDown = True

    def penUp(self):
        self.penIsDown = False

    def setColor(self, c):
        self.coloridx = int(c) % len(COLORS)

    def setWidth(self, w):
        self.penWidth = int(w)

    def rotate(self, degrees):
        self.headingDeg += degrees

    def move(self, dist):
        r = math.radians(self.headingDeg)
        nx = self.x + dist * math.cos(r)
        ny = self.y + dist * math.sin(r)
        if self.penIsDown:
            self.draw_line(nx, ny)
        self.x = nx
        self.y = ny

    def open(self):
        pass

    def close(self):
        pass

    def draw_line(self, nx, ny):
        pass
