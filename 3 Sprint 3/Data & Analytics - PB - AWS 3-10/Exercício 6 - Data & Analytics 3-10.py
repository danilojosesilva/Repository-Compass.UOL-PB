#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = [1, 1, 2, 3, 5, 8, 14, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Convertendo as listas em conjuntos
set_a = set(a)
set_b = set(b)

# Encontrando a interseção entre os conjuntos
intersection = set_a & set_b

# Convertendo o resultado de volta em uma lista
result = list(intersection)

# Imprimindo a lista de valores em comum
print(result)


# In[ ]:




