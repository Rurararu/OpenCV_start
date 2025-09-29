import cv2
import os

img = cv2.imread(os.path.join('.', 'data', 'img.jpg'))

img_convert = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_convert_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_convert_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)



cv2.imshow('img', img)
# cv2.imshow('img_convert', img_convert)
# cv2.imshow('img_convert_gray', img_convert_gray)
cv2.imshow('img_convert_hsv', img_convert_hsv)

cv2.waitKey(0)

