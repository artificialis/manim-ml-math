

from manim import *


# 3D light source position
class ThreeDLightSourcePosition(ThreeDScene):
    """
    3D light source position
    """

    # Construction
    def construct(self):
        """
        Construction
        :return:
        """
        # Axes
        axes = ThreeDAxes()

        # Add a sphere
        sphere = ParametricSurface(
            lambda u, v: np.array([
                1.5 * np.cos(u) * np.cos(v),
                1.5 * np.cos(u) * np.sin(v),
                1.5 * np.sin(u)
            ]),
            v_min=0,
            v_max=TAU,
            u_min=-PI / 2.0,
            u_max=PI / 2.0,
            checkerboard_colors=[RED_D, RED_E],
            resolution=(15, 32)
        )

        # Change the source of the light
        self.renderer.camera.light_source.move_to(3 * IN)

        # Set camera orientation
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        # Add axes and sphere
        self.add(axes, sphere)
        self.wait()
    # end construct

# end ThreeDLightSourcePosition
