console.log("Script works");

window.onload = function() {

document.getElementById("add-field").addEventListener("click", function() {
    if(check_empties("clone-identificator")) return false;
    var template = document.getElementById("field-template");
    var clone = template.cloneNode(true)
    clone.removeAttribute("id")
    clone.classList.remove("hide");
    clone.classList.add("clone-identificator");
    clone.getElementsByTagName("div")[1].getElementsByClassName("nested")[0].addEventListener("click", function() {
        if(check_empties("sub-nested")) return false;
        if(clone.getElementsByTagName("div")[0].childNodes[0].value && !clone.getElementsByTagName("div")[1].childNodes[0].value) {
            open_nested(this);
        }
    });
    var form = document.getElementById("fields-container").append(clone);
});

/*new Vue({
  el: '#app',
  data: {
    message: 'Hello Vue.js!'
  }
});*/


}

function open_nested(elem) {
    var newrow = document.createElement("div");
    newrow.classList.add("row");
    newrow.classList.add("sub-nested");

    var newcol0 = document.createElement("div");
    newcol0.classList.add("col-lg-2");
    newcol0.classList.add("col-md-2");
    newcol0.classList.add("col-sm-2");
    newcol0.innerHTML = "===>";

    var newinput = document.createElement("input");
    newinput.classList.add("m-auto");

    var newcol1 = document.createElement("div");
    newcol1.classList.add("col-lg-5");
    newcol1.classList.add("col-md-5");
    newcol1.classList.add("col-sm-3");
    newcol1.appendChild(newinput);

    var newcol2 = document.createElement("div");
    newcol2.classList.add("col-lg-5");
    newcol2.classList.add("col-md-5");
    newcol2.classList.add("col-sm-7");
    newcol2.appendChild(newinput.cloneNode(true));

    newrow.appendChild(newcol0);
    newrow.appendChild(newcol1);
    newrow.appendChild(newcol2);

    elem.parentElement.parentElement.parentElement.insertBefore(newrow, elem.parentElement.parentElement.nextElementSibling);
}

function check_empties(name) {
    var i = 0;
    var clones = document.getElementsByClassName(name);
    while(i++ < clones.length) {
        var divs = clones[i-1].getElementsByTagName("div");
        var t = 0;
        while(t++ < divs.length) {
            var div = divs[t-1];
            if(div.childNodes[0].tagName != "INPUT") continue;
            if(!div.childNodes[0].value) {
                return true;
            }
            else {
                return false;
            }
        }
    }
    return false;
}