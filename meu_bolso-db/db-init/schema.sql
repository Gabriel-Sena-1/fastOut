-- Tabela de Usuários
CREATE TABLE usuarios (
    id_user INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    sobrenome VARCHAR(100) NOT NULL,
    email VARCHAR(200) NOT NULL UNIQUE,
    senha VARCHAR(100) NOT NULL,
    tipo_usuario INT NOT NULL DEFAULT 1, -- tipo_usuario definido como 1 por padrão
    qtd_grupos INT NOT NULL DEFAULT 3, -- qtd_grupos definido como 3 por padrão
    ativo BOOLEAN NOT NULL DEFAULT TRUE -- ativo definido como TRUE por padrão
    -- SALDO ??? ??? ??? > atualizado com recorrência no servidor
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



INSERT INTO usuarios (nome, sobrenome, email, senha, tipo_usuario, qtd_grupos, ativo)
VALUES
('Joao', 'Silva', 'joao.silva@email.com', 'senha123', 1, 4, true),
('Maria', 'Santos', 'maria.santos@email.com', 'senha456', 1, 3, true),
('Pedro', 'Ferreira', 'pedro.ferreira@email.com', 'senha789', 1, 2, true),
('Ana', 'Oliveira', 'ana.oliveira@email.com', 'senha321', 1, 4, true),
('Carlos', 'Rodrigues', 'carlos.rodrigues@email.com', 'senha654', 1, 3, true),
('Mariana', 'Costa', 'mariana.costa@email.com', 'senha987', 1, 2, true),
('Jose', 'Almeida', 'jose.almeida@email.com', 'senha147', 1, 4, true),
('Fernanda', 'Carvalho', 'fernanda.carvalho@email.com', 'senha258', 1, 3, true),
('Ricardo', 'Martins', 'ricardo.martins@email.com', 'senha369', 1, 2, true),
('Cristina', 'Gomes', 'cristina.gomes@email.com', 'senha741', 1, 4, true),
('Andre', 'Nunes', 'andre.nunes@email.com', 'senha852', 1, 3, true),
('Patricia', 'Melo', 'patricia.melo@email.com', 'senha963', 1, 2, true),
('Paulo', 'Ribeiro', 'paulo.ribeiro@email.com', 'senha159', 1, 4, true),
('Beatriz', 'Cardoso', 'beatriz.cardoso@email.com', 'senha267', 1, 3, true),
('Luis', 'Pinto', 'luis.pinto@email.com', 'senha378', 1, 2, true),
('Sofia', 'Teixeira', 'sofia.teixeira@email.com', 'senha486', 1, 4, true),
('Miguel', 'Correia', 'miguel.correia@email.com', 'senha594', 1, 3, true),
('Ines', 'Moreira', 'ines.moreira@email.com', 'senha612', 1, 2, true),
('Rui', 'Fernandes', 'rui.fernandes@email.com', 'senha723', 1, 4, true),
('Catarina', 'Sousa', 'catarina.sousa@email.com', 'senha834', 1, 3, true),
('Goncalo', 'Lopes', 'goncalo.lopes@email.com', 'senha945', 1, 2, true),
('Teresa', 'Pereira', 'teresa.pereira@email.com', 'senha156', 1, 4, true),
('Daniel', 'Fonseca', 'daniel.fonseca@email.com', 'senha267', 1, 3, true),
('Marta', 'Henriques', 'marta.henriques@email.com', 'senha378', 1, 2, true),
('Diogo', 'Marques', 'diogo.marques@email.com', 'senha489', 1, 4, true),
('Clara', 'Rocha', 'clara.rocha@email.com', 'senha591', 1, 3, true),
('Tiago', 'Antunes', 'tiago.antunes@email.com', 'senha612', 1, 2, true),
('Leonor', 'Brito', 'leonor.brito@email.com', 'senha723', 1, 4, true),
('Hugo', 'Esteves', 'hugo.esteves@email.com', 'senha834', 1, 3, true),
('Diana', 'Coelho', 'diana.coelho@email.com', 'senha945', 1, 2, true);

INSERT INTO gastos (nome, valor, data)
SELECT 
    CASE 
        WHEN RAND() < 0.25 THEN 'Mercado'
        WHEN RAND() < 0.5 THEN 'Restaurante'
        WHEN RAND() < 0.75 THEN 'Combustivel'
        ELSE 'Cinema'
    END,
    ROUND(RAND() * 200 + 10, 2),
    DATE_SUB(NOW(), INTERVAL FLOOR(RAND() * 365) DAY)
FROM 
    usuarios,
    (SELECT 1 UNION SELECT 2 UNION SELECT 3 UNION SELECT 4 UNION SELECT 5
     UNION SELECT 6 UNION SELECT 7 UNION SELECT 8 UNION SELECT 9 UNION SELECT 10
     UNION SELECT 11 UNION SELECT 12 UNION SELECT 13 UNION SELECT 14 UNION SELECT 15
     UNION SELECT 16 UNION SELECT 17 UNION SELECT 18 UNION SELECT 19 UNION SELECT 20) numbers;


INSERT INTO gasto_grupo (id_gasto, id_grupo)
SELECT 
    g.id_gasto,
    CASE 
        WHEN g.nome IN ('Mercado', 'Restaurante') THEN 1 
        WHEN g.nome = 'Combustível' THEN 2 
        WHEN g.nome = 'Cinema' THEN 4 
        ELSE FLOOR(RAND() * 4) + 1 
    END
FROM 
    gastos g;

INSERT INTO usuario_grupo (id_user, id_grupo)
SELECT 
    u.id_user,
    g.id_grupo
FROM 
    usuarios u
CROSS JOIN
    grupos g
WHERE 
    RAND() < 0.75; 

UPDATE usuarios u
SET qtd_grupos = (
    SELECT COUNT(DISTINCT ug.id_grupo)
    FROM usuario_grupo ug
    WHERE ug.id_user = u.id_user
);
