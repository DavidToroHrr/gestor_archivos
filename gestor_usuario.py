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
import subprocess

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

###################################################
#FUNCIONES PARA PODER GESTIONAR LOS USUARIOS
def crear_usuario(usuario, sistema):
    """Crea un usuario en el sistema operativo."""
    try:
        if sistema == "Windows":
            subprocess.run(["net", "user", usuario, "/add"], check=True)
            print(f"Usuario '{usuario}' creado correctamente en Windows.")
        elif sistema == "Linux":
            subprocess.run(["sudo", "useradd", usuario], check=True)
            print(f"Usuario '{usuario}' creado correctamente en Linux.")
        else:
            print("Sistema no soportado.")
    except subprocess.CalledProcessError as e:
        print(f"Error al crear el usuario '{usuario}': {e.stderr}")

def eliminar_usuario(usuario, sistema):
    """Elimina un usuario en el sistema operativo."""
    try:
        if sistema == "Windows":
            subprocess.run(["net", "user", usuario, "/delete"], check=True)
            print(f"Usuario '{usuario}' eliminado correctamente en Windows.")
        elif sistema == "Linux":
            subprocess.run(["sudo", "userdel", usuario], check=True)
            print(f"Usuario '{usuario}' eliminado correctamente en Linux.")
        else:
            print("Sistema no soportado.")
    except subprocess.CalledProcessError as e:
        print(f"Error al eliminar el usuario '{usuario}': {e.stderr}")

def crear_grupo(grupo, sistema):
    """Crea un grupo de usuarios en el sistema operativo."""
    try:
        if sistema == "Windows":
            subprocess.run(["net", "localgroup", grupo, "/add"], check=True)
            print(f"Grupo '{grupo}' creado correctamente en Windows.")
        elif sistema == "Linux":
            subprocess.run(["sudo", "groupadd", grupo], check=True)
            print(f"Grupo '{grupo}' creado correctamente en Linux.")
        else:
            print("Sistema no soportado.")
    except subprocess.CalledProcessError as e:
        print(f"Error al crear el grupo '{grupo}': {e.stderr}")

def eliminar_grupo(grupo, sistema):
    """Elimina un grupo de usuarios en el sistema operativo."""
    try:
        if sistema == "Windows":
            subprocess.run(["net", "localgroup", grupo, "/delete"], check=True)
            print(f"Grupo '{grupo}' eliminado correctamente en Windows.")
        elif sistema == "Linux":
            subprocess.run(["sudo", "groupdel", grupo], check=True)
            print(f"Grupo '{grupo}' eliminado correctamente en Linux.")
        else:
            print("Sistema no soportado.")
    except subprocess.CalledProcessError as e:
        print(f"Error al eliminar el grupo '{grupo}': {e.stderr}")