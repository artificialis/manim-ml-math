
from manim import *


class ManimCELogo(Scene):
    def construct(self):
        # Background color
        self.camera.background_color = "#ece6e2"

        # Colors
        logo_green = "#87c2a5"
        logo_blue = "#525893"
        logo_red = "#e07a5f"
        logo_black = "#343434"

        # Text M
        ds_m = MathTex(r"\mathbb{M}", fill_color=logo_black).scale(7)
        ds_m.shift(2.25 * LEFT + 1.5 * UP)

        # Create a circle and a square
        circle = Circle(color=logo_green, fill_opacity=1).shift(LEFT)
        square = Square(color=logo_blue, fill_opacity=1).shift(UP)
        triangle = Triangle(color=logo_red, fill_opacity=1).shift(RIGHT)

        # Group forms
        logo = VGroup(triangle, square, circle, ds_m)
        logo.move_to(ORIGIN)

        # Add to scene
        self.add(logo)
        self.play(FadeIn(logo))
    # end construct
# end
