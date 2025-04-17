import cv2
import numpy as np

image = cv2.imread("logo.png")

blue_channel, green_channel, red_channel = cv2.split(image)

cv2.imshow("Mavi Kanal",blue_channel)
cv2.imshow("Yeşil Kanal",green_channel)
cv2.imshow("Kırmızı Kanal",red_channel)

cv2.waitKey(0)
cv2.destroyAllWindows()

modified_image = cv2.merge([green_channel,red_channel,blue_channel])

cv2.imshow("Degistirilmis Renkler", modified_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
hsv_image = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

cv2.imshow("Gri Tonlama", gray_image)
cv2.imshow("HSV Goruntu", hsv_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

lower_red = np.array([0,120,70])
upper_red = np.array([10,255,255])

mask = cv2.inRange(hsv_image,lower_red,upper_red)

cv2.imshow("Kirmizi Renk Maskesi:",mask)
cv2.waitKey(0)
cv2.destroyAllWindows()