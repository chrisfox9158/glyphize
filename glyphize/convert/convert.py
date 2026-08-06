from PIL import Image

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

