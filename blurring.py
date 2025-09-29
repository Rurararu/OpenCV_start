import cv2
import os

img = cv2.imread(os.path.join('.', 'data', 'img.jpg'))

k_size = 15
img_blur = cv2.blur(img, (k_size, k_size))
img_blur_Gaussian = cv2.GaussianBlur(img, (k_size, k_size), 5)
img_blur_median = cv2.medianBlur(img, k_size)


cv2.imshow('img', img)

# cv2.imshow('img_blur', img_blur)
# cv2.imshow('img_blur_Gaussian', img_blur_Gaussian)
# cv2.imshow('img_blur_median', img_blur_median)
cv2.waitKey(0)