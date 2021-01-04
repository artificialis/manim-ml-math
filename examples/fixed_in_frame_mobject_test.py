

from manim import *


# Fixed in frame
class FixedInFrameMObjectTest(ThreeDScene):
    """
    Fixed in frame mobject test
    """

    # Construct scene
    def construct(self):
        """
        Construct scene
        :return:
        """
        # 3D axes
        axes = ThreeDAxes()

        # Set camera orientation
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)

        # Text 3D
        text3d = Text("This is a 3D text")

        # ??
        self.add_fixed_in_frame_mobjects(text3d)

        # Put to corner
        text3d.to_corner(UL)

        # Add and wait
        self.add(axes)
        self.wait()
    # end contruct

# end FixedInFrameMObjectTest
