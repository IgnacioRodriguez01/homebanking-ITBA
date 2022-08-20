from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .forms import PrestamoForm

from .models import Prestamo
from Login.models import ClienteUser
from Clientes.models import Cliente, TiposCliente
from Cuentas.models import Cuenta

# Create your views here.

@login_required
def Prestamos(request):
    tipo = ''
    fecha = ''
    monto = ''
    cuentaIban = ''

    montosMaxTipo = {
        'Black': 500000,
        'Gold': 300000,
        'Classic': 100000
    }
    prestamoForm = PrestamoForm()

    if request.method == "POST":
        tipo = request.POST.get('tipo',"")
        fecha = request.POST.get('fecha',"")
        monto = request.POST.get('monto',"")

    #Consultar el tipo de cliente
    userLogged = request.user.id
    try:
        clienteId = ClienteUser.objects.get(user_id__exact=userLogged).cliente_id
        tipoId = Cliente.objects.get(customer_id__exact=clienteId).customer_type
        tipoCliente = TiposCliente.objects.get(tipo_id__exact=tipoId).tipo_name
    except:
        return redirect(reverse('prestamos')+"?error_auth")
    #Traer cuenta

    # Aquí, debido a que agregamos aleatoriamente el tipo de cliente
    # y las cuentas que tiene cada uno son aleatorias, decidimos optar
    # por asignarle el prestamo a la primer cuenta que se encuentre,
    # para cumplir la consigna. Lo ideal sería traer las cuentas que
    # tiene el cliente, y darle a elegir entre ellas, si la información
    # fuera precisa.  

    cuentaQuery = Cuenta.objects.all().filter(customer_id__exact=clienteId)[:1]
    cuenta = cuentaQuery[0]
    cuentaIban = cuenta.iban
    
    #Agregar validacion de fecha (REVISAR)

    #Comprobar monto según cliente
    if (monto):
        if (monto == '0'):
            return redirect(reverse('prestamos')+"?error_empty")
        if (montosMaxTipo[tipoCliente] < float(monto)):
            return redirect(reverse('prestamos')+"?error_monto")
        
        #Formatear a la manera en que se encuentra en la base de datos
        monto = float(monto)
        montoConv = "{0:.2f}".format(monto).replace('.', '')

        newPrestamo = Prestamo(loan_type=tipo.upper(), loan_date=fecha, loan_total=montoConv, customer_id=clienteId)
        #newPrestamo.save()
        
        #Agregar el monto al saldo del cliente, con el formato requerido
        balance = str(cuenta.balance)

        balanceFloat = float(balance[:-2]+'.'+balance[-2:])
        balanceFloat += monto
        
        balanceConv = "{0:.2f}".format(balanceFloat).replace('.', '')
        
        #cuentaQuery.update(balance=balanceConv)
        #Error: Cannot update a query once a slice has been taken. (REVISAR)
        #Debug
        print(cuentaQuery, cuentaIban, balanceConv)

        return redirect(reverse('prestamos')+"?success")
    context = {
        'form':prestamoForm,
        'tipoCliente':tipoCliente,
        'cuentaIban':cuentaIban
    }
    return render(request,'Prestamos/Prestamos.html', context)