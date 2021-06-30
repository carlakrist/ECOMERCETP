# -*- coding: utf-8 -*-
"""
Created on Thu May 27 20:48:21 2021

@author: Usuario
"""
from BaseDatos import dbE

class marca():
    def __init__(self, ID):
        self.__id_marca = ID
        self.__Nombre = ""
        self.__Origen=""
        self.__Garantia=0
        
    def get_id_marca(self):
        return self.__id_marca
    
    def set_id_marca(self,ID):
        self.__id_marca = ID
        
    def get_Nombre(self):
         return self.__Nombre
    
    def set_Nombre(self, Nombre):
        self.__Nombre=Nombre
    
    def get_Origen(self):
         return self.__Origen
    
    def set_Origen(self, Origen):
        self.__Origen=Origen
    
    def get_Garantia(self):
         return self.__Garantia
    
    def set_Garantia(self, Garantia):
        self.__Garantia=Garantia
        
    
    def set_ID_marcaN(self):
        sql="select id_marca from marca where nombre = %s"
        valor=self.__Nombre()
        dbE.get_cursor().execute(sql,valor)
        self.__id_potencia=dbE.get_cursor().fetchone()[0]
        
    
    def marca_Import(self):
        sql="select Nombre, origen, garantia_meses from marcas where id_marca = %s"
        valor=self.get_id_marca()
        dbE.get_cursor().execute(sql,valor)
        result=dbE.get_cursor().fetchone()
        self.set_Nombre(result[0])
        self.set_Origen(result[1])
        self.set_Garantia(result[2])

    
        
"""m = marca(3)
m.marca_Import()
print(m.get_Garantia())"""