function AssociatedWords(props) {
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
        <h3>Words often associated with <span className="search-word">{props.searchWord}</span></h3>
        {
          props.associatedEntries.map((i, index) => {
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
            </div>
            )
          })
        }
      </div>
      </>
    )
  }
}

export default AssociatedWords;