-- 1. Lookup table for Device Types
CREATE TABLE device_types (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE
);

-- 2. Lookup table for Brands
CREATE TABLE brands (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE
);

-- 3. Lookup table for Error Types
CREATE TABLE error_types (
    id INT AUTO_INCREMENT PRIMARY KEY,
    error_name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT
);

-- 4. Main table for Correct Data (Devices)
CREATE TABLE devices (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    device_type_id INT NOT NULL,
    brand_id INT NOT NULL,
    serial_number VARCHAR(255) NOT NULL UNIQUE,
    FOREIGN KEY (device_type_id) REFERENCES device_types(id) ON DELETE RESTRICT,
    FOREIGN KEY (brand_id) REFERENCES brands(id) ON DELETE RESTRICT
);

-- 5. Table for Tracking Error Data & Logging
CREATE TABLE import_errors (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    line_number INT NOT NULL,
    error_type_id INT NOT NULL,
    raw_line_data TEXT NOT NULL,
    occurred_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (error_type_id) REFERENCES error_types(id) ON DELETE RESTRICT
);
