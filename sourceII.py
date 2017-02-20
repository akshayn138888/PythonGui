from os import getenv
import pymssql
conn=pymssql.connect(host='cypress.csil.sfu.ca',user='s_hhammadu', password='mMH47rF6eYf6e36T',database='hhammadu354')
mycursor=conn.cursor()


mycursor.execute(" select dbo.AverageCost('Red') ")
answer= mycursor.fetchone()
print "The average standard cost of the products, red in color is: ", answer
conn.close()

