from PIL import Image
from glyphize.convert.convert import load, normalize

img = normalize(load("assets/plant_transparent.png"))
img.save("assets/plant_transparent_normalized.png")

orig = load("assets/plant_transparent.png")
print("original mode:", orig.mode)
print("original pixel:", orig.getpixel((0, 0)))

norm = normalize(load("assets/plant_transparent_normalized.png"))
print("normalized mode:", norm.mode)
print("normalized pixel:", norm.getpixel((0, 0)))