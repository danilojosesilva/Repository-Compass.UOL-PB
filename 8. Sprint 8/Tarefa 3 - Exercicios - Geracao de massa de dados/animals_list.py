import csv
import codecs
import locale

# Define a localização como português do Brasil
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# Lista de nomes de animais
animais = ["Cachorro", "Gato", "Leão", "Tigre", "Elefante", "Zebra", "Girafa", "Cavalo", "Coelho", "Rato", "Lobo", "Panda", "Urso", "Macaco", "Cobra", "Crocodilo", "Tartaruga", "Gavião", "Águia", "Coruja"]

# Ordena a lista em ordem alfabética considerando acentuação
animais.sort(key=locale.strxfrm)

# Imprime cada animal
for animal in animais:
    print(animal)

# Salva a lista em um arquivo CSV
with codecs.open('animais.csv', 'w', 'utf-8') as file:
    writer = csv.writer(file)
    for animal in animais:
        writer.writerow([animal])
