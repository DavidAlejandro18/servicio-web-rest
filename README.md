# Actividad 8. Desarrollo de servicio web tipo RESTful

## Descripción
En esta actividad se desarrollará un servicio web tipo RESTful que permita realizar operaciones CRUD sobre una entidad de datos. Para ello, se utilizará el framework Flask de Python.

Los datos representan una colección de productos, ordenes y autenticación en los que se pueden realizar las siguientes operaciones:
- Obtener los productos
- Obtener un producto por categoria
- Agregar une nueva orden
- Actualizar una orden
- Eliminar una orden
- Autenticar un usuario

## Instalación
Para poder iniciar el proyecto primero debemos de clonar el repositorio en nuestra máquina local. Para ello, abrimos una terminal y ejecutamos el siguiente comando:
```bash
git clone https://github.com/DavidAlejandro18/servicio-web-rest.git
```

Una vez clonado el repositorio, nos movemos a la carpeta del proyecto:
```bash
cd servicio-web-rest
```

Se recomienda trabajar en un entorno virtual para no tener conflictos con las dependencias del proyecto. Para ello, ejecutamos el siguiente comando:
```bash
python -m venv <nombre_del_entorno>
```

Activamos el entorno virtual:
- En Windows:
```bash
<nombre_del_entorno>\Scripts\activate
```

- En MacOS y Linux:
```bash
source <nombre_del_entorno>/bin/activate
```

Para desactivar el entorno virtual, ejecutamos el siguiente comando:
```bash
deactivate
```

Instalamos las dependencias del proyecto:
```bash
pip install -r requirements.txt
```

## Uso
Para iniciar el servicio web, ejecutamos el siguiente comando:
```bash
python run.py
```

El servicio web estará disponible en la siguiente dirección:
```
http://127.0.0.1:5000
```