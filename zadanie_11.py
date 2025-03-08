import cv2
import math

image = cv2.imread('res/czolg.jpg')

(h, w) = image.shape[:2]

(b, g, r) = (0, 0, 0)
(c1, c2) = (0, 0)

for x in range(w):
    for y in range(h):
        (b1, g1, r1) = image[y, x]
        if int(b1) + int(g1) + int(r1) > int(b + g + r):
            (b, g, r) = (b1, g1, r1)
            (c1, c2) = (x, y)



print("Jasne- Red: {}, Green: {}, Blue: {}".format(r, g, b))
print("Gdzie: x: {} y: {}".format(c1, c2))
cv2.waitKey(0)
cv2.destroyAllWindows()