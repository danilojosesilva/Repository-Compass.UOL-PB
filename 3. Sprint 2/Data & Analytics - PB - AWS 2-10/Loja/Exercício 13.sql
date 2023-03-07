select 
    tbestoqueproduto.cdpro, 
    tbvendas.nmcanalvendas, 
    tbvendas.nmpro, 
    sum(tbvendas.qtd) as quantidade_vendas
from tbvendas 
inner join tbestoqueproduto 
	on tbvendas.cdpro = tbestoqueproduto.cdpro 
where tbvendas.status = 'Concluído' 
	and tbvendas.nmcanalvendas in ('Ecommerce', 'Matriz') 
group by
    tbestoqueproduto.cdpro, 
    tbvendas.nmcanalvendas, 
    tbvendas.nmpro 
order by quantidade_vendas
limit 10
