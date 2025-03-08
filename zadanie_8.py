import cv2
import math

image = cv2.imread('res/czolg.jpg')

(h, w) = image.shape[:2]

(b1, g1, r1) = image[50, 50]
(b2, g2, r2) = image[200, 200]

print("Difference- Red: {}, Green: {}, Blue: {}".format(abs(r1-r2), (g1-g2), (b1-b2)))

cv2.waitKey(0)
cv2.destroyAllWindows()