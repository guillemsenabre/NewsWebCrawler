text = document.getElementById("mainTextContainer");
inputBox = document.getElementById("inputBox");
submitBtn = document.getElementById("searchBtn");

let isVisible = true;

//If the button is clicked, fetch data (using arrow function)
submitBtn.addEventListener('click', () => {
  query = inputBox.value;
  if (query !== ''){
    textFadeOut();
    fetchQueryData();
  }
});

//If the user press enter key (13), fetch data (using anonymous function)
inputBox.addEventListener('keydown', function(e){
  query = inputBox.value;
  if (e.keyCode === 13 && query !== '') {
    textFadeOut();
    fetchQueryData(query);
  }
});

async function fetchQueryData(query) {

  // Use fetch to send query to Flask route /parse_query
  const response = await fetch("/parse_query", {
    method: 'POST',
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ query }),
  })
  .then(response => response.json())
  .then(data => {
    console.log(data.query);
    inputBox.value = '';
  })
  .catch(error => {
    console.error('Error fetching data:', error);
  });
}


function textFadeOut () {
  text.classList.add('disappear');
}