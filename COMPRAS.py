# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 19:56:09 2021

@author: Usuario
"""

from BaseDatos import dbE
from USUARIO import usuario
from BaseDatos import dbE
from VALIDADOR import VAL
from PRODUCTOS import producto
from CATEGORIA import categoria
from MARCA import marca
from POTENCIA import potencia
from datetime import datetime

class compras():
    
    def __init__(self, usuarioID,productoID, Metodo_Pago, fecha_compra ):
        self.__ID = 0
        self.__Num_Orden = 0
        self.__usuarioID = usuarioID
        self.__productoID = productoID
        self.__Metodo_PagoID = 0
        self.__Metodo_Pago = Metodo_Pago
        self.__fecha_compra= fecha_compra
        
    
    def get_ID(self):
        return self.__ID
    
    def get_Num_Orden(self):
        return self.__Num_Orden
    
    def get_IDusuario(self):
        return self.__usuarioID
    
    def set_IDusuario(self,IDusuario):
        self.__usuarioID = IDusuario
        
    
    def get_IDproducto(self):
        return self.__productoID
    
    def get_Metodo_PagoID(self):
        return self.__Metodo_PagoID
    
    def get_Metodo_Pago(self):
        return self.__Metodo_Pago
    
    def get_fecha_compra(self):
        return self.__fecha_compra
    
    def set_Fecha_Compra(self):
        self.__fecha_compra = datetime.now() 
    
    def set_MetodoPago(self):   
        sql="select Id_mp from metodo_pago where nombre = %s"
        valor = self.__Metodo_Pago
        dbE.get_cursor().execute(sql,valor)
        result=dbE.get_cursor().fetchone()[0]
        self.__Metodo_PagoID = result
        
    
    def vista_compra(self):
        p = producto(self.get_IDproducto())
        p.Import_Producto()
        print(f"\n\n------------------- COMPRASTE-------------------------\n")
        p.vista_Producto()
        print(f"El dia: {self.get_fecha_compra()}\tAbonado con {self.__Metodo_Pago}")
        print(f"\n------------------- --- --- -------------------------\n")

    def save_Compra_BD(self):
        sql="insert into compras(id_usuario, Id_producto, fecha_compra, Id_mp) values(%s,%s,%s,%s)"
        valor =(self.get_IDusuario(), self.get_IDproducto(), self.get_fecha_compra(), self.get_Metodo_PagoID())
        dbE.get_cursor().execute(sql,valor)
        dbE.get_conexion().commit()
        self.__ID = (dbE.get_cursor().lastrowid)#Toma el ID de la Ultima linea donde esta el nuevo registro

    
    
