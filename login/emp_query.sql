SELECT EMP.*
	,DEP.dept_name		dept_name
	,CUR.from_date		cur_dept_start_date
	,TTL.title
	,SAL.salary
	,Concat(MGR.last_name, ', ', MGR.first_name) manager
	,MGR.emp_no			mgr_emp_no
FROM employees 					EMP
INNER JOIN salaries				SAL ON EMP.emp_no = SAL.emp_no AND SAL.to_date = '9999-01-01'
INNER JOIN titles					TTL ON EMP.emp_no = TTL.emp_no AND TTL.to_date = '9999-01-01'
INNER JOIN current_dept_emp 	CUR ON EMP.emp_no = CUR.emp_no
INNER JOIN departments 			DEP ON CUR.dept_no = DEP.dept_no
INNER JOIN dept_manager 		DPM ON CUR.dept_no = DPM.dept_no AND DPM.to_date = '9999-01-01'
INNER JOIN employees				MGR ON DPM.emp_no = MGR.emp_no
WHERE EMP.first_name Like '%Facello%' 
	OR EMP.last_name Like '%Facello%';