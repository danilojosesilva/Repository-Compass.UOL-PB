SELECT 
	tbvendas.estado, 
	tbvendas.nmpro, 
	ROUND(AVG(tbvendas.qtd), 4) as quantidade_media
FROM tbvendas
WHERE tbvendas.status = 'Concluído'
GROUP BY tbvendas.estado, tbvendas.nmpro
ORDER BY tbvendas.estado, tbvendas.nmpro