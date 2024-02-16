-- task 4 
-- Creating the table 'id_not_null' with the fields 'id' - which has a default value of 1, and 'name'.

CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);

