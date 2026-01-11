
/* Solution 2 but more optimized */
/* Using LEFT JOIN to find employees without managers directly, form of self - join */

SELECT e1.employee_id
FROM Employees e1
LEFT JOIN Employees e2
ON e1.manager_id = e2.employee_id
WHERE e1.salary < 30000 AND e2.employee_id IS NULL AND e1.manager_id IS NOT NULL
ORDER BY employee_id; 


/* Solution 1 I want to find the employee who has a manager_id that is not in the employee id column */


Select 
    employee_id 
From Employees 
Where manager_id not in (
    Select employee_id 
    From Employees 
) AND salary < 30000 
Order by employee_id ASC 