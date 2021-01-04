
from manim import *


class BezierSpline(Scene):
    def construct(self):
        np.random.seed(42)

        area = 4

        x1 = np.random.randint(-area, area)
        y1 = np.random.randint(-area, area)
        p1 = np.array([x1, y1, 0])
        destination_dot1 = Dot(point=p1).set_color(BLUE)

        x2 = np.random.randint(-area, area)
        y2 = np.random.randint(-area, area)
        p2 = np.array([x2, y2, 0])
        destination_dot2 = Dot(p2).set_color(RED)

        # Delta
        delta_p = p1 - p2
        delta_p_normalized = delta_p / get_norm(delta_p)

        theta = np.radians(90)

        r = np.array(
            (
                (np.cos(theta), -np.sin(theta), 0),
                (np.sin(theta), np.cos(theta), 0),
                (0, 0, 0)
            )
        )

        senk = r.dot(delta_p_normalized)

        offset = 0.1
        offset_along = 0.5
        offset_connect = 0.25

        dest_line1_point1 = p1 + senk * offset - delta_p_normalized * offset_along
        dest_line1_point2 = p2 + senk * offset + delta_p_normalized * offset_along
        dest_line2_point1 = p1 - senk * offset - delta_p_normalized * offset_along
        dest_line2_point2 = p2 - senk * offset + delta_p_normalized * offset_along

        s1 = p1 - offset_connect * delta_p_normalized
        s2 = p2 + offset_connect * delta_p_normalized

        dest_line1 = Line(dest_line1_point1, dest_line1_point2)
        dest_line2 = Line(dest_line2_point1, dest_line2_point2)

        Lp1s1 = Line(p1, s1)

        # Add bezier curves
        Lp1s1.add_cubic_bezier_curve(
            s1,
            s1 - delta_p_normalized * 0.1,
            dest_line2_point1 + delta_p_normalized * 0.1,
            dest_line2_point1 - delta_p_normalized * 0.01
        )
        Lp1s1.add_cubic_bezier_curve(
            s1,
            s1 - delta_p_normalized * 0.1,
            dest_line1_point1 + delta_p_normalized * 0.1,
            dest_line1_point1
        )

        Lp2s2 = Line(p2, s2)

        Lp2s2.add_cubic_bezier_curve(
            s2,
            s2 + delta_p_normalized * 0.1,
            dest_line2_point2 - delta_p_normalized * 0.1,
            dest_line2_point2
        )
        Lp2s2.add_cubic_bezier_curve(
            s2,
            s2 + delta_p_normalized * 0.1,
            dest_line1_point2 - delta_p_normalized * 0.1,
            dest_line1_point2
        )

        mobjects = VGroup(
            Lp1s1, Lp2s2, dest_line1, dest_line2, destination_dot1, destination_dot2
        )

        mobjects.scale(2)
        self.add(mobjects)
        self.wait(1)
    # end construct
# end BezierSpline
