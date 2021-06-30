# -*- coding: utf-8 -*-
"""
Created on Sun May 30 20:37:58 2021

@author: Usuario
"""
from BaseDatos import dbE

class potencia():
    
    def __init__(self, ID):
        self.__id_potencia=ID
        self.__HP = 0
        
    def get_id_potencia(self):
        return self.__id_potencia
    
    def set_id_potencia(self, ID):
        self.__id_potencia=ID
    
    def get_HP(self):
        return self.__HP
       
    def set_HP(self, HP):
        self.__HP=HP
        
    def potencia_import(self):
        sql="select cantidad_hp from potencia where id_potencia = %s"
        valor=self.get_id_potencia()
        dbE.get_cursor().execute(sql,valor)
        self.__HP=dbE.get_cursor().fetchone()[0]
        
    
    