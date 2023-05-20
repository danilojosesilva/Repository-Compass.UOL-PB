#!/usr/bin/env python
# coding: utf-8

# In[9]:


def imprimir_parametros(*args, **kwargs):
    for arg in args:
        print(arg)
    
    for key, value in kwargs.items():
        print(f"{key}={value}")


imprimir_parametros(1, 3, 4, 'hello', 'alguma coisa', 20)


# In[ ]:




