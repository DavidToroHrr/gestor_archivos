import os
import shutil


def crear_directorio(nombre, ruta_base):
    ruta_completa = os.path.join(ruta_base, nombre)

    if not validar_directorio_existe(ruta_base):
        return(f"Error: La ruta base '{ruta_base}' no existe.")
    
    elif validar_directorio_existe(ruta_completa):
        return(f"Error, el directorio {ruta_completa} ya existe y no se puede crear de nuevo.")
    try:
        # Crear el directorio en el sistema de archivos
        os.makedirs(ruta_completa, exist_ok=True)
        return(f"Directorio '{nombre}' creado correctamente.")

    except Exception as e:
        return (f"Error al crear el directorio '{nombre}': {e}.")

def crear_archivo(nombre, ruta_base):
    """
    Crea un archivo en una ruta especificada, en donde se le puede asignar cualquier nombre a determinado archivo
    
    Autor(es):
    - David Esteban Toro Herrera
    -Thomas Alejandro Toro Herrera

    Parámetros:
    nombre (str): Indica el nombre que tendrá el archivo
    ruta_base (str): Indica los directorios en los cuales estará almacenado dicho archivo

    Retorna:
    str: Un mensaje que nos indica el resultado de la operación... Es posible que se retorne un mensaje de éxito o error

    Excepciones:

    """
    ruta_completa = os.path.join(ruta_base, nombre)
    # Validar el nombre del archivo

    if not nombre or not isinstance(nombre, str):
        return("El nombre del archivo no es válido.")

    elif validar_archivo_existe(ruta_completa):
        return(f"Error, el directorio {ruta_completa} ya existe y no se puede crear de nuevo.")


    if not validar_directorio_existe(ruta_base):
            return(f"Error: La ruta base '{ruta_base}' no existe.")
    
    try:
        with open(ruta_completa, 'w') as f:
            # Aquí podrías escribir contenido inicial si es necesario
            return(f"Archivo '{nombre}' creado correctamente.")

    except Exception as e:
        return(f"Error al crear el archivo '{nombre}': {e}")


# Mover archivo o directorio
def mover_elemento(origen, destino):
    if not validar_directorio_existe(origen):
        return (f"Error: La ruta '{origen}' no existe.")
    
    elif not validar_directorio_existe(destino):
        return (f"Error: La ruta '{destino}' no existe.")

    try:
        # Mover el elemento (archivo o directorio)
        shutil.move(origen, destino)
        print(f"Elemento '{origen}' movido a '{destino}' correctamente.")

    except Exception as e:
        print(f"Error al mover el elemento : {e}")

# Listar archivos en un directorio
def listar_archivos(ruta_base):
    """
    Lista los archivos en una ruta especificada, en donde se realiza un filtrado especial para ver solamante los archivos
    en determinado directorio
    
    Autor(es):
    - David Esteban Toro Herrera
    -Thomas Alejandro Toro Herrera

    Parámetros:
    ruta_base (str): Indica los directorios en los cuales se busca listar los archivos

    Retorna:
    str: Un mensaje que nos indica el resultado de la operación... Es posible que se retorne un mensaje de éxito o error

    Excepciones:

    """
    arreglo_archivos=[]

    if not validar_directorio_existe(ruta_base):
        return (f"Error: La ruta '{ruta_base}' no existe.")

    try:
        #SE HACE EL FILTRADO CORRESPONDIENTE DE SOLAMETE LOS ARCHIVOS
        #se recorre el directorio con los elementos f,y se filtran los elementos de tal manera
        #de que si cumplen con la condición de ser archivos se guardan en el arreglo de "archivos"
        archivos = [f for f in os.listdir(ruta_base) if os.path.isfile(os.path.join(ruta_base, f))]
        
        for archivo in archivos:
            arreglo_archivos.append(archivo)

        return (f"los archivos son: {arreglo_archivos}")
    
    except Exception as e:
        return(f"Error al listar los archivos en '{ruta_base}': {e}")

# Función para listar directorios
def listar_directorios(ruta_base):
    arreglo_directorios=[]

    if not validar_directorio_existe(ruta_base):
        return (f"Error: La ruta '{ruta_base}' no existe.")
    
    try:
        directorios= [f for f in os.listdir(ruta_base) if os.path.isdir(os.path.join(ruta_base, f))]

        # print(f"Directorios en el proyecto:")
        for directorio in directorios:
            arreglo_directorios.append(directorio)

        return (f"los directorios son: {arreglo_directorios}")
    except Exception as e:
        return(f"Error al listar los directorios en '{ruta_base}': {e}")

