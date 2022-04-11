# Elenas test
## Solución a la prueba propuesta por elenas
Reto Técnico Backend:
Se requiere hacer una app para registrar tareas como se muestra a continuación:
Escribe un REST API en Django para suplir los siguientes requerimientos
Python - Django.

- Los usuarios se deben autenticar
- Las tareas son privadas. Solo las puede administrar su dueño
- Los usuarios pueden agregar, editar, eliminar y marcar como completa/incompleta las tareas
- El listado de tareas debe ser paginado
- Agregar validaciones, como no aceptar tareas sin descripción, etc
- Buscar por descripción
- Escribir test unitarios en el primer commit

## Tecnologías
Para llevar a cabo el reto se utilizaron las herramientas:
- [Docker - docker compose](https://www.docker.com/) - Para la arquitectura de aplicación!
- [Django](https://www.djangoproject.com/) - Como base del backend de la aplicación.
- [Django rest framework](https://www.django-rest-framework.org/) - Como apoyo de django para crear la API.
- [Postgresql](https://www.postgresql.org/) - Para la persistencia de los datos.

## Instalación

Elenas test requiere docker y docker compose instalados en la maquina.

```sh
git clone https://github.com/camilo300792/elenast-test.git
cd elenas-test
docker-compose up --build
```

## Endpoints

| METODO | ENDPOINT | DESCRIPCION | TOKEN |
| ------ | ------ | ------ | ------ |
| POST | [auth/signup]() | Registro de usuario | N/A
| POST | [auth/signin]() | Solicitar token | N/A
| POST | [task]() | Crear tarea | requerido
| GET | [task]() | Listar tareas | requerido
| GET | [task/{id}]() | Detalle de tarea | requerido
| PUT | [task/{id}]() | Actualizar tarea | requerido
| PATCH | [task/{id}]() | Actualizar tarea parcial | requerido
| DELETE | [task/{id}]() | Eliminar tarea | requerido

## Registro de usuario

### Request

```sh
curl --location --request POST 'localhost:8000/auth/signup/' \
--form 'username="testuser"' \
--form 'password="12345678ABCD$"' \
--form 'password_confirmation="12345678ABCD$"' \
--form 'email="test@example.com"' \
--form 'first_name="Jhon"' \
--form 'last_name="Doe"'
```

### Response
```sh
HTTP/1.1 201 OK

{
    "username": "testuser3",
    "email": "test2@example.com",
    "first_name": "Jhons",
    "last_name": "Does"
}
```

## Solicitar token

### Request

```sh
curl --location --request POST 'localhost:8000/auth/signin/' \
--form 'username="testuser3"' \
--form 'password="12345678ABCD$"'
```

### Response

```sh
HTTP/1.1 201 OK

{
    "token": "2f19994526af9478ffec39267a327dc43a29bfa7"
}
```

## Tareas

### Schema
```json
{
    "id": {
        "type": "integer",
        "read_only": true
    },
    "title": {
        "type": "string",
        "required": true,
        "max_length": 75 
    },
    "description": {
        "type": "string",
        "required": true,
        "max_length": 255 
    },
    "status": {
        "type": "string",
        "required": false,
        "max_length": 2,
        "valid_values": {
            "P": "Pending",
            "IR": "In Review",
            "IP": "In Process",
            "C": "Completed",
        },
        "default": "Pending"
    },
    "owner": {
        "type": "string",
        "read_only": true,
    }
}
```

## Crear Tareas
### Request

```sh
curl --location --request POST 'localhost:8000/tasks/' \
--header 'Authorization: Token 2f19994526af9478ffec39267a327dc43a29bfa7' \
--header 'Content-Type: application/json' \
--data-raw '{
    "title": "Breakfast",
    "description": "Make breakfast"
}'
```

### Response

```sh
HTTP/1.1 201 OK

{
    "id": 9,
    "title": "Breakfast",
    "description": "Make breakfast",
    "owner": "testuser",
    "status": "Pending"
}
```

## Listar Tareas

### Request

```sh
curl --location --request GET 'localhost:8000/tasks' \
--header 'Authorization: Token 2f19994526af9478ffec39267a327dc43a29bfa7'

# filtros
curl --location --request GET 'localhost:8000/tasks?status=P' \
--header 'Authorization: Token 2f19994526af9478ffec39267a327dc43a29bfa7'

curl --location --request GET 'localhost:8000/tasks?titulo=mi tarea' \
--header 'Authorization: Token 2f19994526af9478ffec39267a327dc43a29bfa7'

curl --location --request GET 'localhost:8000/tasks?descripcion=mi descripcion' \
--header 'Authorization: Token 2f19994526af9478ffec39267a327dc43a29bfa7'
```

### Response

```sh
HTTP/1.1 200 OK

{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 9,
            "title": "Breakfast",
            "description": "Make Breakfast",
            "owner": "testuser3",
            "status": "Pending"
        }
    ]
}
```

## Detalle Tarea

### Request

```sh
curl --location --request GET 'localhost:8000/tasks/9' \
--header 'Authorization: Token 2f19994526af9478ffec39267a327dc43a29bfa7'
```

### Response

```sh
HTTP/1.1 200 OK

{
    "id": 9,
    "title": "Breakfast",
    "description": "Make Breakfast",
    "owner": "testuser",
    "status": "Pending"
}
```

## Actualizar Tarea

### Request

```sh
curl --location --request PUT 'localhost:8000/tasks/9' \
--header 'Authorization: Token 2f19994526af9478ffec39267a327dc43a29bfa7' \
--header 'Content-Type: application/json' \
--data-raw '{
    "title": "Breakfast",
    "description": "Make breakfast",
    "status": "Pending"
}'
```

### Response

```sh
HTTP/1.1 200 OK

{
    "id": 9,
    "title": "Breakfast",
    "description": "Make Breakfast",
    "owner": "testuser",
    "status": "Pending"
}
```

## Actualizar Tarea Parcial

### Request

```sh
curl --location --request PATCH 'localhost:8000/tasks/9' \
--header 'Authorization: Token 2f19994526af9478ffec39267a327dc43a29bfa7' \
--header 'Content-Type: application/json' \
--data-raw '{
    "status": "Completed"
}'
```

### Response

```sh
HTTP/1.1 200 OK

{
    "id": 9,
    "title": "Breakfast",
    "description": "Make Breakfast",
    "owner": "testuser",
    "status": "Completed"
}
```

## Elimiar Tarea

### Request

```sh
curl --location --request DELETE 'localhost:8000/tasks/7' \
--header 'Authorization: Token 2f19994526af9478ffec39267a327dc43a29bfa7'
```

### Response

```sh
HTTP/1.1 204 No Content
```

## Listado de errores

| ERROS | DESCRIPCION | SUGERENCIA |
| ------ | ------ | ------ |
| 401 | Usuario no autenticado | Solicita un token |
| 403 | El recurso solicitado no es de otro usuario | Solo puedes trabajar con tus tareas |
| 404 | El recurso solicitado no existe | Asegurate que el id exista |
| 400 | El request enviado contiene errores | Corrige el request |


Autor Camilo Martinez Salcedo