

from manim import *


# Graph Scene
class SinAndCosFunctionPlot(GraphScene):

    # Constructor
    def __init__(self, **kwargs):
        GraphScene.__init__(
            self,
            x_min=-10,
            x_max=10.3,
            num_graph_anchor_points=100,
            y_min=-1.5,
            y_max=1.5,
            graph_origin=ORIGIN,
            axes_color=GREEN,
            x_labeled_nums=range(-10, 12, 2),
            **kwargs
        )
        self.function_color = RED
    # end __init__

    # Construct scene
    def construct(self):
        # Setup the axes, without animation
        self.setup_axes(animate=False)

        # First function to plot
        func_graph = self.get_graph(np.cos, self.function_color)

        # Second function to plot
        func_graph2 = self.get_graph(np.sin)

        # Vertical line
        vert_line = self.get_vertical_line_to_graph(TAU, func_graph, color=YELLOW)

        # Graph labels
        graph_lab = self.get_graph_label(func_graph, label="\\cos(x)")
        graph_lab2 = self.get_graph_label(func_graph2, label="\\sin(x)", x_val=-10, direction=UP / 2.0)

        # 2pi in text
        two_pi = MathTex(r"x = 2 \pi")

        # Label coord
        label_coord = self.input_to_graph_point(TAU, func_graph)

        # Position "x = 2pi"
        two_pi.next_to(label_coord, RIGHT + UP)

        # Add to scene
        self.add(func_graph, func_graph2, vert_line, graph_lab, graph_lab2, two_pi)
        self.wait()
    # end construct

# end SinAndCosFunctionPlot

