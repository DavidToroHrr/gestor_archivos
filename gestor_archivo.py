import os
import shutil


def crear_directorio(nombre, ruta_base):
        ruta_completa = os.path.join(ruta_base, nombre)
        # Crear el directorio en el sistema de archivos
        os.makedirs(ruta_completa, exist_ok=True)
        print(f"Directorio '{nombre}' creado correctamente.")



# Mover archivo o directorio
def mover_elemento(origen, destino, ruta_base):
    ruta_origen = os.path.join(ruta_base, origen)
    ruta_destino = os.path.join(ruta_base, destino)
    
    # Verificar si el elemento de origen existe
    if not os.path.exists(ruta_origen):
        print(f"El elemento '{origen}' no existe.")
        return
    
    try:
        # Mover el elemento (archivo o directorio)
        shutil.move(ruta_origen, ruta_destino)
        print(f"Elemento '{origen}' movido a '{destino}' correctamente.")
    except Exception as e:
        print(f"Error al mover el elemento '{origen}': {e}")


def eliminar_directorio(nombre, ruta_base):
    ruta_completa = os.path.join(ruta_base, nombre)
    if os.path.isdir(ruta_completa):
        try:
            shutil.rmtree(ruta_completa)  # Eliminar el directorio en el sistema de archivos
            print(f"Directorio '{nombre}' eliminado correctamente.")
        except Exception as e:
            print(f"Error al eliminar el directorio '{nombre}': {e}")
    else:
        print(f"El directorio '{nombre}' no se encuentra en el proyecto.")

def renombrar_directorio(nombre_actual, nuevo_nombre, ruta_base):
    ruta_actual = os.path.join(ruta_base, nombre_actual)
    nueva_ruta = os.path.join(ruta_base, nuevo_nombre)
    
    # Verificar si el directorio existe
    if not os.path.isdir(ruta_actual):
        print(f"El directorio '{nombre_actual}' no existe.")
        return
    
    try:
        # Renombrar el directorio
        os.rename(ruta_actual, nueva_ruta)
        print(f"Directorio renombrado de '{nombre_actual}' a '{nuevo_nombre}'.")
    except Exception as e:
        print(f"Error al renombrar el directorio '{nombre_actual}': {e}")


def crear_archivo(nombre, ruta_base):
    # Validar el nombre del archivo
    if not nombre or not isinstance(nombre, str):
        print("El nombre del archivo no es válido.")
        return

    ruta_completa = os.path.join(ruta_base, nombre)
    
    try:
        with open(ruta_completa, 'w') as f:
            # Aquí podrías escribir contenido inicial si es necesario
            print(f"Archivo '{nombre}' creado correctamente.")
    except Exception as e:
        print(f"Error al crear el archivo '{nombre}': {e}")

    

# Listar archivos en un directorio
def listar_archivos(nombre,ruta_base):
    ruta_completa = os.path.join(ruta_base, nombre)
    try:
        archivos = os.listdir(ruta_completa)
        print(f"Archivos en el directorio '{nombre}':")
        for archivo in archivos:
            print(f"- {archivo}")
    except Exception as e:
        print(f"Error al listar los archivos en '{nombre}': {e}")

# Función para listar directorios
def listar_directorios(ruta_base):
    try:
        elementos = os.listdir(ruta_base)
        print(f"Directorios en el proyecto:")
        for elemento in elementos:
            if os.path.isdir(os.path.join(ruta_base, elemento)):
                print(f"- {elemento}")
    except Exception as e:
        print(f"Error al listar los directorios en '{ruta_base}': {e}")


# 9. Eliminar archivo
def eliminar_archivo(nombre,ruta_base):
    ruta_completa = os.path.join(ruta_base, nombre)
    try:
        os.remove(ruta_completa)
        print(f"Archivo '{nombre}' eliminado.")
    except FileNotFoundError:
        print(f"El archivo '{nombre}' no existe.")


# 8. Renombrar archivo
def renombrar_archivo(nombre_actual, nuevo_nombre,ruta_base):
    ruta_actual = os.path.join(ruta_base, nombre_actual)
    nueva_ruta = os.path.join(ruta_base, nuevo_nombre)
    try:
        os.rename(ruta_actual, nueva_ruta)
        print(f"Archivo renombrado de '{nombre_actual}' a '{nuevo_nombre}'.")
    except FileNotFoundError:
        print(f"El archivo '{nombre_actual}' no existe.")