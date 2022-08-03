/****************************** Problemática 2 ******************************/


/** Vista de clientes por edad**/
CREATE VIEW clientes_edad
AS
SELECT 
	customer_id,
	branch_id,
	customer_name,
	customer_surname,
	customer_DNI,
	CURRENT_DATE - strftime( dob ) as age
FROM cliente;

/** Clientes mayores de 40 por dni **/
SELECT customer_id,
	customer_name,
	customer_DNI,
	age
FROM clientes_edad
WHERE customer_name = 'Anne' OR customer_name = 'Tyler'
ORDER BY age ASC;

/** Anne o Tyler por edad **/
SELECT customer_id,
	customer_DNI,
	age
FROM clientes_edad
WHERE age > 40
ORDER BY customer_DNI ASC;

/** Insertar clientes del JSON **/
INSERT INTO cliente (customer_name, customer_surname, customer_DNI, branch_id, dob)
VALUES 	("Lois","Stout",47730534,80,"1984-07-07"),
		("Hall","Mcconell",52055464,45,"1968-04-30"),
		("Hilel","Mclean",43625213,77,"1993-03-28"),
		("Jin","Cooley",21207908,96,"1984-07-07"),
		("Gabriel","Harmon",57063950,27,"1976-04-01");
		
/** Verificar **/
SELECT customer_id, customer_name, customer_surname, customer_DNI, branch_id
FROM cliente
ORDER BY customer_id DESC
LIMIT 6;

/** Actualizar sucursal de últimos 5 **/
UPDATE cliente
SET branch_id = 10
WHERE customer_id > (SELECT MAX(customer_id) - 5 FROM cliente);

/** Eliminar a Noel David **/
/*Prueba para añadir a Noel David
INSERT INTO cliente (customer_name, customer_surname, customer_DNI, branch_id, dob)
VALUES 	("Noel","David",47730534,80,"1984-07-07");
*/
DELETE FROM cliente
WHERE customer_name = 'Noel' AND customer_surname = 'David';

/** Tipo de prestamo de mayor importe **/
SELECT loan_type FROM (
	SELECT loan_type, SUM(CAST(replace(loan_total, substr(loan_total, -2, 2), '.'||substr(loan_total, -2, 2)) AS DECIMAL)) AS importe_total
	FROM prestamo
	WHERE loan_type = 'PERSONAL'
	UNION
	SELECT loan_type, SUM(CAST(replace(loan_total, substr(loan_total, -2, 2), '.'||substr(loan_total, -2, 2)) AS DECIMAL)) AS importe_total
	FROM prestamo
	WHERE loan_type = 'PRENDARIO'
	UNION
	SELECT loan_type, SUM(CAST(replace(loan_total, substr(loan_total, -2, 2), '.'||substr(loan_total, -2, 2)) AS DECIMAL)) AS importe_total
	FROM prestamo
	WHERE loan_type = 'HIPOTECARIO'
	ORDER BY importe_total DESC
	LIMIT 1
);