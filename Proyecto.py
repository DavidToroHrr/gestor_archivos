import os
import shutil

class Proyecto:

    # Crear directorio
    def crear_directorio(self, nombre):
        ruta_completa = os.path.join(self.ruta_base, nombre)
        os.makedirs(ruta_completa, exist_ok=True)
        print(f"Directorio '{nombre}' creado correctamente.")


        # Función para listar directorios en un directorio específico
    def listar_directorios(ruta):
        try:
            # Listar todo en el directorio especificado
            elementos = os.listdir(ruta)
            print(f"Directorios en el directorio '{ruta}':")
            for elemento in elementos:
                # Verificar si el elemento es un directorio
                if os.path.isdir(os.path.join(ruta, elemento)):
                    print(f"- {elemento}")
        except Exception as e:
            print(f"Error al listar los directorios en '{ruta}': {e}")


    # Mover archivo o directorio
    def mover_elemento(self, origen, destino):
        ruta_origen = os.path.join(self.ruta_base, origen)
        ruta_destino = os.path.join(self.ruta_base, destino)
        try:
            shutil.move(ruta_origen, ruta_destino)
            print(f"Elemento '{origen}' movido a '{destino}' correctamente.")
        except Exception as e:
            print(f"Error al mover el elemento '{origen}': {e}")


    # Eliminar un directorio
    def eliminar_directorio(self, nombre):
        ruta_completa = os.path.join(self.ruta_base, nombre)
        try:
            shutil.rmtree(ruta_completa)
            print(f"Directorio '{nombre}' eliminado correctamente.")
        except Exception as e:
            print(f"Error al eliminar el directorio '{nombre}': {e}")


# Función para renombrar un directorio
    def renombrar_directorio(self, nombre_actual, nuevo_nombre):
        ruta_actual = os.path.join(self.ruta_base, nombre_actual)
        nueva_ruta = os.path.join(self.ruta_base, nuevo_nombre)
        try:
            # Verificar si el directorio existe antes de renombrarlo
            if os.path.isdir(ruta_actual):
                os.rename(ruta_actual, nueva_ruta)
                print(f"Directorio renombrado de '{nombre_actual}' a '{nuevo_nombre}'.")
            else:
                print(f"El directorio '{nombre_actual}' no existe.")
        except Exception as e:
            print(f"Error al renombrar el directorio '{nombre_actual}': {e}")