"""
gestor_usuario.py

Descripción:
Este archivo permite gestionar permisos de usuarios basados en roles para un sistema de archivos.
Incluye funcionalidades para verificar si un usuario tiene permiso para realizar acciones
específicas y para cargar roles y permisos desde un archivo de configuración en formato JSON.

Autores:
- David Toro 
- Thomas Toro 


"""

import json

def cargar_roles():

    """
    Carga la configuración de roles y permisos desde un archivo JSON roles.json.

    Retorno:
        dict: Un diccionario con la estructura de roles y sus permisos, por ejemplo: {"administrador": [...]}

    Excepciones:
        FileNotFoundError: Si el archivo roles.json no se encuentra.
        json.JSONDecodeError: Si el archivo roles.json tiene un formato incorrecto.
        Exception: Para cualquier otro error no esperadq.

    Autores: 
        - David Toro
        - Thomas Toro
    """
    with open('roles.json', 'r') as file:
        return json.load(file)

def verificar_permiso(rol, operacion):

    """
    Verifica si un rol específico tiene permiso para realizar una operación.

    Parámetros:
        rol (str): Nombre del rol a verificar (por ejemplo, 'administrador', 'director', 'consultor').
        operacion (str): Operación que se desea realizar (por ejemplo, 'crear', 'listar', 'mover').



    Retorna: bool: Retorna True si el rol tiene permiso para la operación, de lo contrario, False.

    Dependencia: Esta función utiliza 'cargar_roles()' para obtener la configuración de permisos desde 'roles.json'.

    Autores: 
        - David Toro
        - Thomas Toro
    """
    roles = cargar_roles()
    permisos = roles.get("roles").get(rol, [])
    return operacion in permisos