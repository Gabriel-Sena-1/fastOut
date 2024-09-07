# Como rodar?
O primeiro passo consiste em clonar o projeto do repositório remoto do Github para sua máquina. Para isso, basta usar o seguinte comando:
```
  git clone https://github.com/Gabriel-Sena-1/meu_bolso.git
```
Após isso, você deve navegar para o diretório em que o projeto está estruturado, usando o seguinte comando:
```
  cd meu_bolso
  code .
```
Isso irá abrir o projeto direto no [VSCode](https://code.visualstudio.com/), se o mesmo estiver instalado na sua máquina, se não, você pode instalar clicando no link deste texto.
Em seguida, para que o projeto funcione na sua máquina, basta você instalar o [Docker](https://docs.docker.com/engine/install/ubuntu/) e usar o seguinte comando:
```
  docker compose up --build
```
Isso irá instalar automaticamente o projeto e todas as dependências necessárias para seu funcionamento em três containeres separados. Após isso, acessando o endereço http://localhost:8000/docs em qualquer navegador da sua máquina, todos os endpoints da API estarão disponíveis para teste, pois o projeto já entra em funcionamento com um banco de dados feito para testes.

# Escopo do projeto

Uma aplicação para controle de gastos pessoais. Nessa aplicação você deve conseguir criar e gerenciar seus gastos pessoais. Podendo adicionar dispesas e suas naturezas. 

Plus: relatórios mensais em gráficos com base na natureza da despesa.

# System Design
    > HTML, Tailwind CSS, JS        -> Front-end
        > VueJS 
        > Express JS -> consumir api

    > Python + FastAPI                       -> Back-end
    > MySQL                         -> Database
    > Docker

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
        - tipo_usuario: int
        - qtd_grupos: int
```
- Grupos:
    - Descrição: Natureza do gasto, exemplo: contas, lazer, comida, festa...

``` 
    Campos:
        id_grupo: auto increment
        nome: varchar 100
```
- Gastos:
    - Descrição: o gasto em específico, exemplo: conta de luz, festa x, lanche, tv...

    - Regra: em gasto terá um controle de data registrado automaticamente ou preenchido pelo usuário.
```
    Campos:
        id_gasto: auto increment
        nome: varchar 100
        valor: float
        data: tempo atual da transação/data selecionada pelo user
```
- Gasto_grupo:
```
    Campos:
        id_grupo: vinculo
        id_gasto: vinculo
```

*Tarefas:*
* *Status ativo nas tabelas para exclusões sem perca de dados. Atualmente apenas usuário conta com esse atributo.*
* *Token de autenticação.*
* *OAuth2 para guardar as senhas com segurança.*
* *Chart.js para visualização de relatórios de gastos.*


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
        /grupos

    Retorna um grupo
        /grupos/{id_grupo}
        
    Retorna todos os gastos
        /gastos

    Retorna todos os gastos de um grupo
        /gastos/{id_grupo}

    Retorna um gasto de um grupo
        /grupos/{id_grupo}/gasto/{id_gasto}

```

 ### PUT (UPDATE)
```
    User:
         /user/{user_id}
```
```
    Grupo:
         /grupos/{grupo_id}
        Gasto: 
             /grupos/{grupo_id}/gastos/{gasto_id}
```

 ### DELETE (DELETE)
```
    User:
         /user/{user_id}
```
```
    Grupo:
         /grupos/{grupo_id}

        Gasto:
             /grupos/{grupo_id}/gastos/{gasto_id}
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
