

from manim import *


# Sine curve unit circle
class SineCurveUnitCircle(Scene):
    """
    Sine curve unit circle
    """

    # Scene construction
    def construct(self):
        """
        Scene construction
        :return:
        """
        self.show_axis()
        self.show_circle()
        self.move_dot_and_draw_curve()
        self.wait()
    # end construct

    # Show axis
    def show_axis(self):
        """
        Show axis
        :return:
        """
        # X start and end
        x_start = np.array([-6, 0, 0])
        x_end = np.array([6, 0, 0])

        # Y start and end
        y_start = np.array([-4, -2, 0])
        y_end = np.array([-4, 2, 0])

        # Create lines for axes
        x_axis = Line(x_start, x_end)
        y_axis = Line(y_start, y_end)

        # Add to scene
        self.add(x_axis, y_axis)
        self.add_x_labels()

        # Origin point and curve starting point
        self.origin_point = np.array([-4, 0, 0])
        self.curve_start = np.array([-3, 0, 0])
    # end show_axis

    # Add x labels
    def add_x_labels(self):
        """
        Add x labels
        :return:
        """
        x_labels = [
            MathTex("\pi"), MathTex("2 \pi"), MathTex("3 \pi"), MathTex("4 \pi")
        ]

        # For each label
        for i in range(len(x_labels)):
            x_labels[i].next_to(np.array([-1 + 2 * i, 0, 0]), DOWN)
            self.add(x_labels[i])
        # end for
    # end add_x_labels

    # Show circle
    def show_circle(self):
        """
        Show circle
        :return:
        """
        # Create a circle
        circle = Circle(radius=1)

        # Move to origin point
        circle.move_to(self.origin_point)

        # Add circle
        self.add(circle)

        self.circle = circle
    # end show_circle

    # Move dot and draw curve
    def move_dot_and_draw_curve(self):
        """
        Move dot and draw curve
        :return:
        """
        # Orbit
        orbit = self.circle
        origin_point = self.origin_point

        # New dot
        dot = Dot(radius=0.08, color=YELLOW)
        dot.move_to(orbit.point_from_proportion(0))
        self.t_offset = 0
        rate = 0.25

        # Go around circle
        def go_around_circle(mob, dt):
            self.t_offset += (dt * rate)
            mob.move_to(orbit.point_from_proportion(self.t_offset % 1))
        # end go_around_circle

        # Get line to circle
        def get_line_to_circle():
            return Line(origin_point, dot.get_center(), color=BLUE)
        # end get_line_to_circle

        # Get line to curve
        def get_line_to_curve():
            x = self.curve_start[0] + self.t_offset * 4
            y = dot.get_center()[1]
            return Line(dot.get_center(), np.array([x, y, 0]), color=YELLOW_A, stroke_width=2)
        # end get_line_to_curve

        # Group
        self.curve = VGroup()
        self.curve.add(Line(self.curve_start, self.curve_start))

        # Get curve
        def get_curve():
            last_line = self.curve[-1]
            x = self.curve_start[0] + self.t_offset * 4
            y = dot.get_center()[1]
            new_line = Line(last_line.get_end(), np.array([x, y, 0]), color=YELLOW_D)
            self.curve.add(new_line)
            return self.curve
        # end get_curve

        # Add updater to dot
        dot.add_updater(go_around_circle)

        # Origin to circle line
        origin_to_circle_line = always_redraw(get_line_to_circle)
        dot_to_curve_line = always_redraw(get_line_to_curve)
        sine_curve_line = always_redraw(get_curve)

        self.add(dot)
        self.add(orbit, origin_to_circle_line, dot_to_curve_line, sine_curve_line)
        self.wait(8.5)

        dot.remove_updater(go_around_circle)
    # end move_dot_and_draw_curve

# end SineCurveUnitCircle
