#!/usr/bin/env python
# coding: utf-8

# In[43]:


import numpy as np
x = np.array([0,110,220,340,470,590])
y = np.array([0,8,9,1,-8,-10])
print(x)
print(y)


# In[44]:


#Create a fit, Import a scipy package
from scipy.interpolate import *


# In[96]:


p1 = np.polyfit(x,y,1)


# In[67]:


print(p1)


# In[94]:


#import plotting tool 
from matplotlib.pyplot import *


# In[95]:


get_ipython().run_line_magic('matplotlib', 'inline')


# 

# In[93]:


#This plots the blue dots
plot(x,y,'o')
#This plots the red line and linear fit too (USE *****"NP." in front of command)
plot(x,np.polyval(p1,x),'r-')


# In[97]:


#show linear fit with data
plot(x,np.polyval(p1,x))


# In[92]:


#Quadratic and cubic forms 
p1 = np.polyfit(x,y,1)
p2 = np.polyfit(x,y,2)
p3 = np.polyfit(x,y,3)
print(p1)
print(p2)
print(p3)


# In[101]:


plot(x,y,'o')
plot(x,np.polyval(p1,x),'r-')
#squared has green line
plot(x,np.polyval(p2,x),'g:')
#cubed form has blue dashed line
plot(x,np.polyval(p3,x),'b--')


# In[117]:


#substituting Q & R for x & y
q = np.array([0,1,2,3,4,5])
r = np.array([0,0.8,0.9,0.1,-0.8,-1])

#New versions of p1,p2,p3 = p4,p5,p6
p4 = np.polyfit(q,r,1)
p5 = np.polyfit(q,r,2)
p6 = np.polyfit(q,r,3)

plot(q,r,'o')
#make the chart look smoother
xp = np.linspace(-2,6,100)
plot(xp,np.polyval(p4,xp),'r-')
#squared has green line
plot(xp,np.polyval(p5,xp),'g:')
#cubed form has blue dashed line
plot(xp,np.polyval(p6,xp),'b--')

#CUBIC style -> totally changed from above graph


# In[118]:


#Calculate the r squared value from the line of best fit (in RED)
yfit = p1[0] * x + p1[1]
print(yfit)
print(y)


# In[120]:


np.yresid = y - yfit
ssresid = sum(pow(yresid, 2))
SStotal = len(y) * np.var(y)
#sum of squares of residuals/ total
rsq = 1 - SSresid/SStotal
#print r squared
print(rsq)
#Conclusion: r squared value is close to 1, line is good!


# In[ ]:




