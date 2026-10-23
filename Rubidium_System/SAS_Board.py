import FreeCAD as App

from PyOpticL.beam_path import BeamPath
from PyOpticL.layout import Component
from PyOpticL.library import Baseplate, Sinclair_library as sinclair
from PyOpticL.library.IMAQ_library import (
    cube_05,
    fiberport,
    hwp,
    mirror,
    pd2,
    qwp,
    vapor_cell,
)
from PyOpticL.utils import Dimension as dim
from PyOpticL.utils import cardinal_angle, turn_angle


base_dx = dim(14, "in")
base_dy = dim(8, "in")
base_dz = dim(1, "in")
gap = dim(1 / 8, "in")


mount_holes = [(2.5, 0.5), (3.5, 7.5), (13.5, 0.5), (10.5, 7.5)]

input_x = dim(5, "in")
input_y = dim(6.75, "in")


def sas_baseplate(
    label: str = "SAS Board",
    x: float = 0,
    y: float = 0,
    angle: float = 0,
    thumbscrews: bool = True,
):
    """Build the SAS board; x/y are millimeters and angle is in degrees.

    Returns a Component for recompute() or inclusion in a larger layout.
    Beam wavelength/waist are visualization defaults, not a fitted SAS model.
    """
    baseplate = Component(
        label=label,
        definition=Baseplate(
            dimensions=(base_dx, base_dy, base_dz),
            optical_height=dim(0.5, "in"),
            grid_offset=(gap, gap),
            mount_holes=mount_holes,
        ),
    )
    baseplate.get_object().BasePlacement = App.Placement(
        App.Vector(x, y, 0), App.Rotation(App.Vector(0, 0, 1), angle)
    )

    beam = baseplate.add(
        BeamPath(
            label="SAS Beam",
            wavelength=780.24,
            waist=dim(0.5, "mm"),
            final_distance=dim(5, "in"),
        ),
        position=(input_x, input_y, 0),
        rotation=cardinal_angle["left"],
    )

    baseplate.add(
        fiberport("Input Fiberport", thumbscrews=thumbscrews),
        position=(dim(5.5, "in"), input_y, 0),
        rotation=cardinal_angle["left"],
    )

    beam.add(
        mirror("Input Mirror", thumbscrews=thumbscrews),
        beam_index=0b1,
        x_position=dim(1.75, "in"),
        rotation=turn_angle["up-right"],
    )
    beam.add(
        qwp("Input 1/4 Waveplate"),
        beam_index=0b1,
        distance=dim(1, "in"),
        rotation=cardinal_angle["up"],
    )
    beam.add(
        hwp("Input 1/2 Waveplate"),
        beam_index=0b1,
        distance=dim(1, "in"),
        rotation=cardinal_angle["up"],
    )
    beam.add(
        cube_05("Pump-Probe Splitter"),
        beam_index=0b1,
        distance=dim(1, "in"),
        rotation=cardinal_angle["down"],
    )

    # Transmitted pump branch: down, right, up, then left through the cell.
    beam.add(
        mirror("Pump Mirror 1", thumbscrews=thumbscrews),
        beam_index=0b10,
        distance=dim(2.15, "in"),
        rotation=turn_angle["down-right"],
    )
    beam.add(
        qwp("Pump 1/4 Waveplate"),
        beam_index=0b10,
        distance=dim(3, "in"),
        rotation=cardinal_angle["right"],
    )
    beam.add(
        mirror("Pump Mirror 2", thumbscrews=thumbscrews),
        beam_index=0b10,
        distance=dim(3.5, "in"),
        rotation=turn_angle["down-left"],
    )
    beam.add(
        Component(
            label="Pump-Probe Combiner",
            # Invert only the splitting plane. cube_05_rot() also rotates the
            # mechanical mount, whereas V1 used the standard half-inch mount.
            definition=sinclair.cube_splitter(
                invert=True,
                mount_type=sinclair.cube_mount_halfinch,
            ),
        ),
        beam_index=0b10,
        distance=dim(2.15, "in"),
        rotation=cardinal_angle["right"],
    )

    # Reflected probe branch 0b11 runs right at y=3.75 in. The V2 cell
    # definition has geometry/holders but no optical interface, so it cannot
    # be a BeamPath.add() child. Its center remains 3.25 in after the splitter.
    baseplate.add(
        vapor_cell("Rubidium Vapor Cell"),
        position=(dim(1.75 + 3.25, "in"), dim(3.75, "in"), 0),
        rotation=cardinal_angle["right"],
    )

    # Keep the detection optics at the fixed positions used in V1. The beam
    # tracer intersects these automatically after the pump/probe combiner.
    baseplate.add(
        hwp("Detection 1/2 Waveplate"),
        position=(dim(9.5, "in"), dim(3.75, "in"), 0),
        rotation=cardinal_angle["right"],
    )
    baseplate.add(
        cube_05("Detection Splitter"),
        position=(dim(11, "in"), dim(3.75, "in"), 0),
        rotation=cardinal_angle["right"],
    )
    baseplate.add(
        mirror("Detection Mirror", thumbscrews=thumbscrews),
        position=(dim(11, "in"), dim(5.75, "in"), 0),
        rotation=turn_angle["up-right"],
    )
    # Preserve the balanced-detector body position. The installed pd2 model
    # exposes one central Stop, not the two offset detector input apertures;
    # its mesh/adapter are retained, but ray termination is not modeled fully.
    baseplate.add(
        pd2("PDB250A Balanced Photodetector"),
        position=(dim(12, "in"), dim(4.75, "in"), 0),
        rotation=cardinal_angle["left"],
    )

    return baseplate


if __name__ == "__main__":
    board = sas_baseplate()
    board.recompute()
