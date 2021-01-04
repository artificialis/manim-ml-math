
from manim import *


# Square to circle
class SquareToCircle(Scene):
    """
    Square to circle
    """

    # Construct the scene
    def construct(self):
        """
        Construct the scene
        """
        # Create a circle and set color
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)

        # Create square
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)

        # Animate everything
        self.play(ShowCreation(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))
    # end construct

# end SquareToCircle

