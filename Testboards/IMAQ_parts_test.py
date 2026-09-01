from PyOpticL.beam_path import BeamPath
from PyOpticL.layout import Component
from PyOpticL.library import Baseplate
from PyOpticL.library.IMAQ_library import *
from PyOpticL.utils import Dimension as dim
from PyOpticL.utils import cardinal_angle, turn_angle

# Baseplate size and mounting hole locations
base_dx = dim(30, "in")
base_dy = dim(12, "in")
base_dz = dim(1, "in")
gap = dim(1 / 8, "in")

mount_holes = [
    (1, 1),
    (29, 1),
    (1, 11),
    (29, 11),
]

input_x = dim(4, "in")
input_y = dim(9, "in")


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

    beam.add(
        isolator1("Isolator 1"),
        beam_index=0b1,
        distance=dim(3, "in"),
        rotation=cardinal_angle["right"],
    )
    beam.add(
        hwp("HWP 1"),
        beam_index=0b1,
        distance=dim(50, "mm"),
        rotation=cardinal_angle["right"],
    )
    beam.add(
        qwp("QWP 1"),
        beam_index=0b1,
        distance=dim(50, "mm"),
        rotation=cardinal_angle["right"],
    )
    beam.add(
        isolator2("Isolator 2"),
        beam_index=0b1,
        distance=dim(100, "mm"),
        rotation=cardinal_angle["right"],
    )
    beam.add(
        lens_50("Lens 50"),
        beam_index=0b1,
        distance=dim(3, "in"),
        rotation=cardinal_angle["left"],
    )
    beam.add(
        lens_50("Lens 50"),
        beam_index=0b1,
        distance=dim(100, "mm"),
        rotation=cardinal_angle["left"],
    )
    beam.add(
        mirror("Mirror1"),
        beam_index=0b1,
        distance=dim(4, "in"),
        rotation=turn_angle["right-down"],
    )
    beam.add(
        mirror("Mirror2"),
        beam_index=0b1,
        distance=dim(5, "in"),
        rotation=turn_angle["down-left"],        
    )
    beam.add(
        iris("Iris"),
        beam_index=0b1,
        distance=dim(1.2, "in"),
        rotation=cardinal_angle["left"],
    )
    beam.add(
        shutter("Shutter"),
        beam_index=0b1,
        distance=dim(1.5, "in"),
        rotation=cardinal_angle["left"],
    )
    beam.add(
        vapor_cell("Vapor Cell"),
        beam_index=0b1,
        distance=dim(5, "in"),
        rotation=cardinal_angle["left"],
    )

    #AOM, BS splits the beam into two branches: ex) 0b1 -> 0b10 and 0b11
    beam.add(
        aom("AOM", fiber_clamp="None"),
        beam_index=0b1,
        distance=dim(6, "in"),
        rotation=cardinal_angle["left"],
    )
    beam.add(
        cube_05("PBS"),
        beam_index=0b11,
        distance=dim(2, "in"),
        rotation=cardinal_angle["left"],
    )
    beam.add(
        fiberport("Fiberport1", fiber_clamp="None"),
        beam_index=0b111,
        distance=dim(2, "in"),
        rotation=cardinal_angle["up"],
    )
    beam.add(
        fiberport("Fiberport2", fiber_clamp="None"),
        beam_index=0b110,
        distance=dim(2, "in"),
        rotation=cardinal_angle["right"],
    )

    return baseplate


if __name__ == "__main__":
    board = testboard()
    board.recompute()
