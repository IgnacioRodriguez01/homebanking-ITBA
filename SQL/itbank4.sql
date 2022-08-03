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