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
price=input("Enter your price: ")
mycursor11=conn.cursor()
mycursor11.execute(" select dbo.AverageCost(%s) ",color)
answer11=mycursor11.fetchone()
averageCost=answer11[0]
print "Average standard cost for ",color," is ",averageCost
if price < averageCost:
    print "price is too low for ",color
else:
    print "price is ok "

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
ORDER BY HighestPrice desc """)
answer1=mycursor1.fetchone()
f = open('colorinfo.html','w')
message = """<html>
<head></head>
<body><p><b> CustomerID,FirstName,LastName,HighestPrice</b></p></body>
</html>"""
f.write(message)
while answer1:
    s=str(answer1)
    f.write(s)
    message2="""<html><head></head><body><br/></body></html>"""
    f.write(message2)
    answer1=mycursor1.fetchone()

f.close()

conn.close()

