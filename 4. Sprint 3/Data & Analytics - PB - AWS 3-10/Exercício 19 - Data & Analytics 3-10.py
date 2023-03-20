#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random

random_list = random.sample(range(500), 50)

mediana = 0
media = 0
valor_minimo = 0
valor_maximo = 0

# calcular o valor mínimo
valor_minimo = min(random_list)

# calcular o valor máximo
valor_maximo = max(random_list)

# calcular o valor médio
media = sum(random_list) / len(random_list)

# calcular a mediana
sorted_list = sorted(random_list)
meio = len(sorted_list) // 2
if len(sorted_list) % 2 == 0:
    mediana = (sorted_list[meio - 1] + sorted_list[meio]) / 2
else:
    mediana = sorted_list[meio]
    
# imprimir os resultados
print(f'Media: {media:.2f}, Mediana: {mediana}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}')


# In[ ]:




