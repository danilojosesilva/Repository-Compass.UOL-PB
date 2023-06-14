# Normalização da Base de Dados Concessionária

Nesta tarefa, o objetivo é normalizar a base de dados da Concessionária, aplicando as formas normais. A base de dados original apresenta uma tabela chamada `tb_locacao` com várias colunas e dependências funcionais complexas. A normalização é necessária para eliminar redundâncias e garantir a integridade dos dados.

## Passos para a Normalização:

1. Renomear a tabela `tb_locacao` para `tb_locacao_antiga`.

2. Criar uma nova tabela `tb_cliente` para armazenar informações dos clientes, contendo os atributos `idCliente`, `nomeCliente`, `cidadeCliente`, `estadoCliente` e `paisCliente`.

3. Criar uma nova tabela `tb_carro` para armazenar informações dos carros, contendo os atributos `idCarro`, `kmCarro`, `classiCarro`, `marcaCarro`, `modeloCarro`, `anoCarro` e `idcombustivel`.

4. Criar uma nova tabela `tb_combustivel` para armazenar informações dos tipos de combustível, contendo os atributos `idCombustivel` e `tipoCombustivel`.

5. Criar uma nova tabela `tb_locacao` para armazenar informações das locações, contendo os atributos `idLocacao`, `idCliente`, `idCarro`, `dataLocacao`, `horaLocacao`, `qtdDiaria`, `vlrDiaria`, `dataEntrega`, `horaEntrega` e `idVendedor`.

6. Criar uma nova tabela `tb_vendedor` para armazenar informações dos vendedores, contendo os atributos `idVendedor`, `nomeVendedor`, `sexoVendedor` e `estadoVendedor`.

7. Copiar os dados da tabela `tb_locacao_antiga` para as novas tabelas normalizadas, garantindo a integridade referencial através das chaves estrangeiras.

8. Remover a tabela `tb_locacao_antiga`.

```sql
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
```

## Tabelas

Após a normalização, as tabelas apresentaram o seguinte resultado:

<p align="center"><img src="assets\Print_1.jpg"></p>

<p align="center"><img src="assets\Print_2.jpg"></p>

<p align="center"><img src="assets\Print_3.jpg"></p>

<p align="center"><img src="assets\Print_4.jpg"></p>

<p align="center"><img src="assets\Print_5.jpg"></p>

<p align="center"><img src="assets\Print_6.jpg"></p>

<p align="center"><img src="assets\Print_7.jpg"></p>

<p align="center"><img src="assets\Print_8.jpg"></p>

<p align="center"><img src="assets\Print_9.jpg"></p>

<p align="center"><img src="assets\Print_10.jpg"></p>

## Diagrama Lógico

Após a normalização, o diagrama lógico das tabelas fica da seguinte forma:

<p align="center"><img src="assets\Diagrama tarefa 1.png"></p>

O diagrama apresenta as tabelas normalizadas (`tb_locacao`, `tb_cliente`, `tb_carro`, `tb_combustivel` e `tb_vendedor`) e os relacionamentos entre elas.

Este README.md resume os passos seguidos para normalizar a base de dados da Concessionária, incluindo os arquivos SQL necessários e o diagrama lógico resultante.

<p align = "center">
Feito por <a href="https://www.linkedin.com/in/danilojosesilva/">Danilo José Silva</a> ! 
</p>