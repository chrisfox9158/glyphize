from PIL import Image, ImageDraw, ImageFont
import random

def render_ascii(*, cell_map, ramp, floor_brightness, curve_power, font_path, font_size_scale, bg_color, glyph_color):
    canvas_width = cell_map.grid_width * cell_map.cell_size
    canvas_height = cell_map.grid_height * cell_map.cell_size
    canvas_size = (canvas_width, canvas_height)

    canvas = Image.new("RGB", canvas_size, bg_color)
    draw = ImageDraw.Draw(canvas)
    font = ImageFont.truetype(font_path, size=int(cell_map.cell_size * font_size_scale))

    for row in range(cell_map.grid_height):
        for col in range(cell_map.grid_width):
            brightness = cell_map.grid[row, col]["brightness"]

            probability = draw_probability(brightness, floor_brightness, curve_power)
            if random.random() >= probability:
                continue

            ramp_index = int(brightness * (len(ramp) - 1))
            glyph = ramp[ramp_index]

            position = (col * cell_map.cell_size, row * cell_map.cell_size)
            draw.text(position, glyph, font=font, fill=glyph_color)

    return canvas

def draw_probability(brightness, floor_brightness, curve_power):
    if brightness <= floor_brightness:
        return 0.0

    normalized = (brightness - floor_brightness) / (1.0 - floor_brightness)
    return normalized ** curve_power
