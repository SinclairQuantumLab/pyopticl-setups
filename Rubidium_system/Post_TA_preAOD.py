from PyOpticL import layout, optomech

# baseplate constants
base_dx = 15 * layout.inch
base_dy = 32 * layout.inch
base_dz = 1.5 * layout.inch
gap = layout.inch / 8

mount_holes = [(3, 0), (14, 0), (0, 13), (14, 13), (0,25), (14,25)]

input_y = 7 * layout.inch


def Post_TA_preAOD(x=0, y=0, angle=0):
    baseplate = layout.baseplate(base_dx, base_dy, base_dz,
                                 x=x, y=y, angle=angle, gap=gap,
                                 mount_holes=mount_holes,
                                 optics_dz=base_dz + (0.5 * layout.inch))

    beam = baseplate.add_beam_path(x=3 * layout.inch, y=2.5 * layout.inch, angle=layout.cardinal['up'])

    baseplate.place_element("Input Fiberport", optomech.fiberport_mount_km05T_2inch, x=3 * layout.inch, y=2 * layout.inch,
                            angle=layout.cardinal['up'], mount_args=dict(thumbscrews=True))


# f-100 Asphere located 50 away from collimating lens

    baseplate.place_element_along_beam("MountedAL50100", optomech.Mounted_asphere_100, beam,
                                       beam_index=0b1, distance=103, angle=layout.cardinal['down']
                                       )

# f=100 Asphere located 80.713 away
# distance needs to be adjusted accordingly to 93.666 from 80.713
    baseplate.place_element_along_beam("AL50100M", optomech.Mounted_asphere_100, beam,
                                       beam_index=0b1, distance=207.125, angle=layout.cardinal['up'])



    baseplate.place_element_along_beam("Mirror", optomech.mirror_2inch, beam,
                                       beam_index=0b1, distance=75.33, angle=layout.turn['left-down'],
                                       mount_type=optomech.mirror_mount_KM2CE)

    baseplate.place_element_along_beam("Mirror", optomech.mirror_2inch, beam,
                                       beam_index=0b1, distance=100, angle=layout.turn['right-down'],
                                       mount_type=optomech.mirror_mount_KM2CE)

    baseplate.place_element_along_beam("1/2 Waveplate", optomech.waveplate_raised, beam,
                                       beam_index=0b1, distance=100, angle=layout.cardinal['down'],
                                       mount_type=optomech.rotation_stage_rsp05)

    baseplate.place_element_along_beam("AL7560B", optomech.Mounted_asphere_60, beam,
                                       beam_index=0b1, distance=107.017, angle=layout.cardinal['up'])

    # next distance is 357.978 to go to the 4 inch, f=200mm lens, corrected is 374.476

    baseplate.place_element_along_beam("Mirror", optomech.mirror_2inch, beam,
                                       beam_index=0b1, distance=125, angle=layout.turn['down-right'],
                                       mount_type=optomech.mirror_mount_KM2CE)

    baseplate.place_element_along_beam("Mirror", optomech.mirror_2inch, beam,
                                       beam_index=0b1, distance=125, angle=layout.turn['right-up'],
                                       mount_type=optomech.mirror_mount_KM2CE)

    baseplate.place_element_along_beam("AL100200", optomech.Mounted_nostage_200, beam,
                                       beam_index=0b1, distance=70+154.476+150-200+11.52597-25, angle=layout.cardinal['up'])


    # 187.434 to the next expander, correction of 0.999
    #80 to the next lens
    baseplate.place_element_along_beam("AL7560B", optomech.Mounted_asphere_60, beam,
                                       beam_index=0b1, distance=188.434, angle=layout.cardinal['down'])

    baseplate.place_element_along_beam("Mirror", optomech.mirror_2inch, beam,
                                       beam_index=0b1, distance=155, angle=layout.turn['up-left'],
                                       mount_type=optomech.mirror_mount_KM2CE)

    # next distance should be 167.961, it is 117.46
    baseplate.place_element_along_beam("AL75150B", optomech.Mounted_asphere_150, beam,
                                       beam_index=0b1, distance=217.462-156.56, angle=layout.cardinal['right'])

# must be a gap of 661.85mm to from flat face of the f150 asphere to the first asphere AFTER the AOD
# and it will be another f150 asphere

    baseplate.place_element_along_beam("Mirror", optomech.mirror_2inch, beam,
                                       beam_index=0b1, distance=161.85, angle=layout.turn['left-up'],
                                       mount_type=optomech.mirror_mount_KM2CE)




if __name__ == "__main__":
    Post_TA_preAOD()
    layout.redraw()