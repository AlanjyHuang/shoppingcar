#!C:\Users\Alanjy_Huang\AppData\Local\Programs\Python\Python38-32\python.exe
#-*- coding: utf-8 -*-
#處理stdio輸出編碼，以避免亂碼
import codecs, sys 
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
import cgi
from dbconfig import conn, cur
def del_db(id=1,dbchoose="storage"):
    sql="delete from "
    sql+=dbchoose
    sql+=" where id=%s;"
    cur.execute(sql,(id,))
    conn.commit()
    print(f"{id}號物品已刪除!")
if __name__=="__main__":
    del_db()
