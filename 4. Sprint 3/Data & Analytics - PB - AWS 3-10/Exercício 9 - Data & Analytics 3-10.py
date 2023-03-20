#!/usr/bin/env python
# coding: utf-8

# In[3]:


firstNames = ['Joao', 'Douglas', 'Lucas', 'José']
surNames = ['Soares', 'Souza', 'Silveira', 'Pedreira']
ages = [19, 28, 25, 31]

# Itera sobre as listas e imprime os dados
for i, (name, surname, age) in enumerate(zip(firstNames, surNames, ages)):
    print(f"{i} - {name} {surname} está com {age} anos")


# In[ ]:




