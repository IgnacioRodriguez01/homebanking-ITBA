/****************************** Problemática 3 ******************************/


/** Saldos negativos **/ 
SELECT account_id, balance 
FROM cuenta
WHERE balance < 0;

/** Apellido con Z **/
SELECT 	customer_name,
		customer_surname,
		CURRENT_DATE - strftime( dob ) as age
FROM cliente
WHERE customer_surname LIKE '%z%';

/** Brendan por sucursal **/
SELECT 	customer_name,
		customer_surname,
		CURRENT_DATE - strftime( dob ) as age,
		sucursal.branch_name
FROM cliente
LEFT JOIN sucursal ON cliente.branch_id = sucursal.branch_id
WHERE customer_name = 'Brendan'
ORDER BY branch_name;

/** Prestamos de más de 80k + Prendarios **/
SELECT 	loan_id,
		CAST(replace(loan_total, substr(loan_total, -2, 2), '.'||substr(loan_total, -2, 2)) AS DECIMAL) AS loan_float,
		loan_type
FROM prestamo
WHERE loan_float > 80000
UNION
SELECT 	loan_id,
		CAST(replace(loan_total, substr(loan_total, -2, 2), '.'||substr(loan_total, -2, 2)) AS DECIMAL) AS loan_float,
		loan_type
FROM prestamo
WHERE loan_type = 'PRENDARIO';

/** Prestamos mayores al promedio **/
SELECT loan_id,
		CAST(replace(loan_total, substr(loan_total, -2, 2), '.'||substr(loan_total, -2, 2)) AS DECIMAL) AS loan_float,
		loan_type
FROM prestamo
GROUP BY loan_id
HAVING loan_float >= (
	SELECT avg(loan_float)
	FROM prestamo
);

/** Clientes menores de 50 **/
SELECT count(age)
FROM (
	SELECT (CURRENT_DATE - strftime( dob ) as age
	FROM cliente
	WHERE age < 50
);