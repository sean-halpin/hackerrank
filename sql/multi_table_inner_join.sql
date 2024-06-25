explain select * from employees as e
	INNER JOIN salaries as s ON e.emp_no = s.emp_no
	INNER JOIN titles as t ON s.emp_no = t.emp_no AND t.from_date = (s.from_date + interval '2 days')
ORDER BY e.emp_no

-- select * from titles
-- select * from salaries