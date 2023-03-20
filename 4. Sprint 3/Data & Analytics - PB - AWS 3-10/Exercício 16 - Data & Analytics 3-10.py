#!/usr/bin/env python
# coding: utf-8

# In[2]:


def soma_string(string_numeros):
    numeros = string_numeros.split(',')
    soma = 0
    for num in numeros:
        soma += int(num)
    return soma

# string de entrada
string_numeros = "1,3,4,6,10,76"

# chama a função para obter a soma dos valores
soma = soma_string(string_numeros)

# imprime a soma dos valores
print(soma)


# In[ ]:




