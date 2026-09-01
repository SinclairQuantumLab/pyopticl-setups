from PyOpticL import layout, optomech

# baseplate constants
base_dx = 15 * layout.inch
base_dy = 55 * layout.inch
base_dz = 2 * layout.inch
gap = layout.inch / 8

mount_holes = [(3, 0), (14, 0), (0, 13), (14, 13), (0,26), (14,26), (0, 39), (14, 39), (0, 52), (14,52)]

input_y = 7 * layout.inch


def Optics_for_NA(x=0, y=0, angle=0):
    baseplate = layout.baseplate(base_dx, base_dy, base_dz,
                                 x=x, y=y, angle=angle, gap=gap,
                                 mount_holes=mount_holes,
                                 optics_dz=base_dz + (0.4 * layout.inch))

    beam = baseplate.add_beam_path(x=3 * layout.inch, y=2.5 * layout.inch, angle=layout.cardinal['up'])

    baseplate.place_element("Input Fiberport", optomech.fiberport_mount_km05T_raised, x=3 * layout.inch, y=2 * layout.inch,
                            angle=layout.cardinal['up'], mount_args=dict(thumbscrews=True))

    baseplate.place_element_along_beam("1/2 Waveplate", optomech.waveplate_raised, beam,
                                       beam_index=0b1, distance=105, angle=layout.cardinal['down'],
                                       mount_type=optomech.rotation_stage_rsp05)
#    baseplate.place_element_along_beam("1/2 Waveplate", optomech.waveplate_raised, beam,
#                                       beam_index=0b1, distance=25, angle=layout.cardinal['down'],
#                                       mount_type=optomech.rotation_stage_rsp05)


    baseplate.place_element_along_beam("Mirror", optomech.mirror_2inch, beam,
                                       beam_index=0b1, distance=125, angle=layout.turn['left-down'],
                                       mount_type=optomech.mirror_mount_KM2CE)

    baseplate.place_element_along_beam("Mirror", optomech.mirror_2inch, beam,
                                       beam_index=0b1, distance=100, angle=layout.turn['right-down'],
                                       mount_type=optomech.mirror_mount_KM2CE)

# distance from the last AL50100 lens to the f60 lens should be 483.399

    baseplate.place_element_along_beam("AL7560B", optomech.Mounted_asphere_60, beam,
                                       beam_index=0b1, distance=100, angle=layout.cardinal['up'])

    # next distance is 357.978 to go to the 4 inch, f=200mm lens, corrected is 374.476

    baseplate.place_element_along_beam("Mirror", optomech.mirror_2inch, beam,
                                       beam_index=0b1, distance=125, angle=layout.turn['down-right'],
                                       mount_type=optomech.mirror_mount_KM2CE)

    baseplate.place_element_along_beam("Mirror", optomech.mirror_2inch, beam,
                                       beam_index=0b1, distance=125, angle=layout.turn['right-up'],
                                       mount_type=optomech.mirror_mount_KM2CE)

# Distance to this lens from the f60 asphere should be 357.978
    baseplate.place_element_along_beam("AL100200", optomech.Mounted_nostage_200, beam,
                                       beam_index=0b1, distance=161.91, angle=layout.cardinal['up'])

    # the f60 should be 242.934

    baseplate.place_element_along_beam("AL7560B", optomech.Mounted_asphere_60, beam,
                                       beam_index=0b1, distance=188.434, angle=layout.cardinal['down'])

    baseplate.place_element_along_beam("Mirror", optomech.mirror_2inch, beam,
                                       beam_index=0b1, distance=155-15, angle=layout.turn['up-left'],
                                       mount_type=optomech.mirror_mount_KM2CE)

    # next distance should be 166.961
    baseplate.place_element_along_beam("AL100200B", optomech.Mounted_nostage_200, beam,
                                       beam_index=0b1, distance=126.384-44.989, angle=layout.cardinal['left'])

# must be a gap of 661.85mm to from flat face of the f150 asphere to the first asphere AFTER the AOD
# and it will be another f150 asphere

    baseplate.place_element_along_beam("Mirror", optomech.mirror_2inch, beam,
                                       beam_index=0b1, distance=121.85, angle=layout.turn['left-up'],
                                       mount_type=optomech.mirror_mount_KM2CE)

    baseplate.place_element_along_beam("Mirror", optomech.mirror_2inch, beam,
                                       beam_index=0b1, distance=140, angle=layout.turn['up-right'],
                                       mount_type=optomech.mirror_mount_KM2CE)

    baseplate.place_element_along_beam("1/2 Waveplate", optomech.waveplate_2in, beam,
                                       beam_index=0b1, distance=45, angle=layout.cardinal['left'])

    baseplate.place_element_along_beam("Mirror", optomech.mirror_2inch, beam,
                                       beam_index=0b1, distance=215.78-45, angle=layout.turn['right-up'],
                                       mount_type=optomech.mirror_mount_KM2CE)


# POST AOD, ONLY THE MIDDLE DISTANCES IN the 4f are SENSITIVE. The second f150 lens and the first f200 lens should
# be on translation stages then


    baseplate.place_element_along_beam("AL75150B", optomech.Mounted_asphere_150, beam,
                                       beam_index=0b1, distance=150, angle=layout.cardinal['down'])

# waveplate before it in the center to make sure light is LINEARLY polarized for AOD

    baseplate.place_element_along_beam("1/2 Waveplate", optomech.waveplate_raised, beam,
                                       beam_index=0b1, distance=146, angle=layout.cardinal['down'],
                                       mount_type=optomech.rotation_stage_rsp05)

# THE NEXT f150 LENS MUST BE 250.634mm away, not mounted

    baseplate.place_element_along_beam("AL75150B", optomech.Mounted_stage_f150, beam,
                                       beam_index=0b1, distance=134.604, angle=layout.cardinal['up'])

# 719.506mm to the next f=200 lens, this should be on a translation stage

    baseplate.place_element_along_beam("Mirror", optomech.mirror_2inch, beam,
                                       beam_index=0b1, distance=175, angle=layout.turn['up-left'],
                                       mount_type=optomech.mirror_mount_KM2CE)

    baseplate.place_element_along_beam("Mirror", optomech.mirror_2inch, beam,
                                       beam_index=0b1, distance=119.506, angle=layout.turn['left-down'],
                                       mount_type=optomech.mirror_mount_KM2CE)

    baseplate.place_element_along_beam("1/2 Waveplate", optomech.waveplate_2in, beam,
                                       beam_index=0b1, distance=60, angle=layout.cardinal['up'])

    baseplate.place_element_along_beam("AL100200B", optomech.Mounted_stage_f200, beam,
                                       beam_index=0b1, distance=331.872, angle=layout.cardinal['up'])

    baseplate.place_element_along_beam("Mirror", optomech.mirror_2inch, beam,
                                       beam_index=0b1, distance=95, angle=layout.turn['down-left'],
                                       mount_type=optomech.mirror_mount_KM2CE)

    baseplate.place_element_along_beam("Mirror", optomech.mirror_2inch, beam,
                                       beam_index=0b1, distance=113.036, angle=layout.turn['left-up'],
                                       mount_type=optomech.mirror_mount_KM2CE)

    baseplate.place_element_along_beam("1/2 Waveplate", optomech.waveplate_raised, beam,
                                       beam_index=0b1, distance=30, angle=layout.cardinal['down'],
                                       mount_type=optomech.rotation_stage_rsp05
                                       )

    baseplate.place_element_along_beam("1/4 Waveplate", optomech.waveplate_raised, beam,
                                    beam_index=0b1, distance=48-30, angle=layout.cardinal['down'],
                                    mount_type=optomech.rotation_stage_rsp05)

# next distance should be 413.036mm to the 2nd f200 lens
    baseplate.place_element_along_beam("AL100200B", optomech.Mounted_nostage_200, beam,
                                       beam_index=0b1, distance=184.806+5, angle=layout.cardinal['up'])

    baseplate.place_element_along_beam("NPBS2in", optomech.PBS_2in_mounted, beam,
                                       beam_index=0b1, distance=175, angle=layout.cardinal['up'])


if __name__ == "__main__":
    Optics_for_NA()
    layout.redraw()