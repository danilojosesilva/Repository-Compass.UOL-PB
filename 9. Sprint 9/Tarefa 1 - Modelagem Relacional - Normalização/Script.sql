-- Renomear tabela tb_locacao para tb_locacao_antiga
ALTER TABLE tb_locacao RENAME TO tb_locacao_antiga;

-- Criação da tabela tb_cliente
CREATE TABLE tb_cliente (
  idCliente       int primary key,
  nomeCliente     varchar(100),
  cidadeCliente   varchar(40),
  estadoCliente   varchar(40),
  paisCliente     varchar(40)
);

-- Copiar dados da tabela tb_locacao_antiga para a nova tabela
INSERT OR IGNORE INTO tb_cliente (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente)
SELECT DISTINCT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
FROM tb_locacao_antiga;

-- Criação da tabela tb_carro
CREATE TABLE tb_carro (
  idCarro         int primary key,
  kmCarro         int,
  classiCarro     varchar(50),
  marcaCarro      varchar(80),
  modeloCarro     varchar(80),
  anoCarro        int,
  idcombustivel   int,
  foreign key (idcombustivel) references tb_combustivel(idCombustivel)
);

-- Copiar dados da tabela tb_locacao_antiga para a nova tabela
INSERT OR IGNORE INTO tb_carro (idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idcombustivel)
SELECT DISTINCT idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idcombustivel
FROM tb_locacao_antiga;

-- Criação da tabela tb_combustivel
CREATE TABLE tb_combustivel (
  idCombustivel   int primary key,
  tipoCombustivel varchar(20)
);

-- Copiar dados da tabela tb_locacao_antiga para a nova tabela
INSERT OR IGNORE INTO tb_combustivel (idCombustivel, tipoCombustivel)
SELECT DISTINCT idcombustivel, tipoCombustivel
FROM tb_locacao_antiga;

-- Criação da tabela tb_vendedor
CREATE TABLE tb_vendedor (
  idVendedor      int primary key,
  nomeVendedor    varchar(15),
  sexoVendedor    smallint,
  estadoVendedor  varchar(40)
);

-- Copiar dados da tabela tb_locacao_antiga para a nova tabela
INSERT OR IGNORE INTO tb_vendedor (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor)
SELECT DISTINCT idVendedor, nomeVendedor, sexoVendedor, estadoVendedor
FROM tb_locacao_antiga;

-- Criação da tabela tb_locacao
CREATE TABLE tb_locacao (
  idLocacao       int primary key,
  idCliente       int,
  idCarro         int,
  dataLocacao     datetime,
  horaLocacao     time,
  qtdDiaria       int,
  vlrDiaria       decimal(18,2),
  dataEntrega     date,
  horaEntrega     time,
  idVendedor      int,
  foreign key (idCliente) references tb_cliente(idCliente),
  foreign key (idCarro) references tb_carro(idCarro),
  foreign key (idVendedor) references tb_vendedor(idVendedor)
);

-- Copiar dados da tabela tb_locacao_antiga para a nova tabela
INSERT OR IGNORE INTO tb_locacao (idLocacao, idCliente, idCarro, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, idVendedor)
SELECT idLocacao, idCliente, idCarro, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, idVendedor
FROM tb_locacao_antiga;

-- Remover tabela tb_locacao_antiga
DROP TABLE tb_locacao_antiga;
