from PyOpticL.beam_path import BeamPath
from PyOpticL.layout import Component
from PyOpticL.library import Baseplate
from PyOpticL.library.IMAQ_library import *
from PyOpticL.utils import Dimension as dim
from PyOpticL.utils import cardinal_angle, turn_angle

# Baseplate size and mounting hole locations
base_dx = dim(11, "in")
base_dy = dim(5.3, "in")
base_dz = dim(1, "in")
gap = dim(1 / 8, "in")

mount_holes = [
    (1, 5),
    (10, 2),
]

input_x = dim(3.7, "in")
input_y = dim(1.3, "in")


def baseplate(label: str = "Singlepass"):
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
        fiberport("Input", fiber_clamp=True),
        position=(dim(3.2, "in"), input_y, 0),
        rotation=cardinal_angle["right"],
    )

    beam.add(
        hwp("HWP"),
        beam_index=0b1,
        distance=dim(1.4, "in"),
        rotation=cardinal_angle["right"],
    )

    beam.add(
        aom("AOM"),
        beam_index=0b1,
        distance=dim(1.1, "in"),
        rotation=cardinal_angle["left"],
    )

    beam.add(
        mirror("Mirror"),
        beam_index=0b11,
        distance=dim(3, "in"),
        rotation=turn_angle["right-up"],
    )

    beam.add(
        mirror("Mirror 2"),
        beam_index=0b11,
        distance=dim(2.5, "in"),
        rotation=turn_angle["up-left"],
    )

    beam.add(
        hwp("HWP 2"),
        beam_index=0b11,
        distance=dim(1, "in"),
        rotation=cardinal_angle["left"],
    )

    beam.add(
        hwp("HWP 3"),
        beam_index=0b11,
        distance=dim(1, "in"),
        rotation=cardinal_angle["left"],
    )

    beam.add(
        iris("Iris"),
        beam_index=0b11,
        distance=dim(1.5, "in"),
        rotation=cardinal_angle["left"],
    )

    beam.add(
        fiberport("Output", fiber_clamp=True),
        beam_index=0b11,
        distance=dim(2.5, "in"),
        rotation=cardinal_angle["right"],
    )


    return baseplate


if __name__ == "__main__":
    board = baseplate()
    board.recompute()
