import tkinter as tk
from tkinter import ttk, messagebox
from gestor_usuario import *
from gestor_archivo import *

class FileManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestión de Archivos y Directorios")
        self.root.geometry("600x400")
        self.rol_usuario = None

        self.setup_login()

    def setup_login(self):
        """Configura la pantalla de inicio de sesión para ingresar nombre y rol."""
        self.clear_frame()

        tk.Label(self.root, text="Bienvenido a los Archivos Seguros", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.root, text="Ingrese su nombre:").pack(pady=5)
        self.nombre_entry = tk.Entry(self.root)
        self.nombre_entry.pack()

        tk.Label(self.root, text="Seleccione su rol:").pack(pady=5)
        self.rol_var = tk.StringVar(value="administrador")
        ttk.Combobox(self.root, textvariable=self.rol_var, values=["administrador", "director", "consultor"]).pack()

        tk.Button(self.root, text="Ingresar", command=self.login).pack(pady=20)

    def login(self):
        """Inicia sesión del usuario y configura el menú según el rol."""
        nombre = self.nombre_entry.get()
        rol = self.rol_var.get()

        if nombre and rol:
            self.rol_usuario = rol
            messagebox.showinfo("Bienvenido", f"¡Hola, {nombre}! Eres {rol}.")
            self.setup_menu()
        else:
            messagebox.showerror("Error", "Por favor ingrese su nombre y seleccione un rol.")

    def setup_menu(self):
        """Configura el menú principal basado en el rol del usuario."""
        self.clear_frame()

        tk.Label(self.root, text="Menú Principal", font=("Arial", 16)).pack(pady=10)

        options = [
            ("Crear Archivos", self.crear_archivo),
            ("Crear Directorios", self.crear_directorio),
            ("Listar Archivos", self.listar_archivos),
            ("Listar Directorios", self.listar_directorios),
            ("Mover Archivos", self.mover_elemento),
            ("Mover Directorios", self.mover_elemento),
            ("Eliminar Archivos", self.eliminar_archivo),
            ("Eliminar Directorios", self.eliminar_directorio),
            ("Renombrar Archivos", self.renombrar_archivo),
            ("Renombrar Directorios", self.renombrar_directorio),
        ]

        for i, (text, command) in enumerate(options):
            tk.Button(self.root, text=text, width=30, command=command).pack(pady=5)

        tk.Button(self.root, text="Salir", command=self.root.quit).pack(pady=10)

    def crear_archivo(self):
        self.operation_prompt("Crear Archivo", "crear", crear_archivo)

    def crear_directorio(self):
        self.operation_prompt("Crear Directorio", "crear", crear_directorio)

    def listar_archivos(self):
        self.operation_prompt("Listar Archivos", "listar", listar_archivos)

    def listar_directorios(self):
        self.operation_prompt("Listar Directorios", "listar", listar_directorios)

    def mover_elemento(self):
        self.operation_prompt("Mover Elemento", "mover", mover_elemento)

    def eliminar_archivo(self):
        self.operation_prompt("Eliminar Archivo", "eliminar", eliminar_archivo)

    def eliminar_directorio(self):
        self.operation_prompt("Eliminar Directorio", "eliminar", eliminar_directorio)

    def renombrar_archivo(self):
        self.operation_prompt("Renombrar Archivo", "renombrar", renombrar_archivo)

    def renombrar_directorio(self):
        self.operation_prompt("Renombrar Directorio", "renombrar", renombrar_directorio)

    def operation_prompt(self, title, permiso, func):
        """Ventana de entrada para realizar una operación específica."""
        if not verificar_permiso(self.rol_usuario, permiso):
            messagebox.showerror("Permiso denegado", f"No tienes permiso para realizar esta acción: {title}")
            return

        window = tk.Toplevel(self.root)
        window.title(title)
        window.geometry("400x200")

        tk.Label(window, text="Ingrese los detalles de la operación:").pack(pady=10)
        ruta_origen_label = tk.Label(window, text="Ruta/Nombre (según operación):")
        ruta_origen_label.pack(pady=5)
        ruta_origen_entry = tk.Entry(window)
        ruta_origen_entry.pack()

        tk.Label(window, text="Destino/Nuevo Nombre (si aplica):").pack(pady=5)
        ruta_destino_entry = tk.Entry(window)
        ruta_destino_entry.pack()

        def execute():
            ruta_origen = ruta_origen_entry.get()
            ruta_destino = ruta_destino_entry.get()
            resultado = func(ruta_origen, ruta_destino)
            messagebox.showinfo(title, f"Resultado: {resultado}")
            window.destroy()

        tk.Button(window, text="Ejecutar", command=execute).pack(pady=10)

    def clear_frame(self):
        """Limpia todos los widgets en la ventana principal."""
        for widget in self.root.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = FileManagementApp(root)
    root.mainloop()
