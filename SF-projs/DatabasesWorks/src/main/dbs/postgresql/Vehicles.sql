-- Код для PostgreSQL

--DROP TABLE Vehicles, Cars, Motorcycles, Bicycles;
--DROP TYPE vehicle_type, transmission_type, motorcycle_type, bicycle_type;

-- Создание типов данных для перечислений (не актуально)
--CREATE TYPE vehicles_type AS ENUM('Car', 'Motorcycle', 'Bicycle');
--CREATE TYPE transmissions_type AS ENUM('Automatic', 'Manual');
--CREATE TYPE motorcycles_type AS ENUM('Sport', 'Cruiser', 'Touring');
--CREATE TYPE bicycles_type AS ENUM('Mountain', 'Road', 'Hybrid');

-- Создание таблицы Vehicles
CREATE TABLE Vehicles (
    maker VARCHAR(100) NOT NULL,
    model VARCHAR(100) NOT NULL,
    "type" VARCHAR(20) NOT NULL,
    CONSTRAINT pk_vehicle_model PRIMARY KEY (model),
    CONSTRAINT check_vehicles_type CHECK ("type" IN ('Car', 'Motorcycle', 'Bicycle'))
);

-- Создание таблицы Cars
CREATE TABLE Cars (
    vin VARCHAR(17) NOT NULL,
    model VARCHAR(100) NOT NULL,
    engine_capacity DECIMAL(4, 2) NOT NULL,
    horsepower INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    transmission VARCHAR(20) NOT NULL,
    CONSTRAINT pk_car_vin PRIMARY KEY (vin),
    CONSTRAINT fk_car_model FOREIGN KEY (model) REFERENCES Vehicles(model),
    CONSTRAINT check_transmissions_type CHECK (transmission IN ('Automatic', 'Manual'))
);

-- Создание таблицы Motorcycles
CREATE TABLE Motorcycles (
    vin VARCHAR(17) NOT NULL,
    model VARCHAR(100) NOT NULL,
    engine_capacity DECIMAL(4, 2) NOT NULL,
    horsepower INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    "type" VARCHAR(20) NOT NULL,
    CONSTRAINT pk_motorcycle_vin PRIMARY KEY (vin),
    CONSTRAINT fk_motorcycle_model FOREIGN KEY (model) REFERENCES Vehicles(model),
    CONSTRAINT check_motorcycles_type CHECK ("type" IN ('Sport', 'Cruiser', 'Touring'))
);

-- Создание таблицы Bicycles
CREATE TABLE Bicycles (
    serial_number VARCHAR(20) NOT NULL,
    model VARCHAR(100) NOT NULL,
    gear_count INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    "type" VARCHAR(20) NOT NULL,
    CONSTRAINT pk_bicycle_serial_number PRIMARY KEY (serial_number),
    CONSTRAINT fk_bicycle_model FOREIGN KEY (model) REFERENCES Vehicles(model),
    CONSTRAINT check_bicycles_type CHECK ("type" IN ('Mountain', 'Road', 'Hybrid'))
);

-- Вставка данных в таблицу Vehicles
INSERT INTO Vehicles (maker, model, type) VALUES
('Toyota', 'Camry', 'Car'),
('Honda', 'Civic', 'Car'),
('Ford', 'Mustang', 'Car'),
('Yamaha', 'YZF-R1', 'Motorcycle'),
('Harley-Davidson', 'Sportster', 'Motorcycle'),
('Kawasaki', 'Ninja', 'Motorcycle'),
('Trek', 'Domane', 'Bicycle'),
('Giant', 'Defy', 'Bicycle'),
('Specialized', 'Stumpjumper', 'Bicycle');

-- Вставка данных в таблицу Cars
INSERT INTO Cars (vin, model, engine_capacity, horsepower, price, transmission) VALUES
('1HGCM82633A123456', 'Camry', 2.5, 203, 24000.00, 'Automatic'),
('2HGFG3B53GH123456', 'Civic', 2.0, 158, 22000.00, 'Manual'),
('1FA6P8CF0J1234567', 'Mustang', 5.0, 450, 55000.00, 'Automatic');

