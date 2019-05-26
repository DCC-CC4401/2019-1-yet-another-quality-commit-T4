# Su readme para usuarios
Aca voy a poner una lista cagona de cosas que he hecho
* hice un comando para crear los grupos, lo pueden correr de esta forma
    ```shell
    $ python manage.py creategrupos
    ```
*   hice un comando para crear administradores, es asi
    ```shell
    $ python manage.py createadministrador
    ```
    El comando te pide unos parametros y de ahi crea uno de nuestros administradores junto 
    con un usuario de django relacionado. Ahora en el login solo se puede ingresar cuando 
    el usuario es un administrador, si no te deja pasar (para crear un usuario normal
    se puede hacer de la consola de admin de django o a traves del shell de django)
    