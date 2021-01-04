

from manim import *


# Graph scene
class HeatDiagramPlot(GraphScene):

    # Constructor
    def __init__(self, **kwargs):
        GraphScene.__init__(
            self,
            y_axis_label=r"T[$^\circ C$]",
            x_axis_label=r"$\Delta Q$",
            y_min=-8,
            y_max=30,
            x_min=0,
            x_max=40,
            y_labeled_nums=np.arange(-5, 34, 5),
            x_labeled_nums=np.arange(0, 40, 5),
            **kwargs
        )
    # end __init__

    # Construct scene
    def construct(self):
        # Data
        data = [20, 0, 0, -5]
        x = [0, 8, 38, 39]

        # Setup axes
        self.setup_axes()

        # Collection of points
        dot_collection = VGroup()

        # For each data point
        for time, val in enumerate(data):
            dot = Dot().move_to(self.coords_to_point(x[time], val))
            self.add(dot)
            dot_collection.add(dot)
        # end for

        # Three lines
        l1 = Line(dot_collection[0].get_center(), dot_collection[1].get_center())
        l2 = Line(dot_collection[1].get_center(), dot_collection[2].get_center())
        l3 = Line(dot_collection[2].get_center(), dot_collection[3].get_center())

        # Add
        self.add(l1, l2, l3)
        self.wait()
    # end construct

# end HeatDiagramPlot
