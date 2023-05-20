#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Aviao:
    cor = "azul"
    
    def __init__(self, modelo, velocidade_maxima, capacidade):
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.capacidade = capacidade

        
avioes = []

modelo = "BOIENG456"
velocidade_maxima = "1500 km/h"
capacidade = 400
aviao1 = Aviao(modelo, velocidade_maxima, capacidade)
avioes.append(aviao1)

modelo = "Embraer Praetor 600"
velocidade_maxima = "863 km/h"
capacidade = 14
aviao2 = Aviao(modelo, velocidade_maxima, capacidade)
avioes.append(aviao2)

modelo = "Antonov An-2"
velocidade_maxima = "258 km/h"
capacidade = 12
aviao3 = Aviao(modelo, velocidade_maxima, capacidade)
avioes.append(aviao3)


for aviao in avioes:
    print(f"O avião de modelo '{aviao.modelo}' possui uma velocidade máxima de '{aviao.velocidade_maxima}', capacidade para '{aviao.capacidade}' passageiros e é da cor '{aviao.cor}'.")


# In[ ]:




