DROP DATABASE IF EXISTS biblioteca;
CREATE DATABASE biblioteca;
USE biblioteca;

CREATE TABLE livros(
	id INT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(50),
    quantidade_paginas INT,
    autor VARCHAR(50),
    preco DOUBLE,
    isbn VARCHAR(100),
    descricao VARCHAR(1000)
);

SELECT * FROM livros;