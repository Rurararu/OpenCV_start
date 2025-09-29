import cv2
import os
import numpy as np

img = cv2.imread(os.path.join('.', 'data', 'img.jpg'))

img_edg = cv2.Canny(img, 100, 25)

img_edge_dilate = cv2.dilate(img_edg, np.ones((3, 3), dtype=np.int8))

img_edge_erode = cv2.erode(img_edge_dilate, np.ones((3, 3), dtype=np.int8))

cv2.imshow('img', img)
cv2.imshow('edg', img_edg)
cv2.imshow('edge_dilate', img_edge_dilate)
cv2.imshow('edge_erode', img_edge_erode)
cv2.waitKey(0)
