import os
import shutil
from archivo import Archivo


class Directorio:
    # def __init__(self, nombre,  ruta_base="."):
    #     self.ruta_base=ruta_base
    #     self.nombre=nombre
    #     self.archivos=[]

# 1. Crear un archivo vacío
    def crear_archivo(self, nombre,ruta_base):

        ruta_completa = os.path.join(ruta_base, nombre)
        archivo=Archivo(nombre,ruta_completa)
        #self.archivos.append(archivo)
        with open(ruta_completa, 'w') as f:
            print(f"Archivo '{nombre}' creado.")
        

# Listar archivos en un directorio
    def listar_archivos(self, nombre,ruta_base):
        ruta_completa = os.path.join(ruta_base, nombre)
        try:
            archivos = os.listdir(ruta_completa)
            print(f"Archivos en el directorio '{nombre}':")
            for archivo in archivos:
                print(f"- {archivo}")
        except Exception as e:
            print(f"Error al listar los archivos en '{nombre}': {e}")


# Mover archivo o directorio
    def mover_elemento(self, origen, destino,ruta_base):
        ruta_origen = os.path.join(ruta_base, origen)
        ruta_destino = os.path.join(ruta_base, destino)
        try:
            shutil.move(ruta_origen, ruta_destino)
            print(f"Elemento '{origen}' movido a '{destino}' correctamente.")
        except Exception as e:
            print(f"Error al mover el elemento '{origen}': {e}")



# 9. Eliminar archivo
    def eliminar_archivo(self, nombre,ruta_base):
        ruta_completa = os.path.join(ruta_base, nombre)
        try:
            os.remove(ruta_completa)
            print(f"Archivo '{nombre}' eliminado.")
        except FileNotFoundError:
            print(f"El archivo '{nombre}' no existe.")


# 8. Renombrar archivo
    def renombrar_archivo(self, nombre_actual, nuevo_nombre,ruta_base):
        ruta_actual = os.path.join(ruta_base, nombre_actual)
        nueva_ruta = os.path.join(ruta_base, nuevo_nombre)
        try:
            os.rename(ruta_actual, nueva_ruta)
            print(f"Archivo renombrado de '{nombre_actual}' a '{nuevo_nombre}'.")
        except FileNotFoundError:
            print(f"El archivo '{nombre_actual}' no existe.")