Select 
    MAX(salary) as SecondHighestSalary 
From Employee 
Where salary not in (Select MAX(salary) from Employee)