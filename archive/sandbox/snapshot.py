import cv2
cam = cv2.VideoCapture(0)
#cam.set(3,320)
#cam.set(4,240)
ret,frame = cam.read()
cv2.imwrite("NewPicture.jpg",frame)
cam.release()
