import agenda

def borrarPanatalla():
    import os
    os.system("cls")

def esperarTecla():
    input("Oprima cualquier tecla para continuar")

def main():
    datos = []  

    opcion=True
    while opcion:
     agenda.borrarPantalla()
     opcion=agenda.menu_principal()

     match opcion:
        case "1":  
            agenda.AgregarContactos(datos)
            agenda.esperarTecla()
        case "2":
            agenda.MostrarContactos(datos)
            agenda.esperarTecla() 
        case "3":
            agenda.BuscarContactos(datos)
            agenda.esperarTecla()   
        case "4":
             agenda.ModificarContacto(datos)
             agenda.esperarTecla
        case "5":
             agenda.BorrarContacto(datos)
             agenda.esperarTecla
        case "6":
            opcion=False    
            agenda.borrarPantalla()
            print(" Terminaste la ejecucion del SW")
        case _:
            opcion=True 
            print("Opción invalida vuelva a intentarlo") 
            agenda.esperarTecla()

if __name__ == "__main__":
    main()|