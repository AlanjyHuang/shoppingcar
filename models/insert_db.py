#!C:\Users\Alanjy_Huang\AppData\Local\Programs\Python\Python38-32\python.exe
#-*- coding: utf-8 -*-
#處理stdio輸出編碼，以避免亂碼
import codecs, sys ,os
#sys.path.insert(0,'..')
#sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
import cgi
from models.dbconfig import conn, cur

def insert_db_enter(dbchoose="storage"):
    print("insert")
    sql="INSERT INTO "
    sql+=dbchoose
    sql+=" (ID, Name, Price, Number) VALUES (%s,%s, %s, %s)"
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
    print("commit? y,n")
    descision=input()
    if (descision=='y'):
        conn.commit()
    else:
        pass
def insert_db(dbchoose,ret):
    #print("insert")
    sql="INSERT INTO "
    
    sql+=dbchoose
  #  print(sql)
    sql+=" (ID, Name, Price, Number) VALUES ('"
    #print(ret['ID'])
    sql+=str(ret['ID'])
    
    sql+="','"
    sql+=ret['Name']
    sql+="','"
    sql+=str(ret['Price'])
    sql+="','"

    sql+=str(ret['Number'])
    sql+="')"
    print(sql)
    cur.execute(sql)
    conn.commit()


if __name__=='__main__':
    insert_db()

