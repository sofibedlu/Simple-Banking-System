-- creating a db 'sbs_dev_db' if not exist
CREATE DATABASE IF NOT EXISTS sbs_dev_db;
-- selecting the database
USE sbs_dev_db;
-- creating a user 'sbs_dev'
CREATE USER IF NOT EXISTS 'sbs_dev'@'localhost' IDENTIFIED BY 'sbs_dev_pwd';
-- granting privilages
GRANT ALL PRIVILEGES ON sbs_dev_db.* TO 'sbs_dev'@'localhost' WITH GRANT OPTION;
GRANT SELECT ON performance_schema.* TO 'sbs_dev'@'localhost';
-- reloading the grant table
FLUSH PRIVILEGES;
