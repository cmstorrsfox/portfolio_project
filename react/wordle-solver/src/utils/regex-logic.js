function createRegex(greenOne, greenTwo, greenThree, greenFour, greenFive, yellowOne, yellowTwo, yellowThree, yellowFour, yellowFive, usedLetters, word) {
  let letterOne = `^${usedLetters}`;
  let letterTwo = `^${usedLetters}`;
  let letterThree = `^${usedLetters}`;
  let letterFour = `^${usedLetters}`;
  let letterFive = `^${usedLetters}`;

  //handles green letter logic
  if(greenOne !== "") {
    letterOne = greenOne;
  };
  
  if(greenTwo !== "") {
    letterTwo = greenTwo;
  };

  if(greenThree !== "") {
    letterThree = greenThree;
  };

  if(greenFour !== "") {
    letterFour = greenFour;
  };

  if(greenFive !== "") {
    letterFive = greenFive;
  };

  //handles yellow letter logic
  if(yellowOne !== "") {
    letterOne += yellowOne;
  };
  
  if(yellowTwo !== "") {
    letterTwo += yellowTwo;
  };

  if(yellowThree !== "") {
    letterThree += yellowThree
  };

  if(yellowFour !== "") {
    letterFour += yellowFour;
  };

  if(yellowFive !== "") {
    letterFive += yellowFive;
  };

  let regex = RegExp(`([${letterOne}][${letterTwo}][${letterThree}][${letterFour}][${letterFive}])`);

  return regex.test(word);

};

export { createRegex };