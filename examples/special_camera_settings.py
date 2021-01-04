

from manim import *


# Scene
class FollowingGraphCamera(GraphScene, MovingCameraScene):
    """
    Scene
    """

    # Setup scene
    def setup(self):
        """
        Setup scene
        :return:
        """
        GraphScene.setup(self)
        MovingCameraScene.setup(self)
    # end setup

    # Construct
    def construct(self):
        """
        Construct
        :return:
        """
        # Save camera position
        self.camera_frame.save_state()

        # Setup axes (without animation)
        self.setup_axes(animate=False)

        # Create the graph
        graph = self.get_graph(
            lambda x: np.sin(x),
            color=BLUE,
            x_min=0,
            x_max=3 * PI
        )

        # Create the dot
        moving_dot = Dot().move_to(graph.points[0]).set_color(ORANGE)

        # Dots at start and end of the graph
        dot_at_start_graph = Dot().move_to(graph.points[0])
        dot_at_end_graph = Dot().move_to(graph.points[-1])

        # Add objects
        self.add(graph, dot_at_end_graph, dot_at_start_graph, moving_dot)

        # Play and animate camera
        self.play(self.camera_frame.animate.scale(0.5).move_to(moving_dot))

        # Move camera with moving dot
        def update_curve(mob):
            mob.move_to(moving_dot.get_center())
        # end update_curve

        # Add updater to camera
        self.camera_frame.add_updater(update_curve)

        # Play dot moving along path
        self.play(MoveAlongPath(moving_dot, graph, rate_func=linear))
        self.camera_frame.remove_updater(update_curve)

        # Back to origin point
        self.play(Restore(self.camera_frame))
    # end construct

# end FollowingGraphCamera