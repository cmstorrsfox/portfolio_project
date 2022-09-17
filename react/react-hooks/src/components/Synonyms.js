function Synonyms(props) {
  if(props.searchWord === "") {
    return (
      <>
      <div className="word-list-container">
        <h3>This box will show synonyms</h3>
      </div>
      </>
    )
  } else {
    return (
      <>
      <div className="word-list-container">
        <h3>Synonyms of <span className="search-word">{props.searchWord}</span></h3>
        {
          props.synonymsEntries.map((i, index) => {
            return (
              <div className="entry-card" key={`${i.word} - ${index}`}>
                <div className="word-element">
                  <p className="type">Word:</p>
                  <p className="example">{i.word} {i.tags.length > 1 ? `(${i.tags.slice(1).join(", ")})` : ""}</p>
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

export default Synonyms;