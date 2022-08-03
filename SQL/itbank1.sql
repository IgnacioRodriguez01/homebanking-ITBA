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
	direccion_id INTEGER NOT NULL PRIMARY KEY,
	cliente_id INTEGER,
	empleado_id INTEGER,
	sucursal_id INTEGER UNIQUE,
	calle TEXT NOT NULL,
	numero INTEGER NOT NULL,
	ciudad TEXT NOT NULL,
	provincia TEXT NOT NULL,
	pais TEXT NOT NULL,
	FOREIGN KEY (cliente_id)
	REFERENCES cliente(customer_id),
	FOREIGN KEY (empleado_id)
	REFERENCES empleado(employee_id),
	FOREIGN KEY (sucursal_id)
	REFERENCES sucursal(branch_id)
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
