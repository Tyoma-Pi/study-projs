-- Код для PostgreSQL

--DROP TABLE Classes, Cars, Races, Results;
--DROP TYPE classes_type;

--CREATE TYPE classes_type AS ENUM('Racing', 'Street');

-- Создание таблицы Classes
CREATE TABLE Classes (
    "class" VARCHAR(100) NOT NULL,
    "type" VARCHAR(20) NOT NULL,
    country VARCHAR(100) NOT NULL,
    num_doors INT NOT NULL,
    engine_size DECIMAL(3, 1) NOT NULL,
    weight INT NOT NULL,
    CONSTRAINT pk_classes_class PRIMARY KEY ("class"),
    CONSTRAINT check_classes_type CHECK ("type" IN ('Racing', 'Street'))
);

-- Создание таблицы Cars
CREATE TABLE Cars (
    "name" VARCHAR(100) NOT NULL,
    "class" VARCHAR(100) NOT NULL,
    "year" INT NOT NULL,
    CONSTRAINT pk_cars_name PRIMARY KEY ("name"),
    CONSTRAINT fk_cars_class FOREIGN KEY ("class") REFERENCES Classes("class")
);

-- Создание таблицы Races
CREATE TABLE Races (
    "name" VARCHAR(100) NOT NULL,
    "date" DATE NOT NULL,
    CONSTRAINT pk_races_name PRIMARY KEY ("name")
);

-- Создание таблицы Results
CREATE TABLE Results (
    car VARCHAR(100) NOT NULL,
    race VARCHAR(100) NOT NULL,
    position INT NOT NULL,
    CONSTRAINT pk_results_car_race PRIMARY KEY (car, race),
    CONSTRAINT fk_results_car FOREIGN KEY (car) REFERENCES Cars("name"),
    CONSTRAINT fk_results_race FOREIGN KEY (race) REFERENCES Races("name")
);

-- Вставка данных в таблицу Classes
INSERT INTO Classes ("class", "type", country, num_doors, engine_size, weight) VALUES
('SportsCar', 'Racing', 'USA', 2, 3.5, 1500),
('Sedan', 'Street', 'Germany', 4, 2.0, 1200),
('SUV', 'Street', 'Japan', 4, 2.5, 1800),
('Hatchback', 'Street', 'France', 5, 1.6, 1100),
('Convertible', 'Racing', 'Italy', 2, 3.0, 1300),
('Coupe', 'Street', 'USA', 2, 2.5, 1400),
('Luxury Sedan', 'Street', 'Germany', 4, 3.0, 1600),
('Pickup', 'Street', 'USA', 2, 2.8, 2000);

-- Вставка данных в таблицу Cars
INSERT INTO Cars ("name", "class", "year") VALUES
('Ford Mustang', 'SportsCar', 2020),
('BMW 3 Series', 'Sedan', 2019),
('Toyota RAV4', 'SUV', 2021),
('Renault Clio', 'Hatchback', 2020),
('Ferrari 488', 'Convertible', 2019),
('Chevrolet Camaro', 'Coupe', 2021),
('Mercedes-Benz S-Class', 'Luxury Sedan', 2022),
('Ford F-150', 'Pickup', 2021),
('Audi A4', 'Sedan', 2018),
('Nissan Rogue', 'SUV', 2020);

-- Вставка данных в таблицу Races
INSERT INTO Races ("name", "date") VALUES
('Indy 500', '2023-05-28'),
('Le Mans', '2023-06-10'),
('Monaco Grand Prix', '2023-05-28'),
('Daytona 500', '2023-02-19'),
('Spa 24 Hours', '2023-07-29'),
('Bathurst 1000', '2023-10-08'),
('Nürburgring 24 Hours', '2023-06-17'),
('Pikes Peak International Hill Climb', '2023-06-25');

-- Вставка данных в таблицу Results
INSERT INTO Results (car, race, position) VALUES
('Ford Mustang', 'Indy 500', 1),
('BMW 3 Series', 'Le Mans', 3),
('Toyota RAV4', 'Monaco Grand Prix', 2),
('Renault Clio', 'Daytona 500', 5),
('Ferrari 488', 'Le Mans', 1),
('Chevrolet Camaro', 'Monaco Grand Prix', 4),
('Mercedes-Benz S-Class', 'Spa 24 Hours', 2),
('Ford F-150', 'Bathurst 1000', 6),
('Audi A4', 'Nürburgring 24 Hours', 8),
('Nissan Rogue', 'Pikes Peak International Hill Climb', 3);

/*Задача 1
Определить, какие автомобили из каждого класса имеют наименьшую среднюю позицию в гонках, и вывести информацию о каждом таком автомобиле для данного класса, включая его класс, среднюю позицию и количество гонок, в которых он участвовал. Также отсортировать результаты по средней позиции.*/
CREATE VIEW Task1 AS
WITH AveragePositions AS (
    SELECT 
        C.class AS car_class,
        C."name" AS car_name,
        AVG(R.position) AS average_position,
        COUNT(*) AS race_count
    FROM Cars C
    JOIN Results R ON C."name" = R.car
    GROUP BY C.class, C."name"
),
MinimunAveragePositions AS (
    SELECT 
        car_class,
        MIN(average_position) AS minimim_average_position
    FROM AveragePositions
    GROUP BY car_class
)
SELECT
    AP.car_name,
    AP.car_class,
    AP.average_position,
    AP.race_count
FROM AveragePositions AP
JOIN MinimunAveragePositions "MAP" ON AP.car_class = "MAP".car_class AND AP.average_position = "MAP".minimim_average_position
ORDER BY AP.average_position;

