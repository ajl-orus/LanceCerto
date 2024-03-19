
function mostrar_respuesta_remota_para_formulario(nombre) {
    document.forms[nombre].addEventListener('submit', (event) => {
        event.preventDefault();
        fetch(event.target.action, {
            method: 'POST',
            body: new URLSearchParams(new FormData(event.target))
        }).then((response) => {
            return response.json()
        }).then((body) => {
            alert(body["mensaje"])
        })
    })
}

function sube_puja(){
    alert ("Sua proposta foi aceita. Increment de R$50")
}

function sube_puja_un_poco(){
    alert ("Sua proposta foi aceita. Increment de R$100")
}

function sube_puja_un_poco_mas(){
    alert ("Sua proposta foi aceita. Increment de R$250")
}
