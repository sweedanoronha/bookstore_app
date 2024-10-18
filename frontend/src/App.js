import React, { useEffect, useState } from 'react';
import BookList from './BookList';

const App = () => {
    const [books, setBooks] = useState([]);
    const [error, setError] = useState(null);

    const fetchBooks = async () => {
        try {
            const response = await fetch('http://localhost:8000/books'); // FastAPI backend URL
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            const data = await response.json();
            setBooks(data);
        } catch (error) {
            setError(error.message);
        }
    };

    useEffect(() => {
        fetchBooks(); // Fetch books on component mount
    }, []);

    return (
        <div className="container">
            <h1>Bookstore App</h1>
            {error && <div className="error-message">{error}</div>}
            <BookList books={books} />
        </div>
    );
};

export default App;
