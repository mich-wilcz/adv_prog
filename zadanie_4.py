import cv2

image = cv2.imread('res/test.jpg')

(h, w) = image.shape[:2]

x = input("Podaj X:")

y = input("Podaj Y:")

if 0 > int(x) or int(x) >= w:
    print("Bad X")
elif 0 > int(y) or int(y) >= h:
    print("Bad Y")
else:
    image[int(y), int(x)] = (0, 0, 0)

    cv2.imshow("Obrazek", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    