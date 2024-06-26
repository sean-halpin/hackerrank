-- select * from employees;
select e.last_name, e.gender, count(emp_no) from employees as e
group by e.gender, e.last_name
having last_name ilike 'A%'
order by "count" desc, last_name asc