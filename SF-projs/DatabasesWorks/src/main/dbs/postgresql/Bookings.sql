-- Код для PostgreSQL

--DROP TABLE Hotels, Rooms, Customers, Bookings;
--DROP TYPE rooms_type;

--CREATE TYPE rooms_type AS ENUM('Single', 'Double', 'Suite');

-- Создание таблицы Hotels
CREATE TABLE Hotels (
    id_hotel INT GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1),
    "name" VARCHAR(255) NOT NULL,
    location VARCHAR(255) NOT NULL,
    CONSTRAINT pk_hotels_id PRIMARY KEY (id_hotel)
);

-- Создание таблицы Rooms
CREATE TABLE Rooms (
    id_room INT GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1),
    id_hotel INT,
    room_type VARCHAR(20) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    capacity INT NOT NULL,
    CONSTRAINT pk_rooms_id PRIMARY KEY (id_room),
    CONSTRAINT fk_rooms_id_hotel FOREIGN KEY (id_hotel) REFERENCES Hotels(id_hotel),
    CONSTRAINT check_rooms_room_type CHECK (room_type IN ('Single', 'Double', 'Suite'))
);

-- Создание таблицы Customers
CREATE TABLE Customers (
    id_customer INT GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1),
    "name" VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL,
    CONSTRAINT pk_customers_id PRIMARY KEY (id_customer)
);

-- Создание таблицы Bookings
CREATE TABLE Bookings (
    id_booking INT GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1),
    id_room INT,
    id_customer INT,
    check_in_date DATE NOT NULL,
    check_out_date DATE NOT NULL,
    CONSTRAINT pk_bookings_id PRIMARY KEY (id_booking),
    CONSTRAINT fk_bookings_id_room FOREIGN KEY (id_room) REFERENCES Rooms(id_room),
    CONSTRAINT fk_bookings_id_customer FOREIGN KEY (id_customer) REFERENCES Customers(id_customer)
);

-- Вставка данных в таблицу Hotels
INSERT INTO Hotels ("name", "location") VALUES
('Grand Hotel', 'Paris, France'),
('Ocean View Resort', 'Miami, USA'),
('Mountain Retreat', 'Aspen, USA'),
('City Center Inn', 'New York, USA'),
('Desert Oasis', 'Las Vegas, USA'),
('Lakeside Lodge', 'Lake Tahoe, USA'),
('Historic Castle', 'Edinburgh, Scotland'),
('Tropical Paradise', 'Bali, Indonesia'),
('Business Suites', 'Tokyo, Japan'),
('Eco-Friendly Hotel', 'Copenhagen, Denmark');

-- Вставка данных в таблицу Rooms
INSERT INTO Rooms (id_hotel, room_type, price, capacity) VALUES
(1, 'Single', 150.00, 1),
(1, 'Double', 200.00, 2),
(1, 'Suite', 350.00, 4),
(2, 'Single', 120.00, 1),
(2, 'Double', 180.00, 2),
(2, 'Suite', 300.00, 4),
(3, 'Double', 250.00, 2),
(3, 'Suite', 400.00, 4),
(4, 'Single', 100.00, 1),
(4, 'Double', 150.00, 2),
(5, 'Single', 90.00, 1),
(5, 'Double', 140.00, 2),
(6, 'Suite', 280.00, 4),
(7, 'Double', 220.00, 2),
(8, 'Single', 130.00, 1),
(8, 'Double', 190.00, 2),
(9, 'Suite', 360.00, 4),
(10, 'Single', 110.00, 1),
(10, 'Double', 160.00, 2);

-- Вставка данных в таблицу Customers
INSERT INTO Customers ("name", email, phone) VALUES
('John Doe', 'john.doe@example.com', '+1234567890'),
('Jane Smith', 'jane.smith@example.com', '+0987654321'),
('Alice Johnson', 'alice.johnson@example.com', '+1122334455'),
('Bob Brown', 'bob.brown@example.com', '+2233445566'),
('Charlie White', 'charlie.white@example.com', '+3344556677'),
('Diana Prince', 'diana.prince@example.com', '+4455667788'),
('Ethan Hunt', 'ethan.hunt@example.com', '+5566778899'),
('Fiona Apple', 'fiona.apple@example.com', '+6677889900'),
('George Washington', 'george.washington@example.com', '+7788990011'),
('Hannah Montana', 'hannah.montana@example.com', '+8899001122');

