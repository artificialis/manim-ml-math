
from manim import *


class MobjectPlacement(Scene):
    def construct(self):
        # Forms
        circle = Circle()
        square = Square()
        triangle = Triangle()

        # Place the circle two units left from
        # the origin
        circle.move_to(LEFT * 2)

        # Place the square to the left of the circle
        square.next_to(circle, LEFT)

        # Align the left border of the triangle to the
        # left border of the circle.
        triangle.align_to(circle, LEFT)

        # Add everything to the scene
        self.add(circle, square, triangle)
        self.wait(1)
    # end construct
# end MobjectPlacement

