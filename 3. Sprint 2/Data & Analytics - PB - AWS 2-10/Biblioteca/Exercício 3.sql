select
	count (livro.cod) as quantidade,
	editora.nome,
	endereco.estado,
	endereco.cidade
from livro
join editora  
	on livro.editora = editora.codeditora
join endereco
	on editora.endereco = endereco.codendereco
group by editora.codeditora
order by quantidade desc