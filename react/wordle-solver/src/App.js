import './App.css';
import InputBars from './components/InputBars';



function App() {
  return (
    <div className="App">
      <h1 className='title'>Wordle Solver</h1>
      <h3 className='caption'>Stuck on today's Wordle? <br /><br />Use the boxes below to see some helpful suggestions</h3>
      <InputBars />
    </div>
  );
}

export default App;
