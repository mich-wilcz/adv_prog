import cv2

image = cv2.imread("res/cat.jpg")

image_error = cv2.imread("res/catsss.jpg")

# weryfikacja poprawnej ścieżki
if image is None:
    print("Błąd: nie można wczytać obrazu!")
else:
    print("Obraz wczytano poprawnie.")


cv2.imshow("Wyświetlony obraz", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# dla niepoprawnej ścieżki przerywane zostało działanie programu
