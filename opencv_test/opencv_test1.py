#python3
import cv2
import numpy as np

print(cv2.__version__)
image = cv2.imread('face.jpg',cv2.IMREAD_UNCHANGED)
height, width, channel= image.shape

print(height)
print(width)
print(channel)

#flip
image_flip=cv2.flip(image,0)#0 : updown / 1 : leftright

#locate
matrix=cv2.getRotationMatrix2D((width/2,height/2),45,1)
image_rocate=cv2.warpAffine(image,matrix,(width,height))

#colorchange
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('imagewindow',image)
cv2.imshow('imagewindow2',image_flip)
cv2.imshow('imagewindow3',image_rocate)
cv2.imshow('imagewindow4',image_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
