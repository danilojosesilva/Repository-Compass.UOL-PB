SELECT 
	editora.codeditora as CodEditora, 
	editora.nome as NomeEditora, 
	COUNT(*) as QuantidadeLivros
FROM livro
JOIN editora 
	ON livro.editora = editora.codeditora
GROUP BY editora.codeditora, editora.nome
ORDER BY QuantidadeLivros DESC
LIMIT 5