from gestor_usuario import *
from gestor_archivo import *


def main():
    rol_usuario=crearUsuario()
    print(rol_usuario)
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
            print(f"¡Bienvenido!...{nombre_usuario}")
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
            if verificar_permiso(rol,'crear'):
                print ("Opción 2 seleccionada")
                nombre_temporal = input("Escriba el nombre del nuevo directorio: ")
                ruta_temporal = input("Escriba la ruta donde desea crear el directorio: ")
                crear_directorio(nombre_temporal, ruta_temporal)  # Llamar a la función para crear el directorio

            
        elif opcion == 3:
            print ("Opción 3 seleccionada")

        elif opcion == 5: 
            

            if verificar_permiso(rol, 'mover'):

                print ("Opción 4 seleccionada")
                ruta_temporal1= input("Escriba la ruta del elemento que desea mover")
                ruta_temporal2= input("Escriba la ruta final a la que desea mmover el elemento")
                mover_elemento(ruta_temporal1,ruta_temporal2)
                

        else:
            print ("Opción no válida")


if __name__ =="__main__":
    main()