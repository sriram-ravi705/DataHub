-- Create the database if it doesn't already exist
CREATE DATABASE IF NOT EXISTS exampledb;

-- Use the database
USE exampledb;

-- Create the user 'admin' with full privileges, allowing connection from any host
CREATE USER IF NOT EXISTS 'admin'@'%' IDENTIFIED BY 'admin';

-- Grant privileges to 'admin' on 'exampledb'
GRANT ALL PRIVILEGES ON exampledb.* TO 'admin'@'%';

-- Flush privileges to apply changes
FLUSH PRIVILEGES;

-- Create the table if it doesn't already exist
CREATE TABLE IF NOT EXISTS test_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255)
);

-- Insert a record into the test_table if it doesn't exist
INSERT INTO test_table (name) VALUES ('Test Record');