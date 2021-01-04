

from manim import *


class MobjectZOrder(Scene):
    def construct(self):
        circle = Circle().shift(LEFT)
        square = Square().shift(UP)
        triangle = Triangle().shift(RIGHT)

        # Change style
        circle.set_stroke(color=GREEN, width=20)
        square.set_fill(YELLOW, opacity=1.0)
        triangle.set_fill(PINK, opacity=0.8)

        # Add form to the scene (different order)
        self.add(triangle, square, circle)
        self.wait(1)
    # end construct
# end MobjectZOrder

