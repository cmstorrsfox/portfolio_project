const filePicker = document.getElementById("import_path");
const submitBtn = document.getElementById("submit");
const fileList = document.getElementById("file-list");
const fileListContainer = document.getElementById("file-list-container");
const resetBtn = document.getElementById("reset");

//regex
const listening1_2 = new RegExp('(listening1_2(?![A-Za-z])\\d*\\.csv)|(listening1_2_[A-Za-z\\d]*(?!_)\\.csv)');
const listening3 = new RegExp('(listening3(?![A-Za-z])\\d*\\.csv)|(listening3_[A-Za-z\\d]*(?!_)\\.csv)');
const reading = new RegExp('(reading(?![A-Za-z])\\d*\\.csv)|(reading_[A-Za-z\\d]*(?!_)\\.csv)');
const writing = new RegExp('(writing(?![A-Za-z])\\d*\\.csv)|(writing_[A-Za-z\\d]*(?!_)\\.csv)');

function checkFileNames() {
  fileList.innerHTML = ""
  const parent = fileList;    
  for(file of filePicker.files) {
    if(listening1_2.test(file.name) || listening3.test(file.name) || reading.test(file.name) || writing.test(file.name)) {
      const child = document.createElement("li")
      const fileName = document.createTextNode(file.name)
      child.appendChild(fileName);
      parent.appendChild(child);
      child.style.color = "green";
    } else {
      alert(`${file.name} doesn't match the required naming conventions for the app. Rename the file using the examples to help and try again.`)
      const child = document.createElement("li")
      const fileName = document.createTextNode(file.name)
      child.appendChild(fileName);
      parent.appendChild(child);
      child.style.color = "red";
    }
  }

  if(filePicker.files.length % 2 != 0) {
    alert("you've uploaded an odd number of files. Exam sets usually have an even number of exams so you may want to check the files again.")
  }
  fileListContainer.style.display = "block";
}

function resetPage() {
  location.reload()
}

function preventSubmit(event) {
  if(filePicker.files.length < 4) {
    event.preventDefault();
    alert("you need to upload at least 1 exam set. Make sure you have at least one listening 1&2, listening 3, reading and writing exam");
  };
  const listElements = fileListContainer.getElementsByTagName('li');
  for(li of listElements) {
    if(li.style.color === "red") {
      event.preventDefault();
      alert("Check your file names and try again")
    }
  }
}


filePicker.addEventListener("change", checkFileNames);
resetBtn.addEventListener("click", resetPage);
submitBtn.addEventListener("click", preventSubmit);
