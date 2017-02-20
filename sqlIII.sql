
select distinct S1.CustomerID
from AdventureWorksLT.SalesLT.SalesOrderHeader S1, AdventureWorksLT.SalesLT.Product P, AdventureWorksLT.SalesLT.SalesOrderDetail S
where P.Color='red' and P.ProductID=S.ProductID and S.SalesOrderID=S1.SalesOrderID 

go
create view RedSpending AS
select C.CustomerID, C.FirstName, C.LastName, HighestPrice= MAX(S.UnitPrice)
from AdventureWorksLT.SalesLT.Customer C,
	 AdventureWorksLT.SalesLT.Product P, 
	 AdventureWorksLT.SalesLT.SalesOrderDetail S,
	 AdventureWorksLT.SalesLT.SalesOrderHeader S1
where P.ProductID=S.ProductID and S.SalesOrderID=S1.SalesOrderID 
      and S1.CustomerID=C.CustomerID and P.Color='red' and P.Color is not null
      Group BY C.CustomerID, C.FirstName,C.LastName
