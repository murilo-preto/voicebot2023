
CREATE TABLE cargo (
    id_cargo INT NOT NULL AUTO_INCREMENT,
    cargo VARCHAR(255) NOT NULL UNIQUE,
    PRIMARY KEY (id_cargo)
);

CREATE TABLE documento (
    id INT NOT NULL AUTO_INCREMENT,
    cpf VARCHAR(14) NOT NULL UNIQUE,
    primeiro_nome VARCHAR(255) NOT NULL,
    ultimo_nome VARCHAR(255) NOT NULL,
    data_nascimento DATE NOT NULL,
    cargo INT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (cargo) REFERENCES cargo(id_cargo),
    INDEX idx_cpf (cpf)
);

CREATE TABLE login (
    id_login INT NOT NULL AUTO_INCREMENT,
    id_documento INT NOT NULL,
    salt BLOB NOT NULL,
    hash_senha BLOB NOT NULL,
    PRIMARY KEY (id_login),
    INDEX idx_id_documento (id_documento),
    FOREIGN KEY (id_documento) REFERENCES documento(id) ON DELETE CASCADE
);

CREATE TABLE tipo_registro (
    id_tipo_registro INT NOT NULL AUTO_INCREMENT,
    tipo VARCHAR(255) NOT NULL,
    PRIMARY KEY (id_tipo_registro)
);

CREATE TABLE registro (
    id_registro INT NOT NULL AUTO_INCREMENT,
    data_hora DATETIME DEFAULT CURRENT_TIMESTAMP,
    id_documento INT,
    tipo_registro INT,
    valor VARCHAR(255),
    PRIMARY KEY (id_registro),
    INDEX idx_id_documento (id_documento),
    INDEX idx_tipo_registro (tipo_registro),
    FOREIGN KEY (id_documento) REFERENCES documento(id) ON DELETE CASCADE,
    FOREIGN KEY (tipo_registro) REFERENCES tipo_registro(id_tipo_registro) ON DELETE CASCADE
);
