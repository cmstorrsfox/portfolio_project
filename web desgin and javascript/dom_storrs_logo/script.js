const dialOne = document.getElementById('dial-1');
const dialTwo = document.getElementById('dial-2');
const logoContainer = document.getElementById('logo-container');
const trackOne = document.getElementById('track-1');

//page load animations
function onPageLoad() {
  dialOne.style.transition = "all 1000ms ease";
  dialOne.style.transform = "rotate(120deg)";
  dialTwo.style.transition = "all 1500ms ease";
  dialTwo.style.transform = "rotate(-120deg)";

  setTimeout(function() {
    dialOne.style.transition ="all 3000ms ease";
    dialOne.style.transform = "rotate(-120deg)";
  }, 1000);



  setTimeout(function() {
    dialTwo.style.transition = "all 1000ms ease";
    dialTwo.style.transform = "rotate(120deg)";
  }, 1000);

  
  setTimeout(function() {
    dialTwo.style.transition = "all 1000ms ease";
    dialTwo.style.transform = "rotate(0)";
  }, 2000);
};



window.addEventListener('load', onPageLoad);


//dial functions and event listeners
function rotateDials(event) {
  const width = window.innerWidth;
  const height = window.innerHeight;
  const x = Math.round((event.clientX / width) * 120);
  const y = Math.round((event.clientY / height) * 100);


  if(x < 60) {
    dialOne.style.transition = "all 0s linear";
    dialOne.style.transform = `rotate(${-120 + (x*2)}deg)`;
  } else { 
    dialOne.style.transform = "rotate(0deg)";
  }

  if(x > 60) {
    dialTwo.style.transition = "all 0s linear";
    dialTwo.style.transform = `rotate(${-120 + (x*2)}deg)`;
  } else {
    dialTwo.style.transform = "rotate(0deg)";
  }
};

setTimeout( function() {
  document.addEventListener('mousemove', rotateDials);
  }, 2000);

/*  
//play music
function playMusic(event) {
  const width = window.innerWidth;
  const height = window.innerHeight;
  const x = Math.round((event.clientX / width) * 120);
  const y = Math.round((event.clientY / height) * 100);

  if(y >=2 && y <= 20 && x > 30 && x <= 60) {
    trackOne.muted = false; 
    trackOne.play();
    trackOne.volume = ((x - 30) * (0.1/3));
  } else if(y >=2 && y <= 20 && x >= 60 && x < 90) {
    trackOne.muted = false; 
    trackOne.play();
    trackOne.volume = 1 - ((x - 60) * 0.1/3);
  } else {
    trackOne.muted = true;
    trackOne.pause();
  }

}

document.addEventListener('mousemove', playMusic);

*/