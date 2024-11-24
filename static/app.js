const apiUrl = 'http://localhost:8000/api/books/';

// Fetch all books
async function getAllBooks() {
    try {
        const response = await fetch(apiUrl);
        const books = await response.json();
        const booksList = document.getElementById('booksList');
        booksList.innerHTML = '';
        books.forEach(book => {
            const listItem = document.createElement('li');
            listItem.textContent = `ID: ${book.id}, Title: ${book.title}, Author: ${book.author}, Genre: ${book.genre}, Published: ${book.published_date}`;
            booksList.appendChild(listItem);
        });
    } catch (error) {
        console.error('Error fetching books:', error);
    }
}

// Create a new book
async function createBook(event) {
    event.preventDefault();
    const title = document.getElementById('title').value;
    const pages = document.getElementById('pages').value;
    const description = document.getElementById('description').value;
    const author = document.getElementById('author').value;
    const genre = document.getElementById('genre').value;
    const published_date = document.getElementById('published_date').value;

    try {
        const response = await fetch(apiUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ title, pages, description, author, genre, published_date })
        });
        const newBook = await response.json();
        alert('Book created: ' + JSON.stringify(newBook));
        getAllBooks();
    } catch (error) {
        console.error('Error creating book:', error);
    }
}

// Fetch a single book by ID
async function getBook() {
    const bookId = document.getElementById('bookId').value.trim();
    const bookDetails = document.getElementById('bookDetails');
    bookDetails.textContent = ''; // Clear previous results

    if (!bookId) {
        alert('Please enter a valid Book ID.');
        return;
    }

    try {
        const response = await fetch(`${apiUrl}${bookId}/`);

        if (response.status === 404) {
            alert('Book not found');
            return;
        }

        if (!response.ok) {
            // Handle other non-200 status codes
            alert('Something went wrong while fetching the book.');
            console.error(`Error: ${response.status} - ${response.statusText}`);
            return;
        }

        const book = await response.json();

        // Render book details in a readable format
        bookDetails.innerHTML = `
            <p><strong>Title:</strong> ${book.title}</p>
            <p><strong>Author:</strong> ${book.author}</p>
            <p><strong>Pages:</strong> ${book.pages}</p>
            <p><strong>Genre:</strong> ${book.genre}</p>
            <p><strong>Description:</strong> ${book.description}</p>
            <p><strong>Published Date:</strong> ${book.published_date}</p>
        `;
    } catch (error) {
        alert('An error occurred while fetching the book. Please try again.');
        console.error('Error fetching book:', error);
    }
}


// Update a book by ID
async function updateBook() {
    const bookId = document.getElementById('bookId').value;
    if (!bookId) {
        alert('Please enter a Book ID.');
        return;
    }

    const title = prompt('Enter new title:');
    const pages = prompt('Enter new number of pages:');
    const description = prompt('Enter new description:');
    const author = prompt('Enter new author:');
    const genre = prompt('Enter new genre:');
    const published_date = prompt('Enter new published date (YYYY-MM-DD):');

    try {
        const response = await fetch(`${apiUrl}${bookId}/`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ title, pages, description, author, genre, published_date })
        });
        if (response.status === 404) {
            alert('Book not found');
            return;
        }
        const updatedBook = await response.json();
        alert('Book updated: ' + JSON.stringify(updatedBook));
        getAllBooks();
    } catch (error) {
        console.error('Error updating book:', error);
    }
}

// Delete a book by ID
async function deleteBook() {
    const bookId = document.getElementById('bookId').value;
    if (!bookId) {
        alert('Please enter a Book ID.');
        return;
    }

    try {
        const response = await fetch(`${apiUrl}${bookId}/`, {
            method: 'DELETE'
        });
        if (response.status === 404) {
            alert('Book not found');
            return;
        }
        alert('Book deleted');
        getAllBooks();
    } catch (error) {
        console.error('Error deleting book:', error);
    }
}
