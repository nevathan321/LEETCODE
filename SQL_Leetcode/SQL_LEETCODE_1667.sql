Select 
    user_id, 
    CONCAT(UPPER(LEFT(name, 1)), LOWER(SUBSTRING(name, 2))) As name 
From Users 
Order by user_id
