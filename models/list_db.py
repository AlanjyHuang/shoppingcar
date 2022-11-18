#!C:\Users\Alanjy_Huang\AppData\Local\Programs\Python\Python38-32\python.exe
#-*- coding: utf-8 -*-
#處理stdio輸出編碼，以避免亂碼
import codecs, sys 
import os
import cgi
from models.dbconfig import conn, cur
#sys.path.insert(0,os.getcwd())
#sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)

def list_db(dbchoose="storage"):
	#print("listdb OK")
	ret_data=[]
	search="SELECT * FROM "
	search+=dbchoose
	cur.execute(search)
	records = cur.fetchall()
	for (ID, Name, Price, Number) in records:
		#print(f"{ID} {Name} {Price} {Number}")
		temp={
			"ID":ID,
			"Name":Name,
			"Price":Price,
			"Number":Number
		}
		ret_data.append(temp)
	return ret_data
if __name__=='__main__':
	print(list_db())