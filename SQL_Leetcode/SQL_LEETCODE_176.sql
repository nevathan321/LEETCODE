/* Solution 1 */
Select 
    MAX(salary) as SecondHighestSalary 
From Employee 
Where salary not in (Select MAX(salary) from Employee)

/* Solution 2 */
