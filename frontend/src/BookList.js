import React from 'react';

const BookList = ({ books }) => {
    return (
        <ul className="book-list">
            <h2>Bookstore List :</h2>
            {books.map((book) => (
                <li key={book.id}>{book.title}</li>
            ))}
        </ul>
    );
};

export default BookList;
