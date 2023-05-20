#!/usr/bin/env python
# coding: utf-8

# In[2]:


from functools import reduce

def calcula_saldo(lancamentos) -> float:
    valor_final = reduce(lambda acc, x: acc + x[0] if x[1] == 'C' else acc - x[0], map(lambda x: (x[0], x[1]), lancamentos), 0)
    return valor_final

# Testando a função
lancamentos = [(200,'D'), (300,'C'), (100,'C')]
saldo_final = calcula_saldo(lancamentos)
print(saldo_final)


# In[ ]:




