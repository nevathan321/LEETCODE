Select 
    IF(id = (Select Max(id) from Seat) AND id % 2 = 1, 
    id, 
    IF(id % 2 = 0 , id - 1, id + 1) ) 
    as id, 
    student 
From Seat 
Order by id ASC 