-- Код для PostgreSQL

--DROP TABLE Departments, Roles, Employees, Projects, Tasks;

-- Создание таблицы Departments
CREATE TABLE Departments(
    id_department INT GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1),
    department_name VARCHAR(100) NOT NULL,
    CONSTRAINT pk_departments_id PRIMARY KEY (id_department)
);

-- Создание таблицы Roles
CREATE TABLE Roles (
    id_role INT GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1),
    role_name VARCHAR(100) NOT NULL,
    CONSTRAINT pk_roles_id PRIMARY KEY (id_role)
);

-- Создание таблицы Employees
CREATE TABLE Employees (
    id_employee INT GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1),
    "name" VARCHAR(100) NOT NULL,
    "position" VARCHAR(100),
    id_manager INT,
    id_department INT,
    id_role INT,
    CONSTRAINT pk_employees_id PRIMARY KEY (id_employee),
    CONSTRAINT fk_id_manager FOREIGN KEY (id_manager) REFERENCES Employees(id_employee) ON DELETE SET NULL,
    CONSTRAINT fk_employees_id_department FOREIGN KEY (id_department) REFERENCES Departments(id_department) ON DELETE CASCADE,
    CONSTRAINT fk_id_role FOREIGN KEY (id_role) REFERENCES Roles(id_role) ON DELETE SET NULL
);

-- Создание таблицы Projects
CREATE TABLE Projects (
    id_project INT GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1),
    project_name VARCHAR(100) NOT NULL,
    start_date DATE,
    end_date DATE,
    id_department INT,
    CONSTRAINT pk_projects_id PRIMARY KEY (id_project),
    CONSTRAINT fk_projects_id_department FOREIGN KEY (id_department) REFERENCES Departments(id_department) ON DELETE CASCADE
);

-- Создание таблицы Tasks
CREATE TABLE Tasks (
    id_task INT GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1),
    task_name VARCHAR(100) NOT NULL,
    assigned_to INT,
    id_project INT,
    CONSTRAINT pk_tasks_id PRIMARY KEY (id_task),
    CONSTRAINT fk_assigned_to FOREIGN KEY (assigned_to) REFERENCES Employees(id_employee) ON DELETE SET NULL,
    CONSTRAINT fk_id_project FOREIGN KEY (id_project) REFERENCES Projects(id_project) ON DELETE CASCADE
);

-- Вставка данных в таблицу Departments
INSERT INTO Departments (department_name) VALUES
('Отдел продаж'),
('Отдел маркетинга'),
('IT-отдел'),
('Отдел разработки'),
('Отдел поддержки');

-- Вставка данных в таблицу Roles
INSERT INTO Roles (role_name) VALUES
('Менеджер'),
('Директор'),
('Генеральный директор'),
('Разработчик'),
('Специалист по поддержке'),
('Маркетолог');

-- Вставка данных в таблицу Employees
INSERT INTO Employees ("name", "position", id_manager, id_department, id_role) VALUES
('Иван Иванов', 'Генеральный директор', NULL, 1, 3),
('Петр Петров', 'Директор по продажам', 1, 1, 2),
('Светлана Светлова', 'Директор по маркетингу', 1, 2, 2),
('Алексей Алексеев', 'Менеджер по продажам', 2, 1, 1),
('Мария Мариева', 'Менеджер по маркетингу', 3, 2, 1),
('Андрей Андреев', 'Разработчик', 1, 4, 4),
('Елена Еленова', 'Специалист по поддержке', 1, 5, 5),
('Олег Олегов', 'Менеджер по продукту', 2, 1, 1),
('Татьяна Татеева', 'Маркетолог', 3, 2, 6),
('Николай Николаев', 'Разработчик', 6, 4, 4),
('Ирина Иринина', 'Разработчик', 6, 4, 4),
('Сергей Сергеев', 'Специалист по поддержке', 7, 5, 5),
('Кристина Кристинина', 'Менеджер по продажам', 4, 1, 1),
('Дмитрий Дмитриев', 'Маркетолог', 3, 2, 6),
('Виктор Викторов', 'Менеджер по продажам', 4, 1, 1),
('Анастасия Анастасиева', 'Специалист по поддержке', 7, 5, 5),
('Максим Максимов', 'Разработчик', 6, 4, 4),
('Людмила Людмилова', 'Специалист по маркетингу', 3, 2, 6),
('Наталья Натальева', 'Менеджер по продажам', 4, 1, 1),
('Александр Александров', 'Менеджер по маркетингу', 3, 2, 1),
('Галина Галина', 'Специалист по поддержке', 7, 5, 5),
('Павел Павлов', 'Разработчик', 6, 4, 4),
('Марина Маринина', 'Специалист по маркетингу', 3, 2, 6),
('Станислав Станиславов', 'Менеджер по продажам', 4, 1, 1),
('Екатерина Екатеринина', 'Специалист по поддержке', 7, 5, 5),
('Денис Денисов', 'Разработчик', 6, 4, 4),
('Ольга Ольгина', 'Маркетолог', 3, 2, 6),
('Игорь Игорев', 'Менеджер по продукту', 2, 1, 1),
('Анастасия Анастасиевна', 'Специалист по поддержке', 7, 5, 5),
('Валентин Валентинов', 'Разработчик', 6, 4, 4);

