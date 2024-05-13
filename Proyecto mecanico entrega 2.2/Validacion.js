
var Rut = document.getElementById('Rut');
var Nombre = document.getElementById('Nombre');
var Edad = document.getElementById('Edad');
var Celular = document.getElementById('Celular');
var Correo = document.getElementById('Correo');
var Curriculum = document.getElementById('Curriculum');

var error = document.getElementById('error');
error.style.color = 'red';

function enviarFormulario() {
    console.log('Enviando Formulario....');

    var mensajesError = [];

    if (Rut.value === null || Rut.value === '') {
        mensajesError.push('Ingresa tu rut');
    }

    if (Nombre.value === null || Nombre.value === '') {
        mensajesError.push('Ingresa tu nombre');
    }

    if (Edad.value === null || Edad.value === '') {
        mensajesError.push('Ingresa tu Edad');
    }

    if (Celular.value === null || Celular.value === '') {
        mensajesError.push('Ingresa tu Celular');
    }

    if (Correo.value === null || Correo.value === '') {
        mensajesError.push('Ingresa tu Correo');
    }

    if (Curriculum.value === null || Curriculum.value === '') {
        mensajesError.push('Ingresa un Archivo');
    }

    error.innerHTML = mensajesError.join(', ');

    return false;
}

// var form = document.getElementById('formulario');
// form.addEventListener('submit', function (evt) {
//     evt.preventDefault();
//     var mensajesError = [];

//     if (rut.value === null || rut.value === '') {
//         mensajesError.push('Ingresa tu rut');
//     }
//     if (Nombre.value === null || nombre.value === '') {
//         mensajesError.push('Ingresa tu nombre completo');
//     }

//     if (ApellidoPa.value === null || ApellidoPa.value === '') {
//         mensajesError.push('Ingresa tu Apellido Paterno');
//     }

//     if (ApellidoMA.value === null || ApellidoMA.value === '') {
//         mensajesError.push('Ingresa tu Apellido Materno');
//     }

//     if (Edad.value === null || Edad.value === '') {
//         mensajesError.push('Ingresa tu Edad');
//     }
//     if (Celular.value === null || Celular.value === '') {
//         mensajesError.push('Ingresa tu Celular');
//     }
//     error.innerHTML = mensajesError.join(' , ');

      console.log("Enviado Formulario...");
// });
