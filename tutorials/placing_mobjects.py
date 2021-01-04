
from manim import *


class Shapes(Scene):
    def construct(self):
        # Create forms
        circle = Circle()
        square = Square()
        triangle = Triangle()

        # Move 1 unit
        circle.shift(LEFT)
        square.shift(UP)
        triangle.shift(RIGHT)

        # Add to scene
        self.add(circle, square, triangle)
        self.wait(1)
    # end construct
# end Shapes

