-- task 9
-- Listing all the cities in the database.
-- Each record displays the city id, the city name, the state name.

SELECT cities.id, cities.name, states.name
FROM   cities
JOIN states
ON cities.state_id = states.id
ORDER BY cities.id ASC; 

