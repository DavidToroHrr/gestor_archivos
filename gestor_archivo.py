"""
gesto_archivo.py

Autores:
- David Toro
- Thomas Toro

Descripción:
Este archivo proporciona un conjunto de funciones para la gestión de archivos y 
directorios en un sistema de archivos. Incluye funcionalidades como crear, 
mover, listar, renombrar y eliminar archivos y directorios, así como validar 
la existencia de estos. Cada función maneja posibles errores y excepciones, 
dando mensajes claros sobre el estado de las operaciones.


"""
import os
import shutil

def crear_directorio(nombre, ruta_base):

    """
    Crea un nuevo directorio en el sistema en la ruta indicada.
    
    Autores:
    - David Toro
    - Thomas Toro
    
    Parámetros:
    nombre (str): El nombre indica el nombre del directorio que vamos a crear
    ruta_base (str): Es la ruta en la que se desea crear el directorio
    
    Retorna: 
    str: Un mensaje que indica el resultado de la operación.
                Pueden ser mesajes de éxito en la creación o error si el proceso falla.
                
    Excepciones:
    Si la ruta base no existe, devuelve un mensaje de error.
    Si ocurre un error al crear un directorio, devuelve el mensaje de lo que ocurrió.
    
    """
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

    - Si el nombre del archivo es inválido, devuelve un mensaje de error.
    - Si el archivo ya existe en la ruta especificada, devuelve un mensaje de error.
    - Si la ruta base no existe, devuelve un mensaje de error.
    - Si ocurre un error al intentar crear el archivo, devuelve el mensaje del error ocurrido.

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

    """
    Mueve un archivo o directorio de una ruta de origen a una ruta especificada de destino.
    
    Autores: 
    - David Toro
    - Thomas Toro

    Parámetros:
    origen (str): Ruta del archivo o directorio que se desea mover.
    destino (str): Ruta de destino a la que se moverá el archivo o directorio.

    Retorna:
    str: Un mensaje que indica el resultado de la operación. 
        Puede ser un mensaje de éxito o un error dependiendo de si la operación falla.

    Excepciones:
    Si alguna de las rutas no existe, devuelve un mensaje de error.
    Si ocurre un error al mover el archivo o directorio, devuelve un mensaje de error específico.
    """
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
def listar_archivos(ruta_base,Nulo):
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

    - Si la ruta base no existe, devuelve el mensaje:
    Error: La ruta '<ruta>' no existe.
    - Si ocurre cualquier otro error al intentar listar los archivos (por ejemplo, problemas de permisos 
    para acceder a la ruta o directorio), se captura la excepción general y se devuelve el mensaje de error detallado.


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
def listar_directorios(ruta_base,Nulo):

    """
    Muestra los directorios presentes en una ruta especificada
    
    Autores: 
    - David Toro
    - Thomas Toro
    
    Parámetro: 
    ruta_base (str): Es la ruta en la que se desean ver los directorios contenidos
    
    Retorna:
    str: Mensaje que indica el resultado de la operación
                El mensaje puede ser de error, diciendo lo que pasó específicamente
                o puede ser un mensaje que indica los directorios litados de forma efectiva.
                
    Excepciones:
    Si alguna de las rutas no existe, retorna un mensaje de error.
    Si ocurre un error en el listado, devuelve de forma específica el error sucedido. 
		
    """
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

    - Si el archivo a eliminar no existe, devuelve el mensaje:
      "Error, el archivo que buscas eliminar no existe."
    - Si ocurre un error al intentar eliminar el archivo (por ejemplo, problemas de permisos o el archivo está en uso), 
      se captura la excepción general y se devuelve un mensaje detallado con el error ocurrido.


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

    """
    
    Elimina un directorio del sistema dada una ruta y nombre del directorio.
    
    Autores: 
    - David Toro
    - Thomas Toro
    
    Parámetros: 
    nombre (str): Es el nombre del direcotorio a eliminar dada la ruta especificada.
    ruta_base (str): Es la ruta especificada en la que se realizará la eliminación.
    
    Retorna:
    str: Mensaje que indica el resultado de la operación , que puede ser de éxito o fracaso en la eliminación.
    
    Excepciones:
    Si el directorio no existe, retorna un mensaje de error
    Si ocurre un error al tratar la eliminación, retorna el error específico dado
    De lo contrario retorna un mensaje de éxito de la operación.
    
    """
    ruta_completa = os.path.join(ruta_base, nombre)

    if not validar_directorio_existe(ruta_completa):  
        return("Error, el directorio que buscas eliminar no existe")
    
    try:
        shutil.rmtree(ruta_completa)  # Eliminar el directorio en el sistema de archivos
        return(f"Directorio '{nombre}' eliminado correctamente.")

    except Exception as e:
        return(f"Error al eliminar el directorio '{nombre}': {e}")

