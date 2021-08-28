var d = document.getElementById("dibujote");
var lienzo = d.getContext("2d");
var lineas = 30;
var l = 0;
var yi, xf;
var color_linea = "#000080";

function dibujarLinea (color, x_inicial, y_inicial, x_final, y_final){
    lienzo.beginPath();
    lienzo.strokeStyle = color;
    lienzo.moveTo (x_inicial, y_inicial);
    lienzo.lineTo (x_final, y_final);
    lienzo.stroke();
    lienzo.closePath();
}

while (l < lineas){
    yi = 10 * l;
    xf = 10 * (l + 1);
    dibujarLinea(color_linea, 0, yi, xf, 300);
    l++;
}

dibujarLinea(color_linea, 1, 1, 1, 300);
dibujarLinea(color_linea, 1, 299, 299, 299);
