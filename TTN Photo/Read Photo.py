import easyocr
import cv2
import numpy as np
from matplotlib import pyplot as plt




img = cv2.imread('photo_3.jpeg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

_, binary = cv2.threshold(gray, 125,255,cv2.THRESH_BINARY)
# plt.imshow(binary,cmap='gray')
# plt.show()
# test = cv2.imwrite('test.jpeg', binary)
# #
# reader = easyocr.Reader(["ru"])
# result = reader.readtext('photo_3.jpeg',detail=0)
# print(result)

contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
img = cv2.drawContours(img,contours, -1, (0,255,0), 1)
plt.imshow(img)
plt.show()