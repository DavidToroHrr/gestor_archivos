import json

def tiene_permiso(self, accion):
        return accion in self.permisos

def cargar_roles():
    with open('roles.json', 'r') as file:
        return json.load(file)

def verificar_permiso(rol, operacion):
    roles = cargar_roles()
    permisos = roles.get("roles").get(rol, [])
    return operacion in permisos