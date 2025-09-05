from PyOpticL import layout, optomech
from datetime import datetime


def doublepass_f100(x=0, y=0, angle=0, mirror=optomech.mirror_mount_km05, x_split=False, thumbscrews=True):
    
    # Adding name and date to keep a track of the updates
    name = "Doublepass"
    date_time = datetime.now().strftime("%m/%d/%Y")
    label = name + " " +  date_time

    # Dimension of the baseplate

    dx = 16
    dy = 10
    base_dx = dx*layout.inch
    base_dy = dy*layout.inch
    base_dz = layout.inch
    gap = layout.inch/8

    input_y = 5.5*layout.inch
    mount_holes = [(0, 0),  (dx-1, 0),  (dx-1, dy-1), (0, dy-1)]


    # define and place baseplate object
    baseplate = layout.baseplate(base_dx, base_dy, base_dz, x=x, y=y, angle=angle,
                                 gap=gap, mount_holes=mount_holes)

    # add beam
    beam = baseplate.add_beam_path(x=14*layout.inch, y=input_y, angle=layout.cardinal['down'])

    baseplate.place_element("DFB", optomech.TA_butterfly, x=14*layout.inch, y=input_y, angle=270)
    baseplate.place_element_along_beam("Rotation Stage", optomech.waveplate, beam,
                                       beam_index=0b1, distance=layout.inch, angle=layout.cardinal['down'],
                                       mount_type=optomech.rotation_stage_rsp05)

    #Adding the isolator to make sure there is no unwanted beam going back as feedback
    baseplate.place_element_along_beam("Optical_Isolator", optomech.isolator_405, beam,
                                       beam_index=0b1, distance=1.125*layout.inch, angle=layout.cardinal['down'])
    
    baseplate.place_element_along_beam("Output Mirror 2", optomech.circular_mirror, beam,
                                       beam_index=0b1, distance=50, angle=layout.turn['down-left'],
                                       mount_type=mirror, mount_args=dict(thumbscrews=thumbscrews))
    
    # add waveplate along the beam, 1/2" after the PBS , mounted in a rotation stage
    baseplate.place_element_along_beam("Rotation Stage", optomech.waveplate, beam,
                                       beam_index=0b1, distance=1.25*layout.inch, angle=layout.cardinal['right'],
                                       mount_type=optomech.rotation_stage_rsp05)

    # add waveplate along the beam, mounted in a rotation stage
    baseplate.place_element_along_beam("Rotation Stage", optomech.waveplate, beam,
                                       beam_index=0b1, distance=.75*layout.inch, angle=layout.cardinal['right'],
                                       mount_type=optomech.rotation_stage_rsp05)

######################################### lower Part of the baseplate #########################################

    # Adding beam splitter to divide the beam to : to saty on the baseplate and to to send to the next baseplate
    baseplate.place_element_along_beam("Beam Splitter", optomech.cube_splitter, beam,
                                       beam_index=0b1, distance=28, angle=layout.cardinal['up'],
                                       mount_type=optomech.skate_mount)
        # add waveplate along the beam, 1/2" after the PBS , mounted in a rotation stage
    baseplate.place_element_along_beam("Rotation Stage", optomech.waveplate, beam,
                                       beam_index=0b11, distance=1*layout.inch, angle=layout.cardinal['up'],
                                       mount_type=optomech.rotation_stage_rsp05)

    # Adding AOM
    baseplate.place_element_along_beam("AOM", optomech.isomet_1205c_on_km100pm, beam,
                                    beam_index=0b11, distance = 85, angle=layout.cardinal['up'],
                                    forward_direction=-1, backward_direction=1)
    # Mirror 2
    baseplate.place_element_along_beam("Output Mirror 1", optomech.circular_mirror, beam,
                                       beam_index=0b111, distance=70, angle=layout.turn['up-left'],  
                                       mount_type=mirror, mount_args=dict(thumbscrews=thumbscrews))

    
    # Adding Iris to select the beam of right order
    baseplate.place_element_along_beam("Iris", optomech.pinhole_ida12, beam,
                                       beam_index=0b111, distance=20, angle=layout.cardinal['left'])  
    
    baseplate.place_element_along_beam("cleanup Stage", optomech.waveplate, beam,
                                       beam_index=0b111, distance=.75*layout.inch, angle=layout.cardinal['right'],
                                       mount_type=optomech.rotation_stage_rsp05)
    baseplate.place_element_along_beam("cleanup Stage", optomech.waveplate, beam,
                                beam_index=0b111, distance=.75*layout.inch, angle=layout.cardinal['right'],
                                mount_type=optomech.rotation_stage_rsp05)

    # add output fiberport along the transmitted beam
    baseplate.place_element_along_beam("Output Fiberport", optomech.fiberport_mount_km05T_custom, beam,
                                       beam_index=0b111, distance=3*layout.inch, angle=layout.cardinal['right'],
                                       mount_args=dict(thumbscrews=True))


