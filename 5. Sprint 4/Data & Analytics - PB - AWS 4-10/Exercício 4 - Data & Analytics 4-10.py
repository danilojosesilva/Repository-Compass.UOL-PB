#!/usr/bin/env python
# coding: utf-8

# In[6]:


def calcular_valor_maximo(operadores, operandos) -> float:
    operacoes = {'+': lambda x, y: x + y,
                 '-': lambda x, y: x - y,
                 '*': lambda x, y: x * y,
                 '/': lambda x, y: x / y,
                 '%': lambda x, y: x % y}

    resultados = map(lambda xy: operacoes[xy[0]](xy[1][0], xy[1][1]), zip(operadores, operandos))
    return max(resultados)

# Teste de função
operadores = ['+','-','*','/','+']
operandos  = [(3,6), (-7,4.9), (8,-8), (10,2), (8,4)]

resultado = calcular_valor_maximo(operadores, operandos)

print(resultado) # Saída esperada: 12.0


# In[ ]:




