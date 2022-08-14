/********Form objects********/

const formLogin = {
    form: document.getElementById('formLogin'),
    fields: {
        doc: document.querySelector('#docLogin input'),
        usuario: document.getElementById('usuarioLogin'),
        clave: document.getElementById('claveLogin')
    },
    docOpc: document.querySelector('#docLogin button'),
    docOpcList: document.querySelector('#docLogin ul'),
    tipoDoc: '',
    claveToggle: document.getElementById('clave-toggleLogin'),
    recordarme: document.getElementById('recordarme'),
    mensaje: document.getElementById('mensajeLogin'),
    submit: document.getElementById('submitLogin')
}

const formRegister = {
    form: document.getElementById('formRegister'),
    fields: {
        doc: document.querySelector('#docRegister input'),
        usuario: document.getElementById('usuarioRegister'),
        email: document.getElementById('emailRegister'),
        clave: document.getElementById('claveRegister'),
        clave2: document.getElementById('clave2Register')
    },
    docOpc: document.querySelector('#docRegister button'),
    docOpcList: document.querySelector('#docRegister ul'),
    tipoDoc: '',
    mensaje: document.getElementById('mensajeRegister'),
    submit: document.getElementById('submitRegister')
}

const formPassword = {
    form: document.getElementById('formPassword'),
    fields: {
        email: document.getElementById('emailPassword')
    },
    mensaje: document.getElementById('mensajePassword'),
    submit: document.getElementById('submitPassword')
}

const FORMS = [formLogin, formRegister, formPassword];

/********Form objects destructuring********/

document.addEventListener('DOMContentLoaded', formEvents(FORMS));

function formEvents(forms) {
    forms.forEach(form => {
        form.submit.addEventListener('click', (e) => {
            formValidator(form);
        });

        const hasDoc = Object.keys(form.fields).some(field => field === "doc");

        if (hasDoc) {
            form.docOpcList.addEventListener('click', (e) => {
                form.docOpc.textContent = e.target.dataset.id;
                form.tipoDoc = e.target.dataset.id;
            });
        }
    })
}

function formValidator(formObj) {
    const {fields, mensaje} = formObj;

    //Validación campos vacíos
    const emptyField = Object.values(fields).some(field => field.value === "");
    if(emptyField) {
        mostrarAlerta(mensaje, 'Todos los campos son obligatorios');
        return;
    }
    
    //Validación documento
    const hasDoc = Object.keys(fields).some(field => field === "doc");
    if (hasDoc) {
        if (isNaN(fields.doc.value)) {
            mostrarAlerta(mensaje, 'Introducir un documento numérico');
            return;
        }
        if (formObj.tipoDoc === '') {
            mostrarAlerta(mensaje, 'Introducir el tipo de documento');
            return;
        }
    }

    //Validación email
    const hasEmail = Object.keys(fields).some(field => field === "email");
    if (hasEmail) {
        const emailRegex = /[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?/g

        if (!fields.email.value.match(emailRegex)) {
            mostrarAlerta(mensaje, 'Introducir un email válido');
            return;
        }
    }

    //Validación final específica
    if (formObj == formRegister) {
        if (fields.clave.value != fields.clave2.value) {
            mostrarAlerta(mensaje, 'La clave debe ser igual en ambos casos');
            return;
        }
        mostrarAlerta(mensaje, 'Registrado correctamente', 'correcto');
        setTimeout(() => {
            window.location.href = 'index.html';
        }, 3000);
    }

    if (formObj == formPassword) {
        mostrarAlerta(mensaje, 'Correo de recuperación enviado.', 'correcto');
    }

    if(formObj == formLogin) {
        mostrarAlerta(mensaje, 'Logeado correctamente', 'correcto');
        setTimeout(() => {
            window.location.href = 'homebanking.html';
        }, 3000);
    }

}

/********Campos específicos********/

const { fields:{clave} , recordarme, claveToggle} = formLogin;

claveToggle.addEventListener('click', () => {
    const type = clave.getAttribute("type") === "password" ? "text" : "password";
    clave.setAttribute("type", type);
});

recordarme.addEventListener('click', (e) => {
    console.log('Recordarme:', e.target.checked);
});
 
/********Funciones generales********/

function mostrarAlerta(contenedor, error, tipo) {
    const err = document.createElement('div');
    const previous = contenedor.querySelector('.alert');

    err.textContent = error;
    err.className = ('alert');
    
    tipo === 'correcto' ?
    err.classList.add('bg-success')
    :
    err.classList.add('bg-danger') ;

    if (previous != null) { 
        contenedor.removeChild(previous);
        contenedor.insertBefore(err, contenedor.firstChild);

        setTimeout(() => {
            contenedor.removeChild(err);
        }, 2000);
    } else {
        contenedor.insertBefore(err, contenedor.firstChild);
        
        setTimeout(() => {
            contenedor.removeChild(err);
        }, 2000);
    }
}