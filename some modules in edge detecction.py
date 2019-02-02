import numpy as np
import cv2

img=cv2.imread(r"D:\project\OMR\images\new omr\new22.png",0)
#image=cv2.resize(img,(520,520))
canny=cv2.Canny(img,200,600)
cv2.imshow("canny",canny)
'''lower=np.array([0,0,0])
upper=np.array([45,45,45])
shape=cv2.inRange(image,lower,upper)'''
images,contours, hierarchy =cv2.findContours(canny.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
print(contours)

cv2.drawContours(img, contours, -1, (0,255,0), 1)

#-----------invert the image-----------
invert=cv2.bitwise_not(canny)
cv2.imshow("sfd",invert)

#---------create kernel of ones-------------
kernel = np.ones((5,5),np.uint8)

#----------perform dilation--------------
dilation=cv2.dilate(invert,kernel,iterations=1)
inverted_canny=cv2.Canny(invert,200,600)
#-------------find edges--------
images,contours, hierarchy =cv2.findContours(inverted_canny.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(inverted_canny, contours, -1, (0,255,0), 1)
cv2.imshow("dilation of image",dilation)
cv2.imshow('Contours', img)
