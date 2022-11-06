import cv2
import numpy as np

cam = cv2.VideoCapture(0)  
cv2.namedWindow("Capture Image") 
img = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to Capture Photo")
        break
    cv2.imshow("capture Image", frame)

    k = cv2.waitKey(1)
    if k%249 == 27:  #keyboard 27 Number key means ESC
        print("Press Esc for closing window ...!")
        break
    elif k%249 == 32: #keyboar 32 number key means Space
        img_name = "Photo{}.jpg".format(img)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img = img + 1

cam.release()
cv2.destroyAllWindows()
