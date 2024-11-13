from gestor_usuario import *
from gestor_archivo import *


def main():
    rol_usuario=crearUsuario()
    # print(rol_usuario)
    menu(rol_usuario)
    

def crearUsuario():

    roles = {
            1: "administrador",
            2: "director",
            3: "consultor"
        }
    nombre_usuario=input("Bienvenido a la empresa los archivos seguros, escriba su nombre: ")
    bandera=0
    
    while(bandera!=1):
        rol_usuario=int(input("\nAhora, elija su rol dentro de la aplicación: \n"
                            "1: administrador\n"
                            "2: director\n"
                            "3: consultor\n"))

        if rol_usuario in roles:
            print(f"¡Bienvenido!...{nombre_usuario}. Eres {roles[rol_usuario]}")
            return roles[rol_usuario]

        else:
            resultado='ERROR...El rol elegido no existe'
            bandera=0

        print(resultado)

def menu(rol):
    opcion=int
    while (opcion!=0):
        
        print(
            "0: Salir\n"
            "1: crear archivos\n"
            "2: crear directorios\n"         
            "3: listar archivos\n"
            "4: listar directorios\n"         
            "5: mover archivos\n"
            "6: mover directorios\n"          
            "7: eliminar archivos\n"
            "8: eliminar directorios\n"
            "9: renombrar archivos\n"
            "10: renombrar directorios\n"
            )
        
        opcion = int(input("Selecciona una opción (0-10):"))

        if opcion == 0:
            print ("Has seleccionado salir, hasta pronto...")
            return
        
        if opcion == 1:
            print ("Opción 1 seleccionada")

            if verificar_permiso(rol,'crear'):
                nombre_temporal=input("Ingrese el nombre del archivo: ")
                ruta_temporal=input("Ingrese la ruta del archivo: ")

                crear_archivo(nombre_temporal,ruta_temporal)

            else:
                print("no tiene permiso")
            

        elif opcion == 2:
            print ("Opción 2 seleccionada")

        elif opcion == 3:
            print ("Opción 3 seleccionada")

            if verificar_permiso(rol,'listar'):
                nombre_temporal=input("Ingrese el nombre del archivo: ")
                ruta_temporal=input("Ingrese la ruta del archivo: ")

                listar_archivos(nombre_temporal,ruta_temporal)
            else:
                print("no tiene permiso")



        elif opcion == 7:
            print ("Opción 7 seleccionada")

            if verificar_permiso(rol,'eliminar'):
                nombre_temporal=input("Ingrese el nombre del archivo: ")
                ruta_temporal=input("Ingrese la ruta del archivo: ") 
                eliminar_archivo(nombre_temporal,ruta_temporal)

            else:
                print("no tiene permiso")

        
        elif opcion == 9:
            print ("Opción 9 seleccionada")

            if verificar_permiso(rol,'renombrar'):
                nombre_temporal_actual=input("Ingrese el nombre del archivo: ")
                nombre_temporal_nuevo=input("Ingrese el NUEVO nombre del archivo: ")
                ruta_temporal=input("Ingrese la ruta del archivo: ") 

                renombrar_archivo(nombre_temporal_actual,nombre_temporal_nuevo,ruta_temporal)

            else:
                print("no tiene permiso")

        else:
            print ("Opción no válida")
        


if __name__ =="__main__":
    main()