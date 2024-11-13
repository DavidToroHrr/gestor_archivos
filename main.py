from archivogestor import ArchivoGestor
inst_gestor=ArchivoGestor()


from directorio import Directorio
inst_directorio=Directorio(None)

from proyecto import Proyecto
inst_proyecto=Proyecto(nombre=None)


def main():
    crearUsuario()
    menu()


def crearUsuario():

    
    nombre_usuario=input("Bienvenido a la empresa los archivos seguros, escriba su nombre: ")
    bandera=0
    
    while(bandera!=1):
        rol_usuario=input("\nAhora, elija su rol dentro de la aplicación: ")
        if rol_usuario in inst_gestor.roles_permisos:
            resultado =inst_gestor.agregar_usuario(nombre_usuario,rol_usuario)
            
            bandera=1
        else:
            resultado='ERROR...El rol elegido no existe'
            bandera=0

        print(resultado)

def menu():
    opcion=int
    while (opcion!=0):
        
        print(

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
            

        elif opcion == 2:
            print ("Opción 2 seleccionada")
        elif opcion == 3:
            print ("Opción 3 seleccionada")
        else:
            print ("Opción no válida")


if __name__ =="__main__":
    main()