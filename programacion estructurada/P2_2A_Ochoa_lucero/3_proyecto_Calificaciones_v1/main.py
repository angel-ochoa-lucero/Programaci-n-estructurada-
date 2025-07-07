#proyecto 3 
# Crear un proyecto que permita Gestionar (Administrar) calificaciones, colocar un menu de opciones para agregar, mostrar, calcular promedio calificaciones de un estudiante. 

#Notas: 
# 1.- Utilizar funciones y mandar llamar desde otro archivo (modulos)
# 2.- Utilizar list (bidimensional) para almacenar el nombre del alumno, asi como sus tres calificaciones
#  

import Calificaciones

def main():
    datos = []  

    opcion=True
    while opcion:
     Calificaciones.borrarPantalla()
     opcion=Calificaciones.menu_principal()

     match opcion:
        case "1":  
            Calificaciones.agregar_calificaciones(datos)
            Calificaciones.esperarTecla()
        case "2":
            Calificaciones.mostrar_calificaciones(datos)
            Calificaciones.esperarTecla() 
        case "3":
            Calificaciones.calcular_promedios(datos)
            Calificaciones.esperarTecla()   
        case "4":
            opcion=False    
            Calificaciones.borrarPantalla()
            print(" Terminaste la ejecucion del SW")
        case _:
            opcion=True 
            print("Opción invalida vuelva a intentarlo") 
            Calificaciones.esperarTecla()

if __name__ == "__main__":
    main()
    