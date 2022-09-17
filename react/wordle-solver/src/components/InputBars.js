import { useEffect, useState } from "react";
import FilteredWords from "./FilteredWords";

function InputBars() {
  //state setters for 'green' input field
  const [greenOne, setGreenOne] = useState("");
  const [greenTwo, setGreenTwo] = useState("");
  const [greenThree, setGreenThree] = useState("");
  const [greenFour, setGreenFour] = useState("");
  const [greenFive, setGreenFive] = useState("");

  //state setter for 'yellow' input field
  const [yellowOne, setYellowOne] = useState("");
  const [yellowTwo, setYellowTwo] = useState("");
  const [yellowThree, setYellowThree] = useState("");
  const [yellowFour, setYellowFour] = useState("");
  const [yellowFive, setYellowFive] = useState("");

  //state setter for remaining letters input field
  const [incorrectLetters, setIncorrectLetters] = useState('');


  return (
    <>
    <div id="form-container">
      <form key="green-form" id="green-form">
        <fieldset>
          <legend>Green Letters</legend>
          <input name="letter-one" id='green-one' type='text' className="green-input" maxLength={1} value={greenOne.toUpperCase()} onInput={e => setGreenOne(e.target.value)} />
          <input name="letter-two" id='green-two' type='text' className="green-input" maxLength={1} value={greenTwo.toUpperCase()} onInput={e => setGreenTwo(e.target.value)} />
          <input name="letter-three" id='green-three' type='text' className="green-input" maxLength={1} value={greenThree.toUpperCase()} onInput={e => setGreenThree(e.target.value)} />
          <input name="letter-four" id='green-four' type='text' className="green-input" maxLength={1} value={greenFour.toUpperCase()} onInput={e => setGreenFour(e.target.value)} />
          <input name="letter-five" id='green-five' type='text' className="green-input" maxLength={1} value={greenFive.toUpperCase()} onInput={e => setGreenFive(e.target.value)} />
        </fieldset>
      </form>
      <form key="yellow-form" id="yellow-form">
        <fieldset>
          <legend>Yellow Letters</legend>
          <input name="letter-one" id='yellow-one' type='text' className="yellow-input" value={yellowOne.toUpperCase()} onInput={e => setYellowOne(e.target.value)} />
          <input name="letter-two" id='yellow-two' type='text' className="yellow-input" value={yellowTwo.toUpperCase()} onInput={e => setYellowTwo(e.target.value)} />
          <input name="letter-three" id='yellow-three' type='text' className="yellow-input" value={yellowThree.toUpperCase()} onInput={e => setYellowThree(e.target.value)} />
          <input name="letter-four" id='yellow-four' type='text' className="yellow-input" value={yellowFour.toUpperCase()} onInput={e => setYellowFour(e.target.value)} />
          <input name="letter-five" id='yellow-five' type='text' className="yellow-input" value={yellowFive.toUpperCase()} onInput={e => setYellowFive(e.target.value)} />
        </fieldset>
      </form>
      <form key="remaining-form" id="remaining-form">
        <fieldset>
          <legend>Incorrect Letters</legend>
          <input type="text" id="incorrect-letters" placeholder="enter your incorrect letters here" value={incorrectLetters.toUpperCase()} onInput={e => setIncorrectLetters(e.target.value)} />
        </fieldset>
      </form>
    </div>
    <FilteredWords 
      greenOne={greenOne}
      greenTwo={greenTwo}
      greenThree={greenThree}
      greenFour={greenFour}
      greenFive={greenFive}
      yellowOne={yellowOne}
      yellowTwo={yellowTwo}
      yellowThree={yellowThree}
      yellowFour={yellowFour}
      yellowFive={yellowFive}
      incorrectLetters={incorrectLetters} />
    </>
  )
}

export default InputBars;