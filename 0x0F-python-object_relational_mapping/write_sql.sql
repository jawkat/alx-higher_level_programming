SELECT cities.id, cities.name, states.name
FROM cities
WHERE states.name LIKE BINARY %s
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;

