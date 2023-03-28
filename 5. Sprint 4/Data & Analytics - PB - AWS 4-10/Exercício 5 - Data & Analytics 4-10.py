#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import csv

with open('estudantes.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    
    for row in sorted(reader):
        nome = row[0]
        notas = list(map(int, row[1:]))
        tres_maiores_notas = sorted(notas, reverse=True)[:3]
        media_tres_maiores_notas = round(sum(tres_maiores_notas) / 3, 2)
        print(f'Nome: {nome} Notas: {tres_maiores_notas} Média: {media_tres_maiores_notas}')

