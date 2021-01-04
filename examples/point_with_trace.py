

from manim import *


class PointWithTrace(Scene):
    def construct(self):
        # A path
        path = VMobject()

        # A dot
        dot = Dot()

        # ??
        path.set_points_as_corners([dot.get_center(), dot.get_center()])

        # Path updater
        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot.get_center()])
            path.become(previous_path)
        # end update_path

        # Set path updater
        path.add_updater(update_path)

        # Add path and dot
        self.add(path, dot)

        # Rotate dot around RIGHT
        self.play(Rotating(dot, radians=PI, about_point=RIGHT, run_time=2))
        self.wait()

        # Move point up (with animation)
        self.play(dot.animate.shift(UP))
        self.play(dot.animate.shift(LEFT))

        # Wait
        self.wait()
    # end construct
# end PointWithTrace
