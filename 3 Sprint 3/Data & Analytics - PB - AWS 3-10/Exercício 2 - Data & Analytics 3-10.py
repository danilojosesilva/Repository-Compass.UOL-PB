#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Lê os números do teclado
numeros = []
for i in range(3):
    numero = int(input("Digite o {}° número: ".format(i+1)))
    numeros.append(numero)

# Verifica se cada número é par ou ímpar e imprime o resultado
for numero in numeros:
    if numero % 2 == 0:
        print("Par: {}".format(numero))
    else:
        print("Ímpar: {}".format(numero))


# In[ ]:




