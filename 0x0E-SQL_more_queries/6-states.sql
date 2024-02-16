-- task 6
-- Creating the database 'hbtn_0d_usa' with table 'states'
-- 'states' table has the fields:
--      'id' - INT unique, auto generated, not null and is a primary key.
--      'name' - VARCHAR(256) not null.

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
    id INT AUTO_INCREMENT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
