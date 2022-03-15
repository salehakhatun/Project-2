drop TABLE country;
drop TABLE happiness_score;
drop TABLE life_expectancy;
drop TABLE happiness_factors;
drop TABLE merged;

CREATE TABLE country (
country VARCHAR(30),
PRIMARY KEY (country)
);

SELECT * FROM country;

CREATE TABLE happiness_score (
country VARCHAR(30),
"Happiness rank" VARCHAR(10),
"Happiness score" VARCHAR(10),
FOREIGN KEY (country) REFERENCES country (country)	
);

SELECT * FROM happiness_score where country = 'Australia';

CREATE TABLE happiness_factors (
country VARCHAR(30),
"Freedom to make life choices" VARCHAR(10),
"Social support" VARCHAR(10),
"GDP per capita" VARCHAR(10),	
FOREIGN KEY (country) REFERENCES country (country)		
);

SELECT * FROM happiness_factors;

CREATE TABLE life_expectancy (
country VARCHAR(10),
"life expectancy" FLOAT,
FOREIGN KEY (country) REFERENCES country (country)
);

SELECT * FROM life_expectancy;

CREATE TABLE merged (
country VARCHAR(30),
"Freedom to make life choices" VARCHAR(10),
"Social support" VARCHAR(10),
"GDP per capita" VARCHAR(10),
"Happiness rank" VARCHAR(10),
"Happiness score" VARCHAR(10),
"life expectancy" VARCHAR(10) NOT NULL,	
FOREIGN KEY (country) REFERENCES country (country)		
);

SELECT * FROM merged;
