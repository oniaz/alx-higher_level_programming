-- task 7
-- Creating the database 'hbtn_0d_usa' with table 'cities'
-- 'cities' table has the fields:
--      'id' - INT unique, auto generated, not null and is a primary key.
--      'state_id' - INT, not null, is a FOREIGN KEY that references to id of the 'states' table.
--      'name' - VARCHAR(256) not null.

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
    id INT AUTO_INCREMENT NOT NULL,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (state_id) REFERENCES states(id)
);
