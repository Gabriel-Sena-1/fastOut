# Escopo do projeto

Uma aplicação para controle de gastos pessoais. Nessa aplicação você deve conseguir criar e gerenciar seus gastos pessoais. Podendo adicionar dispesas e suas naturezas. 

Plus: relatórios mensais em gráficos com base na natureza da despesa.

# System Design
    > HTML, Tailwind CSS, JS        -> Front-end
        > VueJS > Express JS

    > FastAPI                       -> Back-end
    > MySQL                         -> Database
    
    > Libs:
        -> OAuth2 | Autenticação: para autenticar usuários do sistema;
        -> Passlib | Hash de senha: para armazenar senhas com segurança;
        -> Chart.js | Gráficos: para melhorar a visualização dos relatórios.

# Tabelas:

- Usuário:
```
    - Campos:
        - id_user: auto increment
        - nome: varchar 100
        - sobrenome: varchar 100
        - email: varchar 200
        - senha: varchar 100
```
- Grupo:
    - Descrição: Natureza do gasto, exemplo: contas, lazer, comida, festa...

``` 
    Campos:
        id_grupo: auto increment
        nome: varchar 100
```
- Gasto_grupo:
```
    Campos:
        id_grupo: vinculo
        id_gasto: vinculo
```

```
tabela usuario grupo -> limitar quantidade de grupos criáveis para 3-4 
todas as tabelas -> colocar um status ativo para exclusões sem perca de dados
```


- Gasto:
    - Descrição: o gasto em específico, exemplo: conta de luz, festa x, lanche, tv...

    - Regra: em gasto terá um controle de data registrado automaticamente ou preenchido pelo usuário.
```
    Campos:
        id_gasto: auto increment
        nome: varchar 100
        data: tempo atual da transação/data selecionada pelo user
```

# ROTAS

 ### POST (CREATE)
```
     /login

     /user 

     /grupo

     /grupo/{id_grupo}/gasto
```

 ### GET (READ)
```
    Retorna todos os usuários
        /user

    Retorna um usuário
        /user/{id_user}
```

```
    Retorna todos os grupos
        /grupo

    Retorna um grupo
        /grupo/{id_grupo}
        
    Retorna todos os gastos de um grupo
        /grupo/{id_grupo}/gasto

    Retorna um gasto de um grupo
        /grupo/{id_grupo}/gasto/{id_gasto}

```

 ### PUT (UPDATE)
```
    User:
         /user/{user_id}
```
```
    Grupo:
         /grupo/{grupo_id}
        Gasto: 
             /grupo/{grupo_id}/gasto/{gasto_id}
```

 ### DELETE (DELETE)
```
    User:
         /user/{user_id}
```
```
    Grupo:
         /grupo/{grupo_id}

        Gasto:
             /grupo/{grupo_id}/gasto/{gasto_id}
```


# RETORNOS

## POST /login

- **Parâmetros:**
  - `email` (string) - Email do usuário.
  - `senha` (string) - Senha do usuário.

- **Retorno de Sucesso:**
  - **Status:** `200 OK`
  - **Exemplo de Resposta:**
    ```json
    {
      "message": "Login realizado com sucesso.",
      "token": "jwt_token"
    }
    ```

- **Retorno de Erro:**
  - **Status:** `401 Unauthorized`
  - **Exemplo de Resposta:**
    ```json
    {
      "error": "Credenciais inválidas."
    }
    ```

---

## POST /user

- **Parâmetros:**
  - `nome` (string) - Nome do usuário.
  - `sobrenome` (string) - Sobrenome do usuário.
  - `email` (string) - Email do usuário.
  - `senha` (string) - Senha do usuário.

- **Retorno de Sucesso:**
  - **Status:** `201 Created`
  - **Exemplo de Resposta:**
    ```json
    {
      "message": "Usuário criado com sucesso.",
      "user_id": 1
    }
    ```

- **Retorno de Erro:**
  - **Status:** `400 Bad Request`
  - **Exemplo de Resposta:**
    ```json
    {
      "error": "Erro ao criar o usuário. Verifique os dados enviados."
    }
    ```

---

## POST /grupo

- **Parâmetros:**
  - `nome` (string) - Nome do grupo.

- **Retorno de Sucesso:**
  - **Status:** `201 Created`
  - **Exemplo de Resposta:**
    ```json
    {
      "message": "Grupo criado com sucesso.",
      "grupo_id": 1
    }
    ```

- **Retorno de Erro:**
  - **Status:** `400 Bad Request`
  - **Exemplo de Resposta:**
    ```json
    {
      "error": "Erro ao criar o grupo. Verifique os dados enviados."
    }
    ```

---

## POST /grupo/{id_grupo}/gasto

- **Parâmetros:**
  - `id_grupo` (int) - ID do grupo.
  - `nome` (string) - Nome do gasto.
  - `data` (string, opcional) - Data do gasto.

- **Retorno de Sucesso:**
  - **Status:** `201 Created`
  - **Exemplo de Resposta:**
    ```json
    {
      "message": "Gasto criado com sucesso.",
      "gasto_id": 1
    }
    ```

