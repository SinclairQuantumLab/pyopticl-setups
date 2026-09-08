from PyOpticL.beam_path import BeamPath
from PyOpticL.layout import Component
from PyOpticL.library import Baseplate
from PyOpticL.library import optics
from PyOpticL.library.optics import micro_lens
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
]

input_x = dim(100, "mm")
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
            waist=dim(1.25, "in"),
            final_distance=dim(12, "in"),
        ),
        position=(input_x, input_y, dim(1, "in")),
        rotation=cardinal_angle["right"],
    )


    beam.add(
        Component(
            label="Cavity1",
            definition=optics.Cavity_Mirror(
                diameter=dim(3, "in"),
                ref_ratio=0.99,
                input=True,
            ),
        ),
        beam_index=0b1,
        distance=dim(50, "mm"),
        rotation=cardinal_angle["right"],
    )


    baseplate.add(
        Component(
            label="Micro lens f=50 mm",
            definition=micro_lens(
                focal_length=dim(50, "mm"),
                part_number="micro_lens f=50 mm",
            ),
        ),
        position=(dim(250, "mm"), dim(5, "in"), dim(1, "in")),
        rotation=cardinal_angle["right"],
    )

    baseplate.add(
        Component(
            label="Micro lens f=50 mm",
            definition=micro_lens(
                focal_length=dim(50, "mm"),
                part_number="micro_lens f=50 mm",
            ),
        ),
        position=(dim(250, "mm"), dim(4.5, "in"), dim(1, "in")),
        rotation=cardinal_angle["right"],
    )

    baseplate.add(
        Component(
            label="Micro lens f=50 mm",
            definition=micro_lens(
                focal_length=dim(50, "mm"),
                part_number="micro_lens f=50 mm",
            ),
        ),
        position=(dim(250, "mm"), dim(5.5, "in"), dim(1, "in")),
        rotation=cardinal_angle["right"],
    )

    baseplate.add(
        Component(
            label="Micro lens f=50 mm",
            definition=micro_lens(
                focal_length=dim(50, "mm"),
                part_number="micro_lens f=50 mm",
            ),
        ),
        position=(dim(250, "mm"), dim(4, "in"), dim(1, "in")),
        rotation=cardinal_angle["right"],
    )

    baseplate.add(
        Component(
            label="Micro lens f=50 mm",
            definition=micro_lens(
                focal_length=dim(50, "mm"),
                part_number="micro_lens f=50 mm",
            ),
        ),
        position=(dim(250, "mm"), dim(6, "in"), dim(1, "in")),
        rotation=cardinal_angle["right"],
    )



    baseplate.add(
        Component(
            label="Cavity2",
            definition=optics.Cavity_Mirror(
                diameter=dim(3, "in"),
                ref_ratio=0.99,
                input=False,
            ),
        ),
        position=(dim(300, "mm"), dim(5, "in"), dim(1, "in")),
        rotation=cardinal_angle["left"],
    )






    baseplate.add(
        Component(
            label="Micro lens f=50 mm",
            definition=micro_lens(
                focal_length=dim(50, "mm"),
                part_number="micro_lens f=50 mm",
            ),
        ),
        position=(dim(350, "mm"), dim(5, "in"), dim(1, "in")),
        rotation=cardinal_angle["right"],
    )

    baseplate.add(
        Component(
            label="Micro lens f=50 mm",
            definition=micro_lens(
                focal_length=dim(50, "mm"),
                part_number="micro_lens f=50 mm",
            ),
        ),
        position=(dim(350, "mm"), dim(4.5, "in"), dim(1, "in")),
        rotation=cardinal_angle["right"],
    )

    baseplate.add(
        Component(
            label="Micro lens f=50 mm",
            definition=micro_lens(
                focal_length=dim(50, "mm"),
                part_number="micro_lens f=50 mm",
            ),
        ),
        position=(dim(350, "mm"), dim(5.5, "in"), dim(1, "in")),
        rotation=cardinal_angle["right"],
    )

    baseplate.add(
        Component(
            label="Micro lens f=50 mm",
            definition=micro_lens(
                focal_length=dim(50, "mm"),
                part_number="micro_lens f=50 mm",
            ),
        ),
        position=(dim(350, "mm"), dim(4, "in"), dim(1, "in")),
        rotation=cardinal_angle["right"],
    )

    baseplate.add(
        Component(
            label="Micro lens f=50 mm",
            definition=micro_lens(
                focal_length=dim(50, "mm"),
                part_number="micro_lens f=50 mm",
            ),
        ),
        position=(dim(350, "mm"), dim(6, "in"), dim(1, "in")),
        rotation=cardinal_angle["right"],
    )



    return baseplate


if __name__ == "__main__":
    board = testboard()
    board.recompute()
