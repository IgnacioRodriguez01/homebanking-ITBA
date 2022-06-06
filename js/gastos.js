let gastosArr = [];
let presupuesto = 0;
let presupuestoRestante = 0;

const presupuestoInput = document.getElementById('presupuesto')
const monto = document.getElementById('monto');
const destinatario = document.getElementById('destinatario');

const dateNumber = document.getElementById('dateNumber');
const dateText = document.getElementById('dateText');
const dateMonth = document.getElementById('dateMonth');
const dateYear = document.getElementById('dateYear');
const pTotal = document.getElementById('pTotal');
const pFinal = document.getElementById('pFinal');

const billInput = document.getElementById("bill");

// Tasks Container
const tasksContainer = document.getElementById('tasksContainer');

presupuestoInput.oninput= () => {
    presupuesto= presupuestoInput.value
    console.log(presupuesto);
}
presupuestoInput.disabled = false;
    /*
    document.getElementById('submit').onclick = function() {
   
    var disabled = document.getElementById("name").disabled;
    if (disabled) {
        document.getElementById("name").disabled = false;
    }
    else {
        document.getElementById("name").disabled = true;
    }
    */

const setDate = () => {
    const date = new Date();
    dateNumber.textContent = date.toLocaleString('es', { day: 'numeric' });
    dateText.textContent = date.toLocaleString('es', { weekday: 'long' });
    dateMonth.textContent = date.toLocaleString('es', { month: 'short' });
    dateYear.textContent = date.toLocaleString('es', { year: 'numeric' });
};

const addNewTask = event => { //Nuevo gasto
    event.preventDefault();

    //Validación campos
    if(monto.value=="" || destinatario.value=="" ){
        return;
    }

    //Creación de gasto en HTML
    const fechaid = Date.now();
    const task = document.createElement('div');
    task.classList.add('task', 'roundBorder');
    task.addEventListener('click', changeTaskState)
    task.textContent = `Destinatario ${destinatario.value} Cantidad ${monto.valueAsNumber}`;
    task.id= fechaid;
    tasksContainer.prepend(task);

    //Creación de objeto gasto
    console.log(monto.valueAsNumber,destinatario.value);
    crearGasto(monto.valueAsNumber,destinatario.value, fechaid);
    presupuestoInput.disabled = true;

    //Actualizacion de gasto en propina
    billInput.value = gastosArr.reduce( (total, obj) => total + obj.gasto, 0);
    calculateTip();
    event.target.reset();
};

var changeTaskState = function (){ //Borrar individual
    this.parentNode.removeChild(this); 
    gastosArr = gastosArr.filter(gasto => gasto.dataid != this.id);
    console.log(gastosArr);
    presupuestoRestante = presupuesto - gastosArr.reduce( (total, obj) => total + obj.gasto, 0);
    pFinal.textContent = `$${presupuestoRestante}`;

    //Actualizacion de gasto en propina
    billInput.value = gastosArr.reduce( (total, obj) => total + obj.gasto, 0);
    calculateTip();
};

const renderOrderedTasks = () => { //Borrar todo
    limpiarHTML(tasksContainer)
    presupuestoInput.disabled = false;
    pFinal.textContent = "$0,00";
    pTotal.textContent = "$0,00";
    billInput.value = 0;
    calculateTip();
    gastosArr = [];
}
setDate(); 



function crearGasto(gasto, destinatario, id){
    
    const nuevoGasto = {
        "gasto" : gasto,
        "destinatario" : destinatario,
        "dataid" : id
    }
    console.log(nuevoGasto);

    gastosArr.push(nuevoGasto);
    console.log(gastosArr);
    presupuestoRestante = presupuesto - gastosArr.reduce( (total, obj) => total + obj.gasto, 0);
    pFinal.textContent = `$${presupuestoRestante}`;
    pTotal.textContent = `$${presupuesto}`;
    /*mostrarGasto(nuevoGasto);*/

}

function limpiarHTML(contenedor) {
    while (contenedor.firstChild) {
        contenedor.removeChild(contenedor.firstChild);
    }
}

const sliders = document.querySelectorAll("input[type='range']");
sliders.forEach(function(slider){
    slider.addEventListener("input",calculateTip);
});

billInput.addEventListener("change",calculateTip);


function calculateTip(){
    let bill = parseFloat(billInput.value);
    let tipPercent = document.getElementById("tip").value;
    let noOfPeople = document.getElementById("no-of-people").value;

    billInput.value = bill.toFixed(2);

    let totalTip = parseFloat((bill * (tipPercent/100)).toFixed(2));
    let total = parseFloat((bill + totalTip).toFixed(2));

    let tipPerPerson = (totalTip / noOfPeople).toFixed(2);
    let totalPerPerson = (total / noOfPeople).toFixed(2);

    document.getElementById("tip-amount").textContent = `\$ ${totalTip}`;
    document.getElementById("total-amount").textContent = `\$ ${total}`;
    
    document.getElementById("tip-percent").textContent = `${tipPercent}%`;
    document.getElementById("split-num").textContent = noOfPeople;

    document.getElementById("tip-per-person").textContent = `\$ ${tipPerPerson}`;
    document.getElementById("total-per-person").textContent = `\$ ${totalPerPerson}`;
}
calculateTip();