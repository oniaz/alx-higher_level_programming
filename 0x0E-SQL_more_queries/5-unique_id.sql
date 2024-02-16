-- task 5
-- Creating the table 'unique_id' with the fields 'id' - which is unique and has a default value of 1, and 'name'.

CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1,
    name VARCHAR(256),
    UNIQUE (id)
);
