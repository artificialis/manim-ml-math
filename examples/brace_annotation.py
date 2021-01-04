

from manim import *


class BraceAnnotation(Scene):
    def construct(self):
        # Create two dots
        dot = Dot([-2, -1, 0])
        dot2 = Dot([2, 1, 0])

        # Create a line
        line = Line(dot.get_center(), dot2.get_center()).set_color(ORANGE)

        # Create a brace with a tet
        b1 = Brace(line)
        b1text = b1.get_text("Horizontal distance")

        # Second brace
        b2 = Brace(line, direction=line.copy().rotate(PI / 2.0).get_unit_vector())
        b2text = b2.get_tex("x - x_1")

        # Add object
        self.add(line, dot, dot2, b1, b2, b1text, b2text)
        self.play(FadeIn(line))
        self.wait(1)
    # end construct
# end BraceAnnotation
