# Geração de Massa de Dados em Python

Este repositório contém scripts Python para a geração e manipulação de conjuntos de dados (massa de dados) para uso em testes, simulações e outras aplicações que requerem uma grande quantidade de dados. As tarefas realizadas pelos scripts incluem a geração de listas de números aleatórios, a criação e manipulação de listas de strings, e a geração de grandes conjuntos de nomes de pessoas aleatórios.

## Geração e Manipulação de Listas de Números Aleatórios

O primeiro script (**int_list.py**) gera uma lista de 250 números inteiros aleatórios, inverte a ordem dos elementos da lista, e imprime a lista resultante. Este script utiliza a biblioteca random que já vem pré-instalada com Python e não requer nenhuma outra dependência.

<p align="center"><img src="assets\Print_1.jpg"></p>

## Criação e Manipulação de Listas de Strings

O segundo script (**animals_list.py**) cria uma lista de 20 nomes de animais, ordena a lista em ordem alfabética considerando a acentuação, imprime os nomes dos animais um a um, e grava a lista de nomes em um arquivo no formato CSV (**animais.csv**). Este script utiliza as bibliotecas `codecs` e `csv` para garantir a correta codificação dos caracteres e a gravação em arquivo CSV, e a biblioteca `locale` para realizar a ordenação correta das strings com acentos.

<p align="center"><img src="assets\Print_2.jpg"></p>

<p align="center"><img src="assets\Print_3.jpg"></p>

## Geração de Conjuntos de Dados de Nomes de Pessoas Aleatórios

O terceiro script (**random_names.py**) gera um conjunto de dados de nomes de pessoas aleatórios e grava-os em um arquivo de texto (**nomes_aleatorios.txt**). Este script utiliza a biblioteca `names` para a geração dos nomes e a biblioteca `random` para escolher aleatoriamente os nomes a partir da lista gerada. Para executar este script, é necessário instalar a biblioteca names, o que pode ser feito com o seguinte comando:

    pip install names

<p align="center"><img src="assets\Print_4.jpg"></p>

## Pré-requisitos

Para executar os scripts, é necessário ter Python 3 instalado no seu sistema. Além disso, a biblioteca names precisa ser instalada para a execução do terceiro script.

<p align = "center">
Feito por <a href="https://www.linkedin.com/in/danilojosesilva/">Danilo José Silva</a> ! 
</p>