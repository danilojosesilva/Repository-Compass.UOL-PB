# Modelagem Dimensional - Criação de Modelo

## Objetivo

O objetivo desta tarefa é estabelecer um conjunto de views que correspondam a um esquema de modelo dimensional, extraído de tabelas previamente disponíveis em um modelo relacional. Este procedimento visa facilitar a realização de análises de dados, consultas e geração de relatórios.

## Descrição das Views

Foram criadas as seguintes views para corresponder ao modelo dimensional:

1. **vw_dim_cliente:** Esta view traz as informações únicas dos clientes, extraídas da tabela 'tb_cliente'.

2. **vw_dim_combustivel:** Esta view apresenta os tipos únicos de combustível, derivados da tabela 'tb_combustivel'.

3. **vw_dim_carro:** A view que ilustra as características únicas de cada carro na tabela 'tb_carro'.

4. **vw_dim_vendedor:** Uma view com detalhes únicos de cada vendedor da tabela 'tb_vendedor'.

5. **vw_fatos_locacao:** Esta é a nossa tabela de fatos. Ela inclui detalhes de cada transação de locação a partir da tabela 'tb_locacao'.

```sql
-- Criação da view Dimensão Cliente
CREATE VIEW vw_dim_cliente AS 
SELECT DISTINCT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
FROM tb_cliente;

-- Criação da view Dimensão Combustível
CREATE VIEW vw_dim_combustivel AS 
SELECT DISTINCT idcombustivel, tipoCombustivel
FROM tb_combustivel;

-- Criação da view Dimensão Carro
CREATE VIEW vw_dim_carro AS 
SELECT DISTINCT idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idcombustivel
FROM tb_carro;

-- Criação da view Dimensão Vendedor
CREATE VIEW vw_dim_vendedor AS 
SELECT DISTINCT idVendedor, nomeVendedor, sexoVendedor, estadoVendedor
FROM tb_vendedor;

-- Criação da view Tabela de Fatos Locacao
CREATE VIEW vw_fatos_locacao AS 
SELECT idLocacao, idCliente, idCarro, idVendedor, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega
FROM tb_locacao;
```

## Abordagem 

Nesta tarefa, optou-se por usar "views" em vez de criar novas tabelas, pois as "views" podem simplificar a estrutura do banco de dados para fins de análise. Além disso, elas não armazenam dados fisicamente e podem ser usadas para esconder a complexidade das consultas, tornando o processo de análise mais intuitivo.

<p align="center"><img src="assets\Print_1.jpg"></p>

<p align="center"><img src="assets\Print_2.jpg"></p>

## Próximos Passos

Após a conclusão desta tarefa, o próximo passo seria avaliar a performance e a eficácia dessas views em responder a consultas comuns de negócios e identificar áreas para otimização ou refinamento.

<p align = "center">
Feito por <a href="https://www.linkedin.com/in/danilojosesilva/">Danilo José Silva</a> ! 
</p>