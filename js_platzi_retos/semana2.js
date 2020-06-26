// rETO 1

/* var num1;
var num2;
var diferencia;

function diferencia_numeros() {
    num1 = Number(prompt("Ingresar un número: "))
    num2 = Number(prompt("Ingresar otro número: "))
    diferencia = Math.abs(num1 - num2)

    if (num1 < num2) {
        console.log(`${num2} es mayor que ${num1}`)
        console.log(`${diferencia}`)
    } else if (num1 > num2) {
        console.log(`${num1} es menor que ${num2}`)
        console.log(`${diferencia}`)
    }
}

diferencia_numeros() */

// Reto 2

/* var num_limite;
var num_comparar;

num_limite = Number(prompt("Ingrese un número límite: "))
num_comparar = Number(prompt("Ingrese un número para comparar: "))

if (num_comparar < num_limite){
    console.log(`El número ${num_comparar} se encuentra en el rango, gracias`)

} else {
    console.log(`El número ${num_comparar} excede el límite permitido`)
} */


// Reto 3

/* var num_superior;
var num_superior;
var num;


num_superior = Number(prompt("Introduce un límite superior: "))
num_inferior = Number(prompt("Introduce un límite inferior: "))
num = Number(prompt("Introduce un número a comparar: "))

if (num > num_inferior && num < num_superior) {
    console.log(`${num} se encuentra entre  ${num_inferior} y ${num_superior}`)
} else {
    console.log(`${num} está fuera del rango establecido`)
} */

// Reto 4

/* var animal;

animal = prompt("Ingrese el nombre de un animal: ")

if (animal === 'Tortuga' || animal === 'tortuga' || animal === 'TORTUGA') {
    console.log(`También me gustan las tortugas`)
} else {
    console.log(`Este animal es genial, pero me gustán más las tortugas`)
} */


// Reto 5

/* var it_rain;

it_rain = prompt('Está lloviendo?: ')
if (it_rain === 'Sí' || it_rain == 'Si' || it_rain == 'si' || it_rain === 'SI') {
    viento = prompt("Está haciendo mucho viento? ")
    if (viento === 'Sí' || viento === 'Si' || viento === 'si' || viento === 'SI' ){
        console.log(`Hace mucho viento para salir con una sombrilla`)
    } else {
        console.log('Deberías llevar una sombrilla')
    }
} else {
    console.log('Que tengas un lindo día')
} */

// Reto 6

/* var edad; 

edad = Number(prompt("Ingrese su edad: "))

if (edad >= 30) {
    console.log('Nunca es tarde para aprender \n ¿Qué curso tomaremos?')
} else if (edad >= 18 && edad < 29) {
    console.log('Es un momento excelente para impulsar tu carrera')
} else {
    console.log(`¿Sabes hacia dónde dirigir tu futuro? Seguro puedo ayudarte`)
} */

// Reto 7

var num;

num = Number(prompt('Ingrese un número entre 1 y 6: '))

switch (num) {
    case 1:
        console.log(`Hoy aprenderemos sobre programación`)
        break;
    case 2:
        console.log(`¿Qué tal tomar un curso de Marketing?`)
        break;
    case 3:
        console.log(`Hoy es un gran día para comenzar a aprender de diseño`)
        break;
    case 4:
        console.log(`¿Y si aprendemos algo de negocios online?`)
        break;
    case 5:
        console.log(`Veamos un par de clase sobre producción audiovisual`)
        break;
    case 6:
        console.log(`Tal vez sea bueno desarrollar una habilidad blanda en Platzi`)
        break;
    default:
        console.log(`Por favor, ingresa un número en el rango indicado`)
}