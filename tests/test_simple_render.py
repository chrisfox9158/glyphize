from PIL import Image
from glyphize.render.render import render_ascii
from glyphize.convert.convert import convert
from assets.fonts.fonts import FONTS

def simple_render(cell_map, output_path=None, curve_power=1.0):
    rendering = render_ascii(cell_map=cell_map, ramp=" .-=*#%",
                            floor_brightness=0.0, curve_power=curve_power,
                            font_path=FONTS["Intel-Regular"]["path"], font_size_scale=FONTS["Intel-Regular"]["scale"],
                            bg_color="black", glyph_color="white")

    if output_path:
        rendering.save(output_path)
    else:
        rendering.show()

cell_map_skeleton = convert("assets/skeleton.jpg", cell_size=8)
simple_render(cell_map_skeleton, "assets/skeleton_ascii_render_curved.png", 0.2)

cell_map_wave = convert("assets/great_wave.jpg", cell_size=8)
simple_render(cell_map_wave, "assets/great_wave_ascii_render_curved.png", 1.0)

