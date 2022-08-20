/** Agregar tipos a los clientes **/
ALTER TABLE cliente
ADD customer_type INTEGER; 

/** Joins individuales **/
SELECT 	*
FROM Login_clienteuser
LEFT JOIN cliente ON Login_clienteuser.cliente_id = cliente.customer_id;

SELECT username, user_id
FROM auth_user
LEFT JOIN Login_clienteuser ON auth_user.id = Login_clienteuser.user_id

/** Tabla de informacion de usuario **/
SELECT 	user_id, username, cliente_id, customer_name, customer_surname, customer_DNI, dob, branch_id
FROM Login_clienteuser
LEFT JOIN cliente ON Login_clienteuser.cliente_id = cliente.customer_id
LEFT JOIN auth_user ON Login_clienteuser.user_id = auth_user.id;

/** Query para registro con DNI **/
SELECT customer_id
FROM cliente
WHERE customer_DNI = '62401607';

INSERT INTO Login_clienteuser (cliente_id, user_id)
VALUES 	(,);