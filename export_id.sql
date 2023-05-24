SELECT id, name
FROM states
ORDER BY name
INTO OUTFILE 'states_id.csv'
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
ESCAPED BY '' LINES TERMINATED BY '\n';