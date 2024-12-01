import subprocess
import ntsecuritycon as con
import win32security

def mostrar_acls(ruta):
    """Muestra las ACLs de un archivo o directorio."""
    try:
        resultado = subprocess.run(['icacls', ruta], capture_output=True, text=True, check=True)
        return(f"ACLs de {ruta}:\n{resultado.stdout}")
    except subprocess.CalledProcessError as e:
        return(f"Error al mostrar las ACLs de {ruta}: {e.stderr}")

def asignar_permiso(ruta, usuario_grupo, permiso):
    """
    Asigna un permiso (lectura, escritura, ejecución) a un usuario o grupo en un archivo o directorio.

    :param ruta: Ruta completa del archivo o directorio.
    :param usuario_grupo: Nombre del usuario o grupo.
    :param permiso: Permiso a asignar ('read', 'write', 'execute').
    """
    try:
        # Mapear permiso a constante de Windows
        permisos_map = {
            'read': con.FILE_GENERIC_READ,
            'write': con.FILE_GENERIC_WRITE,
            'execute': con.FILE_GENERIC_EXECUTE
        }
        
        # Validar el permiso
        if permiso.lower() not in permisos_map:
            raise ValueError(f"Permiso inválido: {permiso}. Use 'read', 'write' o 'execute'.")

        # Obtener la máscara de permiso correspondiente
        permisos_bitmask = permisos_map[permiso.lower()]

        # Obtener el descriptor de seguridad del archivo o directorio
        sd = win32security.GetFileSecurity(ruta, win32security.DACL_SECURITY_INFORMATION)

        # Obtener la DACL actual
        dacl = sd.GetSecurityDescriptorDacl()
        if dacl is None:
            dacl = win32security.ACL()

        # Resolver el nombre del usuario o grupo a un SID
        sid, _, _ = win32security.LookupAccountName(None, usuario_grupo)

        # Crear una nueva regla de acceso
        dacl.AddAccessAllowedAce(win32security.ACL_REVISION, permisos_bitmask, sid)

        # Aplicar la DACL modificada
        sd.SetSecurityDescriptorDacl(1, dacl, 0)
        win32security.SetFileSecurity(ruta, win32security.DACL_SECURITY_INFORMATION, sd)

        return(f"Permiso '{permiso}' asignado a '{usuario_grupo}' en '{ruta}'.")
    except Exception as e:
        return(f"Error al asignar permiso: {e}")

def eliminar_permisos(ruta, usuario_grupo):
    """
    Elimina todos los permisos asignados a un usuario o grupo en un archivo o directorio.

    :param ruta: Ruta completa del archivo o directorio.
    :param usuario_grupo: Nombre del usuario o grupo cuyos permisos serán eliminados.
    """
    try:
        # Obtener el descriptor de seguridad del archivo o directorio
        sd = win32security.GetFileSecurity(ruta, win32security.DACL_SECURITY_INFORMATION)

        # Obtener la DACL actual
        dacl = sd.GetSecurityDescriptorDacl()
        if dacl is None:
            print(f"No hay permisos asignados en '{ruta}'.")
            return

        # Resolver el nombre del usuario o grupo a un SID
        sid, _, _ = win32security.LookupAccountName(None, usuario_grupo)

        # Crear una nueva DACL eliminando las reglas asociadas al usuario o grupo
        nueva_dacl = win32security.ACL()
        for i in range(dacl.GetAceCount()):
            ace = dacl.GetAce(i)
            ace_sid = ace[2]
            # Copiar todas las reglas excepto las asociadas al usuario o grupo
            if ace_sid != sid:
                nueva_dacl.AddAce(win32security.ACL_REVISION, i, ace)

        # Aplicar la nueva DACL al archivo o directorio
        sd.SetSecurityDescriptorDacl(1, nueva_dacl, 0)
        win32security.SetFileSecurity(ruta, win32security.DACL_SECURITY_INFORMATION, sd)

        return(f"Todos los permisos eliminados para '{usuario_grupo}' en '{ruta}'.")
    except Exception as e:
        return(f"Error al eliminar permisos: {e}")


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