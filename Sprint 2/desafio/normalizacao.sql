CREATE TABLE tb_pais (
    idPais INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
);

INSERT INTO tb_pais (nome)
SELECT  DISTINCT paisCliente
FROM tb_locacao;

CREATE TABLE tb_estado (
    idEstado INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idPais INTEGER NOT NULL,
    FOREIGN KEY(idPais) REFERENCES tb_pais(idPais)
);

INSERT INTO tb_estado (nome, idPais)
SELECT DISTINCT
    tb_locacao.estadoCliente,
    tb_pais.idPais
FROM tb_locacao
JOIN tb_pais
    ON tb_pais.nome = tb_locacao.paisCliente;

CREATE TABLE tb_cidade (
    idCidade INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idEstado INTEGER NOT NULL,
    FOREIGN KEY(idEstado) REFERENCES tb_estado(idEstado)
);

INSERT INTO tb_cidade (nome, idEstado)
SELECT DISTINCT
    tb_locacao.cidadeCliente,
    tb_estado.idEstado
FROM tb_locacao
JOIN tb_estado
    ON tb_estado.nome = tb_locacao.estadoCliente;

CREATE TABLE tb_cliente (
    idCliente INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idCidade INTEGER NOT NULL,
    FOREIGN KEY(idCidade) REFERENCES tb_cidade(idCidade) 
);

INSERT INTO tb_cliente (idCliente, nome, idCidade)
SELECT DISTINCT
    tb_locacao.idCliente, 
    tb_locacao.nomeCliente, 
    tb_cidade.idCidade
FROM tb_locacao
JOIN tb_cidade
    ON tb_cidade.nome = tb_locacao.cidadeCliente;

CREATE TABLE tb_combustivel (
    idCombustivel INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo TEXT NOT NULL
);

INSERT INTO tb_combustivel (idCombustivel, tipo)
SELECT DISTINCT
    idcombustivel,
    tipoCombustivel
FROM tb_locacao;
    

CREATE TABLE tb_carro (
    idCarro INTEGER PRIMARY KEY AUTOINCREMENT,
    classi TEXT NOT NULL,
    marca TEXT,
    modelo TEXT,
    ano INTEGER,
    idCombustivel INTEGER NOT NULL,
    FOREIGN KEY(idCombustivel) REFERENCES tb_combustivel(idCombustivel)
);

INSERT INTO tb_carro (idCarro, classi, marca, modelo, ano, idCombustivel)
SELECT DISTINCT
    tb_locacao.idCarro,
    tb_locacao.classiCarro,
    tb_locacao.marcaCarro,
    tb_locacao.modeloCarro,
    tb_locacao.anoCarro,
    tb_combustivel.idCombustivel
FROM tb_locacao
JOIN tb_combustivel
    ON tb_combustivel.idCombustivel = tb_locacao.idcombustivel;

CREATE TABLE tb_km_carro (
    idCarro INTEGER NOT NULL,
    km INTEGER NOT NULL,
    FOREIGN KEY(idCarro) REFERENCES tb_carro(idCarro)
);

INSERT INTO tb_km_carro (idCarro, km)
SELECT
    tb_carro.idCarro,
    tb_locacao.kmCarro
FROM tb_locacao
JOIN tb_carro
    ON tb_carro.idCarro = tb_locacao.idCarro;

CREATE TABLE tb_vendedor (
    idVendedor INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    sexo INTEGER,
    idEstado INTEGER NOT NULL,
    FOREIGN KEY(idEstado) REFERENCES tb_estado(idEstado)
);

INSERT INTO tb_vendedor (idVendedor, nome, sexo, idEstado)
SELECT DISTINCT
    tb_locacao.idVendedor,
    tb_locacao.nomeVendedor,
    tb_locacao.sexoVendedor,
    tb_estado.idEstado
FROM tb_locacao
JOIN tb_estado
    ON tb_estado.nome = tb_locacao.estadoVendedor;

CREATE TABLE tb_temp
AS SELECT *
FROM tb_locacao;

DROP TABLE tb_locacao;

CREATE TABLE tb_locacao (
    idLocacao INTEGER PRIMARY KEY AUTOINCREMENT,
    dataHoraLocacao DATETIME NOT NULL,
    qtdDiaria INTEGER,
    vlrDiaria DECIMAL,
    dataHoraEntrega DATETIME,
    idCliente INTEGER NOT NULL,
    idCarro INTEGER NOT NULL,
    idVendedor INTEGER NOT NULL,
    FOREIGN KEY(idCliente) REFERENCES tb_cliente(idCliente),
    FOREIGN KEY(idCarro) REFERENCES tb_carro(idCarro),
    FOREIGN KEY(idVendedor) REFERENCES tb_vendedor(idVendedor)
);

INSERT INTO tb_locacao (idLocacao, dataHoraLocacao, qtdDiaria, vlrDiaria, dataHoraEntrega, idCliente, idCarro, idVendedor)
SELECT
    idLocacao,
    CASE 
		WHEN LENGTH(horaLocacao) = 5 THEN SUBSTRING(dataLocacao, 1, 4) || '-' || SUBSTRING(dataLocacao, 5, 2) || '-' || SUBSTRING(dataLocacao, 7, 2) || ' ' || TIME(horaLocacao)
		WHEN LENGTH(horaLocacao) = 4 THEN SUBSTRING(dataLocacao, 1, 4) || '-' || SUBSTRING(dataLocacao, 5, 2) || '-' || SUBSTRING(dataLocacao, 7, 2) || ' ' || TIME('0' || horaLocacao)
	END AS dataHoraLocacao,
    qtdDiaria,
    vlrDiaria,
    CASE 
		WHEN LENGTH(horaLocacao) = 5 THEN SUBSTRING(dataLocacao, 1, 4) || '-' || SUBSTRING(dataLocacao, 5, 2) || '-' || SUBSTRING(dataLocacao, 7, 2) || ' ' || TIME(horaLocacao)
		WHEN LENGTH(horaLocacao) = 4 THEN SUBSTRING(dataLocacao, 1, 4) || '-' || SUBSTRING(dataLocacao, 5, 2) || '-' || SUBSTRING(dataLocacao, 7, 2) || ' ' || TIME('0' || horaLocacao)
	END AS dataHoraEntrega,
    idCliente,
    idCarro,
    idVendedor
FROM tb_temp;

DROP TABLE tb_temp;