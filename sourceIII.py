from os import getenv
import pymssql
conn=pymssql.connect(host='cypress.csil.sfu.ca',user='s_hhammadu', password='mMH47rF6eYf6e36T',database='hhammadu354')

mycursor=conn.cursor()
mycursor.execute(" select P.Color from AdventureWorksLT.SalesLT.Product P where P.Color is not null Order By P.Color")
answer= mycursor.fetchone()
i=1
while answer:
    print ("color",i,answer)
    answer=mycursor.fetchone()
    i=i+1
color= raw_input("Enter the color name: ")
mycursor1=conn.cursor()
mycursor1.execute(""" create view ColorSpending AS
select C.CustomerID, C.FirstName, C.LastName, HighestPrice= MAX(S.UnitPrice)
from AdventureWorksLT.SalesLT.Customer C,
	 AdventureWorksLT.SalesLT.Product P, 
	 AdventureWorksLT.SalesLT.SalesOrderDetail S,
	 AdventureWorksLT.SalesLT.SalesOrderHeader S1
where P.ProductID=S.ProductID and S.SalesOrderID=S1.SalesOrderID 
      and S1.CustomerID=C.CustomerID and P.Color=%s and P.Color is not null
      Group BY C.CustomerID, C.FirstName,C.LastName""",color)

mycursor1.execute("""
SELECT CustomerID, FirstName,LastName, HighestPrice
FROM hhammadu354.dbo.ColorSpending
ORDER BY FirstName desc,LastName desc """)

answer1=mycursor1.fetchone()
j=1
while answer1:
    print (j,answer1)
    answer1=mycursor1.fetchone()
    j=j+1

conn.close()

