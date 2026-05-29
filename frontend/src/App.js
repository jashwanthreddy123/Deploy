import React, { useEffect, useState } from 'react';
import './App.css';

function App() {
  const [message, setMessage] = useState('Loading...');

  useEffect(() => {
    fetch('http://backend-service:5000')
      .then((res) => res.json())
      .then((data) => setMessage(data.message))
      .catch(() => setMessage('Backend connection failed'));
  }, []);


  return (
    <div className="container">
      <h1>DevOps Practice Project</h1>
      <p>{message}</p>
    </div>
  );
}

export default App;
