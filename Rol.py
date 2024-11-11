class Rol:
    def __init__(self, nombre, permisos):
        self.nombre = nombre
        self.permisos = permisos  # Lista de permisos específicos para el rol

    def tiene_permiso(self, accion):
        return accion in self.permisos