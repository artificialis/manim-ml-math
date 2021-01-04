

from manim import *


class GraphAreaPlot(GraphScene):

    # Constructor
    def __init__(self, **kwargs):
        GraphScene.__init__(
            self,
            x_min=0,
            x_max=5,
            y_min=0,
            y_max=6,
            x_labeled_nums=[0, 2, 3],
            **kwargs
        )
    # end __init__

    # Construct scene
    def construct(self):
        # Set up axes
        self.setup_axes()

        # Two curves
        curve1 = self.get_graph(lambda x: 4 * x - x**2, x_min=0, x_max=4)
        curve2 = self.get_graph(lambda x: 0.8 * x ** 2 - 3 * x + 4, x_min=0, x_max=4)

        # Two lines
        line1 = self.get_vertical_line_to_graph(2, curve1, DashedLine, color=YELLOW)
        line2 = self.get_vertical_line_to_graph(3, curve1, DashedLine, color=YELLOW)

        # Two areas
        area1 = self.get_area(curve1, 0.3, 0.6, dx_scaling=10, area_color=RED)
        # Marche pas
        area2 = self.get_area(curve2, 2, 3, bounded=curve1)

        # Add to scene
        self.add(curve1, curve2, line1, line2, area1, area2)
        self.wait()
    # end construct

# end GraphAreaPlot
