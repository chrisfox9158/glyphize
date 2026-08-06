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
