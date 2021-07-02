# -*- coding: utf-8 -*-
"""
Created on Sun May 23 19:50:56 2021

@author: Usuario
"""
from BaseDatos import dbE
from validate_email import validate_email #PARA VALIDAR CORREOS
import base64


class Validador():
    def __init__(self):
        pass
    
    def validarProducto(self,dic):
        carga={}
        errores={}
        
        for clave, valor in dic.items():
            carga[clave]=valor.strip()#uso strip para sacar espacios de los costados
            
        if carga["Nombre"]=="":
            errores["Nombre"]="Campo Nombre Vacio"
            
        if carga["Marca"]=="":
            errores["Marca"]="Campo Marca Vacio"
         
        if carga["Tipo"]=="":
            errores["Tipo"]="Campo Tipo Vacio"
            
        if carga["Descripcion"]=="":
            pass
            
        if carga["Potencia"]=="":#revisa si el campo esta vacio
            errores["Potencia"]="Campo Potencia Vacio"#revisa si el campo esta vacio
        elif carga["Potencia"].isdigit()==False:#revisa si el campo tiene letras
            errores["Potencia"]="El campo  Potencia contiene Letras"
            
        if carga["Precio"]=="":#revisa si el campo esta vacio
            errores["Precio"]="Campo Precio Vacio"#revisa si el campo esta vacio
        elif carga["Precio"].isdigit()==False:#revisa si el campo tiene letras
            errores["Precio"]="El campo  Precio contiene Letras"
            
        if errores=={}:#si no hay errores
            sql = "select id_producto from productos where nombre=%s"#sentencia de MySQL
            valor = (carga["Nombre"],)
            dbE.get_cursor().execute(sql,valor)
            result=dbE.get_cursor().fetchone()
            if result is not None:#REVISA SI EL REGISTRO YA EXISTE
                errores["Nombre"]="El nombre ya esta registrado"
                return errores
        return errores
    
    def validarUsuario(self,dic):
        carga={}
        errores={}
        carcteresEspeciales=['$','@','#','%']
        
        for clave, valor in dic.items():
            carga[clave]=valor.strip()#uso strip para sacar espacios de los costados
        if carga["Nombre"]=="":
            errores["Nombre"]="Campo Nombre Vacio"
            
        if carga["Email"]=="":
            errores["Email"]="Campo Email Vacio"
        elif validate_email(carga["Email"])==False:
            errores["Email"]="No tiene el formato de email"
        #VALIDACION CONTRASEÑA - MAY/MIN/CARACT-ESPEC/NUM    
        if len(carga["Contraseña"])<6:
           errores['Contraseña']="la Contraseña debe contener mas de 6 caracteres"
        elif carga['Contraseña']=='':
            errores['Contraseña']='campo Contraseña vacio'
        elif not any(i.isupper() for i in carga["Contraseña"]):
            errores["Contraseña"]="Contraseña debe contener una letra mayuscula"
        elif not any(i.isdigit() for i in carga["Contraseña"]):
            errores["Contraseña"]="Contraseña debe contener un caracter numeral"
        elif not any(i.islower() for i in carga["Contraseña"]):
            errores["Contraseña"]="Contraseña debe contener una letra minuscula"
        elif not any(i in carcteresEspeciales for i in carga["Contraseña"]):
            errores["Contraseña"]="Contraseña debe contener carateres especiales $@#"
        
        if errores=={}:
            sql="select id from usuarios where Email=%s"#SENTENCIA MySQL
            valor=(carga['Email'],)
            dbE.get_cursor().execute(sql,valor)
            result=dbE.get_cursor().fetchone()
            if result is not None:#REVISA SI EL REGISTRO YA EXISTE
                errores['Email']='El Email ya esta registrado'
                return errores
        return errores
    
    def validarUsuarioUP(self,dic):#valida el update de usuario
        carga={}
        errores={}
        carcteresEspeciales=['$','@','#','%']
        
        for clave, valor in dic.items():
            carga[clave]=valor.strip()#uso strip para sacar espacios de los costados
        if carga["Nombre"]=="":
            errores["Nombre"]="Campo Nombre Vacio"
        if carga["Email"]=="":
            errores["Email"]="Campo Email Vacio"
        elif validate_email(carga["Email"])==False:
            errores["Email"]="No tiene el formato de email"
        #VALIDACION CONTRASEÑA - MAY/MIN/CARACT-ESPEC/NUM    
        if len(carga["Contraseña"])<6:
           errores['Contraseña']="la Contraseña debe contener mas de 6 caracteres"
        elif carga['Contraseña']=='':
            errores['Contraseña']='campo Contraseña vacio'
        elif not any(i.isupper() for i in carga["Contraseña"]):
            errores["Contraseña"]="Contraseña debe contener una letra mayuscula"
        elif not any(i.isdigit() for i in carga["Contraseña"]):
            errores["Contraseña"]="Contraseña debe contener un caracter numeral"
        elif not any(i.islower() for i in carga["Contraseña"]):
            errores["Contraseña"]="Contraseña debe contener una letra minuscula"
        elif not any(i in carcteresEspeciales for i in carga["Contraseña"]):
            errores["Contraseña"]="Contraseña debe contener carateres especiales $@#"
            
        
        return errores
        
    def validar_login(self,dic):
        sql="select * from usuarios where Email=%s"
        val=(dic['Email'],)
        dbE.get_cursor().execute(sql,val)
        result=dbE.get_cursor().fetchone()
        if result==[]:
            return False
        if base64.decodebytes(result[8].encode("UTF-8")).decode('utf-8')==dic['Contraseña']:
            return result
        else:
            return False
        #print(result)
        

VAL = Validador()
            