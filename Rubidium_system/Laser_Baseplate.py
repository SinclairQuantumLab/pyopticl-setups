from PyOpticL import layout, optomech

# baseplate constants
base_dx = 12*layout.inch
base_dy = 6*layout.inch
base_dz = layout.inch
gap = layout.inch/8

# x-y coordinates of mount holes (in inches) (x,y)
mount_holes = [(2, 0), (4, 5), (7, 0), (11, 5)]

# y coordinate of beam input
input_y = 4*layout.inch

def Laser_baseplate():
    baseplate = layout.baseplate(base_dx, base_dy, base_dz, gap=gap, mount_holes=mount_holes)

    beam = baseplate.add_beam_path(x=3*layout.inch, y=input_y, angle=layout.cardinal['right'])
    
    baseplate.place_element("DFB", optomech.Koheron_DFB_Laser, x=3.125*layout.inch, y=input_y, angle=0)

    baseplate.place_element_along_beam("Optical_Isolator", optomech.isolator_780, beam,
                                       beam_index=0b1, distance=2.25*layout.inch, angle=layout.cardinal['left'])

    baseplate.place_element_along_beam("1/4 Waveplate", optomech.waveplate, beam,
                                       beam_index=0b1, distance=1.5*layout.inch, angle=layout.cardinal['right'],
                                       mount_type=optomech.rotation_stage_rsp05)

    baseplate.place_element_along_beam("Mirror", optomech.circular_mirror, beam,
                                       beam_index=0b1, distance=3.5*layout.inch, angle=layout.turn['up-left'],
                                       mount_type=optomech.mirror_mount_FMP05 )

    baseplate.place_element_along_beam("Mirror", optomech.circular_mirror, beam,
                                       beam_index=0b1, distance=2.5*layout.inch, angle=layout.turn['down-left'],
                                       mount_type=optomech.mirror_mount_M05,
                                       mount_args=dict(thumbscrews=True))

    baseplate.place_element_along_beam("1/2 Waveplate", optomech.waveplate, beam,
                                       beam_index=0b1, distance=1*layout.inch, angle=layout.cardinal['right'],
                                       mount_type=optomech.rotation_stage_rsp05)
    
    baseplate.place_element_along_beam("1/2 Waveplate", optomech.waveplate, beam,
                                       beam_index=0b1, distance=1*layout.inch, angle=layout.cardinal['right'],
                                       mount_type=optomech.rotation_stage_rsp05)
    
    baseplate.place_element_along_beam("Output Fiberport", optomech.fiberport_mount_km05T, beam,
                                       beam_index=0b1, distance=3*layout.inch-5.136, angle=layout.cardinal['right'],
                                       mount_args=dict(thumbscrews=True))
if __name__ == "__main__":
    Laser_baseplate()
    layout.redraw()