-- Вставка данных в таблицу Bookings
INSERT INTO Bookings (id_room, id_customer, check_in_date, check_out_date) VALUES
(1, 1, '2025-05-01', '2025-05-05'),  -- 4 ночи, John Doe
(2, 2, '2025-05-02', '2025-05-06'),  -- 4 ночи, Jane Smith
(3, 3, '2025-05-03', '2025-05-07'),  -- 4 ночи, Alice Johnson
(4, 4, '2025-05-04', '2025-05-08'),  -- 4 ночи, Bob Brown
(5, 5, '2025-05-05', '2025-05-09'),  -- 4 ночи, Charlie White
(6, 6, '2025-05-06', '2025-05-10'),  -- 4 ночи, Diana Prince
(7, 7, '2025-05-07', '2025-05-11'),  -- 4 ночи, Ethan Hunt
(8, 8, '2025-05-08', '2025-05-12'),  -- 4 ночи, Fiona Apple
(9, 9, '2025-05-09', '2025-05-13'),  -- 4 ночи, George Washington
(10, 10, '2025-05-10', '2025-05-14'),  -- 4 ночи, Hannah Montana
(1, 2, '2025-05-11', '2025-05-15'),  -- 4 ночи, Jane Smith
(2, 3, '2025-05-12', '2025-05-14'),  -- 2 ночи, Alice Johnson
(3, 4, '2025-05-13', '2025-05-15'),  -- 2 ночи, Bob Brown
(4, 5, '2025-05-14', '2025-05-16'),  -- 2 ночи, Charlie White
(5, 6, '2025-05-15', '2025-05-16'),  -- 1 ночь, Diana Prince
(6, 7, '2025-05-16', '2025-05-18'),  -- 2 ночи, Ethan Hunt
(7, 8, '2025-05-17', '2025-05-21'),  -- 4 ночи, Fiona Apple
(8, 9, '2025-05-18', '2025-05-19'),  -- 1 ночь, George Washington
(9, 10, '2025-05-19', '2025-05-22'),  -- 3 ночи, Hannah Montana
(10, 1, '2025-05-20', '2025-05-22'), -- 2 ночи, John Doe
(1, 2, '2025-05-21', '2025-05-23'),  -- 2 ночи, Jane Smith
(2, 3, '2025-05-22', '2025-05-25'),  -- 3 ночи, Alice Johnson
(3, 4, '2025-05-23', '2025-05-26'),  -- 3 ночи, Bob Brown
(4, 5, '2025-05-24', '2025-05-25'),  -- 1 ночь, Charlie White
(5, 6, '2025-05-25', '2025-05-27'),  -- 2 ночи, Diana Prince
(6, 7, '2025-05-26', '2025-05-29');  -- 3 ночи, Ethan Hunt

/*Задача 1
Определить, какие клиенты сделали более двух бронирований в разных отелях, и вывести информацию о каждом таком клиенте, включая его имя, электронную почту, телефон, общее количество бронирований, а также список отелей, в которых они бронировали номера (объединенные в одно поле через запятую с помощью CONCAT). Также подсчитать среднюю длительность их пребывания (в днях) по всем бронированиям. Отсортировать результаты по количеству бронирований в порядке убывания.*/
CREATE VIEW Task1 AS
WITH CustomerBookings AS (
    SELECT
        C.name AS customer_name,
        C.email,
        C.phone,
        COUNT(*) AS total_bookings,
        STRING_AGG(DISTINCT h.name, ', ') AS hotels_booked,
        AVG(CAST(B.check_out_date - b.check_in_date AS INTEGER)) AS avg_stay_days
    FROM Customers C
    JOIN Bookings B USING (id_customer)
    JOIN Rooms R USING (id_room)
    JOIN Hotels H USING (id_hotel)
    GROUP BY C.name, C.email, C.phone
    HAVING COUNT(DISTINCT H.id_hotel) > 1 AND COUNT(*) > 2
)
SELECT
    customer_name,
    email,
    phone,
    total_bookings,
    hotels_booked,
    avg_stay_days
FROM CustomerBookings
ORDER BY total_bookings DESC;

