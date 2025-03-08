import cv2

image = cv2.imread('res/czolg.jpg')

cv2.imshow("Original", image)

(h, w) = image.shape[:2]

(cX, cY) = (w // 3, h // 3)

part = image[cY:cY+cY, cX:cX+cX]

cv2.imshow("Part", part)

cv2.waitKey(0)
cv2.destroyAllWindows()
