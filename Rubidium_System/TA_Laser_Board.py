from PyOpticL.beam_path import BeamPath
from PyOpticL.layout import Component
from PyOpticL.library import Baseplate
from PyOpticL.library.IMAQ_library import (
    aom,
    cube_05,
    fiberport,
    hwp,
    iris,
    isolator2,
    lens_150,
    mirror_u,
    mirror_u_3knob,
    qwp,
    shutter,
    ta,
)
from PyOpticL.utils import Dimension as dim
from PyOpticL.utils import cardinal_angle
from PyOpticL.utils import turn_angle


base_dx = dim(20, "in")
base_dy = dim(11.25, "in")
base_dz = dim(1, "in")
gap = dim(1 / 8, "in")

mount_holes = [
    (1, 1),
    (6, 11),
    (19, 1),
    (19, 11),
]

input_x = dim(2.75, "in")
input_y = dim(7.75, "in")


def ta_laser_baseplate():

    baseplate = Component(
        label="TA Laser Baseplate",
        definition=Baseplate(
            dimensions=(base_dx, base_dy, base_dz),
            optical_height=dim(0.5, "in"),
            grid_offset=(gap, gap),
            mount_holes=mount_holes,
        ),
    )

    # TA
    baseplate.add(
        ta("TA"),
        position=(input_x, input_y, 0),
        rotation=cardinal_angle["down"],
    )

    # Beam diameter = 1 mm -> Gaussian waist radius = 0.5 mm.
    beam = baseplate.add(
        BeamPath(
            label="Beam",
            wavelength=780.24,
            waist=dim(0.5, "mm"),
            final_distance=dim(3, "in"),
        ),
        position=(input_x, input_y, 0),
        rotation=cardinal_angle["down"],
    )

    # TA output mirror
    beam.add(
        mirror_u_3knob("TA Output Mirror"),
        beam_index=0b1,
        distance=dim(2, "in"),
        rotation=turn_angle["down-right"],
    )

    # HWP
    beam.add(
        hwp("Input HWP"),
        beam_index=0b1,
        distance=dim(1, "in"),
        rotation=cardinal_angle["right"],
    )

    # Isolator
    # Use the same orientation as the verified working v2 test board.
    beam.add(
        isolator2("Optical Isolator"),
        beam_index=0b1,
        distance=dim(2.95, "in"),
        rotation=cardinal_angle["right"],
    )

    # QWP
    beam.add(
        qwp("Input QWP"),
        beam_index=0b1,
        distance=dim(2.9, "in"),
        rotation=cardinal_angle["right"],
    )

    # HWP before PBS
    beam.add(
        hwp("PBS HWP"),
        beam_index=0b1,
        distance=dim(1.15, "in"),
        rotation=cardinal_angle["right"],
    )

    # PBS
    beam.add(
        cube_05("PBS"),
        beam_index=0b1,
        distance=dim(1, "in"),
        rotation=cardinal_angle["right"],
    )

    # ------------------------------------------------------------------
    # PBS reflected branch: 0b11
    # ------------------------------------------------------------------

    beam.add(
        mirror_u("Pickoff Mirror"),
        beam_index=0b11,
        distance=dim(3, "in"),
        rotation=turn_angle["up-right"],
    )

    beam.add(
        hwp("Pickoff HWP 1"),
        beam_index=0b11,
        distance=dim(1.25, "in"),
        rotation=cardinal_angle["right"],
    )

    beam.add(
        hwp("Pickoff HWP 2"),
        beam_index=0b11,
        distance=dim(1.25, "in"),
        rotation=cardinal_angle["right"],
    )

    beam.add(
        fiberport(
            "Pickoff Output",
            fiber_clamp="Standard",
            thumbscrews=True,
        ),
        beam_index=0b11,
        distance=dim(2.5, "in"),
        rotation=cardinal_angle["left"],
    )

    # ------------------------------------------------------------------
    # PBS transmitted branch: 0b10
    # ------------------------------------------------------------------

    beam.add(
        lens_150("Collimating Lens 1"),
        beam_index=0b10,
        distance=dim(0.5, "in"),
        rotation=cardinal_angle["left"],
    )

    # 150 mm - 1 in = 124.6 mm
    beam.add(
        mirror_u("AOM Input Mirror"),
        beam_index=0b10,
        distance=dim(124.6, "mm"),
        rotation=turn_angle["up-left"],
    )

    beam.add(
        aom(
            "AOM",
            fiber_clamp="Standard",
            rf_frequencies=0,
        ),
        beam_index=0b10,
        distance=dim(1, "in"),
        rotation=cardinal_angle["up"],
    )

    # AOM input branch is 0b10:
    #   0b100 = zero order
    #   0b101 = first diffracted order

    # First-order branch
    beam.add(
        mirror_u("AOM Output Mirror"),
        beam_index=0b101,
        distance=dim(3, "in"),
        rotation=turn_angle["down-left"],
    )

    # 150 mm - 3 in = 73.8 mm
    beam.add(
        lens_150("Collimating Lens 2"),
        beam_index=0b101,
        distance=dim(73.8, "mm"),
        rotation=cardinal_angle["left"],
    )

    # Zero-order branch
    beam.add(
        iris("Zero-Order Iris"),
        beam_index=0b101,
        distance=dim(27.8, "mm"),
        rotation=cardinal_angle["left"],
    )

    # Same orientation as the verified working v2 AOM test.
    beam.add(
        shutter("Shutter"),
        beam_index=0b101,
        distance=dim(42.05, "mm"),
        rotation=cardinal_angle["left"],
    )

    beam.add(
        hwp("Main Output HWP 1"),
        beam_index=0b101,
        distance=dim(2, "in"),
        rotation=cardinal_angle["left"],
    )



    # Continue first-order branch
    beam.add(
        hwp("Main Output HWP 2"),
        beam_index=0b101,
        distance=dim(1.5, "in"),
        rotation=cardinal_angle["left"],
    )

    beam.add(
        fiberport(
            "Main Output",
            fiber_clamp="Standard",
            thumbscrews=True,
        ),
        beam_index=0b101,
        distance=dim(3, "in"),
        rotation=cardinal_angle["right"],
    )

    return baseplate


if __name__ == "__main__":
    baseplate = ta_laser_baseplate()
    baseplate.recompute()
