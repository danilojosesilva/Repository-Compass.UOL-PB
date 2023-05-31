import random
import time
import os
import names

random.seed(40)

qtd_nomes_unicos = 3000
qtd_nomes_aleatorios = 10000000

# Gera a lista de nomes únicos
aux = [names.get_full_name() for _ in range(qtd_nomes_unicos)]

print("Gerando {} nomes aleatórios".format(qtd_nomes_aleatorios))

# Gera a lista de nomes aleatórios
dados = [random.choice(aux) for _ in range(qtd_nomes_aleatorios)]

# Salva a lista em um arquivo de texto
with open('nomes_aleatorios.txt', 'w') as file:
    for nome in dados:
        file.write("%s\n" % nome)
