USE movies_queries;

-- DISPLAYING Studio RECORDS
SELECT * FROM studio;

-- DISPLAYING Genre RECORDS
SELECT * FROM genre;

-- DISPLAYING Short Film RECORDS
SELECT film_name, film_runtime
FROM film
WHERE film_runtime < 120;

-- DISPLAYING Director RECORDS in Order
SELECT film_name, film_director
FROM film
ORDER BY film_director;
