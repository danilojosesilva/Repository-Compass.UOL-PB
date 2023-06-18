-- EXERCÍCIOS ######################################################################

-- (Exercício 1) Selecione os nomes de cidade distintas que existem no estado de
-- Minas Gerais em ordem alfabética (dados da tabela sales.customers)

select distinct city
from sales.customers
where state = 'MG'
order by city

-- (Exercício 2) Selecione o visit_id das 10 compras mais recentes efetuadas
-- (dados da tabela sales.funnel)

select visit_id
from sales.funnel
where paid_date is not null
order by paid_date desc
limit 10

select visit_page_date, add_to_cart_date, start_checkout_date, finish_checkout_date, paid_date
from sales.funnel

-- (Exercício 3) Selecione todos os dados dos 10 clientes com maior score nascidos
-- após 01/01/2000 (dados da tabela sales.customers)

select *
from sales.customers
where birth_date >= '20000101'
order by score desc
limit 10

select score, birth_date
from sales.customers



























