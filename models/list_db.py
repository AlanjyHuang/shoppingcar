#!C:\Users\Alanjy_Huang\AppData\Local\Programs\Python\Python38-32\python.exe
#-*- coding: utf-8 -*-
#處理stdio輸出編碼，以避免亂碼
import codecs, sys 
import os
import cgi
sys.path.append('..')
from models.dbconfig import conn, cur

#sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
#SELECT * FROM customers WHERE Name = '王二'
def search_db(Name,num):
	#print("in search")
	search="SELECT * FROM "
	search+="storage"
	search+=" WHERE Name = '"
	search+=Name
	search+="'"
	#print(search)
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
		temp["Number"]=num
	return temp
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
	print(search_db('shoe',1))