- **Retorno de Erro:**
  - **Status:** `400 Bad Request`
  - **Exemplo de Resposta:**
    ```json
    {
      "error": "Erro ao criar o gasto. Verifique os dados enviados."
    }
    ```

---

## GET /user

- **Parâmetros:** Nenhum.

- **Retorno de Sucesso:**
  - **Status:** `200 OK`
  - **Exemplo de Resposta:**
    ```json
    [
      {
        "id_user": 1,
        "nome": "Gabriel",
        "sobrenome": "Sena",
        "email": "gabriel@example.com"
      }
    ]
    ```

- **Retorno de Erro:**
  - **Status:** `404 Not Found`
  - **Exemplo de Resposta:**
    ```json
    {
      "error": "Nenhum usuário encontrado."
    }
    ```

---

## GET /user/{id_user}

- **Parâmetros:**
  - `id_user` (int) - ID do usuário.

- **Retorno de Sucesso:**
  - **Status:** `200 OK`
  - **Exemplo de Resposta:**
    ```json
    {
      "id_user": 1,
      "nome": "Gabriel",
      "sobrenome": "Sena",
      "email": "gabriel@example.com"
    }
    ```

- **Retorno de Erro:**
  - **Status:** `404 Not Found`
  - **Exemplo de Resposta:**
    ```json
    {
      "error": "Usuário não encontrado."
    }
    ```

---

## PUT /user/{user_id}

- **Parâmetros:**
  - `user_id` (int) - ID do usuário.
  - `nome` (string, opcional) - Novo nome do usuário.
  - `sobrenome` (string, opcional) - Novo sobrenome do usuário.
  - `email` (string, opcional) - Novo email do usuário.
  - `senha` (string, opcional) - Nova senha do usuário.

- **Retorno de Sucesso:**
  - **Status:** `200 OK`
  - **Exemplo de Resposta:**
    ```json
    {
      "message": "Usuário atualizado com sucesso."
    }
    ```

- **Retorno de Erro:**
  - **Status:** `400 Bad Request`
  - **Exemplo de Resposta:**
    ```json
    {
      "error": "Erro ao atualizar o usuário. Verifique os dados enviados."
    }
    ```

---

## PUT /grupo/{grupo_id}

- **Parâmetros:**
  - `grupo_id` (int) - ID do grupo.
  - `nome` (string, opcional) - Novo nome do grupo.

- **Retorno de Sucesso:**
  - **Status:** `200 OK`
  - **Exemplo de Resposta:**
    ```json
    {
      "message": "Grupo atualizado com sucesso."
    }
    ```

- **Retorno de Erro:**
  - **Status:** `400 Bad Request`
  - **Exemplo de Resposta:**
    ```json
    {
      "error": "Erro ao atualizar o grupo. Verifique os dados enviados."
    }
    ```

---

## PUT /grupo/{grupo_id}/gasto/{gasto_id}

- **Parâmetros:**
  - `grupo_id` (int) - ID do grupo.
  - `gasto_id` (int) - ID do gasto.
  - `nome` (string, opcional) - Novo nome do gasto.
  - `data` (string, opcional) - Nova data do gasto.

- **Retorno de Sucesso:**
  - **Status:** `200 OK`
  - **Exemplo de Resposta:**
    ```json
    {
      "message": "Gasto atualizado com sucesso."
    }
    ```

- **Retorno de Erro:**
  - **Status:** `400 Bad Request`
  - **Exemplo de Resposta:**
    ```json
    {
      "error": "Erro ao atualizar o gasto. Verifique os dados enviados."
    }
    ```

---

## DELETE /user/{user_id}

- **Parâmetros:**
  - `user_id` (int) - ID do usuário.

- **Retorno de Sucesso:**
  - **Status:** `200 OK`
  - **Exemplo de Resposta:**
    ```json
    {
      "message": "Usuário deletado com sucesso."
    }
    ```

- **Retorno de Erro:**
  - **Status:** `404 Not Found`
  - **Exemplo de Resposta:**
    ```json
    {
      "error": "Usuário não encontrado."
    }
    ```

---

## DELETE /grupo/{grupo_id}

- **Parâmetros:**
  - `grupo_id` (int) - ID do grupo.

- **Retorno de Sucesso:**
  - **Status:** `200 OK`
  - **Exemplo de Resposta:**
    ```json
    {
      "message": "Grupo deletado com sucesso."
    }
    ```

- **Retorno de Erro:**
  - **Status:** `404 Not Found`
  - **Exemplo de Resposta:**
    ```json
    {
      "error": "Grupo não encontrado."
    }
    ```

---

## DELETE /grupo/{grupo_id}/gasto/{gasto_id}

- **Parâmetros:**
  - `grupo_id` (int) - ID do grupo.
  - `gasto_id` (int) - ID do gasto.

- **Retorno de Sucesso:**
  - **Status:** `200 OK`
  - **Exemplo de Resposta:**
    ```json
    {
      "message": "Gasto deletado com sucesso."
    }
    ```

- **Retorno de Erro:**
  - **Status:** `404 Not Found`
  - **Exemplo de Resposta:**
    ```json
    {
      "error": "Gasto não encontrado."
    }
    ```

---
