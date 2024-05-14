import sqlite3

CREATE TABLE funcionario(id INT, nome VARCHAR(100), cpf VARCHAR (100), data_cadastro VARCHAR(100), endereco VARCHAR(100));
INSERT INTO funcionario values(1, 'Danilo', '11111111111', '05/10/2022', 'RIO TINTO');

SELECT * from funcionario;