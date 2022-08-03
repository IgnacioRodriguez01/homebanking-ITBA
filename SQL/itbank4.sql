/****************************** Problemática 4 ******************************/


/** Cantidad de clientes por sucursal mayor a menor **/

SELECT branch_name, COUNT(cliente.customer_id) as cant_clientes
FROM sucursal
LEFT JOIN cliente on sucursal.branch_id = cliente.branch_id
GROUP BY sucursal.branch_name
ORDER BY cant_clientes DESC

/** Cantidad de empleados por cliente por sucursal **/

SELECT c.branch_id, Sucursal, Cantidad_de_empleados, COUNT(c.branch_id) AS Cantidad_de_clientes,
    ROUND(CAST(Cantidad_de_empleados AS REAL)/ COUNT(c.branch_id),2) AS Empleado_por_cliente
FROM (
    SELECT e.branch_id as id, s.branch_name as Sucursal,
        count(e.branch_id) as Cantidad_de_empleados
    FROM empleado as e
    INNER JOIN sucursal as s
    ON e.branch_id = s.branch_id
    GROUP BY e.branch_id
    ORDER BY Cantidad_de_empleados DESC
    )
INNER JOIN cliente as c
ON c.branch_id = id
GROUP BY c.branch_id
ORDER BY Cantidad_de_clientes, Cantidad_de_empleados DESC;


/*Obtener el promedio de créditos otorgado por sucursal (Muestra error)*/

SELECT c.branch_id, s.branch_name as Sucursal, mt.marca_name, COUNT(t.marca_id) as Cantidad_tarjetas 
FROM tarjetas as t
INNER JOIN marcas_tarjeta as mt
ON t.marca_id = mt.marca_id
INNER JOIN prestamo as c
ON t.customer_id = c.customer_id
INNER JOIN cliente as s
ON c.branch_id = s.branch_id
WHERE tipo = 1 
GROUP BY t.marca_id, c.branch_id
ORDER BY c.branch_id, Cantidad_tarjetas DESC;

