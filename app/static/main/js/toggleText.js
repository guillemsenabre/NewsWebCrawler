const toggleWords = ['Companies', 'Events', 'News'];
let currentIndex = 0;

function toggleText () {
  document.getElementById("toggleText").innerHTML = toggleWords[currentIndex];
  currentIndex = (currentIndex + 1) % toggleWords.length;
}

setInterval(toggleText, 2500);