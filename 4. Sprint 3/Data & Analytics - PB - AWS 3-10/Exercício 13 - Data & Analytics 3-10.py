#!/usr/bin/env python
# coding: utf-8

# In[1]:


def my_map(lista, f):
    return [f(elemento) for elemento in lista]


# define a função que calcula a potência de 2 para cada elemento
def potencia_de_2(x):
    return x ** 2

# define a lista de entrada
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# aplica a função my_map para a lista de entrada e a função potencia_de_2
nova_lista = my_map(lista, potencia_de_2)

# imprime a nova lista
print(nova_lista)


# In[ ]:




