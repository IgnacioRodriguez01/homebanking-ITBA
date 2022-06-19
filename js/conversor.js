const moneda_one = document.getElementById("moneda1")
const moneda_two = document.getElementById("moneda2")
const cantidad_one = document.getElementById("cantidad-uno")
const cantidad_two = document.getElementById("cantidad-dos")
const cambioEl = document.getElementById("cambio")
const taza = document.getElementById("taza")

document.addEventListener('DOMContentLoaded', calculate)

moneda_one.addEventListener("change", e => calculate(e.target));
cantidad_one.addEventListener("input", e => calculate(e.target));
moneda_two.addEventListener("change", e => calculate(e.target));
cantidad_two.addEventListener("input", e => calculate(e.target));

taza.addEventListener('click', (e) =>{
    const temp = moneda_one.value;
    moneda_one.value = moneda_two.value;
    moneda_two.value = temp;
    calculate(e.target);
});

function calculate(target){

    const moneda1 = moneda_one.value;
    const moneda2 = moneda_two.value;

    fetch(`https://api.exchangerate-api.com/v4/latest/${moneda1}`)
    .then(res => res.json())
    .then(data=> {
        const conversion = data.rates[moneda2];
        cambioEl.innerHTML= `1 ${moneda1} = ${conversion} ${moneda2}`
        
        if(target == taza) {
            const valueStore = cantidad_two.value
            cantidad_two.value = cantidad_one.value;
            cantidad_one.value = valueStore;
            return;
        }
        if(target == cantidad_two || target == moneda_two) {
            cantidad_one.value = (cantidad_two.value / conversion).toFixed(3);
            return;
        }
        cantidad_two.value = (cantidad_one.value * conversion).toFixed(3);
    });
}