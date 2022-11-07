#!C:\Users\Alanjy_Huang\AppData\Local\Programs\Python\Python38-32\python.exe
#-*- coding: utf-8 -*-
#處理stdio輸出編碼，以避免亂碼
import codecs, sys 
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
import cgi
from dbconfig import conn, cur
def list_db(dbchoose="storage"):
	search="SELECT * FROM "
	search+=dbchoose
	cur.execute(search)
	records = cur.fetchall()
	for (ID, Name, Price, Number) in records:
		print(f"{ID} {Name} {Price} {Number}")
if __name__=='__main__':
	list_db()