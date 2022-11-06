import cv2
img = cv2.imread(r'E:\Python Programming\Image\car.jpg', 1)
height = img.shape[0]
width = img.shape[1]
channels = img.shape[2]
s = img.size

print("Image Height : ", height)
print("Image width : ", width)
print("Number of channels : ",channels)
print("Image size : ",s)