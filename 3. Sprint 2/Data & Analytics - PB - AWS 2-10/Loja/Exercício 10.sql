SELECT 
    tbvendedor.nmvdd as vendedor,
    SUM(tbvendas.qtd * tbvendas.vrunt) as valor_total_vendas,
    ROUND(SUM(tbvendas.qtd * tbvendas.vrunt) * tbvendedor.perccomissao / 100, 2) as comissao
FROM tbvendedor
JOIN tbvendas 
	ON tbvendedor.cdvdd = tbvendas.cdvdd
WHERE tbvendas.status = 'Concluído'
GROUP BY tbvendedor.nmvdd, tbvendedor.perccomissao
ORDER BY comissao DESC