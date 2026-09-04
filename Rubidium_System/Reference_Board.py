from PyOpticL.beam_path import BeamPath
from PyOpticL.layout import Component
from PyOpticL.library import Baseplate
from PyOpticL.library.IMAQ_library import *
from PyOpticL.utils import Dimension as dim
from PyOpticL.utils import cardinal_angle, turn_angle


base_dx = dim(20, "in")
base_dy = dim(14, "in")
base_dz = dim(1, "in")
gap = dim(1 / 8, "in")

mount_holes = [
    (1, 1),
    (1, 13),
    (19, 1),
    (14, 13),

]

input_y = dim(7, "in")


def reference_baseplate_v2(label: str = "Reference Baseplate"):
    baseplate = Component(
        label=label,
        definition=Baseplate(
            dimensions=(base_dx, base_dy, base_dz),
            optical_height=dim(0.5, "in"),
            grid_offset=(gap, gap),
            mount_holes=mount_holes,
        ),
    )

    # --- reference beam ---
    ref_beam = baseplate.add(
        BeamPath(
            label="Reference Beam",
            wavelength=780.24,
            waist=dim(0.5, "mm"),
            final_distance=dim(5, "in"),
        ),
        position=(dim(3, "in"), input_y, 0),
        rotation=cardinal_angle["right"],
    )

    baseplate.add(
        ips_small("IPS Laser"),
        position=(dim(3.125, "in"), input_y, 0),
        rotation=0,
    )

    ref_beam.add(
        hwp("1/2 Waveplate 1"),
        beam_index=0b1,
        distance=dim(1.25, "in"),
        rotation=cardinal_angle["right"],
    )

    ref_beam.add(
        isolator1("Optical Isolator 1"),
        beam_index=0b1,
        distance=dim(1.375, "in"),
        rotation=cardinal_angle["left"],
    )

    ref_beam.add(
        isolator1("Optical Isolator 2"),
        beam_index=0b1,
        distance=dim(1.875, "in"),
        rotation=cardinal_angle["left"],
    )

    ref_beam.add(
        qwp("1/4 Waveplate"),
        beam_index=0b1,
        distance=dim(1.25, "in"),
        rotation=cardinal_angle["right"],
    )

    ref_beam.add(
        hwp("1/2 Waveplate 2"),
        beam_index=0b1,
        distance=dim(1.0, "in"),
        rotation=cardinal_angle["right"],
    )

    ref_beam.add(
        cube_05("Beam Splitter Cube"),
        beam_index=0b1,
        distance=dim(1.0, "in"),
        rotation=cardinal_angle["right"],
    )

    # reflected branch 0b11
    ref_beam.add(
        mirror("Shared Mirror"),
        beam_index=0b11,
        distance=dim(2.75, "in"),
        rotation=turn_angle["up-left"],
    )

    ref_beam.add(
        hwp("1/2 Waveplate 3"),
        beam_index=0b11,
        distance=dim(2.0, "in"),
        rotation=cardinal_angle["left"],
    )

    ref_beam.add(
        hwp("1/2 Waveplate 4"),
        beam_index=0b11,
        distance=dim(1.25, "in"),
        rotation=cardinal_angle["left"],
    )

    ref_beam.add(
        fiberport(
            "MOT Output Fiberport",
            fiber_clamp="V1",
            thumbscrews=True,
        ),
        beam_index=0b11,
        distance=dim(3.5, "in"),
        rotation=cardinal_angle["right"],
    )

    # transmitted branch 0b10
    ref_beam.add(
        hwp("1/2 Waveplate 5"),
        beam_index=0b10,
        distance=dim(2.125, "in"),
        rotation=cardinal_angle["right"],
    )

    ref_beam.add(
        cube_05("Beam Splitter Cube 2"),
        beam_index=0b10,
        distance=dim(1.0, "in"),
        rotation=cardinal_angle["right"],
    )

    ref_beam.add(
        hwp("1/2 Waveplate 6"),
        beam_index=0b100,
        distance=dim(2.125, "in"),
        rotation=cardinal_angle["right"],
    )

    ref_beam.add(
        cube_05("Beam Splitter Cube 3"),
        beam_index=0b100,
        distance=dim(1.0, "in"),
        rotation=cardinal_angle["right"],
    )

    ref_beam.add(
        mirror("Mirror 4"),
        beam_index=0b1000,
        distance=dim(1.4, "in"),
        rotation=turn_angle["down-left"],
    )

    ref_beam.add(
        hwp("1/2 Waveplate 7"),
        beam_index=0b1000,
        distance=dim(1.0, "in"),
        rotation=cardinal_angle["up"],
    )

    ref_beam.add(
        fiberport("Output1",fiber_clamp="V1",thumbscrews=True,),
        beam_index=0b1000,
        distance=dim(3.0, "in") - dim(5.136, "mm"),
        rotation=cardinal_angle["down"],
    )

    # --- MOT beam ---
    mot_beam = baseplate.add(
        BeamPath(
            label="MOT Beam",
            wavelength=780.24,
            waist=dim(0.5, "mm"),
            final_distance=dim(5, "in"),
        ),
        position=(dim(7.5, "in"), dim(4.5, "in"), 0),
        rotation=cardinal_angle["right"],
    )

    baseplate.add(
        fiberport(
            "MOT Input Fiberport",
            fiber_clamp="V1",
            thumbscrews="None",
        ),
        position=(dim(7.0, "in"), dim(4.5, "in"), 0),
        rotation=cardinal_angle["right"],
    )

    mot_beam.add(
        mirror("MOT Mirror"),
        beam_index=0b1,
        distance=dim(3.25, "in"),
        rotation=turn_angle["down-left"],
    )

    mot_beam.add(
        hwp("MOT Waveplate"),
        beam_index=0b1,
        distance=dim(0.75, "in"),
        rotation=cardinal_angle["up"],
    )

    # --- repump beam ---
    repump_beam = baseplate.add(
        BeamPath(
            label="Repump Beam",
            wavelength=780.24,
            waist=dim(0.5, "mm"),
            final_distance=dim(5, "in"),
        ),
        position=(dim(6.5, "in"), dim(3.0, "in"), 0),
        rotation=cardinal_angle["right"],
    )

    baseplate.add(
        fiberport(
            "Repumper Input Fiberport",
            fiber_clamp="V1",
            thumbscrews="None",
        ),
        position=(dim(6.0, "in"), dim(3.0, "in"), 0),
        rotation=cardinal_angle["right"],
    )

    repump_beam.add(
        mirror("Repump Mirror"),
        beam_index=0b1,
        distance=dim(7.375, "in"),
        rotation=turn_angle["down-left"],
    )

    repump_beam.add(
        hwp("Repump Waveplate"),
        beam_index=0b1,
        distance=dim(1.375, "in"),
        rotation=cardinal_angle["up"],
    )

    ref_beam.add(
        mirror("Shared Mirror 2"),
        beam_index=0b101,
        distance=dim(4.25, "in"),
        rotation=turn_angle["up-left"],
    )

    ref_beam.add(
        hwp("1/2 Waveplate 8"),
        beam_index=0b101,
        distance=dim(1.2, "in"),
        rotation=cardinal_angle["left"],
    )

    ref_beam.add(
        hwp("1/2 Waveplate 9"),
        beam_index=0b101,
        distance=dim(3.0, "in"),
        rotation=cardinal_angle["left"],
    )

    ref_beam.add(
        fiberport(
            "Repumper Output Fiberport",
            fiber_clamp="V1",
            thumbscrews=True,
        ),
        beam_index=0b101,
        distance=dim(3.5, "in"),
        rotation=cardinal_angle["right"],
    )

    # --- spare beam ---
    spare_beam = baseplate.add(
        BeamPath(
            label="Spare Beam",
            wavelength=780.24,
            waist=dim(0.5, "mm"),
            final_distance=dim(5, "in"),
        ),
        position=(dim(5.5, "in"), dim(1.5, "in"), 0),
        rotation=cardinal_angle["right"],
    )

    baseplate.add(
        fiberport(
            "Spare Input Fiberport",
            fiber_clamp="V1",
            thumbscrews=True,
        ),
        position=(dim(5.0, "in"), dim(1.5, "in"), 0),
        rotation=cardinal_angle["right"],
    )

    spare_beam.add(
        mirror("Spare Mirror"),
        beam_index=0b1,
        distance=dim(11.5, "in"),
        rotation=turn_angle["down-left"],
    )

    spare_beam.add(
        hwp("Spare Waveplate"),
        beam_index=0b1,
        distance=dim(1.375, "in"),
        rotation=cardinal_angle["up"],
    )

    ref_beam.add(
        mirror("Shared Mirror 3"),
        beam_index=0b1001,
        distance=dim(5.75, "in"),
        rotation=turn_angle["up-left"],
    )

    ref_beam.add(
        hwp("1/2 Waveplate 10"),
        beam_index=0b1001,
        distance=dim(1.2, "in"),
        rotation=cardinal_angle["left"],
    )

    ref_beam.add(
        hwp("1/2 Waveplate 11"),
        beam_index=0b1001,
        distance=dim(4.5, "in"),
        rotation=cardinal_angle["left"],
    )

    ref_beam.add(
        fiberport(
            "Spare Output Fiberport",
            fiber_clamp="V1",
            thumbscrews=True,
        ),
        beam_index=0b1001,
        distance=dim(3.0, "in"),
        rotation=cardinal_angle["right"],
    )

    return baseplate


if __name__ == "__main__":
    board = reference_baseplate_v2()
    board.recompute()
