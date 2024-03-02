text = document.getElementById("mainTextContainer");
inputBox = document.getElementById("inputBox");
submitBtn = document.getElementById("searchBtn");

let isVisible = true;

//If the button is clicked, fetch data (using arrow function)
submitBtn.addEventListener('click', () => {
  query = inputBox.value;
  if (query != ''){
    textFadeOut();
    fetchQueryData();
  }
});

//If the user press enter key (13), fetch data (using anonymous function)
inputBox.addEventListener('keydown', function(e){
  query = inputBox.value;
  if (e.keyCode === 13 & query != '') {
    textFadeOut();
    fetchQueryData();
  }
});

function fetchQueryData () {
  // Use fetch to send data
  fetch("/process", {
    // ... your fetch options 
  })
  .then(response => response.json())
  .then(data => {
    // Handle the response data
  })
  .catch(error => {
    // Handle any errors
  });
}


function textFadeOut () {
  text.classList.add('disappear');
}