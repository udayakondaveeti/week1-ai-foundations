-- Example join query using a second table
CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(100)
);

INSERT INTO departments (department_id, department_name) VALUES
(1, 'Engineering'),
(2, 'Sales'),
(3, 'Marketing');

SELECT e.name, e.department, d.department_name
FROM employees e
JOIN departments d ON e.department = d.department_name;
