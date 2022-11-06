import cv2
import numpy as np

path = (r'E:\Python Programming\Image\car.jpg')
src = cv2.imread(path)
name = "Image"
image = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
cv2.imshow(name, image)
cv2.waitKey(100)