INSERT INTO usuarios (nome, sobrenome, email, senha, tipo_usuario, qtd_grupos, ativo)
VALUES
('João', 'Silva', 'joao.silva@email.com', 'senha123', 1, 4, true),
('Maria', 'Santos', 'maria.santos@email.com', 'senha456', 1, 3, true),
('Pedro', 'Ferreira', 'pedro.ferreira@email.com', 'senha789', 1, 2, true),
('Ana', 'Oliveira', 'ana.oliveira@email.com', 'senha321', 1, 4, true),
('Carlos', 'Rodrigues', 'carlos.rodrigues@email.com', 'senha654', 1, 3, true),
('Mariana', 'Costa', 'mariana.costa@email.com', 'senha987', 1, 2, true),
('José', 'Almeida', 'jose.almeida@email.com', 'senha147', 1, 4, true),
('Fernanda', 'Carvalho', 'fernanda.carvalho@email.com', 'senha258', 1, 3, true),
('Ricardo', 'Martins', 'ricardo.martins@email.com', 'senha369', 1, 2, true),
('Cristina', 'Gomes', 'cristina.gomes@email.com', 'senha741', 1, 4, true),
('André', 'Nunes', 'andre.nunes@email.com', 'senha852', 1, 3, true),
('Patrícia', 'Melo', 'patricia.melo@email.com', 'senha963', 1, 2, true),
('Paulo', 'Ribeiro', 'paulo.ribeiro@email.com', 'senha159', 1, 4, true),
('Beatriz', 'Cardoso', 'beatriz.cardoso@email.com', 'senha267', 1, 3, true),
('Luís', 'Pinto', 'luis.pinto@email.com', 'senha378', 1, 2, true),
('Sofia', 'Teixeira', 'sofia.teixeira@email.com', 'senha486', 1, 4, true),
('Miguel', 'Correia', 'miguel.correia@email.com', 'senha594', 1, 3, true),
('Inês', 'Moreira', 'ines.moreira@email.com', 'senha612', 1, 2, true),
('Rui', 'Fernandes', 'rui.fernandes@email.com', 'senha723', 1, 4, true),
('Catarina', 'Sousa', 'catarina.sousa@email.com', 'senha834', 1, 3, true),
('Gonçalo', 'Lopes', 'goncalo.lopes@email.com', 'senha945', 1, 2, true),
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
        WHEN RAND() < 0.75 THEN 'Combustível'
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