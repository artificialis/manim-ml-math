

from manim import *


class MovingFrameBox(Scene):
    def construct(self):
        # Math text
        text = MathTex("\\frac{d}{dx}f(x)g(x)=", "f(x)\\frac{d}{dx}g(x)", "+", "g(x)\\frac{d}{dx}f(x)")

        # Show the equation
        self.play(Write(text))

        # Two frame boxes
        framebox1 = SurroundingRectangle(text[1], buff=0.1)
        framebox2 = SurroundingRectangle(text[3], buff=0.1)

        # Show first box
        self.play(ShowCreation(framebox1))
        self.wait()

        # Replace first box with second
        self.play(ReplacementTransform(framebox1, framebox2))
        self.wait()
    # end construct
# end MovingFrameBox
