select
	autor.nome,
	autor.codautor,	
	autor.nascimento,
	count(livro.cod) as quantidade
from livro
full join autor
	on autor.codautor = livro.autor
group by autor.codautor
order by autor.nome 