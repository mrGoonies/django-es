# Proyecto Alexandria
Este repositorio tiene como objetivo aprender Django y Python, creando una aplicación web que permita a los usuarios compartir libros de manera gratuita. 

Dentro de este proyecto aprenderemos los conceptos básicos del framework, como por ejemplo:
- Crear una aplicación web.
- Diferencias entre un proyecto y una aplicación en Django.
- Crear modelos utilizando el ORM que viene por defecto en Django.
- Utilizar templates y renderizarlos en las vistas.
- Usar el sistema de autenticación que viene por defecto en Django.
- Administrar usuarios y la base de datos con Django Admin.
- Usar la migración de base de datos que viene por defecto en Django.

El proyecto se encuentra en la rama `main` y las implementaciones del proyecto se encuentran en las diferentes ramas del proyecto.

# Contenido
- [Django Framework](#Django)
  - [Funcionalidades](#Funcionalidades)
- [Instalación](#Instalación)
---

## Django
Django es un framework web escrito en Python (es el más utilizado) denominado por los creadores, "Un framework con baterías incluidas", esto quiere decir que trae diferentes librerías que permiten desarrollar sin tener que agregar librerías externas.
Este framework utiliza la arquitectura MVT que está basada en MVC. Una de las características más importantes es su seguridad y escalabilidad, no por algo es utilizado por empresas como:
- Netflix 
- Instagram
- Dropbox
- entre otras más.

### Funcionalidades

Django tiene sus propias características y comprenderlas nos ayudará a avanzar aprendiendo con este Framework.
- URL Routes. 
	- Se encarga de tomar el endpoint de nuestra app y redirigirla a una app de nuestro proyecto. Se encarga de asignar las rutas de nuestro proyecto.
- View y Template
	- Las vistas se encargan de la lógica del negocio y el template es la página estática (HTML y CSS).
- Models
	- Son los objetos que interactúan en nuestra base de datos. En otras palabras, los modelos son las tablas en forma de objeto que son administradas por un ORM.
- User y Admins.
	- Es una herramienta compleja que viene por defecto en Django y permite administrar usuarios y nuestra base de datos utilizando una GUI desde el navegador.

---

## Instalación
Para instalar Django, debemos tener instalado Python en nuestro sistema operativo. Para verificar si tenemos instalado Python, debemos abrir una terminal y escribir el siguiente comando:
```bash
# Mac / Linux
python3 --version

#Windows
python --version
```

Si no tenemos instalado Python, debemos instalarlo desde su [página oficial](https://www.python.org/downloads/).

Tras instalara Python es hora de crear un entorno virtual para poder instalar las dependencias de nuestro proyecto. Para ello, debemos abrir una terminal y escribir el siguiente comando:

```bash
# Mac / Linux
python3 -m venv env

# Windows
python -m venv env

# Activar entorno virtual
source env/bin/activate # Mac / linux

entorno\Scripts\activate # Windows

# Instalar dependencias del proyecto
pip -r requirements.txt

```