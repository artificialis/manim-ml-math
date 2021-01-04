

from manim import *


class RotationUpdater(Scene):
    def construct(self):
        def updater_forth(mobj, dt):
            mobj.rotate_about_origin(dt)
        # end updater_forth

        def updater_back(mobj, dt):
            mobj.rotate_about_origin(-dt)
        # end updater_back

        # Reference line
        line_reference = Line(ORIGIN, LEFT).set_color(WHITE)
        line_moving = Line(ORIGIN, LEFT).set_color(YELLOW)
        line_moving.add_updater(updater_forth)

        # Add lines and wait 2 seconds
        self.add(line_reference, line_moving)
        self.wait(2)

        # Remove updater and add back one
        line_moving.remove_updater(updater_forth)
        line_moving.add_updater(updater_back)
        self.wait(2)

        # Remove updater
        line_moving.remove_updater(updater_back)
        self.wait(0.5)
    # end construct
# end RotationUpdater

