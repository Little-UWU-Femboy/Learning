CREATE DATABASE IF NOT EXISTS ResourceManagement;
USE ResourceManagement;

CREATE TABLE IF NOT EXISTS accounts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(10) NOT NULL,
    password VARCHAR(24) NOT NULL
);

INSERT INTO accounts (username, password) VALUES
('User', '2k@NLxoktB!pT[!T'),
('root', 'ROOT');

CREATE TABLE IF NOT EXISTS device_type (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(64) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS device_brand (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(64) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS processed_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    device_type_id INT NOT NULL,
    device_brand_id INT NOT NULL,
    serial_number VARCHAR(67) NOT NULL UNIQUE,
    time_written DATETIME NOT NULL,
    FOREIGN KEY (device_type_id) REFERENCES device_type(id) ON DELETE CASCADE,
    FOREIGN KEY (device_brand_id) REFERENCES device_brand(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS error_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    actual_row_data TEXT NOT NULL,
    error_type VARCHAR(100) NOT NULL,
    line_number INT NOT NULL,
    time_occurred DATETIME NOT NULL
);
