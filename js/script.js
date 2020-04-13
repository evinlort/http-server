
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
oReq.open("POST", "new_unit");
oReq.send();