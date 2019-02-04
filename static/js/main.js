document.addEventListener('DOMContentLoaded', () => {

    // Boton de generar codigo
    const btnCodigo = document.getElementById('btnCodigo');
    if (btnCodigo) {


        btnCodigo.addEventListener('click', (evt) => {


            const codigo = document.getElementById('codigo');
            const alerta = document.getElementById('alerta');

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

                        if (response.success == 1) {

                            alerta.innerHTML = "<div class='alert alert-success' role='alert'> Se creo correctamente su codigo! </div>";

                        } else {

                            alerta.innerHTML = "<div class='alert alert-danger' role='alert'> El codigo ya existe! </div>";
                        }

                    })

            } else {
                alerta.innerHTML = "<div class='alert alert-danger' role='alert'> Llene los campos! </div>";
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
            const alerta = document.getElementById('alerta');

            if (password == confirmpass) {

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
                        .then(data => { return data.json() })

                        .then(response => {

                            if (response.success == 1) {
                                
                                window.location.href = "login"

                            } else if (response.success == 0) {

                                alerta.innerHTML = "<div class='alert alert-danger' role='alert'> El usuario ya registro su codigo o es incorrecto el codigo! </div>";

                            }

                        })

                } else {

                    alerta.innerHTML = "<div class='alert alert-danger' role='alert'> Llena los datos correctamente! </div>";

                }

            } else {
                alerta.innerHTML = "<div class='alert alert-danger' role='alert'> Contraseña de confirmacion es diferente! </div>";
            }


        });

    }

    // Boton de logear usuario

    const btnLogin = document.getElementById('btnLogin');

    if (btnLogin) {



        btnLogin.addEventListener('click', (evt) => {

            const correo = document.getElementById('correo').value;
            const password = document.getElementById('password').value;
            const alerta = document.getElementById('alerta');



            if (correo != "" && password != "") {

                let user = {
                    "correo": correo,
                    "password": password
                };

                fetch('/login', {
                    method: 'POST',
                    body: JSON.stringify(user),
                    headers: {
                        "Content-Type": "application/json",
                    },
                })
                    .then(data => { return data.json() })
                    .then(response => {

                        if (response.success == 1) {

                            window.location.href = "profesorcrud";

                        } else if (response.success == 2) {

                            window.location.href = "usuario";

                        } else if (response.success == 0) {

                            alerta.innerHTML = "<div class='alert alert-danger' role='alert'> El usuario no existe! </div>";

                        } else {

                            alerta.innerHTML = "<div class='alert alert-danger' role='alert'> Error en la base de datos! </div>";
                        }

                    });

            } else {

                alerta.innerHTML = "<div class='alert alert-danger' role='alert'> Llena los datos correctamente! </div>";

            }

        });


    }

    // Boton de crear electiva

    const btnElectiva = document.getElementById('btnElectiva');

    if (btnElectiva) {


        btnElectiva.addEventListener('click', (evt) => {

            const nombre = document.getElementById('nombre').value;
            const descripcion = document.getElementById('descripcion').value;
            const numerocupo = document.getElementById('numerocupo').value;
            const alerta = document.getElementById('alerta');



            if (nombre != "" && numerocupo != "") {

                let electiva = {
                    "nombre": nombre,
                    "descripcion": descripcion,
                    "numerocupo": numerocupo
                };

                fetch('/electivascrud', {
                    method: 'POST',
                    body: JSON.stringify(electiva),
                    headers: {
                        "Content-Type": "application/json",
                    },
                })
                    .then(data => { return data.json() })
                    .then(response => {

                        

                        if (response.success == 1) {

                            alerta.innerHTML = "<div class='alert alert-success' role='alert'> Se creo con exito! </div>";

                            window.location.href = "electivascrud"

                        } else {
                            alerta.innerHTML = "<div class='alert alert-danger' role='alert'> Error al crearlo! </div>";
                        }


                    });

            } else {

                alerta.innerHTML = "<div class='alert alert-danger' role='alert'> Llena los datos correctamente! </div>";

            }

        });


    }

    // Boton de eliminar electiva

    const btnEliminarElectiva = document.getElementById('elec');


    if (btnEliminarElectiva) {


        btnEliminarElectiva.addEventListener('click', (evt) => {

            if (event.target.id == "btnEliminarElectiva") {

                const nombre = [...event.target.parentElement.parentElement.children];
                const alerta = document.getElementById('alerta-table');

                fetch(`/electivaeliminar/${nombre[0].innerHTML}`, {
                    method: 'GET',
                    headers: {
                        "Content-Type": "application/json",
                    },
                })
                    .then(data => { return data.json() })
                    .then(response => {

                       

                        if (response.success == 1) {

                            alerta.innerHTML = "<div class='alert alert-success' role='alert'> Se elimino con exito! </div>";

                            window.location.href = "electivascrud";


                        } else {
                            alerta.innerHTML = "<div class='alert alert-danger' role='alert'> Error al eliminarlo! </div>";
                        }


                    });

            }


        });


    }

    // Boton de editar electiva

    const btnEditarElectiva = document.getElementById('elec');


    if (btnEditarElectiva) {

        var target = "";

        btnEditarElectiva.addEventListener('click', (evt) => {

            if (event.target.id == "btnEditarElectiva") {

                target = [...event.target.parentElement.parentElement.children];

                document.getElementById('nombre-modal').value = target[1].innerHTML;
                document.getElementById('descripcion-modal').value = target[2].innerHTML;
                document.getElementById('numerocupo-modal').value = target[3].innerHTML;
                document.getElementById('alerta-table');


            }


        });

        const btnSaveElectiva = document.getElementById('btnSaveElectiva');

        if (btnSaveElectiva) {

            btnSaveElectiva.addEventListener('click', (evt) => {

                const nombre = document.getElementById('nombre-modal').value;
                const descripcion = document.getElementById('descripcion-modal').value;
                const numerocupo = document.getElementById('numerocupo-modal').value;
                const alerta = document.getElementById('alerta-modal');

                let electiva = {
                    "id": target[0].innerHTML,
                    "nombre": nombre,
                    "descripcion": descripcion,
                    "numerocupo": numerocupo
                };

                if (nombre != "" && numerocupo != "") {

                    fetch(`/electivaeditar`, {
                        method: 'POST',
                        body: JSON.stringify(electiva),
                        headers: {
                            "Content-Type": "application/json",
                        },

                    })
                        .then(data => { return data.json() })
                        .then(response => {


                            if (response.success == 1) {

                                alerta.innerHTML = "<div class='alert alert-success' role='alert'> Se actualizo con exito! </div>";

                                window.location.href = "electivascrud";


                            } else {
                                alerta.innerHTML = "<div class='alert alert-danger' role='alert'> Error al actualizar! </div>";
                            }


                        });

                } else {

                    alerta.innerHTML = "<div class='alert alert-danger' role='alert'> Campos obligatorios! </div>";
                }

            });
        }


    }


    // Boton de crear profesor


    const btnProfesor = document.getElementById('btnProfesor');

    if (btnProfesor) {


        btnProfesor.addEventListener('click', (evt) => {
            const codigo = document.getElementById('idprofe').value;
            const nombre = document.getElementById('nombre').value;
            const selectElement = document.getElementById('electselec');
            const data = parseInt(selectElement.options[selectElement.selectedIndex].id);
            const alerta = document.getElementById('alerta');

            if (nombre != "" && codigo != "") {

                let profesor = {
                    "codigo": codigo,
                    "nombre": nombre,
                    "electiva_id": data,
                };


                fetch('/profesorcrud', {
                    method: 'POST',
                    body: JSON.stringify(profesor),
                    headers: {
                        "Content-Type": "application/json",
                    },
                })
                    .then(data => { return data.json() })
                    .then(response => {

                        

                        if (response.success == 1) {

                            alerta.innerHTML = "<div class='alert alert-success' role='alert'> Se creo con exito! </div>";

                            window.location.href = "profesorcrud"

                        } else {

                            alerta.innerHTML = "<div class='alert alert-danger' role='alert'> Error al crearlo! </div>";

                        }


                    });

            } else {

                alerta.innerHTML = "<div class='alert alert-danger' role='alert'> Campos obligatorios! </div>";

            }

        });


    }


    // Boton de editar profesor

    const btnEditarProfesor = document.getElementById('pro');


    if (btnEditarProfesor) {

        var targetpro = "";

        btnEditarProfesor.addEventListener('click', (evt) => {

            if (event.target.id == "btnEditarProfesor") {

                targetpro = [...event.target.parentElement.parentElement.children];

                document.getElementById('idprofe-modal').value = targetpro[0].innerHTML;
                document.getElementById('nombre-modal').value = targetpro[1].innerHTML;
                document.getElementById('alerta-table');

               

            }


        });

        const btnSaveElectiva = document.getElementById('btnSaveElectiva');

        if (btnSaveElectiva) {

            btnSaveElectiva.addEventListener('click', (evt) => {

                const idprofe = document.getElementById('idprofe-modal').value;
                const nombre = document.getElementById('nombre-modal').value;
                const selectElement = document.getElementById('profe-modal');
                const data = parseInt(selectElement.options[selectElement.selectedIndex].id);
                const alerta = document.getElementById('alerta-modal');

                let profesor = {
                    "idvieja": targetpro[0].innerHTML,
                    "idnueva": idprofe,
                    "nombre": nombre,
                    "electiva_id": data,
                };

                if (idprofe != "" && nombre != "") {

                    fetch(`/profesoreditar`, {
                        method: 'POST',
                        body: JSON.stringify(profesor),
                        headers: {
                            "Content-Type": "application/json",
                        },

                    })
                        .then(data => { return data.json() })
                        .then(response => {


                            if (response.success == 1) {

                                alerta.innerHTML = "<div class='alert alert-success' role='alert'> Se actualizo con exito! </div>";

                                window.location.href = "profesorcrud";


                            } else {
                                alerta.innerHTML = "<div class='alert alert-danger' role='alert'> Error al actualizar! </div>";
                            }


                        });

                } else {

                    alerta.innerHTML = "<div class='alert alert-danger' role='alert'> Campos obligatorios! </div>";
                }

            });
        }


    }

    // Boton de eliminar profesor

    const btnEliminarProfesor = document.getElementById('pro');


    if (btnEliminarProfesor) {


        btnEliminarProfesor.addEventListener('click', (evt) => {



            if (event.target.id == "btnEliminarProfesor") {

                const nombre = [...event.target.parentElement.parentElement.children];
                const alerta = document.getElementById('alerta-table');



                fetch(`/profesoreliminar/${nombre[0].innerHTML}`, {
                    method: 'GET',
                    headers: {
                        "Content-Type": "application/json",
                    },
                })
                    .then(data => { return data.json() })
                    .then(response => {


                        if (response.success == 1) {

                            alerta.innerHTML = "<div class='alert alert-success' role='alert'> Se elimino con exito! </div>";

                            window.location.href = "profesorcrud";


                        } else {
                            alerta.innerHTML = "<div class='alert alert-danger' role='alert'> Error al eliminarlo! </div>";
                        }


                    });

            }


        });


    }


    // Boton de crear profesor


    const btnInscribir = document.getElementById('btnInscribir');

    if (btnInscribir) {


        btnInscribir.addEventListener('click', (evt) => {

            const selectElement = document.getElementById('electselec');
            const data = parseInt(selectElement.options[selectElement.selectedIndex].id);
            const alerta = document.getElementById('alerta');

            let estudiante = {
                "electiva_id": data,
            };

            fetch('/usuario', {
                method: 'POST',
                body: JSON.stringify(estudiante),
                headers: {
                    "Content-Type": "application/json",
                },
            })
                .then(data => { return data.json() })
                .then(response => {


                    if (response.success == 1) {

                        alerta.innerHTML = "<div class='alert alert-success' role='alert'> Muy bien! </div>";


                    } else {

                        alerta.innerHTML = "<div class='alert alert-danger' role='alert'> Ya escogiste esta electiva! </div>";

                    }


                });

        });


    }



});