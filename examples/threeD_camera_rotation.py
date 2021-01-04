

from manim import *


# 3D camera rotation
class ThreeDCameraRotation(ThreeDScene):
    """
    3D camera rotation
    """

    # Construct
    def construct(self):
        """
        Construct
        :return:
        """
        # Create axes
        axes = ThreeDAxes()

        # Circle
        circle = Circle()

        # Set camera orientation
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        # Add axes and circle
        self.add(circle, axes)

        # Begin camera rotation and wait 3 seconds
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(3)

        # Stop rotation
        self.stop_ambient_camera_rotation()

        # Back to the beginning
        self.move_camera(phi=75 * DEGREES, theta=30 * DEGREES)

        # Wait
        self.wait()
    # end construct

# end ThreeDCameraRotation
