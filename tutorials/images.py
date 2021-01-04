
from manimlib.imports import *
import cv2


# Scene Image
class Images(Scene):
    """
    Scene Image
    """

    # Scene construction
    def construct(self):
        """
        Scene construction
        """
        # Load image
        img = cv2.imread("/home/schaetti/Projets/ZUCKER/YouTube/Artificialis Code/Videos/Manim_src/Videos/images/book.jpg")

        # Transform to Manim image object
        im_m_obj = ImageMobject(img)

        # Scale
        im_m_obj.scale(4)

        # Shift image
        #im_m_obj.shift(2 * UP)

        # Display image
        self.play(ShowCreation(im_m_obj))
    # end construct

# end Images
