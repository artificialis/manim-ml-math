

from manim import *


# Moving zoomed scene around
class MovingZoomedSceneAround(ZoomedScene):
    """
    Moving zoomed scene around
    """

    # Constructor
    def __init__(self, **kwargs):
        """
        Constructor
        :param kwargs:
        """
        ZoomedScene.__init__(
            self,
            zoom_factor=0.3,
            zoomed_display_height=1,
            zoomed_display_width=6,
            image_frame_stroke_width=20,
            zoomed_camera_config={
                "default_frame_stroke_width": 3
            },
            **kwargs
        )
    # end __init__

    # Construct
    def construct(self):
        """
        Construct
        :return:
        """
        # Dot
        dot = Dot().shift(UL * 2)

        # A new image
        image = ImageMobject(np.uint8([[0, 100, 30, 200], [255, 0, 5, 33]]))
        image.set_height(7)

        # New text "Frame"
        frame_text = Text("Frame", color=PURPLE).scale(1.4)

        # Zoomed camera text
        zoomed_camera_text = Text("Zoomed camera", color=RED).scale(1.4)

        # Add image and dot
        self.add(image, dot)

        # Zoomed camera and display
        zoomed_camera = self.zoomed_camera
        zoomed_display = self.zoomed_display

        # ??
        frame = zoomed_camera.frame
        zoomed_display_frame = zoomed_display.display_frame

        # Move zoomed camera to dot
        frame.move_to(dot)
        frame.set_color(PURPLE)
        zoomed_display_frame.set_color(RED)
        zoomed_display.shift(DOWN)

        # Zoomed rectangle
        zd_rect = BackgroundRectangle(zoomed_display, fill_opacity=0, buff=MED_SMALL_BUFF)
        self.add_foreground_mobject(zd_rect)

        # Unfold camera
        unfold_camera = UpdateFromFunc(zd_rect, lambda rect: rect.replace(zoomed_display))

        # Move "Frame" text
        frame_text.next_to(frame, DOWN)

        # Show frame and text
        self.play(ShowCreation(frame), FadeInFrom(frame_text, direction=DOWN))
        self.activate_zooming()

        # ??
        self.play(self.get_zoomed_display_pop_out_animation(), unfold_camera)
        zoomed_camera_text.next_to(zoomed_display_frame, DOWN)
        self.play(FadeInFrom(zoomed_camera_text, direction=DOWN))

        scale_factor = [0.5, 1.5, 0]
        self.play(
            frame.animate.scale(scale_factor),
            zoomed_display.animate.scale(scale_factor),
            FadeOut(zoomed_camera_text),
            FadeOut(frame_text)
        )
        self.wait()

        # ??
        self.play(ScaleInPlace(zoomed_display, 2))
        self.wait()

        # ??
        self.play(frame.animate.shift(2.5 * DOWN))
        self.wait()

        # ??
        self.play(self.get_zoomed_display_pop_out_animation(), unfold_camera, rate_func=lambda t: smooth(1 - t))
        self.play(Uncreate(zoomed_display_frame), FadeOut(frame))
        self.wait()
