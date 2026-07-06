Portafolio: Catálogo de Productos en Django

## 1. Descripción
Aplicación web desarrollada como portafolio personal, construida desde cero aplicando buenas prácticas de programación y desarrollo. Permite gestionar un catálogo de productos, facilitando las operaciones de registro, consulta, modificación y eliminación de información, con validaciones y una interfaz clara y fácil de usar.

## 2. Tecnologías y herramientas utilizadas
- **Python 3**: Lenguaje de programación base
- **Django**: Framework para estructurar y desarrollar la aplicación
- **HTML5 + Bootstrap 5**: Para crear la interfaz de usuario y diseño responsivo
- **SQLite**: Base de datos integrada para almacenar la información
- **Git y GitHub**: Control de versiones y alojamiento del proyecto en línea

## 3. Requisitos previos
- Tener instalado Python 3 en el equipo
- Conexión a internet para instalar dependencias

## 4. Pasos para ejecutar el proyecto
1. Descargar o clonar el repositorio en tu computadora
2. Abrir la terminal y acceder a la carpeta del proyecto:
   cd actividad_django
3. Instalar el framework Django si no lo tienes:
   pip install django
4. Aplicar las configuraciones de la base de datos:
   python3 manage.py migrate
5. Iniciar el servidor de desarrollo:
   python3 manage.py runserver
6. Abrir en el navegador la dirección:
   http://127.0.0.1:8000

## 5. Estructura del proyecto
- `actividad_django/`: Carpeta principal con la configuración general
- `productos/`: Módulo que contiene modelos, vistas, formularios y lógica de la aplicación
- `templates/`: Archivos HTML con el diseño de las páginas
- `db.sqlite3`: Archivo de la base de datos
- `manage.py`: Archivo principal para ejecutar comandos de Django

## 6. Funcionalidades principales
- Listar todos los productos registrados
- Agregar nuevos productos con validación de campos
- Editar la información de productos existentes
Eliminar registros con confirmación previa
- Clasificar productos por categorías
- Interfaz adaptada para computadoras, tabletas y celulares
- Mensajes claros para informar al usuario de cada operación
