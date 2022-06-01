//Acá va a estar la validación del formulario

const form = document.getElementById('form');
const doc = document.querySelector('#doc input');
const docOpc = document.querySelector('#doc button');
const docOpcList = document.querySelector('#doc ul');
const usuario = document.getElementById('usuario');
const clave = document.getElementById('clave');
const claveToggle = document.getElementById('clave-toggle');
const recordarme = document.getElementById('recordarme');
const mensaje = document.getElementById('mensaje');

let tipoDoc = '';

form.addEventListener('submit', (e) => {
    e.preventDefault();
    if (doc.value === '' || usuario.value === '' || clave.value === '') {
        mostrarAlerta('Todos los campos son obligatorios');
        return;
    }
    if (isNaN(doc.value)) {
        mostrarAlerta('Introducir un documento numérico');
        return;
    }
    if (tipoDoc === '') {
        mostrarAlerta('Introducir el tipo de documento');
        return;
    }
    mostrarAlerta('Logeado correctamente', 'correcto');
    setTimeout(() => {
        window.location.href = 'homebanking.html';
    }, 3000);

});

docOpcList.addEventListener('click', (e) => {
    docOpc.textContent = e.target.dataset.id;
    tipoDoc = e.target.dataset.id;
});

claveToggle.addEventListener('click', () => {
    const type = clave.getAttribute("type") === "password" ? "text" : "password";
    clave.setAttribute("type", type);
});

recordarme.addEventListener('click', (e) => {
    console.log('Recordarme:', e.target.checked);
});

function mostrarAlerta(error, tipo) {
    const contenedor = mensaje;
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