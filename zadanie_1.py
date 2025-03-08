import cv2

image = cv2.imread('res/czolg.jpg')

cv2.imshow("Original", image)

(b, g, r) = image[0, 0]

print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

cv2.waitKey(0)
cv2.destroyAllWindows()