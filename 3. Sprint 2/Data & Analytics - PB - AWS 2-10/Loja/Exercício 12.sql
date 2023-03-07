select 
	tbdependente.cddep, 
	tbdependente.nmdep, 
	tbdependente.dtnasc, 
	sum(tbvendas.qtd * tbvendas.vrunt) as valor_total_vendas
from tbdependente
inner join tbvendedor
	on tbvendedor.cdvdd = tbdependente.cdvdd
inner join tbvendas 
	on tbvendas.cdvdd = tbvendedor.cdvdd
where tbvendas.status = 'Concluído' 
	and tbvendas.deletado = '0'
group by tbdependente.cddep, tbdependente.nmdep, tbdependente.dtnasc
having valor_total_vendas = (
    select min(valor_total_vendas)
    from (
        select sum(v.qtd * v.vrunt) as valor_total_vendas
        from tbvendas as v
        where v.status = 'Concluído' 
        	and v.deletado = '0'
        group by v.cdvdd
        having sum(v.qtd * v.vrunt) > 0
    ) as tabela_vendas
)