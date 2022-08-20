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
  
### Notas:
Al dia de la fecha, no se logró finalizar el registro de usuarios mediante la pagina. Para hacerlo, creamos un superuser, le quitamos el staff y lo linkeamos manualmente en la tabla ClienteUser.
