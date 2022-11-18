#!C:\Users\Alanjy_Huang\AppData\Local\Programs\Python\Python38-32\python.exe
#-*- coding: utf-8 -*-
#處理stdio輸出編碼，以避免亂碼
#print headers first
print("Content-Type: text/html; charset=utf-8\n")
#print("Content-type: application/json; charset: utf-8\n")

import json
from datetime import date, datetime
import cgi
import sys

sys.path.insert(0,'..')
from models import list_db
from models import insert_db
from models import buy
form = cgi.FieldStorage()
#print("<p> control OK<\p>")
#result=list_db()
try:
        act=form.getvalue('control')
        #print(act)
except:
        print("control argument missing")
        exit()

    #we can start accessing DB now
if act=="get": #get one record by xid
   # print("getOK")
    db=form.getvalue('db')
    result=list_db.list_db(db)
    #print(result)
    json_res=json.dumps(result,ensure_ascii=True)
    print(json_res)

elif act=="add":
    #print('in add')
    Num=form.getvalue('Num')
    Name=form.getvalue('Name')

   # print(Name,Num)
    ret=list_db.search_db(Name,Num)
    #print(ret)
    insert_db.insert_db('shopping',ret)
    #elif act=='del':
     #   mid=int(form.getvalue('id'))
      #  msgModel.kill(mid)
elif act=="cashout":
    #print("incash")
    ret=buy.cash_out()
   # print("OK")
    print(ret)