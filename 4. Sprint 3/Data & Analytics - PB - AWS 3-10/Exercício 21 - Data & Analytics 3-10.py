#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Passaro:
    def voar(self):
        print("Voando...")

    def emitir_som(self):
        print("Passaro emitindo som...")


class Pato(Passaro):
    def emitir_som(self):
        print("Quack Quack")


class Pardal(Passaro):
    def emitir_som(self):
        print("Piu Piu")
        

pato = Pato()
print("Pato")
pato.voar()
pato.emitir_som()

pardal = Pardal()
print("Pardal")
pardal.voar()
pardal.emitir_som()


# In[ ]:




