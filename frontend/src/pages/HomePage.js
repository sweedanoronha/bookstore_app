// main page where you show the book list and add new books
import React from 'react';
import BookList from '../components/books/BookList';

const HomePage = () => {
  return (
    <div className="container">
      <BookList />
    </div>
  );
};

export default HomePage;
