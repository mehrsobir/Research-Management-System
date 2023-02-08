
document.body.addEventListener('htmx:configRequest', (event) => {
      event.detail.headers['X-CSRFToken'] = '{{ csrf_token }}';
    });


//const modal = new bootstrap.Modal(document.getElementById("modal"));
//
//htmx.on("htmx:afterSwap", (e) => {
//      // Response targeting #dialog => show the modal
//      if (e.detail.target.id == "dialog") {
//        modal.show()
//      };
//
//});
//htmx.on("htmx:beforeSwap", (e) => {
//  // Empty response targeting #dialog => hide the modal
//  console.log(e.detail.target.id.startsWith("st"))
//  if (e.detail.target.id.startsWith("st") == true) {
//    modal.hide()
////    e.detail.shouldSwap = false
//  };

//});
//htmx.on("hidden.bs.modal", () => {
//  document.getElementsByClassName("modal-dialog").innerHTML = ""
//});