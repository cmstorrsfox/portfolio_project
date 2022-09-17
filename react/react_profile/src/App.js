import './App.css';
import { cards } from './components/ProfileCard.js';

function App() {
  return (
    <>
    <h1 className="title">Family Members</h1>
    <div className="App">
      { cards }
    </div>
    </>
  );
}

export default App;
