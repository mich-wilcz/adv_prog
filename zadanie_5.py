import cv2


image = cv2.imread("res/cat.jpg")

image2 = cv2.imread("res/gray_cat.jpg", cv2.IMREAD_GRAYSCALE)

cv2.imshow("Obraz 1", image)
cv2.imshow("Obraz 2", image2)

cv2.waitKey(0)
cv2.destroyAllWindows()
