-- Код для PostgreSQL

-- Создание типов данных для перечислений
CREATE TYPE vehicle_type AS ENUM('Car', 'Motorcycle', 'Bicycle');
CREATE TYPE transmission_type AS ENUM('Automatic', 'Manual');
CREATE TYPE motorcycle_type AS ENUM('Sport', 'Cruiser', 'Touring');
CREATE TYPE bicycle_type AS ENUM('Mountain', 'Road', 'Hybrid');

-- Создание таблицы Vehicles
CREATE TABLE Vehicles (
    maker VARCHAR(100) NOT NULL,
    model VARCHAR(100) NOT NULL,
    "type" vehicle_type NOT NULL,
    CONSTRAINT pk_vehicle_model PRIMARY KEY (model)
);

-- Создание таблицы Cars
CREATE TABLE Cars (
    vin VARCHAR(17) NOT NULL,
    model VARCHAR(100) NOT NULL,
    engine_capacity DECIMAL(4, 2) NOT NULL,
    horsepower INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    transmission transmission_type NOT NULL,
    CONSTRAINT pk_car_vin PRIMARY KEY (vin),
    CONSTRAINT fk_car_model FOREIGN KEY (model) REFERENCES Vehicles(model)
);

-- Создание таблицы Motorcycles
CREATE TABLE Motorcycles (
    vin VARCHAR(17) NOT NULL,
    model VARCHAR(100) NOT NULL,
    engine_capacity DECIMAL(4, 2) NOT NULL,
    horsepower INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    type motorcycle_type NOT NULL,
    CONSTRAINT pk_motorcycle_vin PRIMARY KEY (vin),
    CONSTRAINT fk_motorcycle_model FOREIGN KEY (model) REFERENCES Vehicles(model)
);

-- Создание таблицы Bicycles
CREATE TABLE Bicycles (
    serial_number VARCHAR(20) NOT NULL,
    model VARCHAR(100) NOT NULL,
    gear_count INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    type bicycle_type NOT NULL,
    CONSTRAINT pk_bicycle_serial_number PRIMARY KEY (serial_number),
    CONSTRAINT fk_bicycle_model FOREIGN KEY (model) REFERENCES Vehicles(model)
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