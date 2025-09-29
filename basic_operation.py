import cv2
import os

# #resizing
# img = cv2.imread(os.path.join('.','data', 'img.jpg'))
#
# resized_img = cv2.resize(img, (640, 360))
#
# print(img.shape)
# print(resized_img.shape)
#
#
# cv2.imshow('img', img)
# cv2.imshow('resized_img', resized_img)
#
# cv2.waitKey(0)

#crop

img = cv2.imread(os.path.join('.', 'data', 'img.jpg'))

print(img.shape)

cropped_img = img[100:300, 320:560]

cv2.imshow('img', img)
cv2.imshow('cropped_img', cropped_img)

cv2.waitKey(0)






