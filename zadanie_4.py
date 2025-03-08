import cv2

image = cv2.imread("res/cat.jpg", cv2.IMREAD_GRAYSCALE)

cv2.imshow("Obraz w skali szarości", image)

cv2.imwrite('res/gray_cat.jpg', image)

cv2.waitKey(0)
cv2.destroyAllWindows()
