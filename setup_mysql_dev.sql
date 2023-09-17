-- creates new user and new database.
-- grants all privileges for user on the database created.
-- save the privileges.
CREATE DATABASE 'hbnb_dev_db';
CREATE USER 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON 'hbnb_dev_db'.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
