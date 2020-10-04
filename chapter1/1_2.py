#!/usr/bin/env python
# coding: utf-8

# In[8]:


def reverse_string(test_str):
    reverse_str = ''
    for i in range(len(test_str),0,-1):
        reverse_str = reverse_str + test_str[i-1]
    print(reverse_str)

reverse_string('usa')


# In[ ]:




