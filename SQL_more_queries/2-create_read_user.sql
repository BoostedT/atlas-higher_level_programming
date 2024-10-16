-- creates user 2 and database for it
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
CREATE DATABASE IF NOT EXISTS user_0d_2_db;
Grant all privileges on user_0d_2_db.* to 'user_0d_2'@'localhost';

-- connects to user 2's database
USE user_0d_2_db;