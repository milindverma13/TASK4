#!/usr/bin/env python
# coding: utf-8

# In[47]:


import cv2
import numpy


# In[48]:


def showimg(image):
    cv2.imshow("View Image", image)
    cv2.waitKey()
    cv2.destroyAllWindows()
    
def verticalcollage(image_list):
    resize_img=[]
    for i in image_list:
        resize_img.append( cv2.resize(i,(350,250)))
    collage = numpy.vstack(tuple(resize_img))
    return collage
    
def horizontalcollage(image_list):
    resize_img=[]
    for i in image_list:
        resize_img.append( cv2.resize(i,(350,250)))
    collage = numpy.hstack(tuple(resize_img))
    return collage
  


# In[49]:


img1=cv2.imread("sample_images/flower.jpg")
img2=cv2.imread("sample_images/btrfly.jpg")
showimg(img1)
showimg(img2)


# In[50]:


hcollage = horizontalcollage((img1,img2))
showimg(hcollage)
vcollage = verticalcollage((img1,img2))
showimg(vcollage)


# In[53]:


img3=cv2.imread("sample_images/pink.jpg")
showimg(img3)


# In[52]:


hcollage = horizontalcollage((img1,img2,img3))
showimg(hcollage)
vcollage = verticalcollage((img1,img2,img3))
showimg(vcollage)


# In[ ]:




