# -*- coding: utf-8 -*-
"""
Created on Sun May 23 19:49:42 2021

@author: Usuario
"""
from USUARIO import usuario
from BaseDatos import dbE
from VALIDADOR import VAL
from PRODUCTOS import producto


usuario1=usuario("36521788","Carol","Torres","caroltt@gmail.com",1163248975, "cramer 391","Rosario","123#carolT")

usuario2=usuario(29854693, "Diego", "Garcia", "dvgarcia@gmail.com", 1185479652, "Conesa 2171", "Rosario", "567#garcia")
#usuario1.saveBD()
#usuario2.set_ID_ciudad()
#print(usuario2.get_ID_ciudad())

#print(usuario1.Encriptar_Contraseña())

#print(usuario1.desencriptar_Contraseña())



def update_usuario():#Diccionario con los datos - lo Valida y RETORNA el Diccionario
    FormularioUSER={}
    FormularioUSER['DNI']=input("DNI: ")
    FormularioUSER['Nombre']=input("Nombre: ")
    FormularioUSER['Apellido']=input("Apellido: ")
    FormularioUSER['Email']=input("Email: ")
    FormularioUSER['Celular']=input("Numero de Celular: ")
    FormularioUSER['Direccion']=input("Direccion: ")
    c=1
    while c == 1:
        ciudad=int(input("Seleccione una Ciudad:\n(1)CABA\n(2)Rosario\n(3)Carmelo\n(4)Montevideo\n(5)Cordoba\n(6)Barcelona\n-->  "))
        if ciudad == 1:
            FormularioUSER['Ciudad']="CABA"
            c = 0
        elif ciudad == 2:
            FormularioUSER['Ciudad']="Rosario"
            c = 0
        elif ciudad == 3:
            FormularioUSER['Ciudad']="Carmelo"
            c = 0
        elif ciudad == 4:
            FormularioUSER['Ciudad']="Montevideo"
            c = 0
        elif ciudad == 5:
            FormularioUSER['Ciudad']="Cordoba"
            c = 0
        elif ciudad == 6:
            FormularioUSER['Ciudad']="Barcelona"
            c = 0
        else:
            print("Error en seleccion")
            c = 1
    FormularioUSER['Contraseña']=input("Contraseña: NUM, MAYUC, CarctEspeciales=[$,@,#,%]\n")
    errores=VAL.validarUsuarioUP(FormularioUSER)
    if not errores:
            user=usuario(**FormularioUSER)
            user.updateBD()
            return user
            print("Usuario Creado con Exito!")
    [print(i) for i in errores.values()]

def user_view(DNI):
    sql = "select Nombre, Apellido, Email, Celular, Direccion from usuarios where DNI=%s"
    valor = DNI
    dbE.get_cursor().execute(sql,valor)
    dbE.get_conexion().commit()
    result = dbE.get_cursor().fetchone()
    for i in result:
        print(i)

#print(user_view(95731671))

def login():
    Datos={}
    Datos['Email']=input("Ingrese su Email:\n ")
    Datos['Contraseña']=input("Ingrese su Contraseña:\n ")
    errores=VAL.validar_login(Datos)
    
    if isinstance(errores,tuple):
        user=usuario(errores[1],errores[2],errores[3],errores[4],errores[5],errores[6],errores[7],errores[8])
        user.set_ID(errores[0])
        return user
    return errores    


usuario3=usuario(3652301, "Gonzalo Jose", "Mamani", "gmm23@gmail.com", 3515231202, "Calle Bella Vista 625 depto 12 C", "Cordoba", "gjmmC#789")

    
    
    
    
usuario1 = update_usuario()


