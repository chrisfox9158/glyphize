from PIL import Image
import math
import numpy as np

from ..models import CellMap

def load(image):
    with Image.open(image) as im:
        im.load()
        return im

def normalize(image):
    if image.mode in ("RGBA", "LA", "P"):
        x, y = image.size
        white_bg = Image.new(mode="RGBA", size=(x, y), color=(255, 255, 255))

        image = image.convert("RGBA")
        image = Image.alpha_composite(white_bg, image)

        image = image.convert("RGB")
    else:
        image = image.convert("RGB")
    return image

def average_color(pixel_block):
    sum_r, sum_g, sum_b = 0, 0, 0
    count = 0

    for (r, g, b) in pixel_block.get_flattened_data():
        sum_r += r
        sum_g += g
        sum_b += b
        count += 1

    mean_r = round(sum_r / count)
    mean_g = round(sum_g / count)
    mean_b = round(sum_b / count)

    return (mean_r, mean_g, mean_b)

def luminance(mean_rgb):
    r, g, b = mean_rgb
    weighted_sum = (0.299 * r) + (0.587 * g) + (0.114 * b) # based on ITU-R BT.601 standard
    normal_lum = weighted_sum / 255.0
    return normal_lum

def convert_to_map(image, cell_size):
    grid_width = math.ceil(image.width / cell_size)
    grid_height = math.ceil(image.height / cell_size)

    cell_dtype = np.dtype([
        ("mean_rgb", np.uint8, (3,)),
        ("brightness", np.float32)
        ])

    grid = np.empty((grid_height, grid_width), dtype=cell_dtype)

    for row in range(grid_height):
        for col in range(grid_width):
            x0, y0 = col * cell_size, row * cell_size
            x1 = min(x0 + cell_size, image.width)
            y1 = min(y0 + cell_size, image.height)

            pixel_coords = x0, y0, x1, y1
            pixel_block = image.crop(pixel_coords)

            rgb = average_color(pixel_block)
            lum = luminance(rgb)

            grid[row, col] = (rgb, lum)

    return CellMap(grid, grid_width, grid_height, cell_size, image.width, image.height)

