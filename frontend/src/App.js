import React, { useEffect, useState } from 'react';
import BookList from './BookList';

const App = () => {
    const [books, setBooks] = useState([]);
    const [error, setError] = useState(null);

    //TODO: Update this peice of code to use axios handling post request to connect to backend
    const fetchBooks = async () => {
        try {
            //TODO: Store the backend host info in config and Improve configuration to support different environments (prod, dev)
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
