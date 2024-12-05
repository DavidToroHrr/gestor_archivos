import subprocess
import ntsecuritycon as con
import win32security

from gestor_archivo import validar_archivo_existe,validar_directorio_existe

from gestor_usuario import validar_usuario_grupo

def mostrar_acls(ruta):
    """Muestra las ACLs de un archivo o directorio."""
    if not validar_archivo_directorio(ruta):
        return (f"el archivo o directorio ingresado NO existe, error.")
    
    try:
        #captura la salida del comando, interpreta la salia como texto, lanza excepcion si hay errorres
        resultado = subprocess.run(['icacls', ruta], capture_output=True, text=True, check=True)
        return(f"ACLs de {ruta}:\n{resultado.stdout}") #.stdout contiene la salida, las acls
    except subprocess.CalledProcessError as e:
        return(f"Error al mostrar las ACLs de {ruta}: {e.stderr}") #si el comando falla se maneja la excepcion

def asignar_permiso(ruta, usuario_grupo, permiso):
    """
    Asigna un permiso (lectura, escritura, ejecución) a un usuario o grupo en un archivo o directorio.

    :param ruta: Ruta completa del archivo o directorio.
    :param usuario_grupo: Nombre del usuario o grupo.
    :param permiso: Permiso a asignar ('read', 'write', 'execute').
    """
    if not validar_archivo_directorio(ruta):
        return (f"el archivo o directorio ingresado NO existe, error.")
    if not validar_usuario_grupo(usuario_grupo):
        return (f"error, no se encuentra el usuario o grupo")
    try:
        # Mapear permiso a constante de Windows, obtenifos de ntsecuritycon
        permisos_map = {
            'read': con.FILE_GENERIC_READ,
            'write': con.FILE_GENERIC_WRITE,
            'execute': con.FILE_GENERIC_EXECUTE
        }
        
        # Validar el permiso , si está en el dict permisos_map
        if permiso.lower() not in permisos_map:
            raise ValueError(f"Permiso inválido: {permiso}. Use 'read', 'write' o 'execute'.")

        # Obtener la valor numérico de permiso correspondiente
        permisos_bitmask = permisos_map[permiso.lower()]

        # Obtener el descriptor de seguridad del archivo o directorio (que incluye la DACL).
        sd = win32security.GetFileSecurity(ruta, win32security.DACL_SECURITY_INFORMATION)

        # Obtener la DACL actual , lo extrae del descriptor de seguridad, si no hay dacl la crea
        dacl = sd.GetSecurityDescriptorDacl()
        if dacl is None:
            dacl = win32security.ACL()

        # Resolver el nombre del usuario o grupo a un SID, convierte el numbre de un user en un id de seguridad
        sid, _, _ = win32security.LookupAccountName(None, usuario_grupo)

        # Crear una nueva regla de acceso access control entry a la dacl con el permido identificado
        dacl.AddAccessAllowedAce(win32security.ACL_REVISION, permisos_bitmask, sid)

        # Aplicar la DACL modificada Discretionary Access Control List, lista de permisos de users o grupos
        sd.SetSecurityDescriptorDacl(1, dacl, 0) #acrualiza el descriptor de seguridad con la dacl modificada
        win32security.SetFileSecurity(ruta, win32security.DACL_SECURITY_INFORMATION, sd) #aplica los cambios al archivo o dict

        return(f"Permiso '{permiso}' asignado a '{usuario_grupo}' en '{ruta}'.")
    except Exception as e:
        return(f"Error al asignar permiso: {e}")

def eliminar_permisos(ruta, usuario_grupo, permiso):
    
    """
    Elimina un permiso específico asignado a un usuario o grupo en un archivo o directorio.

    :param ruta: Ruta completa del archivo o directorio.
    :param usuario_grupo: Nombre del usuario o grupo cuyos permisos serán modificados.
    :param permiso: Permiso a eliminar ('read', 'write', 'execute').
    """
    if not validar_archivo_directorio(ruta):
        return (f"el archivo o directorio ingresado NO existe, error.")
    if not validar_usuario_grupo(usuario_grupo):
        return (f"error, no se encuentra el usuario o grupo")
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
            print(f"No hay permisos asignados en '{ruta}'.")
            return

        # Resolver el nombre del usuario o grupo a un SID
        sid, _, _ = win32security.LookupAccountName(None, usuario_grupo)

        # Crear una nueva DACL, inicialmente vacía
        nueva_dacl = win32security.ACL()

        # Recorrer las ACEs actuales en la DACL
        for i in range(dacl.GetAceCount()):
            ace = dacl.GetAce(i)  # Obtener la ACE actual
            ace_sid = ace[2]  # Obtener el SID de la ACE actual

            # Si no corresponde al SID del usuario o grupo, se agrega la ACE
            if ace_sid != sid:
                nueva_dacl.AddAccessAllowedAce(win32security.ACL_REVISION, ace[1], ace_sid)
            else:
                # Si es la ACE del usuario o grupo, verificamos si tiene el permiso que queremos eliminar
                if (ace[1] & permisos_bitmask) != 0:  # Verificar si el permiso específico está presente
                    # Si el permiso está presente, no agregamos la ACE (la eliminamos)
                    continue
                else:
                    # Si el permiso no está presente, lo agregamos sin modificarlo
                    nueva_dacl.AddAccessAllowedAce(win32security.ACL_REVISION, ace[1], ace_sid)

        # Aplicar la nueva DACL al archivo o directorio
        sd.SetSecurityDescriptorDacl(1, nueva_dacl, 0)
        win32security.SetFileSecurity(ruta, win32security.DACL_SECURITY_INFORMATION, sd)

        return(f"Permiso '{permiso}' eliminado para '{usuario_grupo}' en '{ruta}'.")
    except Exception as e:
        return(f"Error al eliminar permiso: {e}")

def validar_archivo_directorio(ruta):
    if  validar_archivo_existe(ruta) or validar_directorio_existe(ruta):
        return True
    else: return False


