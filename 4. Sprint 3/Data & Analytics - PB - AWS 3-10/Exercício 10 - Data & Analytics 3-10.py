#!/usr/bin/env python
# coding: utf-8

# In[1]:


def remove_duplicates(lst):
    new_lst = list(set(lst))
    return new_lst

lst = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']
new_lst = remove_duplicates(lst)
print(new_lst)


# In[ ]:




