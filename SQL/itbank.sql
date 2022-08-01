/*Black, Gold, Classic*/
CREATE TABLE tipos_cliente(
	tipo_id INTEGER PRIMARY KEY,
	tipo_name TEXT NOT NULL,
);

/*Corriente, Dolares, Ahorro*/
CREATE TABLE tipos_cuenta(
	tipo_id INTEGER PRIMARY KEY,
	tipo_name TEXT NOT NULL,
);

CREATE TABLE marcas_tarjeta(
	marca_id INTEGER PRIMARY KEY,
	marca_name TEXT NOT NULL
);

CREATE TABLE tarjetas(
	numero TEXT NOT NULL PRIMARY KEY CHECK (length(numero) <= 20),
	tipo TEXT NOT NULL,
	cvv INTEGER NOT NULL CHECK (length(cvv) = 3),
	fecha_emision TEXT NOT NULL,
	fecha_vto TEXT NOT NULL,
	marca_id INTEGER NOT NULL,
	FOREIGN KEY (marca_id)
	REFERENCES marcas_tarjeta(marca_id)
);

INSERT INTO tarjetas
VALUES ('4040222840496339','Crédito',384,'05/20','11/24',1),
('5489426424120703','Débito',750,'03/20','07/24',2);

INSERT INTO marcas_tarjeta (marca_name)
VALUES ('VISA'), ('Mastercard'), ('American Express');

/******************************************/

SELECT * FROM tarjetas

SELECT * FROM marcas_tarjeta

SELECT tarjetas.numero, marcas_tarjeta.marca_name
FROM tarjetas
INNER JOIN marcas_tarjeta
ON tarjetas.marca_id = marcas_tarjeta.marca_id