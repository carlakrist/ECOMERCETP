# -*- coding: utf-8 -*-
"""
Created on Thu May 27 21:06:24 2021

@author: Usuario
"""
from BaseDatos import dbE

class categoria():
    def __init__(self, ID):
        self.__id_categoria=ID
        self.__Tipo=""
        self.__Descripcion=""
        self.__Voltaje=0
    
    def get_id_categoria(self):
        return self.__id_categoria
    
    def set_ID_Categoria(self, ID):
        self.__id_categoria=ID
        
    def set_ID_CategoriaN(self):
        sql="select id_categoria from categoria where Tipo = %s"
        valor=self.__Tipo
        dbE.get_cursor().execute(sql,valor)
        self.__id_categoria = dbE.get_cursor().fetchone()[0]
        
    def get_Tipo(self):
        return self.__Tipo
    
    def set_Tipo(self, Tipo):
        self.__Tipo=Tipo
    
    def get_Descripcion(self):
         return self.__Descripcion
    
    def set_Descripcion(self, Descripcion):
        self.__Descripcion=Descripcion
     
    def get_Voltaje(self):
        return self.__Voltaje
    
    def set_Voltaje(self, Voltaje):
        self.__Voltaje=Voltaje
        
    def categoria_import(self):
        sql="select Tipo, descripcion, tipo_voltaje from categoria where id_categoria = %s"
        valor=self.get_id_categoria()
        dbE.get_cursor().execute(sql,valor)
        result=dbE.get_cursor().fetchone()
        self.set_Tipo(result[0])
        self.set_Voltaje(result[2])
        if result[2] != None:
            self.set_Descripcion(result[1])
        else:
            self.set_Descripcion("Sin Datos")
            


