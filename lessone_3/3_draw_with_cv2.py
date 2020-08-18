import cv2


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


image = cv2.imread('extern_data/s1200.jpeg')
view_image(image, 'Standard version')

# для отрисовки необходимы:
# координаты начала и конца, цвет, толщина
image_with_line = image.copy()
cv2.line(image_with_line, (10, 100), (800, 495), (23, 40, 90), 10)
view_image(image_with_line, 'Line')

# для отрисовки необходимы:
# координаты левого верхнего и правого нижнего углов, цвет, толщина
image_with_rectangle = image.copy()
cv2.rectangle(image_with_rectangle, (900, 900), (495, 10), (90, 40, 23), 5)
view_image(image_with_rectangle, 'Rectangle')