-- Вставка данных в таблицу Motorcycles
INSERT INTO Motorcycles (vin, model, engine_capacity, horsepower, price, type) VALUES
('JYARN28E9FA123456', 'YZF-R1', 1.0, 200, 17000.00, 'Sport'),
('1HD1ZK3158K123456', 'Sportster', 1.2, 70, 12000.00, 'Cruiser'),
('JKBVNAF156A123456', 'Ninja', 0.9, 150, 14000.00, 'Sport');

-- Вставка данных в таблицу Bicycles
INSERT INTO Bicycles (serial_number, model, gear_count, price, type) VALUES
('SN123456789', 'Domane', 22, 3500.00, 'Road'),
('SN987654321', 'Defy', 20, 3000.00, 'Road'),
('SN456789123', 'Stumpjumper', 30, 4000.00, 'Mountain');

/*Задача 1
Найдите производителей (maker) и модели всех мотоциклов, которые имеют мощность более 150 лошадиных сил, стоят менее 20 тысяч долларов и являются спортивными (тип Sport). Также отсортируйте результаты по мощности в порядке убывания.*/
CREATE VIEW Task1 AS
SELECT
	V.maker,
	V.model
FROM Motorcycles M
JOIN Vehicles V USING (model)
WHERE M.horsepower > 150 AND M.price < 20000 AND M."type" = 'Sport'
ORDER BY horsepower DESC;

/*Задача 2
Найти информацию о производителях и моделях различных типов транспортных средств (автомобили, мотоциклы и велосипеды), которые соответствуют заданным критериям.

Автомобили:
Мощность двигателя более 150 лошадиных сил.
Объем двигателя менее 3 литров.
Цену менее 35 тысяч долларов.
В выводе должны быть указаны производитель (maker), номер модели (model), мощность (horsepower), объем двигателя (engine_capacity) и тип транспортного средства, который будет обозначен как Car.

Мотоциклы:
Мощность двигателя более 150 лошадиных сил.
Объем двигателя менее 1,5 литров.
Цену менее 20 тысяч долларов.
В выводе должны быть указаны производитель (maker), номер модели (model), мощность (horsepower), объем двигателя (engine_capacity) и тип транспортного средства, который будет обозначен как Motorcycle.

Велосипеды:
Количество передач больше 18.
Цену менее 4 тысяч долларов.
В выводе должны быть указаны производитель (maker), номер модели (model), а также NULL для мощности и объема двигателя, так как эти характеристики не применимы для велосипедов. Тип транспортного средства будет обозначен как Bicycle.

Сортировка:
Результаты должны быть объединены в один набор данных и отсортированы по мощности в порядке убывания. Для велосипедов, у которых нет значения мощности, они будут располагаться внизу списка.*/
CREATE VIEW Task2 AS
SELECT
	V.maker,
	V.model,
	C.horsepower,
	C.engine_capacity,
	V."type" AS vehicle_type
FROM Vehicles V
JOIN Cars C USING (model)
WHERE C.horsepower > 150 AND C.engine_capacity < 3 AND C.price < 35000
UNION ALL
SELECT
	V.maker,
	V.model,
	M.horsepower,
	M.engine_capacity,
	V."type" AS vehicle_type
FROM Vehicles V
JOIN Motorcycles M USING (model)
WHERE M.horsepower > 150 AND M.engine_capacity < 1.5 AND M.price < 20000
UNION ALL
SELECT
	V.maker,
	V.model,
	NULL,
	NULL,
	V."type" AS vehicle_type
FROM Vehicles V
JOIN Bicycles B USING (model)
WHERE B.gear_count > 18 AND B.price < 4000
ORDER BY horsepower DESC NULLS LAST;