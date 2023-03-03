select autor.nome
from autor
left join livro
	on autor.codautor = livro.autor 
group by autor.codautor
having count(livro.cod) = 0
order by autor.nome