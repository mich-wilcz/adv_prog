import cv2

image = cv2.imread('res/czolg.jpg')


(h, w) = image.shape[:2]

image[50:100, 50:100] = (255, 255, 255)

cv2.imshow("Original", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
