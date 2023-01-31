

document.body.addEventListener('htmx:configRequest', (event) => {
      event.detail.headers['X-CSRFToken'] = '{{ csrf_token }}';
    });

const modal = new bootstrap.Modal(document.getElementById("modal"));
const profmodal = new bootstrap.Modal(document.getElementById("profmodal"));
const planmodal = new bootstrap.Modal(document.getElementById("planmodal"));

htmx.on("htmx:afterSwap", (e) => {
      // Response targeting #dialog => show the modal
      if (e.detail.target.id == "dialog") {
        modal.show()
      };
      if (e.detail.target.id == "profdialog") {
        profmodal.show()
      };
      if (e.detail.target.id == "plandialog") {
        planmodal.show();
      }
});
htmx.on("htmx:beforeSwap", (e) => {
  // Empty response targeting #dialog => hide the modal
  if (e.detail.target.id == "dialog" && !e.detail.xhr.response) {
    modal.hide()
    e.detail.shouldSwap = false
  };
  if (e.detail.target.id == "profdialog" && !e.detail.xhr.response) {
    profmodal.hide()
    e.detail.shouldSwap = false
  };
  if (e.detail.target.id == "plandialog" && !e.detail.xhr.response) {
    planmodal.hide()
    e.detail.shouldSwap = false
  }
});
htmx.on("hidden.bs.modal", () => {
  document.getElementsByClassName("modal-dialog").innerHTML = ""
});