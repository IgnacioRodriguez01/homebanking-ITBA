const oficial = {
    venta: document.querySelector('#oficial .precios .dolar-v'),
    compra: document.querySelector('#oficial .precios .dolar-c')
}
const blue = {
    venta: document.querySelector('#blue .precios .dolar-v'),
    compra: document.querySelector('#blue .precios .dolar-c')
}
const liqui = {
    venta: document.querySelector('#liqui .precios .dolar-v'),
    compra: document.querySelector('#liqui .precios .dolar-c')
}
const bolsa = {
    venta: document.querySelector('#bolsa .precios .dolar-v'),
    compra: document.querySelector('#bolsa .precios .dolar-c')
}


fetch("https:dolarsi.com/api/api.php?type=valoresprincipales")
    .then((data) => data.json())
    .then((data) => {
        oficial.venta.textContent = `V: $${data[0].casa.venta}`;
        oficial.compra.textContent = `C: $${data[0].casa.compra}`;

        blue.venta.textContent = `V: $${data[1].casa.venta}`;
        blue.compra.textContent = `C: $${data[1].casa.compra}`;

        liqui.venta.textContent = `V: $${data[3].casa.venta}`;
        liqui.compra.textContent = `C: $${data[3].casa.compra}`;

        bolsa.venta.textContent = `V: $${data[4].casa.venta}`;
        bolsa.compra.textContent = `C: $${data[4].casa.compra}`;
    });