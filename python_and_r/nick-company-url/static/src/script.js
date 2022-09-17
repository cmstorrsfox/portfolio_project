const form = document.getElementById('form');
const infoBox = document.getElementById('info-box');
const cockroach = document.getElementById('cockroach');
const audio = document.getElementById('audio-play');
const reset = document.getElementById('reset');


function startAudio(evt) {
  if(audio.paused) {
    audio.play();
    cockroach.classList.add('shakeshake');

  } else {
    audio.pause();
    cockroach.classList.remove('shakeshake');
  }
}

function reloadPage(evt) {
  event.preventDefault();
  window.location.href = window.location.href;
} 


cockroach.addEventListener('click', startAudio);
reset.addEventListener('click', reloadPage);