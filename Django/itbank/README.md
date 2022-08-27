# Projecto Django: ITBANK

### Estructura de URLs:
- **Admin:** */admin*
- **Login:** */accounts/login*
- **Homebanking:** */homebanking*
- **Paginas del homebanking:**
  - */homebanking/gastos*
  - */homebanking/conversor*
  - */homebanking/prestamos*

### Usuarios de prueba:
- **Super:** 
  - *User: agustin, Pass: 1234*
  - *User: nacho, Pass: 1234*
- **Cliente genérico:** 
  - *User: Declan, Pass: 1234*

## API REST
### Estructura de URLs:
- **Datos de cliente:** */api/cliente (GET)*
- **Saldo de cliente:** */api/cliente/saldo (GET)*
- **Prestamos de sucursal:** */api/empleados/prestamos-sucursales (GET)*
- **Tarjetas de cliente:** */api/empleados/tarjetas-cliente (GET)*
- **Generar prestamo para un cliente:** */api/empleados/nuevo-prestamo (POST)*
- **Anular prestamo de un cliente:** */api/empleados/anular-prestamo (DELETE)*
- **Modificar direccion de cliente:** */api/cliente/1/editar-direccion (PUT)*
- **Sucursales:** */api/sucursales (GET)*

### Notas:
Al dia de la fecha, no se logró finalizar el registro de usuarios mediante la pagina. Para hacerlo, creamos un superuser, le quitamos el staff y lo linkeamos manualmente en la tabla ClienteUser.
