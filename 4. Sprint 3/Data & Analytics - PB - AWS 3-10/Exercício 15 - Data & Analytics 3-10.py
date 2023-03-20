#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Lampada:
    def __init__(self, ligada):
        self.ligada = ligada
        
    def liga(self):
        self.ligada = True
        
    def desliga(self):
        self.ligada = False
        
    def esta_ligada(self):
        return self.ligada

# cria um objeto da classe Lampada com a lâmpada inicialmente ligada
l = Lampada(True)

# liga a lâmpada (se ela já estiver ligada, não faz nada)
l.liga()

# imprime se a lâmpada está ligada ou desligada
print("A lâmpada está ligada?", l.esta_ligada())

# desliga a lâmpada (se ela já estiver desligada, não faz nada)
l.desliga()

# imprime se a lâmpada está ligada ou desligada
print("A lâmpada ainda está ligada?", l.esta_ligada())


# In[ ]:




