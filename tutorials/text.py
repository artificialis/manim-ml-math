
# Imports
from manimlib.imports import *


# Scene
class makeText(Scene):
    """
    Scene
    """

    # Construct scene
    def construct(self):
        """
        Construct
        """
        # 4 text objects
        first_line = TextMobject("Manim is fun")
        second_line = TextMobject("and useful")
        final_line = TextMobject("Hope you like it too!", color=BLUE)
        color_final_line = TextMobject("Hope you like it too!")

        # Coloring
        color_final_line.set_color_by_gradient(BLUE, PURPLE)

        # Position of the text
        second_line.next_to(first_line, DOWN)

        # Play animation
        # Wait 1 sec
        self.wait(1)

        # Write first and second line and wait 1 sec
        self.play(Write(first_line), Write(second_line))
        self.wait(1)

        # Fade out second line, replace first line with final line, 1 second
        self.play(FadeOut(second_line), ReplacementTransform(first_line, final_line))
        self.wait(1)

        # Replace final line, with colored version, wait 2 seconds
        self.play(Transform(final_line, color_final_line))
        self.wait(2)
    # end construct

# end makeText
