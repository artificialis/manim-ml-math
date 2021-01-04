

from manim import *


class ThreeDCameraIllusionRotation(ThreeDScene):
    """
    3D Camera illusion rotation
    """

    # Scene construction
    def construct(self):
        """
        Scene construction
        :return:
        """
        # Create 3D axes
        axes = ThreeDAxes()

        # Circle
        circle = Circle()

        # Set camera orientation
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        # Add circle and axes
        self.add(circle, axes)

        # Begin 3D illusion camera rotation
        self.begin_3dillusion_camera_rotation(rate=2)

        # Wait
        self.wait(PI)

        # Stop rotation
        self.stop_3dillusion_camera_rotation()
    # end construct

# end ThreeDCameraIllusionRotation
