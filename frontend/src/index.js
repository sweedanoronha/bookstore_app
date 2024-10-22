// entry point of the React app
import React from 'react';
import ReactDOM from 'react-dom';
import './assets/styles/index.css';
import HomePage from './pages/HomePage';
import Header from './components/layout/Header';

const App = () => {
  return (
    <div>
      <Header />
      <HomePage />
    </div>
  );
};

ReactDOM.render(<App />, document.getElementById('root'));
