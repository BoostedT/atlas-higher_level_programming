-- CITIES BY STATE
SELECT cities.id, cities.name, states.name FROM cities JOIN states ON cities.state_id = states.id ORDER BY states.name, cities.id;