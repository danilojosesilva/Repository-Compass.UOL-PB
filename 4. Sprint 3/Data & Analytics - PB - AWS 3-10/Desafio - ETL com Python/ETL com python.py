# abrir arquivo actors.csv e ler as linhas
with open('actors.csv', 'r') as f:
    lines = f.readlines()[1:]

# criar listas para armazenar os dados
actors = []
total_gross = []
num_movies = []
avg_per_movie = []
movies = []
gross = []


# Verificado em qual linha está o erro de conversão se str para float
# index = total_gross.index(' Jr."')

# A linha índice 4 que contém o erro de dados
# lines[4]

# Corrigindo a Linha de índice 4
lines[4] = '"Robert Downey Jr.",3947.30 ,53,74.50 ,The Avengers,623.40'

# armazenar os dados nas listas correspondentes
for line in lines:

    actor = line.split(',')
    t_gross = line.split(',')
    n_movies = line.split(',')
    avg = line.split(',')
    t_movie = line.split(',')
    g = line.split(',')

    actors.append(actor[0])
    total_gross.append(t_gross[1])
    num_movies.append(n_movies[2])
    avg_per_movie.append(avg[3])
    movies.append(t_movie[4])
    gross.append(g[5])


num_movies = [int(n) for n in num_movies]
total_gross = [float(g) for g in total_gross]
avg_per_movie = [float(a) for a in avg_per_movie]
gross = [float(g) for g in gross]

# 1. encontrar o ator/atriz com maior número de filmes
max_num_movies = max(num_movies)
idx_max_num_movies = num_movies.index(max_num_movies)
actor_most_movies = actors[idx_max_num_movies]

# escrever resultado no arquivo etapa-1.txt
with open('etapa-1.txt', 'w') as f:
    f.write(f"O ator/atriz com maior numero de filmes foi '{actor_most_movies}'. "
            f"Ele(a) participou de {max_num_movies} filmes.")

# 2. calcular a média de faturamento bruto por ator
avg_gross_per_actor = {}
for i in range(len(actors)):
    if actors[i] in avg_gross_per_actor:
        avg_gross_per_actor[actors[i]] += total_gross[i]/num_movies[i]
    else:
        avg_gross_per_actor[actors[i]] = total_gross[i]/num_movies[i]

# arredondar a média para 2 casas decimais
for actor, avg in avg_gross_per_actor.items():
    avg_gross_per_actor[actor] = round(avg, 2)

# escrever resultado no arquivo etapa-2.txt
with open('etapa-2.txt', 'w') as f:
    for actor, avg in avg_gross_per_actor.items():
        f.write(f"A media de faturamento bruto do ator/atriz '{actor}' foi de {avg}.\n")

# 3. encontrar o ator/atriz com a maior média de faturamento por filme
max_avg_gross_per_movie = max(avg_per_movie)
idx_max_avg_gross_per_movie = avg_per_movie.index(max_avg_gross_per_movie)
actor_max_avg_gross = actors[idx_max_avg_gross_per_movie]

# escrever resultado no arquivo etapa-3.txt
with open('etapa-3.txt', 'w') as f:
    f.write(f"O ator/atriz com maior media de faturamento por filme foi '{actor_max_avg_gross}'. "
            f"Ele(a) faturou {max_avg_gross_per_movie}.")

# 4. encontrar o(s) filme(s) mais frequente(s)
freq_movies = {}
for m in movies:
    if m in freq_movies:
        freq_movies[m] += 1
    else:
        freq_movies[m] = 1

max_freq = max(freq_movies.values())
most_freq_movies = [k for k, v in freq_movies.items() if v == max_freq]

# escrever resultado no arquivo etapa-4.txt
with open('etapa-4.txt', 'w') as f:
    if len(most_freq_movies) == 1:
        f.write(f"O filme mais frequente foi '{most_freq_movies[0]}'. Ele apareceu {max_freq} vezes.")
    else:
        movies_str = ', '.join(most_freq_movies)
        f.write(f"Os filmes mais frequentes foram '{movies_str}'. Eles apareceram {max_freq} vezes.")

# 5. ordenar a lista de atores pelo faturamento bruto total
total_gross_per_actor = {}
for i in range(len(actors)):
    if actors[i] in total_gross_per_actor:
        total_gross_per_actor[actors[i]] += total_gross[i]
    else:
        total_gross_per_actor[actors[i]] = total_gross[i]

sorted_actors = [(k, v) for k, v in sorted(total_gross_per_actor.items(), key=lambda item: item[1], reverse=True)]

# escrever resultado no arquivo etapa-5.txt
with open('etapa-5.txt', 'w') as f:
    for actor, gross in sorted_actors:
        f.write(f"O ator/atriz '{actor}' teve um faturamento total de {gross}.\n")
