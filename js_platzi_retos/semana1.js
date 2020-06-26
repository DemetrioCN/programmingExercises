// Reto 1

/* var nombre;
nombre = prompt("Ingrese nombre: ")
console.log(`Hola, ${nombre}`) */

// Reto 2

/* var nombre;
var apellido;

nombre = prompt("Ingrese su nombre: ")
apellido = prompt("Ingrese su apellido paterno: ")

console.log(`Hola, ${nombre} ${apellido}`) */

// Reto 3
/* var curso_platzi;

curso_platzi = `
    Platzi cuenta con cursos de: \n\

    Desarrollo en Ingeniería \n\
    Diseño y UX \n\
    Marketing \n\
    Negocios y Emprendimiento \n\
    Producción Audiovisual \n\
    Crecimiento Profesional \n\
    `

console.log(curso_platzi) */

// Reto 4

/* var variable1;
var variable2;
var sumar; 

variable1 = Number(prompt("Ingrese un numero: "))
variable2 = Number(prompt("Ingrese otro numero: "))

sumar = variable1 + variable2;

console.log(`Suma: ${sumar}`) */


// Reto 5

/* var variable1;
var variable2;
var variable3;
var sumar; 
var resultado;

variable1 = Number(prompt("Ingrese un numero: "))
variable2 = Number(prompt("Ingrese otro numero: "))
variable3 = Number(prompt("Ingrese un numero mas: "))

sumar = variable1 + variable2;
resultado = sumar*variable3;

console.log(`Suma: ${resultado.toFixed(2)}`) */



// Reto 6
/* var rebanada;
var y_comida;
var resultado;

rebanada = Number(prompt("Indicar numero de rebanadas: "))

console.log(`Se comieron 5 rebandas`)

y_comida = 15
resultado = rebanada - y_comida;

console.log(`Entonces, quedan ${resultado} rebanadas`) */


// Reto 7
/* var name;
var age;

name = prompt("Ingrese su nombre: ");
age = Number(prompt("Ingrese su edad: "));

console.log(`${name}, el año pasado tenías ${age} y el próximo año tendrás ${age + 1}`)
 */

// Reto 8

/* var total_a_pagar;
var amigos;
var porcentaje_de_propina;
var impuesto;

function cuenta_de_la_cena() {
    total_a_pagar = Number(prompt("Ingrese el total a pagar: "))
    amigos = Number(prompt("Ingrese el numero de personas: "))
    porcentaje_de_propina = Number(prompt("Ingrese el procentaje de propina: "))
    impuesto = 16.0
    Total = total_a_pagar + (total_a_pagar*porcentaje_de_propina/100) + (total_a_pagar*impuesto/100)

    console.log(`El total es ${Total}, incluye ${impuesto} % de impuestos y un ${porcentaje_de_propina}`)
    console.log( `Cada cliente deberá pagar: ${Total/amigos}`)
}

cuenta_de_la_cena() */

// Reto 9

/* var dias;
var horas;
var minutos;
var segundos;

function cuentas_horas() {
    dias = Number(prompt("Introduce cierta cantidad de días: "))
    horas = dias*60
    minutos = horas*60
    segundos = minutos*60

    console.log(`${dias} dias tiene ${horas} horas, ${minutos} minutos y ${segundos} segundos`)
}

cuentas_horas() */

// Reto 10
/* var UNA_MILLA;
var millas;
var km;

function millas_a_km() {
    `
    Convertidor de millas a kilometros 
    1 milla = 1.609344 km 
    ` 
    
    UNA_MILLA = 1.6099344
    millas = Number(prompt("Introduce una cantidad de millas: "))
    km = millas*UNA_MILLA
    console.log(`${millas} millas son ${km} kilometros`)
}

millas_a_km() */


// Reto 11
var mayor;
var menor;
var resultado;

function cuantas_veces() {
    `Este programa regresa cuantas 
    veces caben un numero menora 100 
    en un numero mayor a 1000`
    mayor = Number(prompt("Introduce un número mayor a 1000: "))
    menor = Number(prompt("Introduce un número menor a 100: "))
    resultado = mayor/menor
    console.log(`${resultado.toFixed(0)}`)
}

cuantas_veces()