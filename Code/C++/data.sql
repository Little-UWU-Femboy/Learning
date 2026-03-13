-- =========================================
-- Dummy SQL File Covering Core Concepts
-- =========================================

-- 1. Create a Database
CREATE DATABASE DummyDB;
USE DummyDB;

-- 2. Create Tables with various data types and constraints
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY AUTO_INCREMENT,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    BirthDate DATE,
    HireDate DATETIME DEFAULT CURRENT_TIMESTAMP,
    Salary DECIMAL(10,2) CHECK (Salary >= 0),
    DepartmentID INT,
    Email VARCHAR(100) UNIQUE
);

CREATE TABLE Departments (
    DepartmentID INT PRIMARY KEY AUTO_INCREMENT,
    DepartmentName VARCHAR(100) NOT NULL,
    Location VARCHAR(100)
);

-- 3. Foreign Key Constraint
ALTER TABLE Employees
ADD CONSTRAINT FK_Dept
FOREIGN KEY (DepartmentID)
REFERENCES Departments(DepartmentID)
ON DELETE SET NULL;

-- 4. Insert Sample Data
INSERT INTO Departments (DepartmentName, Location)
VALUES ('HR', 'New York'), ('IT', 'San Francisco'), ('Finance', 'Chicago');

INSERT INTO Employees (FirstName, LastName, BirthDate, Salary, DepartmentID, Email)
VALUES
('Alice', 'Smith', '1990-05-01', 60000, 1, 'alice@example.com'),
('Bob', 'Johnson', '1985-08-12', 75000, 2, 'bob@example.com'),
('Charlie', 'Lee', '1992-11-20', 50000, 3, 'charlie@example.com');

-- 5. Select Queries and Joins
-- Basic Select
SELECT * FROM Employees;

-- Inner Join
SELECT e.FirstName, e.LastName, d.DepartmentName
FROM Employees e
INNER JOIN Departments d
ON e.DepartmentID = d.DepartmentID;

-- Left Join
SELECT e.FirstName, e.LastName, d.DepartmentName
FROM Employees e
LEFT JOIN Departments d
ON e.DepartmentID = d.DepartmentID;

-- 6. Aggregate Functions
SELECT DepartmentID, COUNT(*) AS NumEmployees, AVG(Salary) AS AvgSalary
FROM Employees
GROUP BY DepartmentID;

-- 7. Subqueries
SELECT FirstName, LastName, Salary
FROM Employees
WHERE Salary > (SELECT AVG(Salary) FROM Employees);

-- 8. Views
CREATE VIEW EmployeeDetails AS
SELECT e.FirstName, e.LastName, d.DepartmentName, e.Salary
FROM Employees e
LEFT JOIN Departments d
ON e.DepartmentID = d.DepartmentID;

-- 9. Index
CREATE INDEX idx_salary ON Employees(Salary);

-- 10. Stored Procedure
DELIMITER $$
CREATE PROCEDURE GetEmployeesByDept(IN dept INT)
BEGIN
    SELECT FirstName, LastName, Salary
    FROM Employees
    WHERE DepartmentID = dept;
END$$
DELIMITER ;

-- Call the stored procedure
CALL GetEmployeesByDept(2);

-- 11. Trigger
DELIMITER $$
CREATE TRIGGER before_employee_insert
BEFORE INSERT ON Employees
FOR EACH ROW
BEGIN
    IF NEW.Salary < 0 THEN
        SET NEW.Salary = 0;
    END IF;
END$$
DELIMITER ;

-- 12. Transactions
START TRANSACTION;

UPDATE Employees SET Salary = Salary + 5000 WHERE DepartmentID = 2;
-- Suppose something went wrong
ROLLBACK;

-- 13. Functions
DELIMITER $$
CREATE FUNCTION GetFullName(empID INT) RETURNS VARCHAR(100)
BEGIN
    DECLARE fullName VARCHAR(100);
    SELECT CONCAT(FirstName, ' ', LastName) INTO fullName
    FROM Employees
    WHERE EmployeeID = empID;
    RETURN fullName;
END$$
DELIMITER ;

-- 14. Using the Function
SELECT GetFullName(1) AS FullName;

-- 15. Drop Objects (cleanup)
-- DROP FUNCTION IF EXISTS GetFullName;
-- DROP TRIGGER IF EXISTS before_employee_insert;
-- DROP PROCEDURE IF EXISTS GetEmployeesByDept;
-- DROP VIEW IF EXISTS EmployeeDetails;
-- DROP TABLE IF EXISTS Employees;
-- DROP TABLE IF EXISTS Departments;
-- DROP DATABASE DummyDB;

