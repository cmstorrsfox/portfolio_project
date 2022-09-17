const postPreview = document.getElementById('post-preview');
const titlePreview = document.getElementById('title-preview');
const contentPreview = document.getElementById('content-preview');
const namePreview = document.getElementById('name-preview');
const titleInput = document.getElementById('title');
const contentInput = document.getElementById('content');
const nameInput = document.getElementById('name');
const backgroundInput = document.getElementById('background_img');
const fontInput = document.getElementById('font');
const redInput = document.getElementById('red');
const greenInput = document.getElementById('green');
const blueInput = document.getElementById('blue');
const submitBtn = document.getElementById('submit-btn')

const color = `rgb(${redInput.value}, ${greenInput.value}, ${blueInput.value})`;
console.log(color);

//functions
function updateTitle(event) {
  titlePreview.innerHTML = event.target.value
}

function updateContent(event) {
  contentPreview.innerHTML = event.target.value
}

function updateName(event) {
  namePreview.innerHTML = event.target.value
}

function updateBackground(event) {
  postPreview.style.backgroundImage = `url(${event.target.value})`;
  postPreview.style.backgroundSize = "cover";
}

function updateFont(event) {
  postPreview.style.fontFamily = event.target.value;
}

function updateColor(event, red, green, blue) {
  red = redInput.value;
  green = greenInput.value;
  blue = blueInput.value;
  postPreview.style.color = `rgb(${red}, ${green}, ${blue})`;
}



//event listeners
titleInput.addEventListener('change', updateTitle);
contentInput.addEventListener('change', updateContent);
nameInput.addEventListener('change', updateName);
backgroundInput.addEventListener('change', updateBackground);
fontInput.addEventListener('change', updateFont);
redInput.addEventListener('change', updateColor);
greenInput.addEventListener('change', updateColor);
blueInput.addEventListener('change', updateColor);
