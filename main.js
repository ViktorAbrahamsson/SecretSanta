// const inputEl = document.querySelector("#inputEl")
// const outputEl = document.querySelector(".output")
// const button = document.getElementById("buttonEl")

// button.addEventListener("click", () => {
  
//   if (inputEl.value == null || inputEl.value == "") {
//     return
//   }

//   if (!outputEl.classList.contains("clicked")) {
//     outputEl.classList.add("clicked")
//   }
// })


function decrypt(name, keyAndLengthOffset) {
  const nameArray = [];
  for (const l of name) {
      nameArray.push(l.charCodeAt(0));
  }
  let outName = "";
  const key = nameArray[0] - keyAndLengthOffset;
  const length = nameArray[1] - keyAndLengthOffset;
  let iteration = -1;
  const skipFirst = 2;
  for (const l of nameArray) {
      iteration++;
      if (iteration < skipFirst) {
          continue;
      }
      if (iteration - skipFirst >= length) {
          return outName;
      }
      outName += String.fromCharCode(l - key);
  }
  return outName;
}

document.getElementById("buttonEl").addEventListener("click", function () {
  const keyAndLengthOffset = 100; // You can adjust this value as needed
  const inputString = document.getElementById("inputEl").value;
  const decryptedString = decrypt(inputString, keyAndLengthOffset);
  document.querySelector(".output").textContent = decryptedString;
});