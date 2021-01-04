
from manim import *


# Scene
class MobjectStyling(Scene):
    def construct(self):
        # Forms
        circle = Circle().shift(LEFT)
        square = Square().shift(UP)
        triangle = Triangle().shift(RIGHT)

        # Set style
        circle.set_stroke(color=GREEN, width=20)
        square.set_fill(YELLOW, opacity=1.0)
        triangle.set_fill(PINK, opacity=0.5)

        # Add forms to the scene
        self.add(circle, square, triangle)
        self.wait(1)
    # end construct
# end MobjectStyling

