#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import cv2


# In[2]:


def showimg(image):
    cv2.imshow("View", image)
    cv2.waitKey(10000)
    cv2.destroyAllWindows()


# In[3]:


# Creating chess board pattern image
photo = np.zeros((240,240,3))
showimg(photo)
for i in range(30,241,30):
    if((i//30)%2 == 1):
        start = [0,0,255]
        end = [0,0,0]
    else:
        start = [0,0,0]
        end = [0,0,255]
    for j in range(30,241,30):
        cv2.imshow("View", photo)
        cv2.waitKey(100)
        if((j//30)%2 == 1):
            photo[j-30:j,i-30:i]= start
        else:
            photo[j-30:j,i-30:i]= end
        

cv2.destroyAllWindows()
showimg(photo)


# In[ ]:




