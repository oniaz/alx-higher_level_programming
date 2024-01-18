-- lists score and name for all records of the table second_table where name value isn't null, sorted by descending order. 
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
