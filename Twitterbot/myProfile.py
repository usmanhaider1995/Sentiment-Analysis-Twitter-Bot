# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 00:54:05 2021

@author: usman
"""

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",port=3388
)

print(mydb)