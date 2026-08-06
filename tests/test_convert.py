from PIL import Image
from glyphize.convert.convert import convert

cell_map = convert("assets/skeleton.jpg", cell_size=8)
print(cell_map.grid_width, cell_map.grid_height)
print(cell_map.grid[0, 0])
print(cell_map.grid[30, 5])
print(cell_map.grid[40, 38])
print(cell_map.grid[cell_map.grid_height // 2, cell_map.grid_width // 2])

def preview_brightness(cell_map, output_path=None):
    preview = Image.new("L", (cell_map.grid_width, cell_map.grid_height))
    pixels = preview.load()

    for row in range(cell_map.grid_height):
        for col in range(cell_map.grid_width):
            brightness = cell_map.grid[row, col]["brightness"]
            pixels[col, row] = int(brightness * 255)

    preview = preview.resize(
        (cell_map.grid_width * cell_map.cell_size, cell_map.grid_height * cell_map.cell_size),
        Image.Resampling.NEAREST
    )

    if output_path:
        preview.save(output_path)
    else:
        preview.show()

preview_brightness(cell_map, "assets/skeleton_brightness_preview.png")