#!C:\Users\Alanjy_Huang\AppData\Local\Programs\Python\Python38-32\python.exe
#-*- coding: utf-8 -*-
#處理stdio輸出編碼，以避免亂碼
import codecs, sys 
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
import cgi
from dbconfig import conn, cur
sql="INSERT INTO storage (ID, Name, Price, Number) VALUES (%s,%s, %s, %s)"
value=[]
try:
    print("input ID Name Price Number with space ")
    while True:
        s=input()
        if s!="":
            s=s.split(' ')
            t_s=tuple(s)
            value.append(t_s)
            print(t_s)
        else:
            break
except EOFError:
    pass
#str_value=','.join(value)
#print(value)
cur.executemany(sql,value)
conn.commit()
