

from manim import *


# Opening Manim
class OpeningManim(Scene):
    """
    Opening Manim
    """

    # Scene construction
    def construct(self):
        """
        Scene construction
        :return:
        """
        # Title
        title = Tex(r"This is some \LaTeX")

        # Basel
        basel = MathTex(r"\sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}")

        # Title and based in group
        VGroup(title, basel).arrange(DOWN)

        # Write title and fade in based
        self.play(Write(title), FadeInFrom(basel, UP))
        self.wait()

        # Transformed title and put it to corner
        transform_title = Tex("That was a transform")
        transform_title.to_corner(UP + LEFT)

        # Transform title
        self.play(
            Transform(title, transform_title),
            LaggedStart(*[FadeOutAndShift(obj, direction=DOWN) for obj in basel])
        )
        self.wait()

        # Grid
        grid = NumberPlane()
        grid_title = Tex("This is a grid")
        grid_title.scale(1.5)
        grid_title.move_to(transform_title)

        # Add and play
        self.add(grid, grid_title)
        self.play(
            FadeOut(title),
            FadeInFrom(grid_title, direction=DOWN),
            ShowCreation(grid, run_time=3, lag_ratio=0.1)
        )
        self.wait()

        # Grid transform title
        grid_transform_title = Tex(
            r"That was a non-linear function \\ applied to the grid"
        )
        grid_transform_title.move_to(grid_title, UL)
        grid.prepare_for_nonlinear_transform()

        # Play
        self.play(
            grid.animate.apply_function(
                lambda p: p + np.array([
                    np.sin(p[1]),
                    np.sin(p[0]),
                    0
                ])
            ),
            run_time=3
        )

        # Wait
        self.wait()

        # Transform title (again)
        self.play(Transform(grid_title, grid_transform_title))
        self.wait()
    # end construct

# end OpeningManim
