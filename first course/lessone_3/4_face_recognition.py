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


image_path = 'extern_data/gDnoFvQJ_400x400.jpg'
image = cv2.imread(image_path)
face_cascade = cv2.CascadeClassifier('extern_data/haarcascade_frontalface_default.xml')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(10, 10),
)

# рисование квадратов вокруг лиц
for (x, y, w, h) in faces:
    cv2.rectangle(gray, (x, y), (x+w, y+h), (100, 150, 200), 10)
view_image(gray, 'Faces detect')
