from PyOpticL import layout, optomech
from datetime import datetime


def doublepass_f100(x=0, y=0, angle=0, mirror=optomech.mirror_mount_km05, x_split=False, thumbscrews=True):
    
    # Adding name and date to keep a track of the updates
    name = "Doublepass"
    date_time = datetime.now().strftime("%m/%d/%Y")
    label = ''

    # Dimension of the baseplate
    dx = 10
    dy = 3.5
    base_dx = dx*layout.inch
    base_dy = dy*layout.inch
    base_dz = layout.inch
    gap = layout.inch/8

    input_x = .75*layout.inch
    input_y = 1*layout.inch

    mount_holes = [(1, 0),  (dx-1, 0),  (dx-2, dy-1), (0, dy-1)]
    extra_mount_holes = []

    # Difining the baseplate
    baseplate = layout.baseplate(base_dx, base_dy, base_dz, x=x, y=y, angle=angle,
                                 gap=gap, mount_holes=mount_holes+extra_mount_holes,
                                 name=name, label=label, x_splits=[4*layout.inch]*x_split)
    
    # Adding the beam to the baseplate
    baseplate.place_element("MOT Output Fiberport", optomech.mirror_mount_km100,
                                    x=input_x, y=input_y, angle=layout.cardinal['right'])
    beam = baseplate.add_beam_path(x=input_x, y=input_y, angle=layout.cardinal['right'])    
    
    # Adding a waveplate to control the ploarization
    baseplate.place_element_along_beam("Half waveplate", optomech.waveplate, beam,
                                       beam_index=0b1, distance=30, angle=layout.cardinal['left'],
                                       mount_type=optomech.rotation_stage_rsp05)

    # Adding beam splitter to divide the beam to : to saty on the baseplate and to to send to the next baseplate
    # baseplate.place_element_along_beam("Beam Splitter", optomech.cube_splitter, beam,
    #                                    beam_index=0b1, distance=28, angle=layout.cardinal['up'],
    #                                    mount_type=optomech.skate_mount)
    
    baseplate.place_element_along_beam("Beam Splitter Cube", optomech.cube_splitter, beam,
                                       beam_index=0b1, distance=23, angle=layout.cardinal['up'],
                                       mount_type=optomech.prism_mount_km05pm, mount_args=dict(thumbscrews=thumbscrews))
    
    # Adding half waveplate to control the polarization

    
    # baseplate.place_element_along_beam("shutter", optomech.shutter_sr475, beam,
    #                                    beam_index=0b11, distance=63, angle=layout.cardinal['left'])
    # Adding AOM
    crystal = baseplate.place_element_along_beam("AOM", optomech.isomet_1205c_on_km100pm, beam,
                                    beam_index=0b10, distance = 50, angle=layout.cardinal['left'],
                                    forward_direction=-1, backward_direction=1)

    #Adding lens make collimated beam. 
    baseplate.place_element_relative("Lens f100mm AB coat", optomech.circular_lens, crystal,
                                    x_off=75, angle=layout.cardinal['right'],
                                    focal_length=75, part_number='LA1213-AB', mount_type=optomech.lens_holder_l05g)

        # # Adding Iris to select the beam of right order

    baseplate.place_element_along_beam("Quarter waveplate", optomech.waveplate, beam,
                                    beam_index=0b101, distance=85, angle=layout.cardinal['left'],
                                    mount_type=optomech.rotation_stage_rsp05)
    baseplate.place_element_along_beam("Iris", optomech.pinhole_ida12, beam,
                                       beam_index=0b101, distance=10, angle=layout.cardinal['left'])  
    # Adding another mirror to send the beam back into the AOM
    baseplate.place_element_along_beam("Retro Mirror", optomech.circular_mirror, beam,
                                     beam_index=0b101, distance=10, angle=layout.cardinal['left'],
                                     mount_type=mirror, mount_args=dict(thumbscrews=thumbscrews))

    baseplate.place_element_along_beam("Quarter waveplate", optomech.waveplate, beam,
                                    beam_index=0b10111, distance=15, angle=layout.cardinal['down'],
                                    mount_type=optomech.rotation_stage_rsp05)

    baseplate.place_element_along_beam("Iris", optomech.pinhole_ida12, beam,
                                    beam_index=0b10111, distance=10, angle=layout.cardinal['down'])  
    
    # Fiberport to fiber the beam
    baseplate.place_element_along_beam("MOT Output Fiberport", optomech.mirror_mount_km100, beam,
                                      beam_index=0b10111, distance=20, angle=layout.cardinal['down'])

if __name__ == "__main__":
    doublepass_f100()  # changne the f__ depending on which lens you want
    # doublepass_f100(y = 6)
    layout.redraw()