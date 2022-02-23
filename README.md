# houdini_pdg_wedger_tool
A tool to facilitate the creation of TOP network wedge setup. 

-----
INPUTS:
  - Attributes to wedge
  - Caches needed for the simulation
  - Rendering config (previsualisation/high definition, format etc)

PROCESS:
  - Generates TOP network containing, wedge nodes with the user config, ROP fetch nodes for each cache that was input by the user, render nodes with user config (mantra for now), and a mosaic and ffmpeg setup to write the video to file.

OUTPUT:
  - A mosaic video of the wedged renders.
