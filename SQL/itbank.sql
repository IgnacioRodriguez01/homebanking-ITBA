/****************************** Problemática 1 ******************************/


/** Crear tablas **/

CREATE TABLE tipos_cliente( /*Black, Gold, Classic*/
	tipo_id INTEGER PRIMARY KEY,
	tipo_name TEXT NOT NULL
);
INSERT INTO tipos_cliente (tipo_name)
VALUES ('Black'), ('Gold'), ('Classic');

CREATE TABLE tipos_cuenta( /*Corriente, Dolares, Ahorro*/
	tipo_id INTEGER PRIMARY KEY,
	tipo_name TEXT NOT NULL
);
INSERT INTO tipos_cuenta (tipo_name)
VALUES ('Corriente'), ('Dólares'), ('Ahorro');

CREATE TABLE marcas_tarjeta( /*VISA, Mastercard, Amex, Cabal*/
	marca_id INTEGER PRIMARY KEY,
	marca_name TEXT NOT NULL
);
INSERT INTO marcas_tarjeta (marca_name)
VALUES ('VISA'), ('Mastercard'), ('Amex'), ('Cabal');

CREATE TABLE tarjetas(
	numero TEXT NOT NULL PRIMARY KEY CHECK (length(numero) <= 16),
	tipo TEXT NOT NULL,
	marca_id INTEGER NOT NULL,
	cvv INTEGER NOT NULL CHECK (length(cvv) = 3),
	fecha_emision TEXT NOT NULL,
	fecha_vto TEXT NOT NULL,
	cliente_id INTEGER NOT NULL,
	FOREIGN KEY(cliente_id) 
	REFERENCES cliente(customer_id),
	FOREIGN KEY (marca_id)
	REFERENCES marcas_tarjeta(marca_id)
);
/* Aquí agregar datos desde data-tarjetas */

CREATE TABLE direcciones(
	--id primary? foreigns?
	calle TEXT NOT NULL,
	numero INTEGER NOT NULL,
	ciudad TEXT NOT NULL,
	provincia TEXT NOT NULL,
	pais TEXT NOT NULL
);
/* Aquí agregar datos desde data-direcciones */

/** Añadir el tipo de cuenta a cuenta **/

ALTER TABLE cuenta
ADD COLUMN tipo_cuenta INTEGER NOT NULL DEFAULT 0;

UPDATE cuenta
SET tipo_cuenta = max(1, abs(random() % 4)) --Numero aleatorio entre 1 y 3
WHERE tipo_cuenta = 0;

/** Convertir formato de fecha de employee_hire_date **/

UPDATE empleado
SET employee_hire_date = DATE(substr(employee_hire_date,7,4)
	||'-'
	||substr(employee_hire_date,4,2)
	||'-'
	||substr(employee_hire_date,1,2))
WHERE employee_hire_date LIKE '__/__/%';


/****************************** Problemática 2 ******************************/


CREATE VIEW clientes_edad
AS
SELECT 
	customer_id,
	branch_id,
	customer_name,
	customer_surname,
	customer_DNI,
	CURRENT_DATE - strftime( dob ) as edad
FROM cliente


/****************************** Problemática 3 ******************************/


/** Saldos negativos **/ 
SELECT account_id, balance 
FROM cuenta
WHERE balance < 0;

/** Apellido con Z **/
SELECT 	customer_name,
		customer_surname,
		(strftime('%Y', 'now') - strftime('%Y', dob)) - (strftime('%m-%d', 'now') < strftime('%m-%d', dob)) AS age
FROM cliente
WHERE customer_surname LIKE '%z%';

/** Brendan por sucursal **/
SELECT 	customer_name,
		customer_surname,
		(strftime('%Y', 'now') - strftime('%Y', dob)) - (strftime('%m-%d', 'now') < strftime('%m-%d', dob)) AS age,
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
	SELECT (strftime('%Y', 'now') - strftime('%Y', dob)) - (strftime('%m-%d', 'now') < strftime('%m-%d', dob)) AS age
	FROM cliente
	WHERE age < 50
);


/****************************** Problemática 4 ******************************/


/** Cantidad de clientes por sucursal mayor a menor **/

SELECT branch_name, COUNT(cliente.customer_id) as cant_clientes
FROM sucursal
LEFT JOIN cliente on sucursal.branch_id = cliente.branch_id
GROUP BY sucursal.branch_name
ORDER BY cant_clientes DESC

/** Cantidad de empleados por cliente por sucursal **/

SELECT sucursal.branch_name, empleado.employee_id, cliente.customer_id
FROM empleado, sucursal, cliente
WHERE empleado.branch_id = sucursal.branch_id
AND cliente.branch_id = sucursal.branch_id
GROUP BY sucursal.branch_name


/****************************** Código de prueba (Ignorar) ******************************/


SELECT * FROM cuenta ORDER BY customer_id DESC

SELECT * FROM tarjetas

SELECT * FROM marcas_tarjeta

SELECT tarjetas.numero, marcas_tarjeta.marca_name
FROM tarjetas
INNER JOIN marcas_tarjeta
ON tarjetas.marca_id = marcas_tarjeta.marca_id