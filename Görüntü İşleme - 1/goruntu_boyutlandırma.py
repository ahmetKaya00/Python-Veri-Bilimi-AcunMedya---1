import cv2

image = cv2.imread("logo.png")

new_width = 400
new_height = int(image.shape[0] * (new_width / image.shape[1]))

resized_image = cv2.resize(image, (new_width, new_height))

cv2.imshow("Boyutlandirilmis Goruntu", resized_image)


cv2.waitKey(0)
cv2.destroyAllWindows()

rotate_90 = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

cv2.imshow("90 Derece Dondurulmus Goruntu",rotate_90)
cv2.waitKey(0)
cv2.destroyAllWindows()

cropped_image = image[50:250,50:250]

cv2.imshow("Kirpilmis Goruntu",cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

