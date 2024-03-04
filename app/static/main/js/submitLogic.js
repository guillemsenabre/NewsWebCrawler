text = document.getElementById("mainTextContainer");
inputBox = document.getElementById("inputBox");
searchContainer = document.getElementById("searchBarContainer");
submitBtn = document.getElementById("searchBtn");

let isVisible = true;


      // FETCH QUERY DATA FUNCTION //
async function fetchQueryData(query) {

  // Use fetch to send query to Flask route /parse_query
  const response = await fetch("/parse_query", {
    method: 'POST',
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ query }),
  })
  .then(response => response.json())
  .then(data => {
    console.log(data);
    inputBox.value = '';
  })
  .catch(error => {
    console.error('Error fetching data:', error);
  });
}

//If the button is clicked, fetch data (using arrow function)
submitBtn.addEventListener('click', () => {
  query = inputBox.value;
  if (query !== ''){
    fadeOut();
    fetchQueryData();
  }
});

//If the user press enter key (13), fetch data (using anonymous function)
inputBox.addEventListener('keydown', (e) => {
  query = inputBox.value;
  if (e.keyCode === 13 && query !== '') {
    fadeOut();
    fetchQueryData(query);
  }
});




function fadeOut () {
  text.classList.add('disappear');
  searchContainer.classList.add('disappear')
}