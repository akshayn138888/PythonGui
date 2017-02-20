
CREATE FUNCTION dbo.AverageCost(@color nvarchar(15))
Returns INT
AS
BEGIN
	DECLARE @AverageStandardcost INT;
	SET @AverageStandardcost=( SELECT AVG(P.StandardCost)
							   FROM AdventureWorksLT.SalesLT.Product P
							   WHERE @color=P.Color)
	RETURN @AverageStandardcost;
END






