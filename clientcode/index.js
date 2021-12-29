var apiUrl = "http://127.0.0.1:8000";



const calcForm = document.querySelector("#calc_service");
const dateForm = document.querySelector('#date_service');
const selectApi = document.querySelector('#url_choice');

// var url_choice = document.getElementById('url_choice').value;
// url_choice.onchange = console.log(url_choice)

function apiChange(){
    var url_choice = document.getElementById("url_choice").value;
    console.log(url_choice)
    if (url_choice == "flask"){
        apiUrl =  "http://127.0.0.1:5000";
    }
    else{
        apiUrl = "http://127.0.0.1:8000";
    }
}



function calcSubmit(event) {
    event.preventDefault();

    const xhr = new XMLHttpRequest();
    xhr.open('POST', `${apiUrl}/services/calculator/`);
    console.log(apiUrl)
    xhr.setRequestHeader('Content-Type', 'application/json');
    var arg1 = document.getElementById("arg1").value;
    var arg2 = document.getElementById("arg2").value;
    var op_type = document.getElementById("op_type").value;
    xhr.onload = onRequestHandler1;
    xhr.send(JSON.stringify({
        "arg1": arg1,
        "arg2": arg2,
        "op_type": op_type
    }));

}

function dateSubmit(event) {
    event.preventDefault();

    const xhr = new XMLHttpRequest();
    xhr.open('POST', `${apiUrl}/services/date-fmt/`);
    xhr.setRequestHeader('Content-Type', 'application/json');
    var date = document.getElementById("date").value;
    var days = document.getElementById("days").value;
    var days_float = parseFloat(days)
    xhr.onload = onRequestHandler2;
    xhr.send(JSON.stringify({
        "date": date,
        "days": days_float
    }));

}


function onRequestHandler1(){
    if (this.readyState == 4 && this.status== 200){
        // 0 = UNSET, no se ah llamado al metodo open
        // 1 = OPENED, se ah llamado al metodo open
        // 2 = HEADERS_RECEIVED, se esta llamando al metodo send()
        // 3 = LOADING, esta recibiendo la respuesta
        // 4 = DONE, la operacion se completo
        const data = JSON.parse(this.response);
        const HTMLResponse = document.querySelector("#calc_app");
        console.log(data["resul"])
        HTMLResponse.innerHTML = data["resul"];}
}

function onRequestHandler2(){
    if (this.readyState == 4 && this.status== 200){
        // 0 = UNSET, no se ah llamado al metodo open
        // 1 = OPENED, se ah llamado al metodo open
        // 2 = HEADERS_RECEIVED, se esta llamando al metodo send()
        // 3 = LOADING, esta recibiendo la respuesta
        // 4 = DONE, la operacion se completo
        const data = JSON.parse(this.response);
        const HTMLResponse = document.querySelector("#date_app");
        HTMLResponse.innerHTML = data["date"];}
}

calcForm.addEventListener('submit', calcSubmit)

dateForm.addEventListener('submit', dateSubmit)

selectApi.addEventListener("change", apiChange);
