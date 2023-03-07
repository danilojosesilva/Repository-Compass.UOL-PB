select tbvendas.cdpro, tbvendas.nmpro
from tbvendas
where tbvendas.status = 'Concluído'
	and tbvendas.dtven between '2014-02-03' and '2018-02-02'
group by tbvendas.cdpro, tbvendas.nmpro
order by sum(tbvendas.qtd) desc
limit 1