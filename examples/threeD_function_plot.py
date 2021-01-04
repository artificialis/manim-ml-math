

from manim import *


# 3D function plot
class ThreeDFunctionPlot(ThreeDScene):
    """
    3D function plot
    """

    # Scene construction
    def construct(self):
        """
        Scene construction
        :return:
        """
        # Plot resolution
        resolution_fa = 22

        # Set camera orientation
        self.set_camera_orientation(phi=75 * DEGREES, theta=-30 * DEGREES)

        # Plan parameter
        def param_plan(u, v):
            x = u
            y = v
            z = 0
            return np.array([x, y, z])
        # end param_plan

        # Create a plan
        plane = ParametricSurface(
            param_plan,
            resolution=(resolution_fa, resolution_fa),
            v_min=-2,
            v_max=2,
            u_min=-2,
            u_max=2
        )

        # Scale plane
        plane.scale_about_point(2, ORIGIN)

        # Gauss plan parameter
        def param_gauss(u, v):
            """
            Gauss plan parameter
            :param u:
            :param v:
            :return:
            """
            x = u
            y = v
            d = np.sqrt(x * x + y * y)
            sigma, mu = 0.4, 0.0
            z = np.exp(-((d - mu) ** 2 / (2.0 * sigma ** 2)))
            return np.array([x, y, z])
        # end param_gauss

        # Create Gauss plane
        gauss_plane = ParametricSurface(
            param_gauss,
            resolution=(resolution_fa, resolution_fa),
            v_min=-2,
            v_max=2,
            u_min=-2,
            u_max=2
        )

        # Scale Gauss plane and apply style
        gauss_plane.scale_about_point(2, ORIGIN)
        gauss_plane.set_style(fill_opacity=1)
        gauss_plane.set_style(stroke_color=GREEN)
        gauss_plane.set_fill_by_checkerboard(GREEN, BLUE, opacity=0.1)

        # Create 3D axes
        axes = ThreeDAxes()

        # Add axes and planes
        self.add(axes)
        self.play(Write(plane))
        self.play(Transform(plane, gauss_plane))
        self.wait()
    # end construct

# end ThreeDFunctionPlot

