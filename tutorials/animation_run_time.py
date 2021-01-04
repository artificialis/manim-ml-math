

from manim import *


class RunTime(Scene):
    def construct(self):
        square = Square()
        self.add(square)
        self.play(ApplyMethod(square.shift, UP), run_time=3)
        self.wait(1)
    # end construct
# end RunTime

