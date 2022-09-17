import './ProfileCard.css';
import profiles from '../data/profiles.js';


function createProfileCard(imageUrl, fullName, age, gender) {
  return (
    <div key={fullName} className={`${gender==="Male" ? "profile-card male": "profile-card female"}`}>
      <div className='profile-pic'>
        <img className='photo' alt={`profile pic for ${fullName}`} src={(`${process.env.PUBLIC_URL}${imageUrl}`)}></img>
      </div>
      <div className='profile-info'>
        <h3>Name: {fullName}</h3>
        <h4>Age: {age}</h4>
        <h4>Gender: {gender}</h4>
      </div>
    </div>
  );

}

const cards = profiles.map((profile) => createProfileCard(profile.imageUrl, profile.name, profile.age, profile.gender))


export { cards };