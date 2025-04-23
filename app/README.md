# 🏥 Aplicación de Citas Médicas con Flask y Docker

Esta es una aplicación web básica para agendar citas médicas, construida con **Flask**, **HTML/CSS/JS** y usando **PostgreSQL** como base de datos, todo desplegado a través de **Docker**.

## 📁 Estructura del Proyecto

```
.
├── app.py                 # Backend principal con Flask
├── requirements.txt       # Dependencias
├── Dockerfile             # Imagen Docker para Flask
├── docker-compose.yml     # Orquestación de contenedores
├── templates/             # Archivos HTML (Jinja2)
│   └── cuestionario.html
├── static/                # Archivos CSS y JS
│   ├── styles.css
│   └── script.js
```

## 🚀 ¿Cómo ponerla en marcha?

### 1. Clona este repositorio
```bash
git clone https://github.com/tu-usuario/mi-app-flask.git
cd mi-app-flask
```

### 2. Levanta la aplicación con Docker
```bash
docker-compose up --build
```

### 3. Inicializa la base de datos (una sola vez)
```bash
docker-compose exec web flask initdb
```

## 🌐 Accede a la aplicación

Abre tu navegador en:
```
http://localhost:5000
```

## 🛠 ¿Qué incluye esta aplicación?

- Formulario web para agendar citas
- Listado de doctores y hospitales (precargados)
- Guardado en base de datos PostgreSQL
- Estilo CSS moderno y confirmación con JS
- Deploy completo con Docker

## 🧪 ¿Cómo agregar datos desde consola?

```bash
docker-compose exec web flask shell
```

Dentro de la consola interactiva:

```python
from app import db, Doctor
db.session.add(Doctor(nombre='Dr. Test', especialidad='Odontología'))
db.session.commit()
```

## 📦 Requisitos

- Docker + Docker Compose instalado
- Navegador web
- (Opcional) Git para clonar el repo

## 📤 ¿Cómo desplegarlo online?

Puedes usar servicios gratuitos como:
- [Render.com](https://render.com)
- [Railway.app](https://railway.app)
- [Replit](https://replit.com)

## 👨‍💻 Autor

Desarrollado como parte de un proyecto académico por **[Tu Nombre]**  
📧 contacto@tucorreo.com

## 📝 Licencia

Este proyecto está bajo la licencia MIT. Eres libre de usarlo y modificarlo.
