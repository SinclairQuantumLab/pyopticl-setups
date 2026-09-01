from PyOpticL.beam_path import BeamPath
from PyOpticL.layout import Component
from PyOpticL.library import Baseplate
from PyOpticL.library.IMAQ_library import *
from PyOpticL.utils import Dimension as dim
from PyOpticL.utils import cardinal_angle, turn_angle

# Baseplate size and mounting hole locations
base_dx = dim(14, "in")
base_dy = dim(8, "in")
base_dz = dim(1, "in")
gap = dim(1 / 8, "in")

mount_holes = [
    (3.5, 0.5),
    (0.5, 7.5),
    (12.5, 0.5),
    (13.5, 7.5)
]

input_x = dim(3, "in")
input_y = dim(4, "in")


def baseplate(label: str = "Laserboard"):
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
        position=(dim(3.125, "in"), input_y, 0),
        rotation=cardinal_angle["right"],
    )

    beam.add(
        hwp("HWP1"),
        beam_index=0b1,
        distance=dim(1.25, "in"),
        rotation=cardinal_angle["right"],
    )

    beam.add(
        isolator2("Isolator"),
        beam_index=0b1,
        distance=dim(2.7, "in"),
        rotation=cardinal_angle["right"],
    )

    beam.add(
        qwp("QWP1"),
        beam_index=0b1,
        distance=dim(2.6, "in"),
        rotation=cardinal_angle["right"],
    )

    beam.add(
        hwp("HWP2"),
        beam_index=0b1,
        distance=dim(1.25, "in"),
        rotation=cardinal_angle["right"],
    )

    beam.add(
        cube_05("PBS"),
        beam_index=0b1,
        distance=dim(1, "in"),
        rotation=cardinal_angle["right"],
    )

    beam.add(
        mirror("Mirror1"),
        beam_index=0b11,
        distance=dim(2.25, "in"),
        rotation=turn_angle["up-left"],
    )

    beam.add(
        hwp("HWP3"),
        beam_index=0b11,
        distance=dim(1.75, "in"),
        rotation=cardinal_angle["left"],
    )

    beam.add(
        hwp("HWP4"),
        beam_index=0b11,
        distance=dim(1.25, "in"),
        rotation=cardinal_angle["left"],
    )

    beam.add(
        fiberport("Output1", fiber_clamp="V1"),
        beam_index=0b11,
        distance=dim(2.5, "in"),
        rotation=cardinal_angle["right"],
    )

    ###################

    beam.add(
        mirror_fix("Mirror2"),
        beam_index=0b10,
        distance=dim(0.9, "in"),
        rotation=turn_angle["right-down"],
    )

    beam.add(
        mirror("Mirror3"),
        beam_index=0b10,
        distance=dim(2.25, "in"),
        rotation=turn_angle["down-left"],
    )

    beam.add(
        hwp("HWP5"),
        beam_index=0b10,
        distance=dim(1.75, "in"),
        rotation=cardinal_angle["left"],
    )

    beam.add(
        hwp("HWP6"),
        beam_index=0b10,
        distance=dim(1.25, "in"),
        rotation=cardinal_angle["left"],
    )

    beam.add(
        fiberport("Output2", fiber_clamp=True),
        beam_index=0b10,
        distance=dim(2.5, "in"),
        rotation=cardinal_angle["right"],
    )

    return baseplate


if __name__ == "__main__":
    board = baseplate()
    board.recompute()
