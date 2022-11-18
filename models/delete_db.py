#!C:\Users\Alanjy_Huang\AppData\Local\Programs\Python\Python38-32\python.exe
#-*- coding: utf-8 -*-
#處理stdio輸出編碼，以避免亂碼
import codecs, sys 
#sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
import cgi
from models.dbconfig import conn, cur
def del_db(Name,dbchoose="storage"):
    sql="DELETE FROM "
    sql+=dbchoose
    sql+=" WHERE Name=%s;"
    print(sql)
    cur.execute(sql,(Name,))
    conn.commit()
    print(f"{Name}物品已刪除!")
if __name__=="__main__":
    del_db()
