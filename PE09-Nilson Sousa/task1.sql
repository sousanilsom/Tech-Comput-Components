-- Task 1
-- Return AddressID, City, StateProvince and CountryRegion from SalesLT.Address
-- filtered to only addresses in the state of Texas, United States.
SELECT AddressID, City, StateProvince, CountryRegion
FROM SalesLT.Address
WHERE StateProvince = 'Texas' AND CountryRegion = 'United States';
