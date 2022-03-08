-- List all record of the table second_table of the database hbtn_0c_0
-- print only rows with a name value order by score
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC;
