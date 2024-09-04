-- Tabela de Usuários
CREATE TABLE usuarios (
    id_user INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    sobrenome VARCHAR(100) NOT NULL,
    email VARCHAR(200) NOT NULL UNIQUE,
    senha VARCHAR(100) NOT NULL,
    tipo_usuario INT NOT NULL, 
    qtd_grupos INT NOT NULL,
    ativo BOOLEAN NOT NULL
    -- SALDO ??? ??? ??? > atualizado com recorrencia no servidor
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
    -- CADASTRO DE RECORRENCIA
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
    PRIMARY KEY (id_user, id_grupo),
    FOREIGN KEY (id_user) REFERENCES usuarios(id_user) ON DELETE CASCADE,
    FOREIGN KEY (id_grupo) REFERENCES grupos(id_grupo) ON DELETE CASCADE
);

CREATE TABLE log (
    id INT AUTO_INCREMENT PRIMARY KEY,
    registro TEXT NOT NULL,
    data DATETIME DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO grupos (nome) VALUES ('Alimentacao');
INSERT INTO grupos (nome) VALUES ('Transporte');
INSERT INTO grupos (nome) VALUES ('Educacao');
INSERT INTO grupos (nome) VALUES ('Lazer');

-- Índices para otimização de consultas
CREATE INDEX idx_usuarios_email ON usuarios(email);
CREATE INDEX idx_gastos_data ON gastos(data);




