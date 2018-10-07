from PIL import Image, ImageFilter
import time
#import cv2
import numpy as np

#Read image
#im = cv2.imread( 'Images/testimage.jpg', mode='RGB')
#print type(im)

class imageImport:
    def __init__(self):
        self.image = 1

    def get_image_data(self):
        img = Image.open('Images/testimage.jpg')
        img.load()
        data = np.asarray(img, dtype="int32")

        return data

#Applying a filter to the image
#im_sharp = im.filter( ImageFilter.SHARPEN )
#Saving the filtered image to a new file
#im_sharp.save( 'image_sharpened.jpg', 'JPEG' )

#Splitting the image into its respective bands, i.e. Red, Green,
#and Blue for RGB
'''
r,g,b = im.split()
im.imshow('image',im)
time.sleep(5)

#Viewing EXIF data embedded in image
exif_data = im._getexif()
exif_data
'''
