# -*- coding: utf-8 -*-
"""
Created on Sun May 23 19:31:19 2021

@author: Usuario
"""


import pymysql

db= pymysql.connect(host='localhost',
                       user='root',
                       password='',
                       database='ecomerce bombas')

class Db():
  def __init__(self):
    self.conexion= db
    self.cursor=self.conexion.cursor()

  def get_cursor(self):
    return self.cursor
  
  def get_conexion(self):
    return self.conexion


dbE=Db()