# 8. Renombrar archivo
def renombrar_archivo(nombre_actual,nuevo_nombre):
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
    str: Un mensaje que nos indica el resultado de la operación, retorna un mensaje de éxito o error

    Excepciones:

    - Si el archivo con el nombre actual no existe, devuelve el mensaje:
      Error, el archivo que buscas renombrar no existe.
    - Si el archivo no se puede renombrar por algún problema con el sistema de archivos, la excepción FileNotFoundError es capturada y devuelve el mensaje:
      El archivo nombre_actual no existe.
    - Si ocurre un error inesperado al intentar renombrar el archivo, devuelve el mensaje del error ocurrido.

    """
    
    directorio_actual=os.path.dirname(nombre_actual)
    directorio_actual_v2=os.path.dirname(nuevo_nombre)

    if not validar_directorio_existe(directorio_actual) and validar_directorio_existe(directorio_actual_v2):
        return("Error, el directorio del archivo no existe")

    if not validar_archivo_existe(nombre_actual):  
        return("Error, el archivo que buscas renombrar no existe")
    
    try:
        os.rename(nombre_actual, nuevo_nombre)
        return(f"Archivo renombrado de '{nombre_actual}' a '{nuevo_nombre}'.")
    
    except FileNotFoundError:
        return(f"El archivo '{nombre_actual}' no existe.")

def renombrar_directorio(nombre_actual, nuevo_nombre):

    """
    Renombra un directorio en la ruta especificada.

    Autores: 
    - David Toro
    - Thomas Toro

    Parámetros:
    nombre_actual (str): Es el nombre actual del directorio que se desea renombrar.
    nuevo_nombre (str): Es el nuevo nombre que se desea asignar al directorio.
    ruta_base (str): Es la ruta base donde se encuentra el directorio.

    Retorna:
    str: Un mensaje que indica si el directorio fue renombrado correctamente o si ocurrió un error.

    Excepciones:
    Si el directorio no existe, devuelve un mensaje indicando que no se encontró.
    Si ocurre un error al renombrar, devuelve un mensaje detallado de lo que pasó.		
		
    """
    directorio_base=os.path.dirname(nuevo_nombre)
    # Verificar si el directorio existe
    if not validar_directorio_existe(nombre_actual):
        return(f"El directorio '{nombre_actual}' no existe.")
    if not validar_directorio_existe(directorio_base):
        return(f"El directorio del nuevo nombre no existe {directorio_base}")
    try:
        # Renombrar el directorio
        os.rename(nombre_actual, nuevo_nombre)
        return(f"Directorio renombrado de '{nombre_actual}' a '{nuevo_nombre}'.")

    except Exception as e:
        return(f"Error al renombrar el directorio '{nombre_actual}': {e}")


#####FUNCIONES PARA VERIFICAR LA EXISTENCIA DE ARCHIVOS Y DIRECTORIOS########

def validar_archivo_existe(ruta_archivo):
    """
    Valida si un archivo existe en la ruta especificada.

    Autores: 
    - David Toro
    - Thomas Toro

    Parámetros:
    ruta_archivo (str): La ruta completa del archivo a validar.

    Retorna:
    bool: 
        - True si el archivo existe en la ruta dada.
        - False si el archivo no existe.

    Descripción:
    Esta función utiliza el método os.path.isfile() para ver si un archivo existe en la ruta especificada.
    Retorna True si el archivo se encuentra en la ruta, de lo contrario, retorna False.

    
    """
    if os.path.isfile(ruta_archivo):
        #print(f"El archivo '{ruta_archivo}' existe.")
        return True
    else:
        #print(f"El archivo '{ruta_archivo}' no existe.")
        return False

def validar_directorio_existe(ruta_directorio):
    """
    Valida si un directorio existe en la ruta especificada.

    Autor(es): 
    - David Toro
    - Thomas Toro

    Parámetros:
    ruta_directorio (str): La ruta completa del directorio a validar.

    Retorna:
    bool: 
        - True si el directorio existe en la ruta dada.
        - False si el directorio no existe.

    Descripción:
    Esta función utiliza el método os.path.isdir() para ver la existencia de un directorio en la ruta dada.
    Retorna True si el directorio se encuentra en la ruta, o si no existe retorna False.

  
    """
    if os.path.isdir(ruta_directorio):
        ##print(f"El directorio '{ruta_directorio}' existe.")
        return True
    else:
        #print(f"El directorio '{ruta_directorio}' no existe.")
        return False