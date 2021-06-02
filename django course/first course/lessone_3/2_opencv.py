import cv2

image = cv2.imread('extern_data/unnamed.jpg')
print(type(image))
# загрузка происходит в BGR, а не RGB


def view_image(image, name_of_window: str):
    """

    :param name_of_window: str
    :type image: object
    to destroy press any key
    """
    cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
    cv2.imshow(name_of_window, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# ресайз слайсами
cropped = image[20:40, 0:1000]
view_image(cropped, 'Cropped image')


# cv2.resize
scale_percent = 120
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dim = (width, height)
# Итерполяция - cv2.INTER_AREA
# Алгоритм, который будет высчитывать 'пустые' пикселы
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
view_image(resized, 'Resize image')


# cv2.cvtColor
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
view_image(gray_image, 'Gray version')
