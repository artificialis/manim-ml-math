
from manimlib.imports import *
from math import cos, sin, pi


# Shapes
class Shapes(Scene):
    """
    Shapes
    """

    # Construct scene
    def construct(self):
        """
        Construct scene
        """
        # Make shapes
        circle = Circle(color=YELLOW)
        square = Square(color=DARK_BLUE)
        square.surround(circle)

        # Other shapes
        rectangle = Rectangle(height=2, width=3, color=RED)
        ring = Annulus(inner_radius=2, outer_radius=1, color=BLUE)
        ring2 = Annulus(inner_radius=0.6, outer_radius=1, color=BLUE)
        ring3 = Annulus(inner_radius=0.2, outer_radius=1, color=BLUE)
        ellipse = Ellipse(width=5, height=3, color=DARK_BLUE)

        # Create a list of points
        points = []
        for i in range(8):
            points.append(
                Line(
                    ORIGIN,
                    np.array([cos(pi/180 * 360/8 * i), sin(pi/180 * 360/8 * i), 0]),
                    color=YELLOW
                )
            )
        # end for

        # Add the circle to the scene
        self.add(circle)

        # Show (Fade in) the square
        self.play(FadeIn(square))

        # Transform the square to the rectangle
        self.play(Transform(square, rectangle))

        # Circle disapear (fade out) and the ring appear (fade in)
        self.play(FadeOut(circle), FadeIn(ring))

        # Transform the first ring to the second
        self.play(Transform(ring, ring2))

        # Back to the first
        self.play(Transform(ring2, ring))

        # Remove square, Ellipse grow from center, transform ring 2 to ring 3
        self.play(FadeOut(square), GrowFromCenter(ellipse), Transform(ring2, ring3))

        # Add points
        self.add(*points)

        # Wait 2 seconds
        self.wait(2)
# end Shapes
