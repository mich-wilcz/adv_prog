import cv2

image = cv2.imread('res/czolg.jpg')

cv2.imshow("Original", image)

(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)
(b, g, r) = image[cX, cY]

print("Pixel at  middle - Red: {}, Green: {}, Blue: {}".format(r, g, b))

cv2.waitKey(0)
cv2.destroyAllWindows()
