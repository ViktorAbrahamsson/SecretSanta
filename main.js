const inputEl = document.querySelector("#inputEl")
const outputEl = document.querySelector(".output")
const button = document.getElementById("buttonEl")

button.addEventListener("click", () => {
  
  if (inputEl.value == null || inputEl.value == "") {
    return
  }

  if (!outputEl.classList.contains("clicked")) {
    outputEl.classList.add("clicked")
  }
})