-- Query all employees
SELECT * FROM employees;

-- Query employees in Engineering
SELECT name, department, salary
FROM employees
WHERE department = 'Engineering';
