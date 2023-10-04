# proyecto_web_curso

Repositorio Git para el proyecto Django.

# Instalar virtualenv

Para instalarlo y luego crearlo ejecutamos:

`apt install python3-virtualenv`

`cd <carpeta_del_repositorio_git>`

`virtualenv -p /usr/bin/python3.8 --prompt "(virtualenv-PWC)" virtualenv`

Activar el virtualenv recién creado y luego actualizar pip:

`source virtualenv/bin/activate`

Descargar e instalar pip por medio del script get-pip.py:

`curl -sS https://bootstrap.pypa.io/get-pip.py | python3`

Luego actualizamos pip mas otras deps relacionadas:

`pip install --upgrade pip setuptools wheel`
