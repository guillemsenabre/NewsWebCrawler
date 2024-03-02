text = document.getElementById("mainTextContainer");
inputBox = document.getElementById("inputBox");
let isVisible = true;


inputBox.addEventListener('submit', function() {
  if (isVisible) {
    text.classList.add('disappear');
    text.classList.remove('appear');
    isVisible = false;
  }
  else {
    text.classList.add('appear');
    text.classList.remove('disappear');
    isVisible = true;
  }
});