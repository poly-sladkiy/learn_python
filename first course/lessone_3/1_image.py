from PIL import Image, ImageDraw
import time


def negative(pix):
    for i in range(width // 2):
        for j in range(height // 2):
            a = 255 - pix[i, j][0]
            b = 255 - pix[i, j][1]
            c = 255 - pix[i, j][2]
            draw.point((i, j), (a, b, c))  # (255 - a, 255 - b, 255 - c)


def gray_shape(pix):
    for i in range(width // 2, width):
        for j in range(height // 2):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            s = (a + b + c) // 3
            draw.point((i, j), (s, s, s))


def sepia(pix):
    depth = 30
    for i in range(width // 2):
        for j in range(height // 2, height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            s = (a + b + c) // 3
            a = s + depth * 2
            b = s + depth
            c = s
            if a > 255:
                a = 255
            if b > 255:
                b = 255
            if c > 255:
                c = 255
            draw.point((i, j), (a, b, c))


image = Image.open('extern_data/gDnoFvQJ_400x400.jpg')
pixels = image.load()
draw = ImageDraw.Draw(image)  # кисточка
# Определяем ширину и высоту
width = image.size[0]
height = image.size[1]
print(f'Ширина изображения - {width}, высота - {height}')

start = time.monotonic()
negative(pixels)
gray_shape(pixels)
sepia(pixels)
result = time.monotonic() - start
print(f'Все 3 функции сработали за {result} сек.')

del draw
image.save('extern_data/400x400_effect.jpg')
