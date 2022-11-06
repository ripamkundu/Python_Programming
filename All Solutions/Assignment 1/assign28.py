# the Size (Resolution) of a Image

def jpeg(image):
   with open(image,'rb') as photo:
    photo.seek(165)
    
    a = photo.read(2)
    height = (a[0] << 8) + a[1]
    
    a = photo.read(2)
    width = (a[0] << 8) + a[1]

   print("The resolution of the image is : ",width,"x",height)
jpeg("img.jpg")