#!/usr/bin/env python
# coding: utf-8

# In[3]:


words = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']

for word in words:
    if word == word[::-1]:
        print(f"A palavra: {word} é um palíndromo")
    else:
        print(f"A palavra: {word} não é um palíndromo")


# In[ ]:




