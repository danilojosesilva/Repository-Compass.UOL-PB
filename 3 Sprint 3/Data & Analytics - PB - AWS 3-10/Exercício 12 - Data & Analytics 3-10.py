#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json

# abre o arquivo person.json
with open('person.json', 'r') as f:
    # carrega o conteúdo do arquivo em um objeto Python
    data = json.load(f)

# imprime o conteúdo do objeto Python
print(data)

