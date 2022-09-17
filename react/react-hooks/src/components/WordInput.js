import { useState, useEffect } from 'react';
import { getWords } from '../utils/datamuse';
import AssociatedWords from './AssociatedWords';
import Synonyms from './Synonyms';
import RhymingWords from './RhymingWords';

//function to get synonyms




function WordInput() {
  const [searchWord, setSearchWord] = useState("");
  const [synonymsEntries, setSynonymsEntries] = useState([]);
  const [associatedEntries, setAssociatedEntries] = useState([]);
  const [rhymingEntries, setRhymingEntries] = useState([]);

  useEffect(() => {
    //call getWords with synonym params
    getWords('ml', searchWord, setSynonymsEntries)

    //call getWords with associated words params
    getWords('rel_trg', searchWord, setAssociatedEntries)

    //call getWords with rhyming words params
    getWords('rel_rhy', searchWord, setRhymingEntries)

  }, [searchWord])
  

  return (
    <>
    <input onInput={(e) => setSearchWord(e.target.value)} />
    <div id="lists-container">
      <Synonyms synonymsEntries={synonymsEntries} searchWord={searchWord} />
      <AssociatedWords associatedEntries={associatedEntries} searchWord={searchWord} />
      <RhymingWords rhymingEntries={rhymingEntries} searchWord={searchWord} />
    </div>
    </>
  )

}

export default WordInput;