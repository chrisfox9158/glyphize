from glyphize.convert.convert import convert

cell_map = convert("assets/skeleton.jpg", cell_size=8)
print(cell_map.grid_width, cell_map.grid_height)
print(cell_map.grid[0, 0])
print(cell_map.grid[30, 5])
print(cell_map.grid[40, 38])
print(cell_map.grid[cell_map.grid_height // 2, cell_map.grid_width // 2])