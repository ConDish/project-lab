document.addEventListener('DOMContentLoaded', () => {

    // Boton de generar codigo
    const btnCodigo = document.getElementById('btnCodigo');
    if (btnCodigo) {


        btnCodigo.addEventListener('click', (evt) => {


            const codigo = document.getElementById('codigo');

            if (codigo.value != "") {


                fetch('/generarCodigo', {
                    method: 'POST',
                    body: JSON.stringify({ "codigo": codigo.value }),
                    headers: {
                        "Content-Type": "application/json",
                        // "Content-Type": "application/x-www-form-urlencoded",
                    },
                }).then(data => data.json())
                    .then(response => {

                        console.log(response);

                    })

            } else {
                alert("Llena el campo");
            }

        });

    }

    // Boton de registrar usuario

    const btnRegistro = document.getElementById('btnRegistro');

    if (btnRegistro) {



        btnRegistro.addEventListener('click', (evt) => {

            const correo = document.getElementById('correo').value;
            const cdestudiante = document.getElementById('cdestudiante').value;
            const password = document.getElementById('password').value;
            const confirmpass = document.getElementById('confirmpass').value;

            if (correo != "" && cdestudiante != "" && password != "" && confirmpass != "") {

                const user = {
                    "correo": correo,
                    "cdestudiante": cdestudiante,
                    "password": password,
                    "confirmpass": confirmpass
                }

                fetch('/registro', {
                    method: 'POST',
                    body: JSON.stringify(user),
                    headers: {
                        "Content-Type": "application/json",
                        // "Content-Type": "application/x-www-form-urlencoded",
                    },
                })
                .then(data => {return data.json()})

                .then(response => {
                        
                        if(response.success == 1){
                            window.location.href = "login"
                            
                        }else if(response.success == 0){
                            alert("El usuario ya registro su codigo o es incorrecto el codigo");
                        }else{
                            alert("Error en la base de datos");
                        }

                    })

            } else {

                alert("Llena los datos");

            }


        })

    }


});