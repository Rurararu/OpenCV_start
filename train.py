import cv2
import os

# # read img
# image_path = os.path.join('.','data', 'img.jpg')
#
# img = cv2.imread(image_path)
#
# # write img
# cv2.imwrite(os.path.join('.','data', 'img_out.jpg'), img)
#
#
# #visualize img
# cv2.imshow('img', img)
# cv2.waitKey(0)



# # read video
# video_path = os.path.join('.','data','cat.mov')
#
# video = cv2.VideoCapture(video_path)
#
# #visualize video
# ret = True
# while ret:
#     ret, frame = video.read()
#
#     if ret:
#         cv2.imshow('frame',frame)
#         cv2.waitKey(1)
#
# video.release()
# cv2.destroyAllWindows()



# read webcam
webcam = cv2.VideoCapture(0)

#visualize webcam

while True:
    ret, frame = webcam.read()

    cv2.imshow('frame', frame)
    if cv2.waitKey(40) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()