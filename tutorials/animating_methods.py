

from manim import *


class ApplyMethodExample(Scene):
    def construct(self):
        # Add a square
        square = Square().set_fill(RED, opacity=1.0)
        self.add(square)

        # Animate the change of color
        self.play(ApplyMethod(square.set_fill, WHITE))
        self.wait(1)

        # Animate the change of position
        self.play(ApplyMethod(square.shift, UP))
        self.wait(1)
    # end construct
# end ApplyMethodExample
