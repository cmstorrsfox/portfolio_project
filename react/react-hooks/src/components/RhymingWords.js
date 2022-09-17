function RhymingWords(props) {
  if(props.searchWord === "") {
    return (
      <>
      <div className="word-list-container">
        <h3>This box will show rhyming words</h3>
      </div>
      </>
    )
  } else {
    return (
      <>
      <div className="word-list-container">
        <h3>Words that rhyme with <span className="search-word">{props.searchWord}</span></h3>
        {
          props.rhymingEntries.map((i, index) => {
            return (
              <div className="entry-card" key={`${i.word} - ${index}`}>
                <div className="word-element">
                  <p className="type">Word:</p>
                  <p className="example">{i.word}</p>
                </div>
                <div className="score-element">
                  <p className="type">Score:</p>
                  <p className="example">{i.score}</p>
                </div>
                <div className="pos-element">
                  <p className="type">Number of Syllables:</p>
                  <p className="example">{i.numSyllables}</p>
                </div>
            </div>
            )
          })
        }
      </div>
      </>
    )
  }
}

export default RhymingWords;