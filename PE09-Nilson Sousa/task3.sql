-- Task 3
-- Return CustomerID, CompanyName, FirstName, LastName and Phone from SalesLT.Customer
-- filtered to customers whose last name starts with the letter A.
SELECT CustomerID, CompanyName, FirstName, LastName, Phone
FROM SalesLT.Customer
WHERE LastName LIKE 'A%';
