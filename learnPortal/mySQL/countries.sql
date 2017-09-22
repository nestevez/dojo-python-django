#get all the countries that speak Slovene. return the name of the country, language and language percentage by language percentage in descending order
/*
SELECT countries.name, languages.language, languages.percentage 
FROM languages
JOIN countries ON countries.id = languages.country_id
WHERE languages.language = "Slovene"
ORDER BY languages.percentage DESC;
*/

#display the total number of cities for each country. return the name of the country and the total number of cities by the number of cities in descending order.
/*
SELECT countries.name, COUNT(*) AS num_of_cities 
FROM cities
JOIN countries ON countries.id = cities.country_id
GROUP BY countries.name
ORDER BY num_of_cities DESC;
*/

#get all the cities in Mexico with a population of greater than 500,000. arrange the result by population in descending order
/*
SELECT cities.name, cities.population
FROM cities
JOIN countries
ON countries.id = cities.country_id
WHERE countries.name = "Mexico"
AND cities.population > 500000
ORDER BY cities.population DESC;
*/

#get all languages in each country with a percentage greater than 89%. arrange the result by percentage in descending order
/*
SELECT countries.name, languages.language, languages.percentage
FROM languages
JOIN countries 
ON countries.id = languages.country_id
WHERE languages.percentage > 89
ORDER BY languages.percentage DESC;
*/

#get all the countries with Surface Area below 501 and Population greater than 100,000
/*
SELECT countries.name, countries.surface_area, countries.population
FROM countries
WHERE countries.surface_area < 501
AND countries.population > 100000
*/

#get countries with only Constitutional Monarchy with a capital greater than 200 and a life expectancy greater than 75 years
/*
SELECT countries.name, countries.government_form, countries.capital, countries.life_expectancy
FROM countries
WHERE government_form = "Constitutional Monarchy"
AND capital > 200
AND life_expectancy > 75;
*/

#get all the cities of Argentina inside the Buenos Aires district and have the population greater than 500,000. return the Country Name, City Name, District and Population
/*
SELECT countries.name, cities.name, cities.district, cities.population
FROM cities
JOIN countries
ON countries.id = cities.country_id
WHERE countries.name = "Argentina" 
AND cities.district = "Buenos Aires"
AND cities.population > 500000;
*/

#display the name of the region and the number of countries. arrange the result by the number of countries in descending order

SELECT countries.region, COUNT(*) AS num_of_countries
FROM countries
GROUP BY countries.region
ORDER BY num_of_countries DESC;
