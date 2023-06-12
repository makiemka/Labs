from PIL import Image

def mirror():
    img = Image.open("image.jpg")

    width, height = img.size

    new_img = img.copy()

    for x in range(width // 2):
        for y in range(height):
            pixel1 = img.getpixel((x, y))
            pixel2 = img.getpixel((width - x - 1, y))
            new_img.putpixel((x, y), pixel2)
            new_img.putpixel((width - x - 1, y), pixel1)

    new_img.save("res.jpg")