######################################### middle Part of the baseplate #########################################

    # add waveplate along the beam, mounted in a rotation stage
    baseplate.place_element_along_beam("Rotation Stage", optomech.waveplate, beam,
                                       beam_index=0b10, distance=1*layout.inch, angle=layout.cardinal['right'],
                                       mount_type=optomech.rotation_stage_rsp05)

    # Adding beam splitter to divide the beam to : to saty on the baseplate and to to send to the next baseplate
    baseplate.place_element_along_beam("Beam Splitter", optomech.cube_splitter, beam,
                                       beam_index=0b10, distance=30, angle=layout.cardinal['up'],
                                       mount_type=optomech.skate_mount)
    

        # add waveplate along the beam, 1/2" after the PBS , mounted in a rotation stage
    baseplate.place_element_along_beam("Rotation Stage", optomech.waveplate, beam,
                                       beam_index=0b100, distance=1*layout.inch, angle=layout.cardinal['right'],
                                       mount_type=optomech.rotation_stage_rsp05)

    # Adding AOM
    baseplate.place_element_along_beam("AOM", optomech.isomet_1205c_on_km100pm, beam,
                                    beam_index=0b100, distance = 60, angle=layout.cardinal['left'],
                                    forward_direction=-1, backward_direction=1)
    baseplate.place_element_along_beam("Iris", optomech.pinhole_ida12, beam,
                                       beam_index=0b1001, distance=55, angle=layout.cardinal['left'])  
    # Adding output mirror to send the beam properly to the fiberport. Mirror 1
    baseplate.place_element_along_beam("Output Mirror 2", optomech.circular_mirror, beam,
                                       beam_index=0b1001, distance=40, angle=layout.turn['left-up'],
                                       mount_type=mirror, mount_args=dict(thumbscrews=thumbscrews))
    
    # Adding Iris to select the beam of right order

    
    baseplate.place_element_along_beam("cleanup Stage", optomech.waveplate, beam,
                                       beam_index=0b1001, distance=.75*layout.inch, angle=layout.cardinal['down'],
                                       mount_type=optomech.rotation_stage_rsp05)
    baseplate.place_element_along_beam("cleanup Stage", optomech.waveplate, beam,
                                beam_index=0b1001, distance=.75*layout.inch, angle=layout.cardinal['down'],
                                mount_type=optomech.rotation_stage_rsp05)
    # add output fiberport along the transmitted beam
    baseplate.place_element_along_beam("Output Fiberport", optomech.fiberport_mount_km05T_custom, beam,
                                       beam_index=0b1001, distance=3*layout.inch, angle=layout.cardinal['down'],
                                       mount_args=dict(thumbscrews=True))
    
######################################### Upper Part of the baseplate #########################################
    

        # add waveplate along the beam, 1/2" after the PBS , mounted in a rotation stage
    baseplate.place_element_along_beam("Rotation Stage", optomech.waveplate, beam,
                                       beam_index=0b101, distance=1*layout.inch, angle=layout.cardinal['up'],
                                       mount_type=optomech.rotation_stage_rsp05)

    # Adding AOM
    baseplate.place_element_along_beam("AOM", optomech.isomet_1205c_on_km100pm, beam,
                                    beam_index=0b101, distance = 30, angle=layout.cardinal['down'],
                                    forward_direction=-1, backward_direction=1)

    # Adding output mirror to send the beam properly to the fiberport. Mirror 1
    baseplate.place_element_along_beam("Output Mirror 2", optomech.circular_mirror, beam,
                                       beam_index=0b1011, distance=100, angle=layout.turn['up-left'],
                                       mount_type=mirror, mount_args=dict(thumbscrews=thumbscrews))
    
    # Adding Iris to select the beam of right order
    baseplate.place_element_along_beam("Iris", optomech.pinhole_ida12, beam,
                                       beam_index=0b1011, distance=20, angle=layout.cardinal['right'])  
    baseplate.place_element_along_beam("cleanup Stage", optomech.waveplate, beam,
                                       beam_index=0b1011, distance=.75*layout.inch, angle=layout.cardinal['right'],
                                       mount_type=optomech.rotation_stage_rsp05)
    baseplate.place_element_along_beam("cleanup Stage", optomech.waveplate, beam,
                                beam_index=0b1011, distance=.75*layout.inch, angle=layout.cardinal['right'],
                                mount_type=optomech.rotation_stage_rsp05)
    # add output fiberport along the transmitted beam
    baseplate.place_element_along_beam("Output Fiberport", optomech.fiberport_mount_km05T_custom, beam,
                                       beam_index=0b1011, distance=3*layout.inch, angle=layout.cardinal['right'],
                                       mount_args=dict(thumbscrews=True))

if __name__ == "__main__":
    doublepass_f100()  # changne the f__ depending on which lens you want
    # doublepass_f100(y = 6)
    layout.redraw()