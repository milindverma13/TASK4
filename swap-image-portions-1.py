#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np


# In[2]:


def showimg(image):
    cv2.imshow("View", image)
    cv2.waitKey()
    cv2.destroyAllWindows()
    


# In[3]:


img1 = cv2.imread("Documents/boss.jpg")
img2 = cv2.imread("Documents/img1.jpg")
showimg(img1)
showimg(img2) 


# In[4]:


#Cropping faces
face1 = img1[5:128,70:190]
showimg(face1)
face2 = img2[5:180,30:149]
showimg(face2)

#Resizing faces
face2_resize = cv2.resize(face2,(120,123))
showimg(face2_resize) 
face1_resize = cv2.resize(face1,(119,175))
showimg(face1_resize)                          


# In[5]:


#Exchanging faces
img1[5:128,70:190] = face2_resize
showimg(img1)
img2[5:180,30:149] = face1_resize
showimg(img2)


# In[ ]:




