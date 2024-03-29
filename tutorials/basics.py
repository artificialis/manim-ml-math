
from manimlib.imports import *


class Shapes(Scene):

    # Construct the scene
    def construct(self):
        """
        Construct the scene
        :return:
        """
        circle = Circle()
        square = Square()
        triangle = Polygon(
            np.array([0, 0, 0]),
            np.array([1, 1, 0]),
            np.array([1, -1, 0])
        )

        # Showing shapes
        self.wait(3)
        self.play(ShowCreation(circle))
        self.play(FadeOut(circle))
        self.play(GrowFromCenter(square))
        self.play(Transform(square, triangle))
        self.play(FadeOut(triangle))
        self.wait(3)
    # end construct

# end Shapes
