import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [movie, setMovie] = useState(null);

  useEffect(() => {
    // Fetch the recommended movie from your backend when the component mounts
    axios.get(process.env.REACT_APP_BACKEND_URL)
      .then(response => setMovie(response.data));
  }, []);

  // If the movie data has not been loaded yet, display a loading message
  if (!movie) {
    return <div>Loading...</div>;
  }

  // Once the movie data has been loaded, display the movie recommendation
  return (
    <div className="App">
      <header className="App-header">
        <img src={movie.poster_path} alt={movie.title} style={{width: "350px"}}/>
        <h2>{movie.title}</h2>
        <p>{movie.overview}</p>
      </header>
    </div>
  );
}

export default App;
