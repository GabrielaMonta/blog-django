
# FeCh - Informatorio 2024
## Descripcion
Esta es la propuesta de proyecto final desarrollado en la segunda etapa del Informatorio 2024 (Resistencia - Chaco). 
FeCh (Festivales Chaqueños) es un blog dedicado a la promoción y difusión de festivales y eventos en toda la extension del Chaco, Argentina. Su objetivo principal es servir como una plataforma informativa y accesible donde los usuarios pueden descubrir, compartir y participar en diversas actividades culturales, recreativas y educativas que se llevan a cabo en la provincia.

## Objetivo
El blog busca promover la cultura y las actividades sociales en el Chaco, incentivando la participación de la comunidad en eventos que enriquecen la vida provincial. Al ser una plataforma accesible y fácil de usar, pretende conectar a los ciudadanos con las iniciativas locales, fomentar el turismo interno y fortalecer el tejido social de la región.

## Idea Original del proyecto
https://drive.google.com/drive/u/4/folders/1QO9CoN6eD1qscVi0jfoPjp1l8_m6_PWz?authuser=0

## Deploy link
https://benjaminpaez.pythonanywhere.com/

## Video presentacion
https://drive.google.com/drive/folders/16wVbfA4Ai_d6m-yykHg4cElCrQxWfIMh?usp=drive_link

## Estructura del proyecto
ESTRUCTURA DEL PROYECTO

```
├── entorno/						<--- Carpeta del entorno
│ ├── Scripts/
│ │ ├── activate.bat
│ │ ├── deactivate.bat
│ │ └── ...
│ └── ...
├── blog-repo/					<--- Carpeta del Repositorio
│ ├── blog/					    <--- Carpeta del proyecto Django
│ │ ├── apps/					<--- Aplicaciones Django
│ │ │ ├── post/
│ │ │ │ ├── __pycache__/	    **Ignorada en el .gitignore**
│ │ │ │ ├── migrations/		    **Ignorada en el .gitignore**
│ │ │ │ ├── __init__.py
│ │ │ │ ├── admin.py
│ │ │ │ ├── apps.py
│ │ │ │ ├── models.py
│ │ │ │ ├── tests.py
│ │ │ │ ├── urls.py
│ │ │ │ └── views.py
│ │ │ ├── user/
│ │ │ │ ├── __pycache__/	    **Ignorada en el .gitignore**
│ │ │ │ ├── migrations/		    **Ignorada en el .gitignore**
│ │ │ │ ├── __init__.py
│ │ │ │ ├── admin.py
│ │ │ │ ├── apps.py
│ │ │ │ ├── models.py
│ │ │ │ ├── tests.py
│ │ │ │ ├── urls.py
│ │ │ │ └── views.py
│ │ │ └── ...
│ │ ├── blog/
│ │ │ ├── __pycache__/		    **Ignorada en el .gitignore**
│ │ │ ├── configurations/	    <--- Configuraciones django (opcional)
│ │ │ │ ├── __pycache__/	    **Ignorada en el .gitignore**
│ │ │ │ ├── local.py		    <--- Configuraciones para desarrollo local
│ │ │ │ ├── production.py	    <--- Configuraciones para produccion
│ │ │ │ ├── settings.py		    <--- Configuraciones base
│ │ │ │ └── ...
│ │ │ ├── __init__.py
│ │ │ ├── asgi.py
│ │ │ ├── settings.py
│ │ │ ├── urls.py
│ │ │ ├── wsgi.py
│ │ │ └── ...
│ │ ├── media/				    <--- Archivos multimedia - **Podria ser ignorada en el .gitignore**
│ │ │ ├── post/
│ │ │ │ ├── post_default.jpeg
│ │ │ │ └── ...
│ │ │ ├── user/
│ │ │ │ ├── user_default.png
│ │ │ │ └── ...
│ │ │ └── ...
│ │ ├── static/				    <--- Archivos estáticos
│ │ │ ├── assets/
│ │ │ │ ├── img/
│ │ │ │ ├── svg/
│ │ │ │ ├── favicon.ico
│ │ │ │ └── ...
│ │ │ ├── css/
│ │ │ │ ├── style.css
│ │ │ │ └── ...
│ │ │ ├── js/
│ │ │ │ ├── main.js
│ │ │ │ └── ...
│ │ │ └── ...
│ │ ├── templates/			    <--- Archivos templates
│ │ │ ├── auth/
│ │ │ │ ├── auth_login.html
│ │ │ │ ├── auth_register.html
│ │ │ │ └── ...
│ │ │ ├── errors/
│ │ │ │ ├── not_found.html
│ │ │ │ ├── internal_error.html
│ │ │ │ └── ...
│ │ │ ├── includes/
│ │ │ │ ├── base.html
│ │ │ │ ├── footer.html
│ │ │ │ ├── header.html
│ │ │ │ └── ...
│ │ │ ├── post/
│ │ │ │ ├── post_delete.html
│ │ │ │ ├── post_detail.html
│ │ │ │ ├── post_list.html
│ │ │ │ ├── post_new.html
│ │ │ │ ├── post_update.html
│ │ │ │ └── ...
│ │ │ ├── user/
│ │ │ │ ├── user_profile.html
│ │ │ │ ├── user_update.html
│ │ │ │ └── ...
│ │ │ ├── index.html
│ │ │ └── ...
│ │ ├── db.sqlite3			    <--- Base de datos - **Ignorada en el .gitignore**
│ │ ├── manage.py
│ │ └── ...
│ ├── .gitignore
│ ├── README.md				    <--- Archivo README.md - Describe el proyecto
│ ├── requeriments.txt		    <--- Archivo requeriments.txt - Enlista los paquetes
| └── ...
└── ...
```

## Desarrolladores
- JUDKEVICH, Natasha --                email: njudkevich@gmail.com
- MONTANARO, Gabriela Antonella --    email: gabrielaam201@gmail.com
- PAEZ, Benjamin  --                  email: benjamineliaspaez@gmail.com