-- Вставка данных в таблицу Projects
INSERT INTO Projects (project_name, start_date, end_date, id_department) VALUES
('Проект A', '2025-01-01', '2025-12-31', 1),
('Проект B', '2025-02-01', '2025-11-30', 2),
('Проект C', '2025-03-01', '2025-10-31', 4),
('Проект D', '2025-04-01', '2025-09-30', 5),
('Проект E', '2025-05-01', '2025-08-31', 3);

-- Вставка данных в таблицу Tasks
INSERT INTO Tasks (task_name, assigned_to, id_project) VALUES
('Задача 1: Подготовка отчета по продажам', 4, 1),
('Задача 2: Анализ рынка', 9, 2),
('Задача 3: Разработка нового функционала', 10, 3),
('Задача 4: Поддержка клиентов', 12, 4),
('Задача 5: Создание рекламной кампании', 5, 2),
('Задача 6: Обновление документации', 6, 3),
('Задача 7: Проведение тренинга для сотрудников', 8, 1),
('Задача 8: Тестирование нового продукта', 11, 3),
('Задача 9: Ответы на запросы клиентов', 12, 4),
('Задача 10: Подготовка маркетинговых материалов', 9, 2),
('Задача 11: Интеграция с новым API', 10, 3),
('Задача 12: Настройка системы поддержки', 7, 5),
('Задача 13: Проведение анализа конкурентов', 9, 2),
('Задача 14: Создание презентации для клиентов', 4, 1),
('Задача 15: Обновление сайта', 6, 3);

/*Задача 1
Найти всех сотрудников, подчиняющихся Ивану Иванову (с EmployeeID = 1), включая их подчиненных и подчиненных подчиненных. Для каждого сотрудника вывести следующую информацию:

EmployeeID: идентификатор сотрудника.
Имя сотрудника.
ManagerID: Идентификатор менеджера.
Название отдела, к которому он принадлежит.
Название роли, которую он занимает.
Название проектов, к которым он относится (если есть, конкатенированные в одном столбце через запятую).
Название задач, назначенных этому сотруднику (если есть, конкатенированные в одном столбце через запятую).
Если у сотрудника нет назначенных проектов или задач, отобразить NULL.

Требования:
Рекурсивно извлечь всех подчиненных сотрудников Ивана Иванова и их подчиненных.
Для каждого сотрудника отобразить информацию из всех таблиц.
Результаты должны быть отсортированы по имени сотрудника.
Решение задачи должно представлять из себя один sql-запрос и задействовать ключевое слово RECURSIVE.*/
CREATE VIEW Task1 AS
WITH RECURSIVE IvanSubordinates AS (
    SELECT
        E.id_employee,
        E.name,
        E.id_manager
    FROM Employees E
    WHERE id_manager = 1  -- ID Ивана Иванова
    UNION ALL
    SELECT
        E.id_employee,
        E.name,
        E.id_manager
    FROM Employees E
    JOIN IvanSubordinates "IS" ON E.id_manager = "IS".id_employee
)
SELECT
    "IS".id_employee AS employee_id,
    "IS".name AS employee_name,
    "IS".id_manager AS manager_id,
    D.department_name,
    R.role_name,
    STRING_AGG(DISTINCT P.project_name, ', ') AS project_names,
    STRING_AGG(DISTINCT T.task_name, ', ') AS task_names
FROM IvanSubordinates "IS"
JOIN Employees E USING (id_employee)
JOIN Departments D USING (id_department)
JOIN Roles R USING (id_role)
LEFT JOIN Tasks T ON E.id_employee = T.assigned_to
LEFT JOIN Projects P USING (id_project)
GROUP BY "IS".id_employee, "IS".name, "IS".id_manager, D.department_name, R.role_name
ORDER BY "IS".name;

