
from manim import *


# Artim Scene
class Equations(Scene):
    """
    Artim Scene
    """

    # Scene construction
    def construct(self):
        """
        Scene construction
        """
        # Making equations
        first_equation = TextMobject(
            "$$J(\\theta) = -\\frac{1}{m} [\\sum_{i=1}^{m} y^{(i)} \\log{h_{\\theta}(x^{(i)})} + (1-y^{(i)}) \\log{(1-h_{\\theta}(x^{(i)}))}] $$"
        )

        # Second equation
        second_mob = TextMobject(
            *[
                "$J(\\theta_{0}, \\theta_{1})$",
                "=",
                "$\\frac{1}{2m}$",
                "$\\sum\\limits_{i=1}^m$",
                "(",
                "$h_{\\theta}(x^{(i)})$",
                "-",
                "$y^{(i)}$", "$)^2$"
            ]
        )

        # For each equation
        for i, item in enumerate(second_mob):
            if i != 0:
                item.next_to(second_mob[i-1], RIGHT)
            # end if
        # end for

        # Group of equation
        eq2 = VGroup(*second_mob)

        # Textes
        text1 = TextMobject("With Artim, you can write complex equations like this...")
        text2 = TextMobject("Or this...")
        text3 = TextMobject("And it looks nice!!")

        # Coloring equation
        second_mob.set_color_by_gradient("#33ccff", "#ff00ff")

        # Positioning equations
        text1.shift(2 * UP)
        text2.shift(2 * UP)

        # Animation equations
        self.play(Write(text1))
        self.play(Write(first_equation))
        self.play(
            ReplacementTransform(text1, text2),
            Transform(first_equation, eq2)
        )
        self.wait(1)

        # Different colors for each equation
        for i, item in enumerate(eq2):
            if i < 2:
                eq2[i].set_color(color=PURPLE)
            else:
                eq2[i].set_color(color='#00FFFF')
            # end if
        # end for

        self.add(eq2)
        self.wait(1)
        self.play(
            FadeOutAndShiftDown(eq2),
            FadeOutAndShiftDown(first_equation),
            Transform(text2, text3)
        )
    # end construct

# end Equations
