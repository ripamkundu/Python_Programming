import cv2
import numpy as np 
cap = cv2.VideoCapture(0)
cv2.namedWindow("Capture Image")
img = 0
while (Ture):
    ret, frame = cap.read()
    if not ret:
        print("Faild to Capture.!")
        break
    cv2.imshow("Capture image", frame)
    k = cv2.waitkey(1)
    if k%249 ==27:
        print("Press ESC colse the Window")
        break
    elif k%249 ==32:
        img_name ="picture {}.jpg". format(img)
        cv2.imwrite(img_name, frame)
        print("{} Written..!".format(img_name))
        img = img+1
cap.release()
cv2.destroyAllWindows()