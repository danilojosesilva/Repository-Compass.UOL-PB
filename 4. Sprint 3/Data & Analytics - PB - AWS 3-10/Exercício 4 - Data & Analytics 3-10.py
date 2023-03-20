#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Verifica se um número é primo
def primos(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5)+1):
        if numero % i == 0:
            return False
    return True

# Imprime todos os números primos entre 1 e 100
for i in range(1, 101):
    if primos(i):
        print(i)


# In[ ]:




