from PIL import Image
from glyphize.render.render import render_ascii
from glyphize.convert.convert import convert
from assets.fonts.fonts import FONTS

def simple_render(cell_map, output_path=None):
    rendering = render_ascii(cell_map, " .-=*#%", 0.0,
                            FONTS["Intel-Regular"]["path"], FONTS["Intel-Regular"]["scale"],
                            "black", "white")

    if output_path:
        rendering.save(output_path)
    else:
        rendering.show()

cell_map = convert("assets/skeleton.jpg", cell_size=8)
simple_render(cell_map, "assets/skeleton_ascii_render.png")