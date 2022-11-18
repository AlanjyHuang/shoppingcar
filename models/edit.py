#!C:\Users\Alanjy_Huang\AppData\Local\Programs\Python\Python38-32\python.exe
#-*- coding: utf-8 -*-
#處理stdio輸出編碼，以避免亂碼
import codecs, sys 
import cgi
from models.dbconfig import conn, cur

def edit(Name,buy_num=1,dbchoose="storage"):
    print("in")
    sql="UPDATE "+dbchoose+" SET Number=%s WHERE Name=%s;"
    print(sql)
    cur.execute(sql,(buy_num,Name, ))
    conn.commit()
    