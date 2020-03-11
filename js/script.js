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
    clone.classList.add("clone-identificator")
    var form = document.getElementById("fields-container").append(clone);
});

/*new Vue({
  el: '#app',
  data: {
    message: 'Hello Vue.js!'
  }
});*/


}