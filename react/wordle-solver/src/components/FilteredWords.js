import { createRegex } from "../utils/regex-logic";
import wordList from "../utils/wordle-list";

function FilteredWords(props) {
  const filtered = [];
  for (let word of wordList) {
    if(createRegex(props.greenOne.toLowerCase(), props.greenTwo.toLowerCase(), props.greenThree.toLowerCase(), props.greenFour.toLowerCase(), props.greenFive.toLowerCase(), props.yellowOne.toLowerCase(), props.yellowTwo.toLowerCase(), props.yellowThree.toLowerCase(), props.yellowFour.toLowerCase(), props.yellowFive.toLowerCase(), props.incorrectLetters.toLowerCase(), word)) {
      filtered.push(word);
    } else {
      continue;
    }
  }
  return (
    <div id="possible-words">
      <h4>Possible Words</h4>
      <ul id="remaining-word-list">
        {
          filtered.sort().map((word, index) => {
            if(filtered.length === wordList.length) {
              return <li key={index}></li>
            }
            if(filtered.length === 1) {
              return <li className="remaining-word final-word" key={`${word}-${index}`}>{word}</li>
            } else {
              return <li className="remaining-word" key={`${word}-${index}`}>{word}</li>
            }
          })
        }
      </ul>
    </div>
  )
};

export default FilteredWords;