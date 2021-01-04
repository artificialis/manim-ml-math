
from manim import *


class MovingAround(Scene):
    def construct(self):
        # Form
        square = Square(color=BLUE, fill_opacity=1)

        # Play animation
        self.play(square.animate.shift(LEFT))
        self.play(square.animate.set_fill(ORANGE))
        self.play(square.animate.scale(0.3))
        self.play(square.animate.rotate(0.4))
    # end construct
# end MovingAround
