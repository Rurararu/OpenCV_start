import cv2
import os

img = cv2.imread(os.path.join('.', 'data', 'img.jpg'))

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 85, 255, cv2.THRESH_BINARY)

img_thresh = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 10)
# img_thresh = cv2.blur(img_thresh, (25, 25))

# cv2.imshow('img', img)
# cv2.imshow('img_gray', img_gray)
# cv2.imshow('thresh', thresh)
cv2.imshow('img_thresh', img_thresh)
cv2.waitKey(0)