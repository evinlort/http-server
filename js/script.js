
console.log("Script works");

window.addEventListener('DOMContentLoaded', function(){
    var myDatepicker = document.querySelector('input[name="expiration"]');
    myDatepicker.DatePickerX.init({
        format           : 'yyyy-mm-dd',
        mondayFirst      : false,
    });
});

var oReq = new XMLHttpRequest();
oReq.responseType = "json";
oReq.onreadystatechange = function() {
    if (oReq.readyState === 4) {
    build_options(oReq.response);
    }
}
oReq.open("POST", "get_units");
oReq.send();

function build_options(response) {
    var unit_list = document.getElementById("units-list");
    console.log(response);
    response.forEach(function(val){
        var option = document.createElement("OPTION");
        option.setAttribute("value", val);
        unit_list.appendChild(option);
    });
}