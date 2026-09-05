-- Task 5
-- Attempt: modify Task 4 to sort the results by the city column, United States only.

-- Attempt 1 (fails):
-- SELECT a.CountryRegion, COUNT(*) AS NumberOfCustomers
-- FROM SalesLT.Customer c
-- JOIN SalesLT.CustomerAddress ca ON c.CustomerID = ca.CustomerID
-- JOIN SalesLT.Address a ON ca.AddressID = a.AddressID
-- WHERE a.CountryRegion = 'United States'
-- GROUP BY a.CountryRegion
-- ORDER BY a.City;
--
-- Error returned by Azure SQL:
-- Column "SalesLT.Address.City" is invalid in the ORDER BY clause because it is
-- not contained in either an aggregate function or the GROUP BY clause.
--
-- Why: SQL only allows ORDER BY on columns that are either grouped or wrapped in
-- an aggregate function. City is grouped by, aggregated, or selected nowhere in
-- this query, so the engine has no single value of City to sort each collapsed
-- CountryRegion group by.
--
-- Fix: add City to both the SELECT list and the GROUP BY clause, so each row in
-- the result set has one specific City value to sort on.

SELECT a.CountryRegion, a.City, COUNT(*) AS NumberOfCustomers
FROM SalesLT.Customer c
JOIN SalesLT.CustomerAddress ca ON c.CustomerID = ca.CustomerID
JOIN SalesLT.Address a ON ca.AddressID = a.AddressID
WHERE a.CountryRegion = 'United States'
GROUP BY a.CountryRegion, a.City
ORDER BY a.City;

-- Effect of adding City to GROUP BY on the number of groups:
-- Before (Task 4, United States only): 1 group, one row total for the whole
-- country, with a single customer count.
-- After (grouping by CountryRegion + City): 199 groups, one row per distinct
-- city, each with its own customer count.
-- Adding a second, more granular column to GROUP BY always increases (or at
-- best keeps the same) number of groups, since two rows now only fall in the
-- same group when they match on both columns, not just one.
