

from manim import *


class GradientImageFromArray(Scene):
    def construct(self):
        n = 256
        image_array = np.uint8(
            [[i * 256 / n for i in range(0, n)] for _ in range(0, n)]
        )

        image = ImageMobject(image_array).scale(2)
        self.add(image)
        self.wait(1)
    # end construct
# end GradientImageFromArray
