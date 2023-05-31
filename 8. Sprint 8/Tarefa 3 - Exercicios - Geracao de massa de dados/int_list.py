import random

# Gera uma lista de 250 números aleatórios entre 1 e 1000
lista = [random.randint(1, 1000) for _ in range(250)]

# Inverte a lista
lista.reverse()

# Imprime a lista
print(lista)
