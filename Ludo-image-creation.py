#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import cv2


# In[2]:


def showimg(image):
    cv2.imshow("View", image)
    cv2.waitKey()
    cv2.destroyAllWindows()


# In[3]:


photo = np.ones((300,300,3))
showimg(photo)
#Colors : bgr value
blue = [255,0,0]
green = [0,255,0]
red = [0,0,255]
yellow = [0,148,255]
black = [0,0,0]
white = [1,1,1]


# In[4]:


# Creating Ludo Borad image
# Creating four colored blocks
photo[0:120,0:120] = blue #blue
photo[0:120,180:300] = green #green
photo[180:300,0:120] = red #red
photo[180:300,180:300] = yellow #yellow
photo[120:180,120:180] = black
showimg(photo)

#Creating lines
for i in range(140,181,20):
    cv2.line(photo,(0,i),(300,i),black,1)
    cv2.line(photo,(i,0),(i,300),black,1)
showimg(photo)

for i in range(0,300,20):
    cv2.line(photo,(120,i),(180,i),black,1)
    cv2.line(photo,(i,120),(i,180),black,1)
showimg(photo)  

#Creating home path 
photo[120:140,20:40] = blue
photo[140:160,20:120] = blue
showimg(photo) 
photo[20:40,160:180] = green
photo[20:120,140:160] = green
showimg(photo) 
photo[160:180,260:280] = yellow
photo[140:160,180:280] = yellow
showimg(photo)
photo[180:280,140:160] = red
photo[260:280,120:140] = red
showimg(photo)

#Creating circles and stops
radius = 10
def makecircle(radius,x1,y1,color):
    x2 = x1 + 41
    y2 = y1 + 41
    for i in range(x1,x2,40):
        for j in range(y1,y2,40):
            cv2.circle(photo,(i,j),radius,color,-1)
            
makecircle(radius,220,40,white)
makecircle(radius,40,40,white)
makecircle(radius,40,220,white)
makecircle(radius,220,220,white)
cv2.circle(photo,(130,50),8,blue,-1)
cv2.circle(photo,(250,130),8,green,-1)
cv2.circle(photo,(170,250),8,yellow,-1)
cv2.circle(photo,(50,170),8,red,-1)
showimg(photo)

#Creating arrows
cv2.arrowedLine(photo, (110,130), (130,110), black, 1,shift=0, tipLength = 0.1) 
cv2.arrowedLine(photo, (170,110), (190,130), black, 1,shift=0, tipLength = 0.1) 
cv2.arrowedLine(photo, (130,190), (110,170), black, 1,shift=0, tipLength = 0.1) 
cv2.arrowedLine(photo, (190,170), (170,190), black, 1,shift=0, tipLength = 0.1) 
showimg(photo)

#Putting text
cv2.putText(photo, "YOU", (130,140),color=white, thickness=1, fontFace=cv2.FONT_HERSHEY_TRIPLEX,fontScale=0.5 ,lineType = cv2.LINE_AA)
showimg(photo)
cv2.putText(photo, "WIN!!", (130,160),color=white, thickness=1, fontFace=cv2.FONT_HERSHEY_TRIPLEX,fontScale=0.5 ,lineType = cv2.LINE_AA)
showimg(photo)


# In[ ]:




