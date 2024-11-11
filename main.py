from archivogestor import ArchivoGestor
inst_gestor=ArchivoGestor()


from directorio import Directorio
inst_directorio=Directorio(None)

from proyecto import Proyecto
inst_proyecto=Proyecto()

def main():
    
    
    def switch_case():
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
                inst_directorio.crear_archivo("elpepe")
            elif opcion == 2:
                print ("Opción 2 seleccionada")
            elif opcion == 3:
                print ("Opción 3 seleccionada")
            else:
                print ("Opción no válida")
    
    switch_case()
    


if __name__ =="__main__":
    main()