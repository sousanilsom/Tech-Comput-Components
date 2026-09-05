-- Task 2
-- Return AddressID, City, StateProvince and CountryRegion from SalesLT.Address
-- filtered to addresses in Washington, Texas, or Missouri, United States.
SELECT AddressID, City, StateProvince, CountryRegion
FROM SalesLT.Address
WHERE StateProvince IN ('Washington', 'Texas', 'Missouri') AND CountryRegion = 'United States';
