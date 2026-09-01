from importlib import reload

from PyOpticL.beam_path import BeamPath
from PyOpticL.layout import Component
from PyOpticL.library import Baseplate
from PyOpticL.library import Sinclair_library as sinclair
from PyOpticL.utils import Dimension as dim
from PyOpticL.utils import turn_angle

reload(sinclair)


baseplate = Component(
    label="1529 nm pMOT Test",
    definition=Baseplate(
        dimensions=(
            dim(19, "in"),
            dim(17, "in"),
            dim(1, "in"),
        ),
        optical_height=dim(46.718, "mm"),
    ),
)



############################beam1######################


beam = baseplate.add(
    BeamPath(
        label="1529.366 nm Beam",
        wavelength=1529.366,
        waist=dim(17.5, "mm"),
        final_distance=dim(5, "in"),
    ),
    position=(
        dim(6, "in"),
        dim(13, "in"),
        dim(44.3335, "mm"),
    ),
    rotation=-45,
)


# First 80 mm lens
beam.add(
    Component(
        label="80 mm Lens 1",
        definition=sinclair.pmot_lens_80(),
    ),
    beam_index=0b1,
    distance=dim(2, "in"),
    rotation=-45,
)


# Glass-cell center: x = 0 mm
# Distance from first lens at x = -86.896 mm

import FreeCAD as App

cell_definition = sinclair.pmot_glass_cell()

cell_definition.mesh = cell_definition.mesh.copy()

cell_definition.mesh.transform(
    App.Rotation("XYZ", 0, 0, 0).toMatrix()
)

glass_cell = beam.add(
    Component(
        label="pMOT Glass Cell",
        definition=cell_definition,
    ),
    beam_index=0b1,
    distance=dim(89.896, "mm"),
    rotation=0,
)


# Second 80 mm lens: x = 76.670 mm
beam.add(
    Component(
        label="80 mm Lens 2",
        definition=sinclair.pmot_lens_80(),
    ),
    beam_index=0b1,
    distance=dim(79.670, "mm"),
    rotation=135,
)


# Retro mirror: x = 163.811 mm
# 163.811 - 76.670 = 87.141 mm
beam.add(
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



#############beam1 - 780#################


# 780.24 nm beam launched 5 in behind beam1.
# Place this lens 160 mm before beam1's first 80 mm lens.
beam780_1 = baseplate.add(
    BeamPath(
        label="780.24 nm Beam",
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














###################################beam2#########################################



beam2 = baseplate.add(
    BeamPath(
        label="1529.366 nm Beam 2",
        wavelength=1529.366,
        waist=dim(17.5, "mm"),
        final_distance=dim(5, "in"),
    ),
    position=(
        dim(13.83363, "in"),
        dim(13, "in"),
        dim(44.3335, "mm"),
    ),
    rotation=-135,
)


# First 80 mm lens
beam2.add(
    Component(
        label="Beam 2 - 80 mm Lens 1",
        definition=sinclair.pmot_lens_80(),
    ),
    beam_index=0b1,
    distance=dim(2, "in"),
    rotation=-135,
)


# Beam 2 passes through the existing glass cell.
# Once it has crossed the glass-cell interface,
# place Lens 2 79.670 mm farther along the same beam.
beam2.add(
    Component(
        label="Beam 2 - 80 mm Lens 2",
        definition=sinclair.pmot_lens_80(),
    ),
    beam_index=0b1,
    distance=dim(79.670, "mm"),
    after_object=glass_cell,
    rotation=45,
)


# Lens 2 -> Retro mirror = 87.141 mm
beam2.add(
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

#######780_2##########


# 780.24 nm beam launched 5 in behind beam1.
# Place this lens 160 mm before beam1's first 80 mm lens.
beam780_2 = baseplate.add(
    BeamPath(
        label="780.24 nm Beam",
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









############################beam3######################


beam3 = baseplate.add(
    BeamPath(
        label="1529.366 nm Beam 3",
        wavelength=1529.366,
        waist=dim(0.25, "in"),
        final_distance=dim(5, "in"),
    ),
    position=(
        dim(11.916815, "in"),
        dim(9.083185, "in"),
        dim(-27.668, "mm"),
    ),
    rotation=180   # +Z
)


############################beam3 - 780############################


# 780.24 nm beam launched 2 in before the beam3 start position.
# The lens is 80 mm before beam3's first AC254 lens.
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


beam3.add(
    Component(
        label="CCM1-P01",
        definition=sinclair.mirror_cube_ccm1_p01(),
    ),
    beam_index=0b1,
    distance=dim(2, "in"),
    rotation=(0, 0, 180),
)



# Lens 1: 1 inch after beam start
# Position relative to cell center: z = -52.268 mm
beam3.add(
    Component(
        label="Beam 3 - AC254-040-C-ML 1",
        definition=sinclair.mounted_lens_AC254_040_C_ML(),
    ),
    beam_index=0b1,
    distance=dim(19.05, "mm"),
    rotation=(0, -90, 0),
)
#95.4->19.05: 76.35 down
# 52.268+39.305=91.573
# The existing glass cell is encountered automatically at z = 0.
# Lens 2 is 39.305 mm above the glass-cell center.
beam3.add(
    Component(
        label="Beam 3 - AC254-040-C-ML 2",
        definition=sinclair.mounted_lens_AC254_040_C_ML(),
    ),
    beam_index=0b1,
    distance=dim(94.513, "mm"),
    rotation=(0, 90, 0),
)


# Retro mirror:
# z = 92.791 mm relative to cell center
# 92.791 - 39.305 = 53.486 mm after Lens 2
#
# Mirror faces downward and reflects +Z -> -Z.
beam3.add(
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








#########################color#########################


import colorsys


if __name__ == "__main__":
    baseplate.recompute()

    for beam_path in (beam, beam2, beam3, beam780_1, beam780_2, beam780_3):
        for segment in beam_path.get_object().BeamSegments:
            segment.ViewObject.Transparency = 50

            if beam_path is beam780_1 or beam_path is beam780_2 or beam_path is beam780_3:
                segment.ViewObject.ShapeColor = (1.0, 1.0, 0.0)
                continue

            direction = segment.Proxy.get_global_direction()

            r, g, b = segment.ViewObject.ShapeColor[:3]
            _, s, v = colorsys.rgb_to_hsv(r, g, b)

            # Vertical beam: use Z direction
            if abs(direction[2]) > abs(direction[1]):

                # +Z = red
                if direction[2] > 1e-6:
                    segment.ViewObject.ShapeColor = colorsys.hsv_to_rgb(
                        0.0,
                        s,
                        v,
                    )

                # -Z = blue
                elif direction[2] < -1e-6:
                    segment.ViewObject.ShapeColor = colorsys.hsv_to_rgb(
                        2.0 / 3.0,
                        s,
                        v,
                    )

            # Horizontal beams: use Y direction
            else:

                # -Y = red
                if direction[1] < -1e-6:
                    segment.ViewObject.ShapeColor = colorsys.hsv_to_rgb(
                        0.0,
                        s,
                        v,
                    )

                # +Y = blue
                elif direction[1] > 1e-6:
                    segment.ViewObject.ShapeColor = colorsys.hsv_to_rgb(
                        2.0 / 3.0,
                        s,
                        v,
                    )
