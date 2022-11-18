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
form = cgi.FieldStorage()
#print("<p> control OK<\p>")
#result=list_db()
try:
        act=form.getvalue('control')
        
except:
        print("control argument missing")
        exit()


    #we can start accessing DB now
if act=="get": #get one record by xid
   # print("getOK")
    result=list_db.list_db()
    #print(result)
    json_res=json.dumps(result,ensure_ascii=True)
    print(json_res)
   # elif act=='like':
     #   mid=int(form.getvalue('id'))
      #  likeit(mid)
   # elif act=='del':
    #    mid=int(form.getvalue('id'))
     #   msgModel.kill(mid)
