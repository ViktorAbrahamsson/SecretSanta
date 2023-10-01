console.log(`  *  .  . *       *    .        .        .   *    ..
.    *        .   ###     .      .        .            *
   *.   *        #####   .     *      *        *    .
 ____       *  ######### *    .  *      .        .  *   .
/   /\  .     ###\#|#/###   ..    *    .      *  .  ..  *
/___/  ^8/      ###\|/###  *    *            .      *   *
|   ||%%(        # }|{  #
|___|,  \\  ejm    }|{`, "God jul önskar Viktor & Gustav!");

const keyAndLengthOffset = 100;

const decrypt = (name) => {
  const name_array = [];
  for (const l of name) {
      name_array.push(l.charCodeAt(0));
  }
  let out_name = "";
  const key = name_array[0] - keyAndLengthOffset;
  const length = name_array[1] - keyAndLengthOffset;
  let iteration = -1;
  const skip_first = 2;
  for (const l of name_array) {
      iteration++;
      if (iteration < skip_first) {
          continue;
      }
      if (iteration - skip_first >= length) {
          return out_name;
      }
      out_name += String.fromCharCode(l - key);
  }
};

const decryptAndDisplay = () => {
  const inputString = document.getElementById("inputString").value;
  const decryptedString = decrypt(inputString, keyAndLengthOffset);
  document.querySelector(".output").textContent = decryptedString;
};

document.querySelector(".decryptButton").addEventListener("click", decryptAndDisplay);

document.addEventListener("keydown", (event) => {
  if (event.key === "Enter") {
      event.preventDefault();
      decryptAndDisplay();
  }
});