# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 21:26:13 2021

@author: Usuario
"""
from USUARIO import usuario
from BaseDatos import dbE
from VALIDADOR import VAL
from PRODUCTOS import producto
from CATEGORIA import categoria
from MARCA import marca
from POTENCIA import potencia
from COMPRAS import compras
from datetime import datetime
import random

class ecomerce:
    
    def __init__(self, NombreE):
        self.NombreE = NombreE

E = ecomerce("CR BOMBAS")

def regitro_usuario():#Diccionario con los datos de reg/lo Valida y RETORNA USER
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
    FormularioUSER['Contraseña']=input("Contraseña: ")
    errores=VAL.validarUsuario(FormularioUSER)
    if not errores:
            user=usuario(**FormularioUSER)
            user.saveBD()
            return user
            print("Usuario Creado con Exito!")
    [print(i) for i in errores.values()]

def login():#Recibe EMAIL y Contaseña los VALIDA y RETORNA USER
    Datos={}
    Datos['Email']=input("Ingrese su Email:\n ")
    Datos['Contraseña']=input("Ingrese su Contraseña:\n ")
    errores=VAL.validar_login(Datos)
    
    if isinstance(errores,tuple):
        user=usuario(errores[1],errores[2],errores[3],errores[4],errores[5],errores[6],errores[7],errores[8])
        user.set_ID(errores[0])
        return user
    return errores     

def vista_Productos():#VISTA DE TODOS LOS PRODUCTOS
    sql= "select * from productos"
    dbE.get_cursor().execute(sql)
    result = dbE.get_cursor().fetchall()
    for i in result:
        if i[5]==None:
            print(f"ID: {i[0]}")
            c=categoria(i[3])
            c.categoria_import()
            print(f"Bomba {c.get_Tipo()}\tVoltage: {c.get_Voltaje()}")
            m = marca(i[2])
            m.marca_Import()
            print(f"Marca: {m.get_Nombre()}\t Origen: {m.get_Origen()}\t Garantia: {m.get_Garantia()} meses")
            print(f"Nombre: {i[1]}\t Precio: {i[6]}")
            p=potencia(i[4])
            p.potencia_import()
            print(f"Potencia: {p.get_HP()} HP \"Caballos de Fuerza\"\n")
        else:
            print(f"ID: {i[0]}")
            c=categoria(i[3])
            c.categoria_import()
            print(f"Bomba {c.get_Tipo()}\tVoltage: {c.get_Voltaje()}")
            m = marca(i[2])
            m.marca_Import()
            print(f"Marca: {m.get_Nombre()}\t Origen: {m.get_Origen()}\t Garantia: {m.get_Garantia()} meses")
            print(f"Nombre: {i[1]}\tDescripcion: {i[5]}\t Precio: {i[6]}")
            p=potencia(i[4])
            p.potencia_import()
            print(f"Potencia: {p.get_HP()} HP \"Caballos de Fuerza\"\n")
    
def Vista_Categorias():#VISTA de PRODUCTOS por CATEGORIA
    valor = 0
    while valor == 0:
        valor = int(input("Tipos Bombas: \n(1) Centrifuga\n(2)Presurizadora \n(3)Periferica \n(4)Sumergible \n(5)Autocebantes \n(6)Autoaspirante \n(7)Calefaccion \n (Coloque el Numero de su Seleccion)-----> "))
        sql="select * from productos where id_categoria=%s"
        dbE.get_cursor().execute(sql,valor)
        result=dbE.get_cursor().fetchall()
        #print(result)
        if  len(result)==0:
            print(f"\n------------------- --- --- -------------------------\n")
            print("\nNo hay Stock\n\n")
            print(f"\n------------------- --- --- -------------------------\n")
            valor = 0
        else:
            for i in result:
                c=categoria(valor)
                c.categoria_import()
                print(f"\nBomba {c.get_Tipo()}")
                print(f"ID: {i[0]} \nVoltage: {c.get_Voltaje()}")
                m = marca(i[2])
                m.marca_Import()
                print(f"Marca: {m.get_Nombre()}\t Origen: {m.get_Origen()}\t Garantia: {m.get_Garantia()} meses")
                print(f"Nombre: {i[1]}\t Precio: {i[6]}")
                p=potencia(i[4])
                p.potencia_import()
                print(f"Potencia: {p.get_HP()} HP \"Caballos de Fuerza\"\n")

def MP():#metodo de pago
    mp = ""
    while mp == "":
        selec = int(input("Seleccione Metodo de Pago: \t(1) Efectivo\t(2) Transferencia\n---> "))
        if selec == 1:
            mp = "Efectivo"
        elif selec == 2:
            mp = "Transferencia"
        else:
            print("Error en seleccion")
            mp = ""
    return mp

def H_Compra(ID_Usuario):
    sql="select id_compras, Id_producto, Fecha_Compra, Id_mp from compras where id_usuario = %s"
    valor = ID_Usuario
    dbE.get_cursor().execute(sql,valor)
    result=dbE.get_cursor().fetchone()
    if result == None:
        return result
    else:
        sql="select nombre from metodo_pago where id_mp = %s"
        valor = result[3]
        dbE.get_cursor().execute(sql,valor)
        mp=dbE.get_cursor().fetchone()[0]
        compra = compras(ID_Usuario, result[1], mp, result[2])
    
        return compra      

     

print(f"--------------------MENU PRINCIPAL------------------------\n\t\t\t{E.NombreE}")
MENU_INICIO=True
while MENU_INICIO==True:
    try:
        opcion = int(input("\tBienvenido a Nuestra pagina de Compras\n\nOPCIONES: 1. Registro Usuario \t 2. Iniciar sesión\n ----> "))
        if opcion == 1:
            user1 = regitro_usuario()
            print(f" Hola! {user1.get_Nombre()} {user1.get_Apellido()}")
            MENU_USER = str(user1.get_ID())
            MENU_INICIO=False
        elif opcion ==2:
            user1 = login()
            print(f"\n\n Hola! {user1.get_Nombre()} {user1.get_Apellido()}\n")
            MENU_INICIO=False
            MENU_USER = str(user1.get_ID())
        else:
            MENU_INICIO=True
    except (ValueError, TypeError, SyntaxError,AttributeError,NameError):
        print("\n\tError en Tipo o Valor ingresado")
        MENU_INICIO=True
    
  
while MENU_USER.isdigit() == True:
           
        try:
            selec=int(input("\tMenu Usuario \n(1)Historial de Compras\n(2)Nueva Compra\n(3)Salir de la Cuenta \n(Coloque el Numero de su Seleccion)-----> "))
            if selec == 1:
                H  = H_Compra(user1.get_ID())
                if H == None:
                   print(f" \n--- El Usuario No Tiene Compras Registradas ---\n ")
                   print(f"\n------------------- --- --- -------------------------\n")
                else:
                    H.vista_compra()
                    print(f"\n------------------- --- --- -------------------------\n")
            elif selec == 2:
                    print(f"\n------------------- --- --- -------------------------\n")
                    subselec= int(input("\t PRODUCTOS:\n(1) VER TODOS\n(2) VER POR TIPOS \n(3)Volver\n(Coloque el Numero de su Seleccion)-----> "))
                    if subselec == 1:
                        vista_Productos()
                        IDp= int(input("Selecciona el ID del Producto a comprar.. ID: "))
                        p =  producto(IDp)
                        p.Import_Producto()
                        print(f"\n{user1.get_Nombre()}, Seleccionaste {p.get_Nombre()} por ${p.get_Precio()}\n")
                        pago = MP()
                        print(f"Compra Realizada Con Exito! Abonaste ${p.get_Precio()} con {pago}")
                        print(f"\n------------------- --- --- -------------------------\n")
                        #compra = compras(user1.get_ID(), p.get_id_Producto(), pago, datetime.now())
                        #compra.set_MetodoPago()
                        #compra.save_Compra_BD()
                    elif subselec == 2:
                        Vista_Categorias()
                        IDp = int(input("Selecciona el ID del Producto a comprar.. ID: "))
                        p =  producto(IDp)
                        p.Import_Producto()
                        print(f"\n{user1.get_Nombre()}, Seleccionaste {p.get_Nombre()} por ${p.get_Precio()}\n")
                        pago = MP()
                        print(f"Compra Realizada Con Exito! Abonaste ${p.get_Precio()} con {pago}")
                        print(f"\n------------------- --- --- -------------------------\n")
                        #compra = compras(user1.get_ID(), p.get_id_Producto(), pago, datetime.now())
                        #compra.set_MetodoPago()
                        #compra.save_Compra_BD()
                    elif subselec == 3:
                        break
                    break
            elif selec == 3:
                break
            break
        except (ValueError, TypeError, SyntaxError,AttributeError):
            print("\n\tError en Tipo o Valor ingresado")
    MENU_INICIO=True
            




