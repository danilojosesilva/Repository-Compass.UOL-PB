-- PARA QUE SERVE ##################################################################
-- Serve para filtrar linhas da seleção por uma coluna agrupada


-- EXEMPLOS ########################################################################

-- (Exemplo 1) seleção com filtro no HAVING 
-- Calcule o nº de clientes por estado filtrando apenas estados acima de 100 clientes

select 
    state, 
    count(*)
from sales.customers
-- where count(*) > 100 -- funciona apenas com colunas não agregadas
group by state
having count(*) > 100 -- funciona tanto com colunas agregadas como não agregadas

select 
    state, 
    count(*)
from sales.customers
where state <> 'MG' 
group by state
having count(*) > 100

select 
    state, 
    count(*)
from sales.customers
group by state
having count(*) > 100
	and state <> 'MG'

-- RESUMO ##########################################################################
-- (1) Tem a mesma função do WHERE mas pode ser usado para filtrar os resultados 
-- das funções agregadas enquanto o WHERE possui essa limitação
-- (2) A função HAVING também pode filtrar colunas não agregadas








