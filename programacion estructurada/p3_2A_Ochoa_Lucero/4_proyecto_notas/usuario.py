from conexionBD import
import datetime

def registrar (nombre,apellidos,email,contrasena):
    try:
        fecha=datetime.now()
        sql="insert into usuario(nombre,apellidos,email,password,fecha) values (%s,%s,%s)"
        val=(nombre,apellidos,email,contrasena,fecha)
        cursor execute(sql,val)
        conexion.commit()
        return True
    except:
        return False
    
def inicio_secion(emial,contrasena):
    try:
        sql="select *from usuarios where email =%s and password = %s"
        val()
        cursor.execute(sql,val)
        registro = cursor.fetchone()
        if registro:
            return registro
        else:
            return None
    except:
        return None
    
