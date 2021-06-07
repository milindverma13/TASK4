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


img1 = cv2.imread("Documents/btrfly.jpg")
img2 = cv2.imread("Documents/flower.jpg")
showimg(img1)
showimg(img2) 


# In[4]:


bfly = img1[35:150,230:350]
showimg(bfly)
flower = img2[80:230,60:230]
showimg(flower)


# In[5]:


img2[35:150,230:350] = bfly
img1[80:230,60:230] = flower
showimg(img1)
showimg(img2)


# In[ ]:




