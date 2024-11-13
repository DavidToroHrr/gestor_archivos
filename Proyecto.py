import os
import shutil

class Proyecto:

    # Crear directorio
    def crear_directorio(self, nombre, ruta_base):
        ruta_completa = os.path.join(ruta_base, nombre)
        # Crear el directorio en el sistema de archivos
        os.makedirs(ruta_completa, exist_ok=True)
        print(f"Directorio '{nombre}' creado correctamente.")

    # Función para listar directorios
    def listar_directorios(self, ruta_base):
        try:
            elementos = os.listdir(ruta_base)
            print(f"Directorios en el proyecto:")
            for elemento in elementos:
                if os.path.isdir(os.path.join(ruta_base, elemento)):
                    print(f"- {elemento}")
        except Exception as e:
            print(f"Error al listar los directorios en '{ruta_base}': {e}")

    # Mover archivo o directorio
    def mover_elemento(self, origen, destino, ruta_base):
        ruta_origen = os.path.join(ruta_base, origen)
        ruta_destino = os.path.join(ruta_base, destino)
        
        # Verificar si el directorio de origen existe
        if not os.path.isdir(ruta_origen):
            print(f"El directorio '{origen}' no existe.")
            return
        
        try:
            # Mover el directorio
            shutil.move(ruta_origen, ruta_destino)
            print(f"Elemento '{origen}' movido a '{destino}' correctamente.")
        except Exception as e:
            print(f"Error al mover el elemento '{origen}': {e}")

    def eliminar_directorio(self, nombre, ruta_base):
        ruta_completa = os.path.join(ruta_base, nombre)
        if os.path.isdir(ruta_completa):
            try:
                shutil.rmtree(ruta_completa)  # Eliminar el directorio en el sistema de archivos
                print(f"Directorio '{nombre}' eliminado correctamente.")
            except Exception as e:
                print(f"Error al eliminar el directorio '{nombre}': {e}")
        else:
            print(f"El directorio '{nombre}' no se encuentra en el proyecto.")

    def renombrar_directorio(self, nombre_actual, nuevo_nombre, ruta_base):
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