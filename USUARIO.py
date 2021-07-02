# -*- coding: utf-8 -*-
"""
Created on Thu May 20 20:04:36 2021

@author: Usuario
"""
import base64
from BaseDatos import dbE

class usuario():
    
    def __init__(self, DNI, Nombre, Apellido, Email, Celular, Direccion, Ciudad, Contraseña):
        self.__ID=0
        self.__DNI = DNI
        self.__Nombre = Nombre
        self.__Apellido = Apellido
        self.__Email=Email
        self.__Celular=Celular
        self.__Direccion=Direccion
        self.__Ciudad=Ciudad
        self.__id_ciudad = 0
        self.__Contraseña = Contraseña
    
    def get_ID(self):
         return self.__ID
     
    def get_DNI(self):
        return self.__DNI
    
    def get_Nombre(self):
        return self.__Nombre
    
    def get_Apellido(self):
        return self.__Apellido
    
    def get_Email(self):
        return self.__Email
    
    def get_Celular(self):
        return self.__Celular
    
    def get_Direccion(self):
        return self.__Direccion
    
    def get_Ciudad(self):
        return self.__Ciudad
    
    def get_ID_ciudad(self):
        return self.__id_ciudad
    
    def get_Contraseña(self):
        return self.__Contraseña
    
    def set_ID(self, ID):
        self.__ID=ID
    
    def set_Nombre(self, Nombre):
        self.__Nombre=Nombre
    
    def set_Apellido(self, Apellido):
        self.__Apellido=Apellido
    
    def set_Email(self, Email):
        self.__Email=Email
        
    def set_Celular(self, Celular):
        self.__Celular=Celular
        
    def set_Direccion(self, Direccion):
        self.__Direccion=Direccion
        
    def set_Ciudad(self, Ciudad):
        self.__Ciudad=Ciudad
        
    def set_ID_ciudad(self):
        sql="select id_ciudad from ciudad where nombre_ciudad = %s"
        valor=self.get_Ciudad()
        dbE.get_cursor().execute(sql,valor)
        self.__id_ciudad = dbE.get_cursor().fetchone()[0]
    
    def set_Contraseña(self, Contraseña):
        self.__Contraseña=Contraseña
    
    def Encriptar_Contraseña(self):
        return base64.encodebytes(bytes(self.get_Contraseña(),'utf-8'))
    
    def desencriptar_Contraseña(self):
        return base64.decodebytes(self.Encriptar_Contraseña()).decode('utf-8')
    
    
    def saveBD(self):
        self.set_ID_ciudad()
        sql="insert into usuarios(DNI, Nombre, Apellido, Email, Celular, direccion, id_ciudad, Contraseña) values(%s,%s,%s,%s,%s,%s,%s,%s)"
        valor =(self.get_DNI(), self.get_Nombre(), self.get_Apellido(), self.get_Email(), self.get_Celular(),self.get_Direccion(),self.get_ID_ciudad(),self.Encriptar_Contraseña())
        dbE.get_cursor().execute(sql,valor)
        dbE.get_conexion().commit()
        self.set_ID(dbE.get_cursor().lastrowid)#Toma el ID de la Ultima linea donde esta el nuevo registro
        
    def updateBD(self):
        self.set_ID_ciudad()
        sql = "update usuarios set DNI=%s, Nombre=%s, Apellido=%s, Email=%s, Celular=%s, direccion=%s, id_ciudad=%s, Contraseña=%s  where id=%s"
        valor = (self.get_DNI(),self.get_Nombre(), self.get_Apellido(), self.get_Email(), self.get_Celular(),self.get_Direccion(),self.get_ID_ciudad(),self.Encriptar_Contraseña(),self.get_ID())
        dbE.get_cursor().execute(sql,valor)
        dbE.get_conexion().commit()
        

    
    def deleteBD(self):
        sql = "delete from usuarios where id=%s"
        valor = (self.get_ID(),)
        dbE.get_cursor().execute(sql,valor)
        dbE.get_conexion().commit()
        
    def user_view(self):
        sql = "select nombre, apellido, Email, celular, direccion from usuarios where id=%s"
        valor = (self.get_ID())
        dbE.get_cursor().execute(sql,valor)
        result = dbE.get_cursor().fetchone()
        return result
    
    def vista_usuario(DNI):#IMPRIME Datos del usuario Recibiendo el DNI
        sql = "select Nombre, Apellido, Email, Celular, Direccion from usuarios where DNI=%s"
        valor = DNI
        dbE.get_cursor().execute(sql,valor)
        dbE.get_conexion().commit()
        result = dbE.get_cursor().fetchone()
        for i in result:
            print(i)
            
    

    

        
    