from conexionBD import *
import datetime
import hashlib

def hash_password(contrasena):
    return hashlib.sha256(contrasena.encode()).hexadigest()

def registrar(nombre,apellido,email,contrasena):
    try:
        fecha=datetime.datetime.now()
        contrasena = hashlib.sha256(contrasena.encode()).hexadigest()
        sql=" insert into usuarios(nombre,apellido,email,password,fecha) values (%s,%s,%s,%s,%s)"
        val=()
        cursor.execute(sql,val)
        conexion.commit()
        return True
    except:
        return False
    
def inicio_sesion(email,contrasena):
    try:
        hashlib.sha256(contrasena.encode()).hexadigest()
        sql="select * from usuario where email=%s and password=%s"
        val=()
        cursor.execute(sql,val)
        registro=cursor.fetchone()
        if registro:
            return registro
        else:
            return None
    except:
        return None
