# Aplicación de Citas Médicas con Flask y Docker

Esta es una aplicación web básica para agendar citas médicas, construida con **Flask**, **HTML/CSS/JS** y usando **PostgreSQL** como base de datos, todo desplegado a través de **Docker**.

## ¿Cómo ponerla en marcha?

### 1. Clona este repositorio
```bash
git clone https://github.com/tu-usuario/mi-app-flask.git
cd mi-app-flask
```

### 2. Levantar la aplicación con Docker
```bash
docker-compose up --build
```

### 3. Inicializar la base de datos (una sola vez)
```bash
docker-compose exec web flask initdb
```

## Accede a la aplicación

Abre el navegador en:
```
http://localhost:5000
```

## ¿Qué hace la aplicación?

- Formulario web para agendar citas
- Listado de doctores y hospitales (precargados)
- Guardado en base de datos PostgreSQL

## ¿Cómo agregar datos desde consola?

```bash
docker-compose exec web flask shell
```

Dentro de la consola interactiva:

```python
from app import db, Doctor
db.session.add(Doctor(nombre='Dr. Test', especialidad='Odontología'))
db.session.commit()
```

## Requisitos

- Docker + Docker Compose instalado
- Git para clonar el repo (Opcional)