/*Задача 2
Найти всех сотрудников, подчиняющихся Ивану Иванову с EmployeeID = 1, включая их подчиненных и подчиненных подчиненных. Для каждого сотрудника вывести следующую информацию:

EmployeeID: идентификатор сотрудника.
Имя сотрудника.
Идентификатор менеджера.
Название отдела, к которому он принадлежит.
Название роли, которую он занимает.
Название проектов, к которым он относится (если есть, конкатенированные в одном столбце).
Название задач, назначенных этому сотруднику (если есть, конкатенированные в одном столбце).
Общее количество задач, назначенных этому сотруднику.
Общее количество подчиненных у каждого сотрудника (не включая подчиненных их подчиненных).
Если у сотрудника нет назначенных проектов или задач, отобразить NULL.*/
CREATE VIEW Task2 AS
WITH RECURSIVE Subordinates AS (
    SELECT
        E.id_employee,
        E.name,
        E.id_manager,
        E.id_department,
        E.id_role
    FROM Employees E
    WHERE E.id_manager = 1
    UNION ALL
    SELECT
        E.id_employee,
        E.name,
        E.id_manager,
        E.id_department,
        E.id_role
    FROM Employees E
    INNER JOIN Subordinates S ON E.id_manager = S.id_employee
)
SELECT
    S.id_employee AS employee_id,
    S.name AS employee_name,
    S.id_manager AS manager_id,
    D.department_name AS department_name,
    R.role_name AS role_name,
    STRING_AGG(DISTINCT P.project_name, ', ') AS project_names,
    STRING_AGG(DISTINCT T.task_name, ', ') AS task_names,
    COUNT(T.id_task) AS total_tasks,
    (SELECT COUNT(*) FROM Employees WHERE id_manager = S.id_employee) AS total_subordinates
FROM Subordinates S
JOIN Departments D USING (id_department)
JOIN Roles R USING (id_role)
LEFT JOIN Tasks T ON S.id_employee = T.assigned_to
LEFT JOIN Projects P USING (id_project)
GROUP BY S.id_employee, S.name, S.id_manager, D.department_name, R.role_name
ORDER BY S.name;

/*Задача 3
Найти всех сотрудников, которые занимают роль менеджера и имеют подчиненных (то есть число подчиненных больше 0). Для каждого такого сотрудника вывести следующую информацию:

EmployeeID: идентификатор сотрудника.
Имя сотрудника.
Идентификатор менеджера.
Название отдела, к которому он принадлежит.
Название роли, которую он занимает.
Название проектов, к которым он относится (если есть, конкатенированные в одном столбце).
Название задач, назначенных этому сотруднику (если есть, конкатенированные в одном столбце).
Общее количество подчиненных у каждого сотрудника (включая их подчиненных).
Если у сотрудника нет назначенных проектов или задач, отобразить NULL.*/
CREATE VIEW Task3 AS
WITH RECURSIVE Subordinates AS (
    SELECT
        E.id_employee,
        E.name,
        E.id_manager,
        E.id_department,
        E.id_role
    FROM Employees E
    WHERE id_manager IS NULL  --Начальные значения 
    UNION ALL
    SELECT
        E.id_employee,
        E.name,
        E.id_manager,
        E.id_department,
        E.id_role
    FROM Employees E
    INNER JOIN Subordinates S ON E.id_manager = S.id_employee
), manager_counts AS (
  SELECT
    E.id_manager,
    COUNT(*) as subordinate_count
  FROM Employees E
  GROUP BY id_manager
  HAVING COUNT(*) > 0
)
SELECT
    E.id_employee AS EmployeeID,
    E.name AS EmployeeName,
    E.id_manager AS ManagerID,
    D.department_name AS DepartmentName,
    R.role_name AS RoleName,
    STRING_AGG(DISTINCT P.project_name, ', ') AS ProjectNames,
    STRING_AGG(DISTINCT T.task_name, ', ') AS TaskNames,
    MC.subordinate_count as TotalSubordinates
FROM Employees E
JOIN Roles R USING (id_role)
JOIN Departments D USING (id_department)
JOIN manager_counts MC ON E.id_employee = MC.id_manager
LEFT JOIN Tasks T ON E.id_employee = T.assigned_to
LEFT JOIN Projects P USING (id_project)
WHERE R.role_name = 'Менеджер'
GROUP BY E.id_employee, E.name, E.id_manager, D.department_name, R.role_name, MC.subordinate_count
ORDER BY E.name;