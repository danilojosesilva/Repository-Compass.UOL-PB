#!/usr/bin/env python
# coding: utf-8

# In[2]:


def dividir_lista(lista):
    tamanho = len(lista)
    tamanho_terco = tamanho // 3
    
    lista1 = lista[:tamanho_terco]
    lista2 = lista[tamanho_terco:2*tamanho_terco]
    lista3 = lista[2*tamanho_terco:]
    
    return lista1, lista2, lista3


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

lista1, lista2, lista3 = dividir_lista(lista)

print(lista1, lista2, lista3)  


# In[ ]:




