#!C:\Users\Alanjy_Huang\AppData\Local\Programs\Python\Python38-32\python.exe
#-*- coding: utf-8 -*-
#處理stdio輸出編碼，以避免亂碼
import codecs, sys 
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
import cgi
from dbconfig import conn, cur
def buy(id=1,buy_num=1,dbchoose="storage"):
    sql="update "+dbchoose+"set num=num-"+str(buy_num)+"where id=%s;"
    cur.execute(sql,(id,))
    conn.commit()
