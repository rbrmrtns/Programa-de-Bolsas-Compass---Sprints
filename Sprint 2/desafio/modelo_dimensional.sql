CREATE VIEW dim_cliente AS
SELECT 
    tb_cliente.idCliente,
    tb_cliente.nome,
    tb_cidade.nome AS cidade,
    tb_estado.nome AS estado,
    tb_pais.nome AS pais
FROM tb_cliente
JOIN tb_cidade
	ON tb_cidade.idCidade = tb_cliente.idCidade
JOIN tb_estado
	ON tb_estado.idEstado = tb_cidade.idEstado
JOIN tb_pais
	ON tb_pais.idPais = tb_estado.idPais;
	
CREATE VIEW dim_vendedor AS
SELECT 
    tb_vendedor.idVendedor,
    tb_vendedor.nome,
    tb_vendedor.sexo,
    tb_estado.nome AS estado,
    tb_pais.nome AS pais
FROM tb_vendedor
JOIN tb_estado
	ON tb_estado.idEstado = tb_vendedor.idEstado
JOIN tb_pais
	ON tb_pais.idPais = tb_estado.idPais;
	
CREATE VIEW dim_carro AS
SELECT
	tb_carro.idCarro,
	tb_carro.classi,
	tb_carro.marca,
	tb_carro.modelo,
	tb_carro.ano,
	tb_combustivel.tipo AS tipoCombustivel
FROM tb_carro
JOIN tb_combustivel
	ON tb_combustivel.idCombustivel = tb_carro.idCombustivel;
	
CREATE VIEW dim_km_carro AS
SELECT
	idCarro,
	km
FROM tb_km_carro;

CREATE VIEW dim_data_hora AS
SELECT
	dataHoraLocacao,
	STRFTIME('%Y', dataHoraLocacao) AS anoLocacao,
	STRFTIME('%m', dataHoraLocacao) AS mesLocacao,
	STRFTIME('%W', dataHoraLocacao) AS semanaLocacao,
	STRFTIME('%d', dataHoraLocacao) AS diaLocacao,
	STRFTIME('%H', dataHoraLocacao) AS horaLocacao,
	dataHoraEntrega,
	STRFTIME('%Y', dataHoraEntrega) AS anoEntrega,
	STRFTIME('%m', dataHoraEntrega) AS mesEntrega,
	STRFTIME('%W', dataHoraEntrega) AS semanaEntrega,
	STRFTIME('%d', dataHoraEntrega) AS diaEntrega,
	STRFTIME('%H', dataHoraEntrega) AS horaEntrega
FROM tb_locacao;

CREATE VIEW fato_locacao AS
SELECT *
FROM tb_locacao;