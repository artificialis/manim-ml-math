
from manimlib.imports import *


# 3D surface
class ThreeDSurface(ParametricSurface):
    """
    Surface parametric 3D
    """

    # Constructor
    def __init__(self, **kwargs):
        """
        Constructor
        :param kwargs: Arguments
        """
        kwargs = {
            'u_min': -2,
            'u_max': 2,
            'v_min': -2,
            'v_max': 2,
            'checkerboard_colors': [BLUE_D]
        }
        ParametricSurface.__init__(self, self.func, **kwargs)
    # end __init__

    # Function
    def func(self, x, y):
        """
        Function
        :param x:
        :param y:
        :return:
        """
        return np.array([x, y, x**2 - y**2])
    # end func

# end ThreeDSurface


# Test
class Test(ThreeDScene):
    """
    Test
    """

    # Scene construction
    def construct(self):
        """
        Scene construction
        :return:
        """
        # Camera orientation
        self.set_camera_orientation(0.6, -0.7853981, 86.6)

        # Surface 3D
        surface = ThreeDSurface()
        self.play(ShowCreation(surface))

        # Show a dot
        d = Dot(np.array([0, 0, 0]), color=YELLOW)
        self.play(ShowCreation(d))

        # Play
        self.wait()
        self.move_camera(0.8 * np.pi / 2, -0.45 * np.pi)
        self.begin_ambient_camera_rotation()
        self.wait(9)
    # end constructor

# end Test
