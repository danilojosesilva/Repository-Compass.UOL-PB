#!/usr/bin/env python
# coding: utf-8

# In[ ]:


with open("arquivo_texto.txt", "r") as arquivo:
    conteudo = arquivo.readlines()
    for linha in conteudo:
        print(linha, end="")

