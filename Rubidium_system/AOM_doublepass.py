from PyOpticL.beam_path import BeamPath
from PyOpticL.layout import Component
from PyOpticL.library import Baseplate
from PyOpticL.library.IMAQ_library import *
from PyOpticL.utils import Dimension as dim
from PyOpticL.utils import cardinal_angle, turn_angle


base_dx = dim(13, "in")
base_dy = dim(5.3, "in")
base_dz = dim(1, "in")
gap = dim(1 / 8, "in")

mount_holes = [
    (0.5, 2.5),
    (12.5, 2.5),
]

input_x = dim(1.7, "in")
input_y = dim(2.2, "in")


def doublepass_f100(
    label: str = "AOM Doublepass",
    x: float = 0,
    y: float = 0,
    angle: float = 0,
    thumbscrews: bool = True,
):
    baseplate = Component(
        label=label,
        definition=Baseplate(
            dimensions=(base_dx, base_dy, base_dz),
            optical_height=dim(0.5, "in"),
            grid_offset=(gap, gap),
            mount_holes=mount_holes,
        ),
    )
    beam = baseplate.add(
        BeamPath(
            label="AOM Doublepass Beam",
            wavelength=780.24,
            waist=dim(0.5, "mm"),
            final_distance=dim(3, "in"),
        ),
        position=(input_x, input_y, 0),
        rotation=cardinal_angle["down"],
    )

    baseplate.add(
        fiberport("Input", fiber_clamp=True),
        position=(input_x, dim(2.5, "in"), 0),
        rotation=cardinal_angle["down"],
    )

    beam.add(
        mirror("Mirror 1"),
        beam_index=0b1,
        distance=dim(0.9, "in"),
        rotation=turn_angle["down-right"],
    )

    beam.add(
        hwp("HWP 1"),
        beam_index=0b1,
        distance=dim(1.1, "in"),
        rotation=cardinal_angle["right"],
    )

    beam.add(
        cube_05_rot("PBS"),
        beam_index=0b1,
        distance=dim(1.3, "in"),
        rotation=cardinal_angle["up"],
    )

    beam.add(
        aom("AOM", fiber_clamp="None"),
        beam_index=0b10,
        distance=dim(1.75, "in"),
        rotation=cardinal_angle["left"],
    )

    beam.add(
        lens_50("Cateye Lens"),
        beam_index=0b101,
        distance=dim(3.5, "in"),
        rotation=cardinal_angle["right"],
    )

    beam.add(
        qwp("QWP"),
        beam_index=0b101,
        distance=dim(20, "mm"),
        rotation=cardinal_angle["left"],
    )

    beam.add(
        iris("Iris"),
        beam_index=0b101,
        distance=dim(20, "mm"),
        rotation=cardinal_angle["left"],
    )

    beam.add(
        mirror("Retro Mirror"),
        beam_index=0b101,
        distance=dim(10, "mm"),
        rotation=cardinal_angle["left"],
    )

    beam.add(
        mirror("Mirror"),
        beam_index=0b11,
        distance=dim(2.5, "in"),
        rotation=turn_angle["up-right"],
    )

    beam.add(
        hwp("HWP 2"),
        beam_index=0b11,
        distance=dim(0.8, "in"),
        rotation=cardinal_angle["left"],
    )

    beam.add(
        qwp("QWP 2"),
        beam_index=0b11,
        distance=dim(1, "in"),
        rotation=cardinal_angle["left"],
    )

    beam.add(
        iris("Iris 2"),
        beam_index=0b11,
        distance=dim(1.75, "in"),
        rotation=cardinal_angle["left"],
    )

    beam.add(
        fiberport("Output Fiberport", fiber_clamp=True),
        beam_index=0b11,
        distance=dim(1.9, "in"),
        rotation=cardinal_angle["left"],
    )



    return baseplate


if __name__ == "__main__":
    board = doublepass_f100()
    board.recompute()