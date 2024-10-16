-- creates user 2 and database for it
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
Grant SELECT ON hbtn_0d_2 .* TO 'user_0d_2'@'localhost';
Flush privileges;