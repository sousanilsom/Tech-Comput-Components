-- Task 4
-- Return all customers grouped by each country region. CountryRegion lives on
-- SalesLT.Address, not SalesLT.Customer, so Customer is joined to Address through
-- the CustomerAddress bridge table.
-- COUNT(*) gives the number of customers in each country region.
SELECT a.CountryRegion, COUNT(*) AS NumberOfCustomers
FROM SalesLT.Customer c
JOIN SalesLT.CustomerAddress ca ON c.CustomerID = ca.CustomerID
JOIN SalesLT.Address a ON ca.AddressID = a.AddressID
GROUP BY a.CountryRegion;
