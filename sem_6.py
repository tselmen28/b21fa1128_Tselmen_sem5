# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 18:27:47 2023

@author: tselm
"""

# In[1]:


def myfunction(n):
    for i in range(n):
        for j in range(i+1):
            print('*', end='')
        print()
myfunction(6)


# In[2]:


def myfunction(n):
    for i in range(n):
        for j in range(i+1):
            print('*', end='')
        print()
myfunction(6)


# In[3]:


dict1 = {'Bat':18,'Oyun':22, 'Dulam':21, 'Suren':20}
def func2(dict):
        ih = max(dict, key=dict.get)
        baga= min(dict, key=dict.get)
        return ih, baga
print(func2(dict1))


# In[4]:


import numpy as np
x=(np.arange(1,1000))
sum=0
for i in x:
    if((i%3==0) | (i%7==0)):
        sum += i;
print(sum)