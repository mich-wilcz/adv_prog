import cv2
image = cv2.imread("res/cat.jpg", cv2.IMREAD_GRAYSCALE)

cv2.imshow("Obraz w skali szarości", image)


if len(image.shape) == 2:
    print("1 kanał kolorów")
else:
    (h, w, c) = image.shape[:3]
    print(f'channels: {c}')

cv2.waitKey(0)
cv2.destroyAllWindows()
