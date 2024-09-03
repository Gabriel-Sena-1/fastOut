-- Tabela de Usuários
CREATE TABLE usuarios (
    id_user INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    sobrenome VARCHAR(100) NOT NULL,
    email VARCHAR(200) NOT NULL UNIQUE,
    senha VARCHAR(100) NOT NULL,
    tipo_usuario INT NOT NULL
);


-- Tabela de Grupos (Natureza do gasto)
-- cadastro previo: Alimentacao, transporte, lazer, educacao
CREATE TABLE grupos (
    id_grupo INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL 
);

-- Tabela de Gastos
CREATE TABLE gastos (
    id_gasto INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    valor FLOAT NOT NULL,
    data DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Tabela de relacionamento entre Gastos e Grupos
CREATE TABLE gasto_grupo (
    id_gasto INT,
    id_grupo INT,
    PRIMARY KEY (id_gasto, id_grupo),
    FOREIGN KEY (id_gasto) REFERENCES gastos(id_gasto) ON DELETE CASCADE,
    FOREIGN KEY (id_grupo) REFERENCES grupos(id_grupo) ON DELETE CASCADE
);

-- Tabela de relacionamento entre Usuarios e Grupos
CREATE TABLE usuario_grupo (
    id_user INT,
    id_grupo INT,
    PRIMARY KEY (id_usuario, id_grupo),
    FOREIGN KEY (id_user) REFERENCES usuarios(id_user) ON DELETE CASCADE,
    FOREIGN KEY (id_grupo) REFERENCES grupos(id_grupo) ON DELETE CASCADE
);

INSERT INTO grupo (nome) VALUES ('Alimentação');
INSERT INTO grupo (nome) VALUES ('Transporte');
INSERT INTO grupo (nome) VALUES ('Educação');
INSERT INTO grupo (nome) VALUES ('Lazer');

-- Índices para otimização de consultas
CREATE INDEX idx_usuarios_email ON usuarios(email);
CREATE INDEX idx_gastos_data ON gastos(data);

