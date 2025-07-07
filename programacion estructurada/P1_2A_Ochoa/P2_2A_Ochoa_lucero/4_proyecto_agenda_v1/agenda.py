def borrarPantalla():
  import os  
  os.system("cls")

def esperarTecla():
    input("Oprima cualquier tecla para continuar")  

def menu_principal():
   print(".:: SISTEMA DE AGENDA PERSONAL ::.. \n1️⃣.-Agregar contacto\n2️⃣.-Mostrar contacto\n3️⃣.-Buscar contacto por nombre\n4️.-Modificar contacto\n5️⃣.-Eliminar contacto\n6️⃣.-SALIR ")
   opcion=input("Elige una opción (1-6): ") 
   return opcion 
def AgregarContactos(lista):
    borrarPantalla()
    nombre = input("Nombre del contacto: ").strip().capitalize()
    telefono = input("Teléfono: ").strip()
    correo = input("Correo electrónico: ").strip()
    contacto = {"nombre": nombre, "telefono": telefono, "correo": correo}
    lista.append(contacto)
    print("\n✅ Contacto agregado con éxito.")

def MostrarContactos(lista):
    borrarPantalla()
    if not lista:
        print("\n❌ No hay contactos para mostrar.")
    else:
        print("\n📒 Lista de contactos:")
        for i, contacto in enumerate(lista, start=1):
            print(f"{i}. {contacto['nombre']} - {contacto['telefono']} - {contacto['correo']}")

def BuscarContactos(lista):
    borrarPantalla()
    nombre = input("🔍 Ingresa el nombre a buscar: ").strip().capitalize()
    encontrados = [c for c in lista if c['nombre'] == nombre]
    if encontrados:
        print("\n✅ Contactos encontrados:")
        for c in encontrados:
            print(f"{c['nombre']} - {c['telefono']} - {c['correo']}")
    else:
        print("\n❌ No se encontró ningún contacto con ese nombre.")

def ModificarContacto(lista):
    borrarPantalla()
    print("Modificar contacto: ")
    if not lista:
        print("no hay contactos en la agenda")
    else :
        nombre=input("nombre: " ).capitalize().strip()
        if nombre in lista:
            print(f"{'nombre':<15}{'telefono':<15}{'correo':<15}")
            print(f"'-"*60)
            print(f"{'nombre':<15}{lista[nombre][0]:<15}{lista[nombre][1]:<15}")
            print(f"'-"*60)
            resp=input("Deseas modificar el contacto❓❓ (Si/No)").lower().strip()
            if resp=="si":
                tel=input("Telefono: ").strip()
                correo=input("Correo").upper().strip()
                lista[nombre]=[tel,correo]
                print("Accion realizada con exito ✔✔✔")
            else:
               print("No exite el contacto ❗❗❗❗")

def BorrarContacto(lista):
    borrarPantalla()
    print("eliminar contacto")
    if not lista:
        print("no hay contactos en la agenda")
    else :
        nombre=input("🔍 Ingresa el nombre a buscar: " ).capitalize().strip()
        if nombre in lista:
            print(f"{'nombre':<15}{'telefono':<15}{'correo':<15}")
            print(f"'-"*60)
            print(f"{'nombre':<15}{lista[nombre][0]:<15}{lista[nombre][1]:<15}")
            print(f"'-"*60)
            resp=input("Deseas borrar el contacto⁉⁉⁉ (si/no)").lower().strip()
            if resp=="si":
                lista.pop(nombre)
                print("Accion realizada con exito ✔✔✔")
        else:
            print("Este contacto no existe ‼‼")