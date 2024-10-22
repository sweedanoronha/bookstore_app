// fetches and displays the list of books from the backend
import React, { useEffect, useState } from 'react';
import booksApi from '../../api/booksApi';  // Axios instance

const BookList = () => {
  const [books, setBooks] = useState([]);
  const [error, setError] = useState(null);

  // Fetch book data from backend
  const fetchBooks = async () => {
    try {
      const response = await booksApi.get();
      setBooks(response.data);
    } catch (err) {
      setError('Failed to fetch books');
      console.error(err);
    }
  };

  useEffect(() => {
    fetchBooks();
  }, []);

  return (
    <div>
      <h2>Book List</h2>      
      {error && <div className="error-message">{error}</div>}
      <ul className="book-list">
        {books.map((book) => (
          <li key={book.id}>{book.title}</li>
        ))}
      </ul>
    </div>
  );
};

export default BookList;
