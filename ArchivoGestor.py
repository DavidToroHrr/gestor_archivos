import os
import shutil

class ArchivoGestor:
    def __init__(self, ruta_base="."):
        self.ruta_base = ruta_base

        self.roles_permisos = {
            "administrador": ["crear", "listar", "mover", "eliminar", "renombrar"],
            "director_proyecto": ["crear", "listar", "mover"],
            "consultor": ["listar"]
        }
        self.usuarios = {}  # Almacenar usuarios y roles


    
    def agregar_usuario(self, usuario, rol):
        self.usuarios[usuario] = rol
        return f"Usuario '{usuario}' agregado con rol '{rol}'."

    


    def verificar_permiso(self, usuario, accion):
        if usuario.nombre in self.usuarios:
            rol = self.usuarios[usuario.nombre].rol
            if rol.tiene_permiso(accion):
                return True
        print(f"Usuario '{usuario.nombre}' no tiene permiso para '{accion}'.")
        return False

    def crear_proyecto(self, nombre_proyecto, usuario):
        if not self.verificar_permiso(usuario, "crear"):
            return
        # Lógica para crear el proyecto
        print(f"Proyecto '{nombre_proyecto}' creado por '{usuario.nombre}'.")
        

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


    # # 3. Leer desde un archivo
    # def leer_archivo(self, nombre):
    #     ruta_completa = os.path.join(self.ruta_base, nombre)
    #     try:
    #         with open(ruta_completa, 'r') as f:
    #             contenido = f.read()
    #             print(f"Contenido de '{nombre}':\n{contenido}")
    #     except FileNotFoundError:
    #         print(f"El archivo '{nombre}' no existe.") 


    # 4. Añadir contenido al final de un archivo
    # def agregar_a_archivo(self, nombre, contenido):
    #     ruta_completa = os.path.join(self.ruta_base, nombre)
    #     with open(ruta_completa, 'a') as f:
    #         f.write(contenido)
    #         print(f"Contenido añadido a '{nombre}'.")

    # 5. Reposicionar el puntero del archivo
    # def reposicionar_archivo(self, nombre, posicion):
    #     ruta_completa = os.path.join(self.ruta_base, nombre)
    #     try:
    #         with open(ruta_completa, 'r') as f:
    #             f.seek(posicion)
    #             contenido = f.read()
    #             print(f"Contenido desde la posición {posicion}:\n{contenido}")
    #     except FileNotFoundError:
    #         print(f"El archivo '{nombre}' no existe.")

    # # 6. Obtener atributos del archivo
    # def obtener_atributos_archivo(self, nombre):
    #     ruta_completa = os.path.join(self.ruta_base, nombre)
    #     try:
    #         file_stats = os.stat(ruta_completa)
    #         print(f"Atributos de '{nombre}':")
    #         print(f"Tamaño: {file_stats.st_size} bytes")
    #         print(f"Última modificación: {file_stats.st_mtime}")
    #     except FileNotFoundError:
    #         print(f"El archivo '{nombre}' no existe.")

    

    

    

    
