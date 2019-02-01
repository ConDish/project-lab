document.addEventListener('DOMContentLoaded', () => {


    const btnCodigo = document.getElementById('btnCodigo');

    btnCodigo.addEventListener('click', (evt) => {


        const codigo = document.getElementById('codigo');

        if (codigo.value != ""){


        fetch('/generarCodigo', {
            method: 'POST',
            body: JSON.stringify({ "codigo" : codigo.value}),
            headers: {
                "Content-Type": "application/json",
                // "Content-Type": "application/x-www-form-urlencoded",
            },
        }).then( data => data.json())
        .then(response => {

            console.log(response);

        })

        }else{
            alert("Llena el campo");
        }

    })


});