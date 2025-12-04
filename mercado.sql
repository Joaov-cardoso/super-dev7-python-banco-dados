DROP DATABASE IF EXISTS mercado;
CREATE DATABASE mercado;
USE mercado;

CREATE TABLE categorias(
	id int primary key auto_increment,
    nome VARCHAR(100)
);

INSERT INTO categorias (nome) VALUES ('Hortifruti'); -- id gerado 1
INSERT INTO categorias (nome) VALUES ('Embutidos'); -- id gerado 2

-- PK = Primary Key (chave primaria)
-- FK = Foreign Key (chave estrangeira) sempre está relacionada a outra chave primaria
-- FK tem que estar atralada a uma PK
CREATE TABLE produtos(
	id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100),
    id_categoria INT,
    
    FOREIGN KEY(id_categoria) REFERENCES categorias(id)
);

SELECT * FROM categorias;

INSERT INTO produtos(nome, id_categoria) VALUES ('Batatinha',1);
INSERT INTO produtos(nome, id_categoria) VALUES ('Calabresa',2);
INSERT INTO produtos(nome, id_categoria) VALUES ('Bacon',2);
INSERT INTO produtos(nome, id_categoria) VALUES ('Toddy',3);

SELECT produtos.id, produtos.nome, produtos.id_categoria from produtos;

SELECT
	categorias.nome as 'Nome da categoria',
    produtos.nome as 'Nome do produto'
    from produtos
    inner join categorias on (produtos.id_categoria = categorias.id)






