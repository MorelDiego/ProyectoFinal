# CinemaRevs

CinemaRevs es un proyecto de blog realizado para CoderHouse. 

## Instalacion

- Clonar el repositorio
- Crear entorno virtual 
```bash
cd ..
python -m virtualenv django
```
- Activar el entorno virtual
```bash
django\Scripts\activate 
```
- Instalar Django
```bash
pip install django 
pip install pillow
```
- Ahora esta listo para correr
```bash
cd ProyectoFinalMorel
python manage.py runserver
```
- Desde la url dada por consola podremos visualizar el proyecto, junto con todas sus funciones:

1. Boton home "CinemaRevs".
2. Boton "Search" buscar peliculas por su titulo.
3. Boton "Reviews" visualiza los Reviews creados, y en caso de estar logueado, brinda la opcion de crear, editar o eliminar posts propios (o todos en caso de admin status).
4. Boton "Share a Review" nos lleva al formulario para crear posts.
5. Boton "About" presenta descripcion sobre la creacion del blog.
6. Boton "Contact us" visualiza formulario de contacto.
7. Botones Login, Sign up, Logout. Formularios de creacion de usuarios, inicio de sesion, cierre de sesion, edicion de usuarios (avatares añadidos mediante django admin).
