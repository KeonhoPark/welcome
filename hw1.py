import cv2
import matplotlib.pyplot as plt

img = cv2.imread('face.bmp')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
plt.plot(hist)
plt.show()

cv2.imshow('dst', gray)
cv2.waitKey()