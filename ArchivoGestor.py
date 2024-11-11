import os
import shutil

class ArchivoGestor:
    def __init__(self, ruta_base="."):
        self.ruta_base = ruta_base

    # 1. Crear un archivo vacío
    def crear_archivo(self, nombre):
        ruta_completa = os.path.join(self.ruta_base, nombre)
        with open(ruta_completa, 'w') as f:
            print(f"Archivo '{nombre}' creado.")


    # Crear directorio
    def crear_directorio(self, nombre):
        ruta_completa = os.path.join(self.ruta_base, nombre)
        os.makedirs(ruta_completa, exist_ok=True)
        print(f"Directorio '{nombre}' creado correctamente.")



    
    # Listar archivos en un directorio
    def listar_archivos(self, nombre):
        ruta_completa = os.path.join(self.ruta_base, nombre)
        try:
            archivos = os.listdir(ruta_completa)
            print(f"Archivos en el directorio '{nombre}':")
            for archivo in archivos:
                print(f"- {archivo}")
        except Exception as e:
            print(f"Error al listar los archivos en '{nombre}': {e}")



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


    

    # 9. Eliminar archivo
    def eliminar_archivo(self, nombre):
        ruta_completa = os.path.join(self.ruta_base, nombre)
        try:
            os.remove(ruta_completa)
            print(f"Archivo '{nombre}' eliminado.")
        except FileNotFoundError:
            print(f"El archivo '{nombre}' no existe.")

    

    # Eliminar un directorio
    def eliminar_directorio(self, nombre):
        ruta_completa = os.path.join(self.ruta_base, nombre)
        try:
            shutil.rmtree(ruta_completa)
            print(f"Directorio '{nombre}' eliminado correctamente.")
        except Exception as e:
            print(f"Error al eliminar el directorio '{nombre}': {e}")


    
    # 8. Renombrar archivo
    def renombrar_archivo(self, nombre_actual, nuevo_nombre):
        ruta_actual = os.path.join(self.ruta_base, nombre_actual)
        nueva_ruta = os.path.join(self.ruta_base, nuevo_nombre)
        try:
            os.rename(ruta_actual, nueva_ruta)
            print(f"Archivo renombrado de '{nombre_actual}' a '{nuevo_nombre}'.")
        except FileNotFoundError:
            print(f"El archivo '{nombre_actual}' no existe.")


    
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


    # 7. Cambiar permisos del archivo
    def cambiar_permisos_archivo(self, nombre, modo):
        ruta_completa = os.path.join(self.ruta_base, nombre)
        try:
            os.chmod(ruta_completa, modo)
            print(f"Permisos de '{nombre}' cambiados a {oct(modo)}.")
        except FileNotFoundError:
            print(f"El archivo '{nombre}' no existe.")




    # 2. Escribir en un archivo
    # def escribir_archivo(self, nombre, contenido):
    #     ruta_completa = os.path.join(self.ruta_base, nombre)
    #     with open(ruta_completa, 'w') as f:
    #         f.write(contenido)
    #         print(f"Contenido escrito en '{nombre}'.")


    # 3. Leer desde un archivo
    def leer_archivo(self, nombre):
        ruta_completa = os.path.join(self.ruta_base, nombre)
        try:
            with open(ruta_completa, 'r') as f:
                contenido = f.read()
                print(f"Contenido de '{nombre}':\n{contenido}")
        except FileNotFoundError:
            print(f"El archivo '{nombre}' no existe.") 


    # 4. Añadir contenido al final de un archivo
    # def agregar_a_archivo(self, nombre, contenido):
    #     ruta_completa = os.path.join(self.ruta_base, nombre)
    #     with open(ruta_completa, 'a') as f:
    #         f.write(contenido)
    #         print(f"Contenido añadido a '{nombre}'.")

    # 5. Reposicionar el puntero del archivo
    def reposicionar_archivo(self, nombre, posicion):
        ruta_completa = os.path.join(self.ruta_base, nombre)
        try:
            with open(ruta_completa, 'r') as f:
                f.seek(posicion)
                contenido = f.read()
                print(f"Contenido desde la posición {posicion}:\n{contenido}")
        except FileNotFoundError:
            print(f"El archivo '{nombre}' no existe.")

    # 6. Obtener atributos del archivo
    def obtener_atributos_archivo(self, nombre):
        ruta_completa = os.path.join(self.ruta_base, nombre)
        try:
            file_stats = os.stat(ruta_completa)
            print(f"Atributos de '{nombre}':")
            print(f"Tamaño: {file_stats.st_size} bytes")
            print(f"Última modificación: {file_stats.st_mtime}")
        except FileNotFoundError:
            print(f"El archivo '{nombre}' no existe.")

    

    

    

    
