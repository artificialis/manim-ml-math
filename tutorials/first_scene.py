
# Imports
from manim import *


# Square to circle scene
class SquareToCircle(Scene):
    """
    Square to circle scene
    """

    # Scene construction
    def construct(self):
        """
        Scene construction
        """
        # Create a circle
        circle = Circle()

        # Set the color and transparency
        circle.set_fill(PINK, opacity=0.5)

        # Show the circle
        self.play(ShowCreation(circle))
    # end construct

# end SquareToCircle
