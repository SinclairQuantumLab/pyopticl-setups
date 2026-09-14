from importlib import reload
from math import sqrt

import FreeCAD as App

from PyOpticL.beam_path import BeamPath
from PyOpticL.layout import Component
from PyOpticL.library import Baseplate
from PyOpticL.library import Sinclair_library as sinclair
from PyOpticL.utils import Dimension as dim

reload(sinclair)


baseplate = Component(
    label="780 nm pMOT Test",
    definition=Baseplate(
        dimensions=(
            dim(19, "in"),
            dim(17, "in"),
            dim(1, "in"),
        ),
        optical_height=dim(46.718, "mm"),
    ),
)


# Beam 1: horizontal path at -45 degrees.


beam780_1 = baseplate.add(
    BeamPath(
        label="780.24 nm Beam 1",
        wavelength=780.24,
        waist=dim(6.35, "mm"),
        final_distance=dim(5, "in"),
    ),
    position=(
        dim(1, "in"),
        dim(18, "in"),
        dim(44.3335, "mm"),
    ),
    rotation=-45,
)


beam780_1.add(
    Component(
        label="780.24 nm - 80 mm Lens 1",
        definition=sinclair.pmot_lens_80(),
    ),
    beam_index=0b1,
    distance=dim(70.405, "mm"),
    rotation=-45,
)


# Preserve the original first-lens position after the diagonal start shift.
# Distance from the existing 780 nm lens: approximately 160 mm.


beam780_1.add(
    Component(
        label="80 mm Lens 1",
        definition=sinclair.pmot_lens_80(),
    ),
    beam_index=0b1,
    distance=dim(5, "in") * sqrt(2) + dim(2, "in") - dim(70.405, "mm"),
    rotation=-45,
)


cell_definition = sinclair.pmot_glass_cell()

cell_definition.mesh = cell_definition.mesh.copy()

cell_definition.mesh.transform(
    App.Rotation("XYZ", 0, 0, 0).toMatrix()
)

glass_cell = beam780_1.add(
    Component(
        label="pMOT Glass Cell",
        definition=cell_definition,
    ),
    beam_index=0b1,
    distance=dim(89.896, "mm"),
    rotation=0,
)


# Keep the MOT coil at the glass cell's position and orientation.
mot_coil = glass_cell.add(
    Component(
        label="MOT Coil",
        definition=sinclair.mot_coil(),
    ),
    position=(0, 0, 0),
    rotation=(0, 0, 0),
)


beam780_1.add(
    Component(
        label="80 mm Lens 2",
        definition=sinclair.pmot_lens_80(),
    ),
    beam_index=0b1,
    distance=dim(79.670, "mm"),
    rotation=135,
)


beam780_1.add(
    Component(
        label="Retro Mirror",
        definition=sinclair.circular_mirror(
            diameter=dim(2, "in"),
            thickness=dim(6, "mm"),
            part_number="KA2T test mirror",
            mount_type=sinclair.mirror_mount_KA2T,
        ),
    ),
    beam_index=0b1,
    distance=dim(87.141, "mm"),
    rotation=135,
)


# Beam 2: horizontal path at -135 degrees.


beam780_2 = baseplate.add(
    BeamPath(
        label="780.24 nm Beam 2",
        wavelength=780.24,
        waist=dim(6.35, "mm"),
        final_distance=dim(5, "in"),
    ),
    position=(
        dim(18.83363, "in"),
        dim(18, "in"),
        dim(44.3335, "mm"),
    ),
    rotation=-135,
)


beam780_2.add(
    Component(
        label="780.24 nm - 80 mm Lens 1",
        definition=sinclair.pmot_lens_80(),
    ),
    beam_index=0b1,
    distance=dim(70.405, "mm"),
    rotation=-135,
)


# Apply the same diagonal start-shift correction as Beam 1.


beam780_2.add(
    Component(
        label="Beam 2 - 80 mm Lens 1",
        definition=sinclair.pmot_lens_80(),
    ),
    beam_index=0b1,
    distance=dim(5, "in") * sqrt(2) + dim(2, "in") - dim(70.405, "mm"),
    rotation=-135,
)


# Place the second lens 79.670 mm after the shared glass cell.


beam780_2.add(
    Component(
        label="Beam 2 - 80 mm Lens 2",
        definition=sinclair.pmot_lens_80(),
    ),
    beam_index=0b1,
    distance=dim(79.670, "mm"),
    after_object=glass_cell,
    rotation=45,
)


beam780_2.add(
    Component(
        label="Beam 2 - Retro Mirror",
        definition=sinclair.circular_mirror(
            diameter=dim(2, "in"),
            thickness=dim(6, "mm"),
            part_number="KA2T test mirror",
            mount_type=sinclair.mirror_mount_KA2T,
        ),
    ),
    beam_index=0b1,
    distance=dim(87.141, "mm"),
    rotation=45,
)


# Beam 3: enter along -X, then turn upward at CCM1-P01.


beam780_3 = baseplate.add(
    BeamPath(
        label="780.24 nm Beam 3",
        wavelength=780.24,
        waist=dim(6.35, "mm"),
        final_distance=dim(5, "in"),
    ),
    position=(
        dim(13.916815, "in"),
        dim(9.083185, "in"),
        dim(-27.668, "mm"),
    ),
    rotation=180,
)


beam780_3.add(
    Component(
        label="780.24 nm - AC254-040-C-ML 1",
        definition=sinclair.mounted_lens_AC254_040_C_ML(),
    ),
    beam_index=0b1,
    distance=dim(30.65, "mm"),
    rotation=(0, 0, 180),
)


# Preserve the turning-mirror position: 4 in from the new start,
# minus the 30.65 mm to the existing 780 nm lens (70.95 mm).


beam780_3.add(
    Component(
        label="CCM1-P01",
        definition=sinclair.mirror_cube_ccm1_p01(),
    ),
    beam_index=0b1,
    distance=dim(4, "in") - dim(30.65, "mm"),
    rotation=(0, 0, 180),
)


beam780_3.add(
    Component(
        label="Beam 3 - AC254-040-C-ML 1",
        definition=sinclair.mounted_lens_AC254_040_C_ML(),
    ),
    beam_index=0b1,
    distance=dim(19.05, "mm"),
    rotation=(0, -90, 0),
)


beam780_3.add(
    Component(
        label="Beam 3 - AC254-040-C-ML 2",
        definition=sinclair.mounted_lens_AC254_040_C_ML(),
    ),
    beam_index=0b1,
    distance=dim(94.513, "mm"),
    rotation=(0, 90, 0),
)


beam780_3.add(
    Component(
        label="Beam 3 - KA1 Retro Mirror",
        definition=sinclair.circular_mirror(
            diameter=dim(1, "in"),
            thickness=dim(6, "mm"),
            part_number="KA1 Retro Mirror",
            mount_type=sinclair.mirror_mount_KA1,
        ),
    ),
    beam_index=0b1,
    distance=dim(50.546, "mm"),
    rotation=(0, 90, 0),
)


if __name__ == "__main__":
    baseplate.recompute()

    for beam_path in (beam780_1, beam780_2, beam780_3):
        for segment in beam_path.get_object().BeamSegments:
            segment.ViewObject.Transparency = 50
            segment.ViewObject.ShapeColor = (1.0, 1.0, 0.0)
