from os import getenv
import pymssql
conn=pymssql.connect(host='cypress.csil.sfu.ca',user='s_hhammadu', password='mMH47rF6eYf6e36T',database='AdventureWorksLT')
mycursor=conn.cursor()
mycursor.execute(' Select Count(*) From SalesLT.Customer ')
answer=mycursor.fetchone()
print answer
conn.close()

