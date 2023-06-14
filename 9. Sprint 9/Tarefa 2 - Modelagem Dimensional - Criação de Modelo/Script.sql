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