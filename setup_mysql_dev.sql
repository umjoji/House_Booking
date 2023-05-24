-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS house_finder_db;
CREATE USER IF NOT EXISTS 'house_finder_dev'@'localhost' IDENTIFIED BY 'house_finder_user_pwd';
GRANT ALL PRIVILEGES ON `house_finder_db`.* TO 'house_finder_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'house_finder_dev'@'localhost';
FLUSH PRIVILEGES;
