#!/usr/bin/env python
# coding: utf-8

# In[2]:


def conta_vogais(texto:str)-> int:
    vogais = "aeiou"
    return len(list(filter(lambda x: x in vogais, texto.lower())))

# Teste de função
texto = "String de exemplo"
num_vogais = conta_vogais(texto)
print(num_vogais)


# In[ ]:




