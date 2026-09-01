from PyOpticL.beam_path import BeamPath
from PyOpticL.layout import Component
from PyOpticL.library import Baseplate
from PyOpticL.library.IMAQ_library import *
from PyOpticL.utils import Dimension as dim
from PyOpticL.utils import cardinal_angle, turn_angle

# Baseplate size and mounting hole locations
base_dx = dim(20, "in")
base_dy = dim(8, "in")
base_dz = dim(1, "in")
gap = dim(1 / 8, "in")

mount_holes = [
    (1, 1),
    (1, base_dy - dim(1, "in")),
    (base_dx - dim(1, "in"), 1),
    (base_dx - dim(1, "in"), base_dy - dim(1, "in")),
]

input_x = dim(5, "in")
input_y = dim(5, "in")


def testboard(label: str = "Testboard"):
    baseplate = Component(
        label=label,
        definition=Baseplate(
            dimensions=(base_dx, base_dy, base_dz),
            optical_height=dim(0.5, "in"),
            grid_offset=(gap, gap),
            mount_holes=mount_holes,
        ),
    )

    #Add a beam
    beam = baseplate.add(
        BeamPath(
            label="beam",
            wavelength=780.24,
            waist=dim(0.5, "mm"),
            final_distance=dim(12, "in"),
        ),
        position=(input_x, input_y, 0),
        rotation=cardinal_angle["right"],
    )

    # Laser input
    baseplate.add(
        ips_small("Laser"),
        position=(input_x, input_y, 0),
        rotation=cardinal_angle["right"],
    )

    return baseplate


if __name__ == "__main__":
    board = testboard()
    board.recompute()
