/*
	Find employees and their managers/
*/
select
	a.employeeNumber, a.lastName, a.firstName, 
    b.employeeNumber as managerNumber, 
		b.lastName as managerLastName, 
			b.firstName as managerFirstName
from employees as a join employees as b
on a.reportsTo=b.employeeNumber
	where (a.lastName='Bow' or a.lastName='Patterson'); 

/*
	Find employees and their manager's manager.
*/
select
	a.employeeNumber, a.lastName, a.firstName,
    c.employeeNumber as managerMangerNumber, 
		c.lastName as managerManagerLastName,
    c.firstName as managerManagerFirstName
from 
	(employees as a join employees as b 
		on a.reportsTo=b.employeeNumber) 
join
	employees as c on b.reportsTo=c.employeeNumber
where a.lastName='Bow'  or a.lastName='Patterson';
