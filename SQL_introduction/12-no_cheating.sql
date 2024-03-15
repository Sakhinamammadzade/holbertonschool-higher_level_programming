-- updates the score of Bob to 10
UPDATE second_table 
SET score = REPLACE(score, 14, 10) 
WHERE 
	name = 'Bob';
