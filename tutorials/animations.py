

from manim import *


class SomeAnimations(Scene):
    def construct(self):
        # Add a square
        square = Square()
        self.add(square)

        # Display the square
        self.play(FadeIn(square))

        # Rotate square
        self.play(Rotate(square, PI / 4.0))

        # Remove square
        self.play(FadeOut(square))

        # Wait 1 sec
        self.wait(1)
    # end construct
# end SomeAnimations