/*Задача 2
Определить автомобиль, который имеет наименьшую среднюю позицию в гонках среди всех автомобилей, и вывести информацию об этом автомобиле, включая его класс, среднюю позицию, количество гонок, в которых он участвовал, и страну производства класса автомобиля. Если несколько автомобилей имеют одинаковую наименьшую среднюю позицию, выбрать один из них по алфавиту (по имени автомобиля).*/
CREATE VIEW Task2 AS
WITH AveragePositions AS (
    SELECT 
        C.name AS car_name,
        AVG(R.position) AS average_position,
        COUNT(*) AS race_count,
        C."class"
    FROM Cars C
    JOIN Results R ON C.name = R.car
    GROUP BY C.name, C.class
),
MinimunAveragePositions AS (
    SELECT MIN(average_position) AS minimum_average_position FROM AveragePositions
)
SELECT 
    AP.car_name,
    CL.class AS car_class,
    AP.average_position,
    AP.race_count,
    CL.country AS car_country
FROM AveragePositions AP
JOIN MinimunAveragePositions "MAP" ON AP.average_position = "MAP".minimum_average_position
JOIN Cars C ON AP.car_name = C."name"
JOIN Classes CL ON C.class = CL.class
ORDER BY AP.car_name
LIMIT 1;

/*Задача 3
Определить классы автомобилей, которые имеют наименьшую среднюю позицию в гонках, и вывести информацию о каждом автомобиле из этих классов, включая его имя, среднюю позицию, количество гонок, в которых он участвовал, страну производства класса автомобиля, а также общее количество гонок, в которых участвовали автомобили этих классов. Если несколько классов имеют одинаковую среднюю позицию, выбрать все из них.*/
CREATE VIEW Task3 AS
WITH ClassAveragePositions AS (
    SELECT
        C.class,
        AVG(r.position) AS average_position,
        COUNT(*) AS total_races
    FROM Cars C
    JOIN Results R ON C.name = R.car
    GROUP BY C.class
),
MinimumClassAveragePosition AS (
    SELECT MIN(average_position) AS min_average_position
    FROM ClassAveragePositions
)
SELECT
    c.name AS car_name,
    c."class" AS car_class,
    cap.average_position,
    COUNT(r.race) AS race_count,
    cl.country AS car_country,
    cap.total_races
FROM Cars C
JOIN ClassAveragePositions cap USING ("class")
JOIN Classes cl USING ("class")
LEFT JOIN Results R ON C.name = R.car
JOIN MinimumClassAveragePosition mcap ON cap.average_position = mcap.min_average_position
GROUP BY C.name, cap.average_position, cl.country, cap.total_races
ORDER BY C.name;

/*Задача 4
Определить, какие автомобили имеют среднюю позицию лучше (меньше) средней позиции всех автомобилей в своем классе (то есть автомобилей в классе должно быть минимум два, чтобы выбрать один из них). Вывести информацию об этих автомобилях, включая их имя, класс, среднюю позицию, количество гонок, в которых они участвовали, и страну производства класса автомобиля. Также отсортировать результаты по классу и затем по средней позиции в порядке возрастания.*/
CREATE VIEW Task4 AS
WITH ClassAveragePositions AS (
    SELECT
        C.class,
        AVG(R.position) AS average_position,
        COUNT(*) AS total_races
    FROM Cars C
    JOIN Results R ON C.name = R.car
    GROUP BY C.class
    HAVING COUNT(*) >= 2 -- Условие: минимум 2 автомобиля в классе
),
CarAveragePositions AS (
    SELECT
        C.name,
        C.class,
        AVG(R.position) AS average_position,
        COUNT(R.race) AS race_count
    FROM Cars C
    JOIN Results R ON C.name = R.car
    GROUP BY C.name, C.class
)
SELECT
    CAP.name AS car_name,
    CAP.class AS car_class,
    CAP.average_position,
    CAP.race_count,
    CL.country AS cart_country
FROM CarAveragePositions CAP
JOIN ClassAveragePositions ClAP USING ("class")
JOIN Classes CL USING ("class")
WHERE CAP.average_position < ClAP.average_position
ORDER BY CAP.class, CAP.average_position;

/*Задача 5
Определить, какие классы автомобилей имеют наибольшее количество автомобилей с низкой средней позицией (больше 3.0) и вывести информацию о каждом автомобиле из этих классов, включая его имя, класс, среднюю позицию, количество гонок, в которых он участвовал, страну производства класса автомобиля, а также общее количество гонок для каждого класса. Отсортировать результаты по количеству автомобилей с низкой средней позицией.*/
CREATE VIEW Task5 AS
WITH CarAveragePositions AS (
    SELECT
        C.name AS car_name,
        C.class AS car_class,
        AVG(R.position) AS average_position,
        COUNT(*) AS race_count
    FROM Cars C
    JOIN Results R ON C.name = R.car
    GROUP BY C.name, C.class
),
ClassStats AS (
    SELECT
        car_class,
        COUNT(*) AS total_races,
        COUNT(CASE WHEN average_position > 3 THEN 1 END) AS cars_with_low_avg
    FROM CarAveragePositions
    GROUP BY car_class
    HAVING COUNT(*) >= 2
)
SELECT
    CAP.car_name,
    CAP.car_class,
    CAP.average_position,
    CAP.race_count,
    CL.country AS car_country,
    CS.total_races,
    CS.cars_with_low_avg AS low_position_count
FROM CarAveragePositions CAP
JOIN ClassStats CS USING (car_class)
JOIN Classes CL ON cap.car_class = CL.class
ORDER BY CS.cars_with_low_avg DESC;