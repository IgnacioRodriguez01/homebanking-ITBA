/*const moneda_one = document.getElementById("moneda1")
const moneda_two = document.getElementById("moneda2")
const cantidad_one = document.getElementById("cantidad-uno")
const cantidad_two = document.getElementById("cantidad-dos")
const cambioEl = document.getElementById("cambio")
const taza = document.getElementById("taza")


function calculate(){

    const moneda1 = moneda_one.value;
    const moneda2 = moneda_two.value;

    fetch(`https://api.exchangerate-api.com/v4/latest/${moneda1}`)
    .then(res => res.json())
    .then(data=> {
        const taza = data.rates[moneda2];
        cambioEl.innerHTML= `1 ${moneda1} = ${taza} ${moneda2}`
        cantidad_two.value = (cantidad_one.value * taza).toFixed(2);
});
}

moneda_one.addEventListener("change", calculate);
cantidad_one.addEventListener("input", calculate);
moneda_two.addEventListener("change", calculate);
cantidad_two.addEventListener("input", calculate);

taza.addEventListener('click', () =>{
    const temp = moneda_one.value;
    moneda_one.value = moneda_two.value;
    moneda_two.value = temp;
    calculate();
} );
calculate();/