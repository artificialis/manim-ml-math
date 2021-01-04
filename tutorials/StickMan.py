

from manimlib.imports import *


# StickMan object
class StickMan(SVGMobject):
    """
    StickMan object
    """

    # Configuration
    CONFIG = {
        'color': BLUE_E,
        'stroke_width': 2,
        'stroke_color': WHITE,
        'fill_opacity': 1.0,
        'propagate_style_to_family': True,
        'height': 3,
        'corner_scale_factor': 0.75,
        'flip_at_start': False,
        'is_looking_direction_purposeful': False,
        'start_corner': None,
        'right_arm_range': [0.55, 0.7],
        'left_arm_range': [0.34, 0.462]
    }

    # Constructor
    def __init__(self, mode="plain", **kwargs):
        """
        Constructor
        :param mode:
        :param kwargs:
        """
        # ??
        self.parts_named = False

        # Try
        try:
            # Path to SVG file
            svg_file = os.path.join(
                SVG_IMAGE_DIR,
                "stick_man_{}.svg".format(mode)
            )

            # Create SVGM object
            SVGMobject.__init__(self, file_name=svg_file, **kwargs)
        except:
            # Show warning
            warnings.warn("No StickMan design with mode {}".format(mode))

            # Path to SVG file
            svg_file = os.path.join(
                SVG_IMAGE_DIR,
                "stick_man.svg"
            )


            SVGMobject.__init__(self, file_name=svg_file, **kwargs)
        # end try
