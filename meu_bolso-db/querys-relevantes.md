### Retorna todos os gastos de acordo com o grupo selecionado por ID (alterar o desc para relatórios)
```
SELECT u.nome AS nome_usuario, u.sobrenome AS sobrenome_usuario,
       g.nome AS nome_gasto, g.valor, g.data,
       gr.nome AS grupo
FROM usuarios u
JOIN usuario_grupo ug ON u.id_user = ug.id_user
JOIN grupos gr ON ug.id_grupo = gr.id_grupo
JOIN gasto_grupo gg ON gr.id_grupo = gg.id_grupo
JOIN gastos g ON gg.id_gasto = g.id_gasto
WHERE u.id_user = ?
  AND gr.id_grupo = ?
ORDER BY g.data DESC;
```
* Logica interessante: se o usuário está logado, vc tem acesso ao id dele, o que resta é alterar o parametro que vai estar mandando pro endpoint