#!C:\Users\Alanjy_Huang\AppData\Local\Programs\Python\Python38-32\python.exe
#-*- coding: utf-8 -*-
#處理stdio輸出編碼，以避免亂碼
import codecs, sys 
import cgi
from models.dbconfig import conn, cur

def buy(id=1,buy_num=1,dbchoose="storage"):
    
    sql="UPDATE "+dbchoose+" SET Number=Number-%s WHERE Id=%s;"
   # print(sql)
    cur.execute(sql,(buy_num,id, ))
    conn.commit()

def cash_out():
  #  print("incash out:")
    search="SELECT ID, Price, Number FROM shopping;"
    total=0
    cur.execute(search)
    records = cur.fetchall()
    
    for ( ID ,Price, Number) in records:
       total+=int(Price)*int(Number)
       buy(int(ID),int(Number),"storage")
    #print(total)
    delete="DELETE FROM shopping"
    
    cur.execute(delete)
    conn.commit()
    #print("delete done")
    return total
   # SELECT Price, Number FROM customers;
if __name__=='__main__':
      cash_out()


