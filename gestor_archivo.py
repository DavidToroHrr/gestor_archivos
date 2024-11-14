import os
import shutil


def crear_directorio(nombre, ruta_base):
    ruta_completa = os.path.join(ruta_base, nombre)

    if not validar_directorio_existe(ruta_base):
        return(f"Error: La ruta base '{ruta_base}' no existe.")
    
    try:
        # Crear el directorio en el sistema de archivos
        os.makedirs(ruta_completa, exist_ok=True)
        return(f"Directorio '{nombre}' creado correctamente.")

    except Exception as e:
        return (f"Error al crear el directorio '{nombre}': {e}.")

def crear_archivo(nombre, ruta_base):
    # Validar el nombre del archivo
    if not nombre or not isinstance(nombre, str):
        return("El nombre del archivo no es válido.")
        
    ruta_completa = os.path.join(ruta_base, nombre)

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
def listar_archivos(nombre,ruta_base):
    arreglo_archivos=[]

    ruta_completa = os.path.join(ruta_base, nombre)

    if not validar_directorio_existe(ruta_completa):
        return (f"Error: La ruta '{ruta_completa}' no existe.")

    try:
        #SE HACE EL FILTRADO CORRESPONDIENTE DE SOLAMETE LOS ARCHIVOS
        archivos = [f for f in os.listdir(ruta_completa) if os.path.isfile(os.path.join(ruta_completa, f))]

        for archivo in archivos:
            arreglo_archivos.append(archivo)

        return (f"los archivos son: {arreglo_archivos}")
    
    except Exception as e:
        return(f"Error al listar los archivos en '{nombre}': {e}")

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


####FUNCION DE LISTAR GENERALIZADA#######
# def listar(ruta,tipo):
#     arreglo_elementos=[]

#     try:
#         if tipo==0:
#             elementos= [f for f in os.listdir(ruta) if os.path.isdir(os.path.join(ruta, f))]

#         elif tipo ==1:
#             elementos = [f for f in os.listdir(ruta) if os.path.isfile(os.path.join(ruta, f))]

#             for elemento in elementos:
#                 arreglo_elementos.append(elemento)

#     except Exception as e:
#         return(f"Error al listar los directorios en '{ruta}': {e}")





# 9. Eliminar archivo
def eliminar_archivo(nombre,ruta_base):
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
def renombrar_archivo(nombre_actual, nuevo_nombre,ruta_base):
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


#####FUNCIONES PARA VERIFICAR LA EXISTENCIA DE ARCHIVOS Y DIRECTORIOS###

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