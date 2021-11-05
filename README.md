# **Coopers**
Este sistema foi desenvolvido como um teste técnico e tem o objetivo de automatizar a tarefa de guardar dados de usuários sobre suas To-do lists.

Ao utilizar esta API, deve ser possível criar novas tasks, bem como listar, excluir ou atualizar tais informações caso o usuário tenha as devidas permissões.

Como instalar e rodar? 🚀
Para instalar o sistema, é necessário seguir alguns passos, como baixar o projeto e fazer instalação das dependências. Para isso, é necessário abrir uma aba do terminal e digitar o seguinte:

# Este passo é para baixar o projeto
git clone https://github.com/<your_user>/coopers-back.git
Depois que terminar de baixar, é necessário entrar na pasta, criar um ambiente virtual e entrar nele:

# Entrar na pasta
cd coopers-back

# Criar um ambiente virtual
python3 -m venv venv

# Entrar no ambiente virtual
source venv/bin/activate
Então, para instalar as dependências, basta:

pip install -r requirements.txt
Depois de ter instalado as dependências, é necessário rodar as migrations para que o banco de dados e as tabelas sejam criadas:

./manage.py migrate
Então, para rodar, basta digitar o seguinte, no terminal:

./manage.py runserver
E o sistema estará rodando em http://127.0.0.1:8000/

Utilização 🖥️
Para utilizar este sistema, é necessário utilizar um API Client, como o Insomnia

## **Rotas:**

### **Rotas de Usuários:**
**POST /api/accounts/**
Esta rota serve para registrar novos usuários, podendo ele ser, aluno, instrutor ou facilitador dependendo dos valores dos campos booleanos is_staff e is_superuser

*RESPONSE STATUS -> HTTP 201 (created)*

Body:

```
{
    "username": "student",
    "password": "1234",
}
```

Response:

```
{
    "id": 1,
    "username": "student",
}
```

**POST /api/login/**
Esta rota serve para realizar o login do usuário.

*RESPONSE STATUS -> HTTP 200 (OK)*

Body:

```
{
    "username": "student",
    "password": "1234"
}
```
Response:

```
{
    "token": <token de autenticação>
}
```

### **Rotas de Tasks:**

**POST /api/tasks/**
Esta rota serve para criar novas tasks, o usuário necessita estar logado para tal

*RESPONSE STATUS -> HTTP 201 (created)*

Body:

```
{
    "name": "Node"
}
```

Response:

```
{
    "id": 1,
    "name": "Node",
    "users": []
}
```

**PUT /api/courses/<int:course_id>/**
Esta rota serve para atualizar o nome de um curso.

*RESPONSE STATUS -> HTTP 200 (OK)*

Body:

```
{
    "title": "Ler o README"
}
```

Response:

```
{
    "id": 1,
    "title": "Ler o README",
    "completed": false,
    "user_id": 1
}
```

**PUT /api/tasks/<int:task_id>/**
Esta rota serve para atualizar uma task, alterando o nome ou atualizando o status de completed.

*RESPONSE STATUS -> HTTP 200 (OK)*

Body:

```
{
    "title": "Continuar lendo o README"
    "completed": false,
}
```
Response:

```
{
    "id": 1,
    "title": "Continuar lendo o README"
    "completed": false,
    "user_id": 1
}
```
**_é necessário enviar ambos os campos._**


**GET /api/tasks/**
Esta rota retorna todas as tasks pertencentes ao usuário.

*RESPONSE STATUS -> HTTP 200 (OK)*

Response:

```
[
    {
        "id": 1,
        "title": "Continuar lendo o README"
        "completed": false,
        "user_id": 1
    },
    {
        "id": 2,
        "title": "Ler metade do README"
        "completed": true,
        "user_id": 1
    }
]
```

**GET /api/tasks/<int:task_id>/**
Esta rota retorna uma task específica pertencente ao usuário.

*RESPONSE STATUS -> HTTP 200 (OK)*

Response:

```
{
    "id": 2,
    "title": "Ler metade do README"
    "completed": true,
    "user_id": 1
}
```

**DELETE /api/tasks/**
Esta rota deleta todas as tasks do usuário.

Não há conteúdo no retorno da requisição.

*RESPONSE STATUS -> HTTP 204 (no content)*


**DELETE /api/tasks/<int:task_id>/**
Esta rota deleta uma task específica do usuário.

Não há conteúdo no retorno da requisição.

*RESPONSE STATUS -> HTTP 204 (no content)*

**DELETE /api/tasks/completed/**
Esta rota deleta tasks com o campo completed = true do usuário.

Não há conteúdo no retorno da requisição.

*RESPONSE STATUS -> HTTP 204 (no content)*

**DELETE /api/tasks/incompleted/**
Esta rota deleta tasks com o campo completed = false do usuário.

Não há conteúdo no retorno da requisição.

*RESPONSE STATUS -> HTTP 204 (no content)*

### **Tecnologias utilizadas** 📱
  Django
  Django Rest Framework
  Django Rest Framework AuthToken
  SQLite

Licence
  MIT