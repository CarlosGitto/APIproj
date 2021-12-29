// Initial value of Api
var apiUrl = "http://127.0.0.1:8000";

//Form of calculator
const calcForm = document.querySelector("#calc_service");

//Form of date_calculator
const dateForm = document.querySelector('#date_service');

//Select of api
const selectApi = document.querySelector('#url_choice');

// Initial value of vars on onHandlerRequest function
var logId = "#calc_app";
var resulKey = "resul";


function apiChange(){
    /*
    Change the var url_choice to
    use the correct api
    */
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
    /*
    Make a prevent deafault submit and 
    send a POST request with the data submited
    to an api selected
    */
    event.preventDefault();

    logId = "#calc_app";
    resulKey = "resul";

    const xhr = new XMLHttpRequest();
    xhr.open('POST', `${apiUrl}/services/calculator/`);
    console.log(apiUrl)
    xhr.setRequestHeader('Content-Type', 'application/json');
    var arg1 = document.getElementById("arg1").value;
    var arg2 = document.getElementById("arg2").value;
    var op_type = document.getElementById("op_type").value;
    xhr.onload = onRequestHandler;
    xhr.send(JSON.stringify({
        "arg1": arg1,
        "arg2": arg2,
        "op_type": op_type
    }));

}

function dateSubmit(event) {
    /*
    Make a prevent deafault submit and 
    send a POST request with the data submited
    to an api selected
    */
    event.preventDefault();

    logId = "#date_app";
    resulKey = "date";

    const xhr = new XMLHttpRequest();
    xhr.open('POST', `${apiUrl}/services/date-fmt/`);
    xhr.setRequestHeader('Content-Type', 'application/json');
    var date = document.getElementById("date").value;
    var days = document.getElementById("days").value;
    var days_float = parseFloat(days)
    xhr.onload = onRequestHandler;
    xhr.send(JSON.stringify({
        "date": date,
        "days": days_float
    }));

}


function onRequestHandler(){
    /*
    Return the response of a succesful POST 
    in CALCULATOR service and put it in on the page
    */
    if (this.readyState == 4 && this.status== 200){
        // 0 = UNSET, no se ah llamado al metodo open
        // 1 = OPENED, se ah llamado al metodo open
        // 2 = HEADERS_RECEIVED, se esta llamando al metodo send()
        // 3 = LOADING, esta recibiendo la respuesta
        // 4 = DONE, la operacion se completo
        const data = JSON.parse(this.response);
        const HTMLResponse = document.querySelector(logId);
        console.log(data[resulKey])
        HTMLResponse.innerHTML = data[resulKey];}
}



// Call the calcSubmit function when submit values in the Calculator
calcForm.addEventListener('submit', calcSubmit)

// Call the dateSubmit function when submit values in DateCalculator
dateForm.addEventListener('submit', dateSubmit)

// Call the apiChange function when change values in api selector
selectApi.addEventListener("change", apiChange);