/*Задача 2
Необходимо провести анализ клиентов, которые сделали более двух бронирований в разных отелях и потратили более 500 долларов на свои бронирования. Для этого:

Определить клиентов, которые сделали более двух бронирований и забронировали номера в более чем одном отеле. Вывести для каждого такого клиента следующие данные: ID_customer, имя, общее количество бронирований, общее количество уникальных отелей, в которых они бронировали номера, и общую сумму, потраченную на бронирования.

Также определить клиентов, которые потратили более 500 долларов на бронирования, и вывести для них ID_customer, имя, общую сумму, потраченную на бронирования, и общее количество бронирований.

В результате объединить данные из первых двух пунктов, чтобы получить список клиентов, которые соответствуют условиям обоих запросов. Отобразить поля: ID_customer, имя, общее количество бронирований, общую сумму, потраченную на бронирования, и общее количество уникальных отелей.
Результаты отсортировать по общей сумме, потраченной клиентами, в порядке возрастания.*/
CREATE VIEW Task2 AS
WITH CustomerBookings AS (
    SELECT
        C.id_customer,
        C.name,
        COUNT(*) AS total_bookings,
        COUNT(DISTINCT H.id_hotel) AS unique_hotels,
        SUM(R.price) AS total_spent
    FROM Customers C
    JOIN Bookings B USING (id_customer)
    JOIN Rooms R USING (id_room)
    JOIN Hotels H USING (id_hotel)
    GROUP BY C.id_customer, C.name
    HAVING COUNT(*) > 2 AND COUNT(DISTINCT H.id_hotel) > 1
),
HighSpenders AS (
    SELECT
        C.id_customer,
        C.name,
        SUM(r.price) AS total_spent,
        COUNT(*) AS total_bookings
    FROM Customers C
    JOIN Bookings B USING (id_customer)
    JOIN Rooms R USING (id_room)
    GROUP BY C.id_customer, C.name
    HAVING SUM(R.price) > 500
)
SELECT
    CB.id_customer,
    CB.name,
    CB.total_bookings,
    CB.total_spent,
    CB.unique_hotels
FROM CustomerBookings CB
WHERE CB.id_customer IN (SELECT id_customer FROM HighSpenders);

/*Задача 3
Вам необходимо провести анализ данных о бронированиях в отелях и определить предпочтения клиентов по типу отелей. Для этого выполните следующие шаги:
	
Категоризация отелей.
Определите категорию каждого отеля на основе средней стоимости номера:
«Дешевый»: средняя стоимость менее 175 долларов.
«Средний»: средняя стоимость от 175 до 300 долларов.
«Дорогой»: средняя стоимость более 300 долларов.

Анализ предпочтений клиентов.
Для каждого клиента определите предпочитаемый тип отеля на основании условия ниже:
Если у клиента есть хотя бы один «дорогой» отель, присвойте ему категорию «дорогой».
Если у клиента нет «дорогих» отелей, но есть хотя бы один «средний», присвойте ему категорию «средний».
Если у клиента нет «дорогих» и «средних» отелей, но есть «дешевые», присвойте ему категорию предпочитаемых отелей «дешевый».

Вывод информации.
Выведите для каждого клиента следующую информацию:
ID_customer: уникальный идентификатор клиента.
name: имя клиента.
preferred_hotel_type: предпочитаемый тип отеля.
visited_hotels: список уникальных отелей, которые посетил клиент.

Сортировка результатов.
Отсортируйте клиентов так, чтобы сначала шли клиенты с «дешевыми» отелями, затем со «средними» и в конце — с «дорогими».*/
CREATE VIEW Task3 AS
WITH HotelCategories AS (
    SELECT
        H.id_hotel,
        H.name as hotel_name,
        CASE
            WHEN AVG(R.price) < 175 THEN 'Дешевый'
            WHEN AVG(R.price) BETWEEN 175 AND 300 THEN 'Средний'
            ELSE 'Дорогой'
        END AS hotel_category
    FROM Hotels H
    JOIN Rooms R USING (id_hotel)
    GROUP BY H.id_hotel, H.name
),
CustomerHotelPreferences AS (
    SELECT
        C.id_customer,
        C.name,
        MAX(CASE WHEN HC.hotel_category = 'Дорогой' THEN 'Дорогой'
                 WHEN HC.hotel_category = 'Средний' THEN 'Средний'
                 ELSE 'Дешевый' END) AS preferred_hotel_type,
        array_to_string(ARRAY_AGG(DISTINCT HC.hotel_name), ', ') AS visited_hotels
    FROM Customers C
    JOIN Bookings B USING (id_customer)
    JOIN Rooms R USING (id_room)
    JOIN Hotels H USING (id_hotel)
    JOIN HotelCategories HC USING (id_hotel)
    GROUP BY C.id_customer, C.name
)
SELECT
    id_customer,
    name,
    preferred_hotel_type,
    visited_hotels
FROM CustomerHotelPreferences
ORDER BY 
    CASE preferred_hotel_type
        WHEN 'Дешевый' THEN 1
        WHEN 'Средний' THEN 2
        ELSE 3
    END, id_customer;