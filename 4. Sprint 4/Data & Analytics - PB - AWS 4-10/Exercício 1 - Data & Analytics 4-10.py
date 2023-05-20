#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Lê o arquivo com os números inteiros
with open('number.txt', 'r') as arquivo:
    numeros = list(map(int, arquivo.readlines()))

# Filtra apenas os números pares
pares = filter(lambda x: x % 2 == 0, numeros)

# Mapeia os números pares para o negativo
negativos = map(lambda x: -x, pares)

# Ordena os números pares em ordem decrescente
maiores_pares_negativos = sorted(negativos)[:5]

# Mapeia os números negativos para o positivo novamente
maiores_pares = list(map(lambda x: -x, maiores_pares_negativos))

# Calcula a soma dos 5 maiores números pares
soma_maiores_pares = sum(maiores_pares)

# Exibe o resultado na saída
print(f'{maiores_pares}')
print(f'{soma_maiores_pares}')

