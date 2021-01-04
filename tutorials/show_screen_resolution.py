

from manim import *


class ShowScreenResolution(Scene):
    def construct(self):
        # Screen info
        pixel_height = config["pixel_height"]
        pixel_width = config["pixel_width"]
        frame_width = config["frame_width"]
        frame_height = config["frame_height"]

        # Add a dot
        self.add(Dot())

        # Add a line
        d1 = Line(frame_width * LEFT / 2, frame_width * RIGHT / 2).to_edge(DOWN)
        self.add(d1)

        # Add a text
        self.add(Text(str(pixel_width)).next_to(d1, UP))

        # Add a second line
        d2 = Line(frame_height * UP / 2, frame_height * DOWN / 2).to_edge(LEFT)
        self.add(d2)

        # Add text
        self.add(Text(str(pixel_height)).next_to(d2, RIGHT))

        # Show
        self.play(FadeIn(d1))
    # end construct
# end ShowScreenResolution