# 9. Eliminar archivo
def eliminar_archivo(nombre,ruta_base):
    """
    Elimina un archivo en una ruta especificada
    
    Autor(es):
    - David Esteban Toro Herrera
    -Thomas Alejandro Toro Herrera

    Parámetros:
    nombre (str): Indica el nombre que tendrá el archivo
    ruta_base (str): Indica los directorios en los cuales estará almacenado dicho archivo

    Retorna:
    str: Un mensaje que nos indica el resultado de la operación... Es posible que se retorne un mensaje de éxito o error

    Excepciones:

    """
    ruta_completa = os.path.join(ruta_base, nombre)

    if not validar_archivo_existe(ruta_completa):
        return("Error, el archivo que buscas eliminar no existe")
    try:
        os.remove(ruta_completa)
        return(f"Archivo '{nombre}' eliminado.")

    except Exception as e:
        return(f"Error al eliminar el archivo '{nombre}': {e}.")

def eliminar_directorio(nombre, ruta_base):
    ruta_completa = os.path.join(ruta_base, nombre)

    if not validar_directorio_existe(ruta_completa):  
        return("Error, el directorio que buscas eliminar no existe")
    
    try:
        shutil.rmtree(ruta_completa)  # Eliminar el directorio en el sistema de archivos
        return(f"Directorio '{nombre}' eliminado correctamente.")

    except Exception as e:
        return(f"Error al eliminar el directorio '{nombre}': {e}")

# 8. Renombrar archivo
def renombrar_archivo(nombre_actual,nuevo_nombre,ruta_base):
    """
    Renombra un archivo en una ruta especificada
    
    Autor(es):
    - David Esteban Toro Herrera
    -Thomas Alejandro Toro Herrera

    Parámetros:
    nombre_actual (str): Indica el nombre que tiene
    nuevo_nombre (str): Indica el nuevo nombre que tendrá el archivo
    ruta_base (str): Indica los directorios en los cuales estará almacenado dicho archivo. Es la misma ruta para ambos nombres
    porque lo que se busca hacer es renombrar un mismo archivo

    Retorna:
    str: Un mensaje que nos indica el resultado de la operación... Es posible que se retorne un mensaje de éxito o error

    Excepciones:

    """
    ruta_actual = os.path.join(ruta_base, nombre_actual)
    nueva_ruta = os.path.join(ruta_base, nuevo_nombre)

    if not validar_archivo_existe(ruta_actual):  
        return("Error, el archivo que buscas renombrar no existe")

    try:
        os.rename(ruta_actual, nueva_ruta)
        return(f"Archivo renombrado de '{nombre_actual}' a '{nuevo_nombre}'.")
    
    except FileNotFoundError:
        return(f"El archivo '{nombre_actual}' no existe.")

def renombrar_directorio(nombre_actual, nuevo_nombre, ruta_base):
    ruta_actual = os.path.join(ruta_base, nombre_actual)
    nueva_ruta = os.path.join(ruta_base, nuevo_nombre)
    
    # Verificar si el directorio existe
    if not validar_directorio_existe(ruta_actual):
        return(f"El directorio '{nombre_actual}' no existe.")
        
    try:
        # Renombrar el directorio
        os.rename(ruta_actual, nueva_ruta)
        return(f"Directorio renombrado de '{nombre_actual}' a '{nuevo_nombre}'.")

    except Exception as e:
        return(f"Error al renombrar el directorio '{nombre_actual}': {e}")


#####FUNCIONES PARA VERIFICAR LA EXISTENCIA DE ARCHIVOS Y DIRECTORIOS########

def validar_archivo_existe(ruta_archivo):
    """Valida si un archivo existe."""
    if os.path.isfile(ruta_archivo):
        #print(f"El archivo '{ruta_archivo}' existe.")
        return True
    else:
        #print(f"El archivo '{ruta_archivo}' no existe.")
        return False

def validar_directorio_existe(ruta_directorio):
    """Valida si un directorio existe."""
    if os.path.isdir(ruta_directorio):
        ##print(f"El directorio '{ruta_directorio}' existe.")
        return True
    else:
        #print(f"El directorio '{ruta_directorio}' no existe.")
        return False