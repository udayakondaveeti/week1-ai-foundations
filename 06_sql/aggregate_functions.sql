-- Aggregate functions
SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department;

SELECT MAX(salary) AS highest_salary, MIN(salary) AS lowest_salary
FROM employees;
