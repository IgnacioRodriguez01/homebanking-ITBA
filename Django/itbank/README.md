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
- **Super/Staff:** 
  - *User: agustin, Pass: 1234*
  - *User: nacho, Pass: 1234*
- **Cliente genérico:** 
  - *User: Declan, Pass: 1234*

## API REST
### Estructura de URLs:
- **Datos de cliente:** */api/cliente/ (GET)*
- **Saldo de cliente:** */api/cliente/saldo/ (GET)*
- **Prestamos de sucursal:** */api/empleados/prestamos-sucursal/<pk>/ (GET)*
- **Tarjetas de cliente:** */api/empleados/tarjetas-cliente/<pk>/ (GET)*
- **Generar prestamo para un cliente:** */api/empleados/nuevo-prestamo/ (POST)*
- **Anular prestamo de un cliente:** */api/empleados/anular-prestamo/<pk>/ (DELETE)*
- **Modificar direccion propia:** */api/cliente/editar-direccion/ (PUT)*
- **Modificar direccion de cliente:** */api/empleados/editar-direccion/<pk>/ (PUT)*
- **Sucursales:** */api/sucursales/ (GET)*

### Notas:
Al dia de la fecha, no se logró finalizar el registro de usuarios mediante la pagina. Para hacerlo, creamos un superuser, le quitamos el staff y lo linkeamos manualmente en la tabla ClienteUser.
