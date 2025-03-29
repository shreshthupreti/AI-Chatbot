CREATE DATABASE learning_platform;
USE learning_platform;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL,
    role VARCHAR(50) NOT NULL
);

CREATE TABLE progress (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    course_name VARCHAR(255),
    status VARCHAR(50) DEFAULT 'Not Started',
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

