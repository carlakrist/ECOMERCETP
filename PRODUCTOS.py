# -*- coding: utf-8 -*-
"""
Created on Thu May 20 21:45:31 2021

@author: Usuario
"""
from BaseDatos import dbE

from CATEGORIA import categoria
from MARCA import marca
from POTENCIA import potencia

class producto():
    
    def __init__(self, ID):
        self.__id_Producto = ID
        self.__Nombre =  ""
        self.__IDMarca = 0
        self.__IDCategoia = 0
        self.__IDPotencia = 0
        self.__DescripcionPro = ""
        self.__Precio = 0
        
    def get_id_Producto(self):
        return self.__id_Producto
    
    def set_ID_Producto(self, ID):
         self.__id_Producto = ID
     
    def set_ID_ProductoN(self):
        sql="select id_producto from productos where nombre=%s"
        valor=self.__Nombre
        dbE.get_cursor().execute(sql,valor)
        try:
            self.__id_Producto = dbE.get_cursor().fetchone()[0]
        except TypeError:
            print("Nombre del producto No Existe")
    
    def get_Nombre(self):
         return self.__Nombre
     
    def get_IDMarca(self):
         return self.__IDMarca
    
    def get_IDCategoia(self):
         return self.__IDCategoia 
    
    def get_IDPotencia(self):
         return self.__IDPotencia
    
    def get_Descripcion(self):
         return self.__Descripcion
    
    def get_Precio(self):
         return self.__Precio
     
    def set_Nombre(self,Nombre):
        self.__Nombre = Nombre
    
    def set_IDMarca(self,ID):
        self.__IDMarca = ID
    
    def set_IDCategoia(self,ID):
        self.__IDCategoia = ID
    
    def set_IDPotencia(self,ID):
        self.__IDPotencia = ID
    
    def set_DescripcionPro(self, D):
        self.__DescripcionPro = D
        
    def get_DescripcionPro(self):
        return self.__DescripcionPro
        
    def set_Precio(self, Precio):
        self.__Precio = Precio
    
    
    def Import_Producto(self):
        sql= "select nombre, id_marca, id_categoria, id_potencia, descripcion,precio from productos where id_producto=%s"
        valor=self.__id_Producto
        dbE.get_cursor().execute(sql,valor)
        result = dbE.get_cursor().fetchone()
        self.set_Nombre(result[0])
        self.set_IDMarca(result[1])
        self.set_IDCategoia(result[2])
        self.set_IDPotencia(result[3])
        self.set_Precio(result[5])
        self.set_DescripcionPro(result[4])
        if result[4] != None:
            self.set_DescripcionPro(result[4])
        else:
            self.set_DescripcionPro("Consultar uso")
        
    
    def vista_Producto(self):
        print(f"ID: {self.get_id_Producto()}")
        c=categoria(self.get_IDCategoia())
        c.categoria_import()
        print(f"Bomba {c.get_Tipo()}\tVoltage: {c.get_Voltaje()}")
        m = marca(self.get_IDMarca())
        m.marca_Import()
        print(f"Marca: {m.get_Nombre()}\t Origen: {m.get_Origen()}\t Garantia: {m.get_Garantia()} meses")
        print(f"Nombre: {self.get_Nombre()}\t Descripcion: {self.get_DescripcionPro()}\t Precio: {self.get_Precio()}")
        p=potencia(self.get_IDPotencia())
        p.potencia_import()
        print(f"Potencia: {p.get_HP()} HP \"Caballos de Fuerza\"\n")
"""        
p = producto()
p.set_ID_Producto(5)
p.Producto_Import()
p.vista_Producto()"""
