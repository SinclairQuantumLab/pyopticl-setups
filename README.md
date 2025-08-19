# Rb87 Neutral Atom Optical Platform (PyOpticL + FreeCAD)

This repository contains a PyOpticL-based optical/mechanical layout for building an optical platform targeting Rb-87 neutral atom experiments. It assembles a complete, code-driven CAD model in FreeCAD, organizing the setup into modular boards.

The project originates from (and depends on) PyOpticL, a code-to-CAD tooling framework for modular optics systems engineering, and uses FreeCAD as the CAD backend.

- Project webpage (origin): https://github.com/UMassIonTrappers/PyOpticL
- Affiliation: UC Berkeley, Department of Physics — Prof. Sulyemanzade’s research group
- Lab website: https://suleymanzadelab.com/
- Collaborators:
  - Prof. Josiah Sinclair, University of Wisconsin–Madison — https://www.physics.wisc.edu/directory/sinclair-josiah/
  - Dr. Brandon Grinkemeyer, Harvard University (Postdoctoral Researcher) — https://lukin.physics.harvard.edu/people/brandon-grinkemeyer

## Overview

- Purpose: Build a modular optical platform for Rb-87 neutral atom quantum computing.
- CAD Backend: FreeCAD
- Optical/CAD Tooling: PyOpticL
- Project Structure: The system is organized into six main boards:
  - Reference_board
  - MOT_board
  - Repumper_board
  - Spectroscopy_board
  - TA_board
  - post_TA_board

## Prerequisites

- FreeCAD (latest stable recommended)
- PyOpticL module installed in FreeCAD

## Installation

1. Install FreeCAD on your system.
2. Install PyOpticL in FreeCAD, following the official instructions at https://github.com/UMassIonTrappers/PyOpticL.
3. Update the PyOpticL module directory with this project’s assets:
   - Copy the `stl` folder from this repository into the PyOpticL module’s directory.
   - Copy `optomech.py` from this repository into the PyOpticL module’s directory, replacing the existing file if present.

Note: The exact PyOpticL module path depends on your OS and FreeCAD configuration (e.g., on macOS it may be under `~/Library/Application Support/FreeCAD/Mod/PyOpticL/PyOpticL`).

## Project Files

- `stl/` — Mechanical part models used by the layout (mounts, adapters, etc.) in stl format.
- `optomech.py` — Project-specific mechanical and optical component definitions/overrides for PyOpticL.
- `Adapters/` - 3D\-printable files(most of them are in step format) for the adapters on the boards, along with the Rb cell holders.
- Main script: See the provided Python script (e.g., “PyOpticL_Rubidium_System”) that constructs all boards in FreeCAD using PyOpticL.

## Boards

- Reference_board:![The schematic of reference board in FreeCAD](<pics/Ref.png>)
  After exiting the laser, the main beam passes through polarizing elements and isolators, then through several PBSs before entering the fiber, which leads to the Spectroscopy board for frequency locking. Three beams, including the MOT light and Repump light, are each combined with side beams split from the main beam by PBSs, using beatnote technology to achieve frequency locking of these beams.<br><br>

- MOT_board:  ![The schematic of 780nm MOT board in Freecad](<pics/MOT_780.png>) ![The schematic of 852nm MOT board in Freecad](<pics/MOT_852.png>)
The MOT board’s beam splits into two paths: one for MOT operation and one to the Reference board for frequency locking. 
Because different wavelengths require different isolators, there are two versions of the MOT board (780nm and 852nm).<br><br>

- Repumper_board:![The schematic of repumper board in FreeCAD](<pics/Repump.png>)
The Repumper board’s beam similarly splits into two paths. In the repump path, we add a single-pass AOM, an iris, and a shutter to enable fast on/off control of the repumper light.<br><br>

- Spectroscopy_board: ![The schematic of spectroscopy board in FreeCAD](<pics/Spectroscopy.png>)
After going through the reference board, the main beam splits into two beams, one strong(pump) and one weak(probe), which counterpropagate through the Rb atomic vapor at this board. The stronger beam finally goes to the photodetector. Here we use the Saturation absorption spectroscopy method, which will selectively saturate zero-velocity atoms in a vapor, producing a narrow Lamb dip that overcomes Doppler broadening and provides a stable reference for high-precision laser frequency locking.<br><br>

- TA_board: 
(Coming Soon)<br><br>

- post_TA_board:  ![The schematic of post-TA board in FreeCAD](<pics/post-TA.png>)
After amplifying the laser, we split the beam into three paths for different uses. Each path includes an AOM, iris, and shutter for on/off control.

(The pictures of the board may not be the latest version.)
## How to Use

Please see the Quickstart Guide in the PyOpticL wiki:
https://github.com/UMassIonTrappers/PyOpticL/wiki#quickstart-guide

## Customization

(Coming soon)

## Acknowledgments

- Core development by UC Berkeley, Department of Physics — Prof. Sulyemanzade’s group (Lab website: https://suleymanzadelab.com/).
- Collaboration and valuable input from:
  - Prof. Josiah Sinclair, University of Wisconsin–Madison — https://www.physics.wisc.edu/directory/sinclair-josiah/
  - Dr. Brandon Grinkemeyer, Harvard University (Postdoctoral Researcher) — https://lukin.physics.harvard.edu/people/brandon-grinkemeyer
- Built on PyOpticL: a code-to-CAD optical layout tool enabling parametric, modular optics design inside FreeCAD.
- FreeCAD: Open-source parametric 3D CAD modeler used to render and manipulate the generated assemblies.

## Citation

If you use this work in academic settings, please also cite:
- PyOpticL and its associated publications.
- This repository (include commit or release tags).
- UC Berkeley Physics — Sulyemanzade Lab; UW–Madison — Prof. Josiah Sinclair; Harvard University — Dr. Brandon Grinkemeyer.

---
