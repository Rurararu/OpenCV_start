import cv2
import os

img = cv2.imread(os.path.join('.', 'data', 'white.jpg'))
print(img.shape)

# line
cv2.line(img,(0,0),(736,491),(100,200,100),5)

# rectangle
cv2.rectangle(img,(10,10),(726,481),(134,15,250),10)

# circle
cv2.circle(img,(350, 250),70,(150,50,100), 10)
# text
cv2.putText(img, 'Hell world!', (360, 260), cv2.FONT_HERSHEY_PLAIN, 2.0, (255,0,200), 2)

cv2.imshow('image', img)
cv2.waitKey(0)
