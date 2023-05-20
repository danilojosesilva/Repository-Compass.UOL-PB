#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Ordenadora:
    def __init__(self, listaBaguncada):
        self.listaBaguncada = listaBaguncada
        
    def ordenacaoCrescente(self):
        self.listaBaguncada.sort()
        return self.listaBaguncada
    
    def ordenacaoDecrescente(self):
        self.listaBaguncada.sort(reverse=True)
        return self.listaBaguncada

# Instanciando o primeiro objeto com lista [3,4,2,1,5] e ordenando de forma crescente
crescente = Ordenadora([3,4,2,1,5])
print(crescente.ordenacaoCrescente()) # Saída: [1, 2, 3, 4, 5]

# Instanciando o segundo objeto com lista [9,7,6,8] e ordenando de forma decrescente
decrescente = Ordenadora([9,7,6,8])
print(decrescente.ordenacaoDecrescente()) # Saída: [9, 8, 7, 6]


# In[ ]:




