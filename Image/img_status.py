import cv2
import numpy as np 
img = (r'E:\Python Programming\Image\Ripam.jpg')
src = cv2.imread(img)
window_name = 'Image'
image = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
cv2.imshow(window_name, image)
cv2.waitkey(3000)