SELECT 
	livro.cod as CodLivro, 
	livro.titulo as Titulo, 
	autor.codautor as CodAutor, 
	autor.nome as NomeAutor, 
	livro.valor as Valor, 
	editora.codeditora as CodEditora, 
	editora.nome as NomeEditora
FROM livro
JOIN autor 
	ON livro.autor = autor.codautor
JOIN editora 
	ON livro.editora = editora.codeditora
ORDER BY livro.valor DESC
LIMIT 10