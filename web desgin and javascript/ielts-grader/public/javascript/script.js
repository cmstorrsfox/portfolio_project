const whatWeOffer = document.getElementById('what-we-offer');
const ourPrices = document.getElementById('our-prices');
const contactUs = document.getElementById('contact-us');
const branding = document.getElementById('branding');
const offerLink = document.getElementById('what-we-offer-link');
const priceLink = document.getElementById('our-prices-link');
const contactLink = document.getElementById('contact-us-link');
const taskTypeSelector = document.getElementById('task-type-selector');
const writingTaskDiv = document.getElementById('writing-task-div');
const speakingTaskDiv = document.getElementById('speaking-task-div');
const step3 = document.getElementById('step-3');
const logInBtn = document.getElementById('log-in-btn');
const screenSizeWarning = document.getElementById('device-warning');
const writingSubmitBtn = document.getElementById('writing-submit');
const speakingSubmitBtn = document.getElementById('speaking-submit');
const dateTime = document.getElementById('datetime');

const goToPrices = (event) => {
  const url = window.location.href;
  if(url == "https://www.gradeielts.com/") {
    ourPrices.scrollIntoView({ behavior: "smooth", block: "start"});
    event.preventDefault();
  } else {
    location.href = "https://www.gradeielts.com/#our-prices";
  }

};

priceLink.addEventListener("click", goToPrices);


const goToOffer = (event) => {
  const url = window.location.href;
  if(url == "https://www.gradeielts.com/") {
  whatWeOffer.scrollIntoView({ behavior: "smooth", block: "start"});
  event.preventDefault();
  } else {
    location.href = "https://www.gradeielts.com/#what-we-offer"
  }
};

offerLink.addEventListener("click", goToOffer);

const goToContact = (event) => {
  const url = window.location.href;
  if(url == "https://www.gradeielts.com/") {
  contactUs.scrollIntoView({ behavior: "smooth", block: "start"});
  event.preventDefault();
  } else {
    location.href = "https://www.gradeielts.com/#contact-us"
  }
};

contactLink.addEventListener("click", goToContact);

const scrollToTop = (event) => {
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

branding.addEventListener('click', scrollToTop);


//task-type selector
function renderTaskType() {
  if(taskTypeSelector.value === 'writing') {
    writingTaskDiv.style.display = "flex";
    speakingTaskDiv.style.display = "none";
    step3.style.display = "flex";
    step3.innerHTML = "Step 3 - Complete the writing tasks below then click 'Submit'"
  } else if (taskTypeSelector.value == 'speaking') {
    speakingTaskDiv.style.display = "flex";
    writingTaskDiv.style.display = "none";
    step3.style.display = "flex";
    step3.innerHTML = "Step 3 - To give an accurate idea of a Speaking score we need to do a face-to-face assessment. Click 'Contact Us' below and one of our experts will be in touch shortly."
  } else {
    speakingTaskDiv.style.display = "none";
    writingTaskDiv.style.display = "none";
    step3.style.display = "none";
  }
};

//display log in btn
if(logInBtn.innerHTML == "") {
  logInBtn.style.display = 'none';
}

//show device warning for writing section
if(window.innerWidth >= 768) {
  screenSizeWarning.style.display = "none";

}

//get date on form submission
const getDate = () => {
  let d = new Date().toLocaleString("en-US", { timeZone: "Europe/London" });
  datetime.value = d;
}

writingSubmitBtn.addEventListener('click', getDate);
speakingSubmitBtn.addEventListener('click', getDate);

