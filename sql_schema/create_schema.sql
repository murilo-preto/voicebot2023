USE voicebot;

CREATE TABLE documento (
    id int NOT NULL AUTO_INCREMENT,
    cpf int NOT NULL,
    primeiro_nome varchar(255) NOT NULL,
    ultimo_nome varchar(255) NOT NULL,
    data_nascimento date NOT NULL,
    cargo varchar(255),
    PRIMARY KEY (id)
);

CREATE TABLE login (
    id_login int NOT NULL AUTO_INCREMENT,
    id_user int NOT NULL,
    salt varchar(255) NOT NULL,
    hash_senha varchar(255) NOT NULL,

    FOREIGN KEY (id_user) REFERENCES documento(id),
    PRIMARY KEY (id_login)
);

CREATE TABLE tipo_registro (
	id_tipo_registro int NOT NULL AUTO_INCREMENT,
	tipo varchar(255) NOT NULL,
	PRIMARY KEY (id_tipo_registro)
);

CREATE TABLE registro (
	id_registro int NOT NULL AUTO_INCREMENT,
    data_hora datetime DEFAULT(current_timestamp()),
    id_user int,
    tipo int,
    valor varchar(255),

	PRIMARY KEY (id_registro),
    FOREIGN KEY (id_user) REFERENCES documento(id),
    FOREIGN KEY (tipo) REFERENCES tipo_registro(id_tipo_registro)
);

SHOW tables;