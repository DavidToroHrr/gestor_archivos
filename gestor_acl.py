import subprocess

def mostrar_acls(ruta):
    """Muestra las ACLs de un archivo o directorio."""
    try:
        resultado = subprocess.run(['getfacl', ruta], capture_output=True, text=True, check=True)
        print(f"ACLs de {ruta}:\n{resultado.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"Error al mostrar las ACLs de {ruta}: {e.stderr}")

def asignar_permisos(ruta, usuario_grupo, permisos):
    """Asigna permisos (lectura, escritura, ejecución) a un usuario o grupo."""
    try:
        subprocess.run(['setfacl', '-m', f'{usuario_grupo}:{permisos}', ruta], check=True)
        print(f"Permisos '{permisos}' asignados a '{usuario_grupo}' en '{ruta}'.")
    except subprocess.CalledProcessError as e:
        print(f"Error al asignar permisos: {e.stderr}")

def eliminar_permisos(ruta, usuario_grupo):
    """Elimina los permisos asignados a un usuario o grupo."""
    try:
        subprocess.run(['setfacl', '-x', usuario_grupo, ruta], check=True)
        print(f"Permisos eliminados para '{usuario_grupo}' en '{ruta}'.")
    except subprocess.CalledProcessError as e:
        print(f"Error al eliminar permisos: {e.stderr}")

# Ejemplo de uso:
# if __name__ == "__main__":
#     print("Gestión de ACLs:")
#     print("1. Mostrar ACLs")
#     print("2. Asignar permisos")
#     print("3. Eliminar permisos")
#     opcion = input("Seleccione una opción (1/2/3): ")

#     ruta = input("Ingrese la ruta del archivo o directorio: ")

#     if opcion == '1':
#         mostrar_acls(ruta)
#     elif opcion == '2':
#         usuario_grupo = input("Ingrese el usuario o grupo (formato: usuario o grupo:usuario): ")
#         permisos = input("Ingrese los permisos (r, w, x o combinados como rwx): ")
#         asignar_permisos(ruta, usuario_grupo, permisos)
#     elif opcion == '3':
#         usuario_grupo = input("Ingrese el usuario o grupo cuyo permiso desea eliminar: ")
#         eliminar_permisos(ruta, usuario_grupo)
#     else:
#         print("Opción no válida.")