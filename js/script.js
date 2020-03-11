console.log("Script works");

window.onload = function() {

document.getElementById("add-field").addEventListener("click", function() {
    var i = 0;
    var clones = document.getElementsByClassName("clone-identificator");
    while(i++ < clones.length) {
        console.log(i-1);
        var divs = clones[i-1].getElementsByTagName("div");
        if(!divs[0].childNodes[0].value || !divs[1].childNodes[0].value) {
            return false;
        }
    }
    var template = document.getElementById("field-template");
    var clone = template.cloneNode(true)
    clone.removeAttribute("id")
    clone.classList.remove("hide");
    clone.classList.add("clone-identificator");
    clone.getElementsByTagName("div")[1].getElementsByClassName("nested")[0].addEventListener("click", function() {
        open_nested(this);
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
    var newcol0 = document.createElement("div");
    newcol0.classList.add("col-lg-2,col-md-2,col-sm-2");
    newcol0.innerHTML = "===>";
    var newinput = document.createElement("input");
    newinput.classList.add("m-auto");
    var newcol1 = document.createElement("div");
    newcol1.classList.add("col-lg-5,col-md-5,col-sm-3");
    newcol1.appendChild(newinput);
    var newcol2 = document.createElement("div");
    newcol2.classList.add("col-lg-5,col-md-5,col-sm-7");
    newcol2.appendChild(newinput.cloneNode(true));
    newrow.appendChild(newcol0);
    newrow.appendChild(newcol1);
    newrow.appendChild(newcol2);
    elem.parentElement.parentElement.parentElement.insertBefore(newrow, elem.parentElement.parentElement.nextElementSibling);
}