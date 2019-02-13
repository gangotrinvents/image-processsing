
import numpy as np
import cv2
image=cv2.imread(r"C:\Users\ashum\OneDrive\Desktop\sudoko.jpeg")
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
edges=cv2.Canny(gray,50,150)
minl=100
maxl=10
lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minl,maxl)
print(lines)
for i in range(0,72):
    cv2.line(image,(lines[i][0][0],lines[i][0][1]),(lines[i][0][2],lines[i][0][3]),(0,255,0),2)
    cv2.imshow("line",image)
cv2.imshow('houghlines5.jpg',image)

