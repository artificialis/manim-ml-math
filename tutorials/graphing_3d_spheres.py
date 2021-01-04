
from manimlib.imports import *
import math


# Artim Scene
class Graphing(GraphScene):
    """
    Artim Scene
    """

    # Configuration
    CONFIG = {
        'x_min': -5,
        'x_max': 5,
        'y_min': -4,
        'y_max': 4,
        'graph_origin': ORIGIN,
        'function_color': WHITE,
        'axes_color': BLUE
    }

    # Scene construction
    def construct(self):
        """
        Scene construction
        :return:
        """
        # Make graph
        self.setup_axes(animate=True)

        # Function graph
        func_graph = self.get_graph(
            self.func_to_graph,
            self.function_color
        )

        # Graph lab
        graph_lab = self.get_graph_label(
            func_graph,
            label="x^{2}"
        )

        # Function graph 2
        func_graph_2 = self.get_graph(
            self.func_to_graph_2,
            self.function_color
        )

        # Graph lab 2
        graph_lab_2 = self.get_graph_label(
            func_graph_2,
            label='x^{3}'
        )

        # Vertical line
        vert_line = self.get_vertical_line_to_graph(
            1,
            func_graph,
            color=YELLOW
        )

        # Two points
        x = self.coords_to_point(1, self.func_to_graph(1))
        y = self.coords_to_point(0, self.func_to_graph(1))

        # Horizontal line
        horz_line = Line(x, y, color=YELLOW)

        # Point
        point = Dot(self.coords_to_point(1, self.func_to_graph(1)))

        # Display graph
        self.play(ShowCreation(func_graph), Write(graph_lab))
        self.wait(1)
        self.play(ShowCreation(vert_line))
        self.play(ShowCreation(horz_line))
        self.add(point)
        self.wait(1)
        self.play(Transform(func_graph, func_graph_2), Transform(graph_lab, graph_lab_2))
        self.wait(2)
    # end construct

    # Function to graph
    def func_to_graph(self, x):
        return(x**2)
    # end func_to_graph

    # Function to graph 2
    def func_to_graph_2(self, x):
        return(x**3)
    # end func_to_graph_2

# end Graphing
