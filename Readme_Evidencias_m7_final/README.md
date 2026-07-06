# Actividad Módulo 7 – Administración de Catálogo de Productos

## Motor de base de datos utilizado
Se emplea **SQLite3**, que es el motor de base de datos por defecto en Django. Se almacena en el archivo `db.sqlite3` dentro de la carpeta principal del proyecto.

## Descripción del modelo de datos
Se definieron dos modelos relacionados:

### 1. Categoría
Sirve para agrupar los productos.
- `nombre`: Campo de texto, único y obligatorio para identificar la categoría.
- `descripcion`: Campo de texto opcional para detalles adicionales.

### 2. Producto
Representa cada artículo del catálogo.
- `nombre`: Nombre del producto (obligatorio).
- `descripcion`: Detalles y características del producto.
- `precio`: Valor numérico con dos decimales, validado para ser **mayor a 0**.
- `stock`: Cantidad de unidades disponibles en inventario.
- `categoria`: Relación de tipo **muchos a uno** con el modelo `Categoría` (un producto pertenece a una sola categoría).
- `fecha_creacion`: Fecha y hora automática en el momento de registrar el producto.
- `activo`: Estado del producto (activo o inactivo).

## Rutas principales
- `/products/` → Listado completo de todos los productos registrados.
- `/products/create/` → Formulario para agregar un producto nuevo.
- `/products/edit/<int:id>/` → Formulario para modificar los datos de un producto existente.
- `/products/delete/<int:id>/` → Pantalla de confirmación antes de eliminar un producto.
- `/admin/` → Panel de administración de Django para gestionar categorías y productos.

## Pasos para ejecutar el proyecto
1. Abrir la terminal en la carpeta raíz del proyecto (`actividad_django`).
2. Verificar que Django esté instalado:
   ```bash
   pip install django

3. Aplicar las migraciones para crear las tablas en la base de datos:
python3 manage.py makemigrations
python3 manage.py migrate

4. Crear usuario administrador (si es necesario):
python3 manage.py createsuperuser

5. Iniciar el servidor de desarrollo:
python3 manage.py runserver

6. Acceder desde el navegador:
Catálogo de productos: http://127.0.0.1:8000/products/
Panel de administración: http://127.0.0.1:8000/admin/
