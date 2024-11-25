const apiUrl = 'http://localhost:8000/api/books/';

// Fetch all books
async function getAllBooks() {
    try {
        const response = await fetch(apiUrl);

        if (!response.ok) {
            console.error('Error fetching books:', response.statusText);
            alert('Failed to fetch books. Please try again later.');
            return;
        }

        const data = await response.json(); // Parse the response JSON
        const books = data.results || data; // Handle paginated or non-paginated response

        const booksList = document.getElementById('booksList');
        booksList.innerHTML = ''; // Clear any previous content

        if (!Array.isArray(books)) {
            console.error('Unexpected response format:', books);
            alert('Unexpected response format from the API.');
            return;
        }

        books.forEach(book => {
            const authorNames = book.author.map(author => author.name).join(", "); // Handle authors correctly
            const listItem = document.createElement('li');
            listItem.textContent = `ID: ${book.id}, Title: ${book.title}, Authors: ${authorNames}, Genre: ${book.genre}, Published: ${book.published_date}`;
            booksList.appendChild(listItem);
        });
    } catch (error) {
        console.error('Error fetching books:', error);
        alert('An unexpected error occurred while fetching books.');
    }
}



// Create a new book
async function createBook(event) {
    event.preventDefault();

    const title = document.getElementById("title").value.trim();
    const pages = document.getElementById("pages").value.trim();
    const description = document.getElementById("description").value.trim();
    const authorInput = document.getElementById("author").value.trim();
    const genre = document.getElementById("genre").value;
    const published_date = document.getElementById("published_date").value;

    // Split the comma-separated author input into an array of objects
    const authors = authorInput
        .split(",")
        .map((name) => ({ name: name.trim() }))
        .filter((author) => author.name !== "");

    const bookData = {
        title,
        pages: parseInt(pages),
        description,
        author: authors,
        genre,
        published_date,
    };

    try {
        const response = await fetch("/api/books/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(bookData),
        });

        if (response.ok) {
            const createdBook = await response.json();
            alert("Book created: " + JSON.stringify(createdBook));
        } else {
            const errorData = await response.json();
            alert("Error creating book: " + JSON.stringify(errorData));
        }
    } catch (error) {
        console.error("Error creating book:", error);
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

        // Join all author names into a single string
        const authorNames = book.author.map(author => author.name).join(", ");

        // Render book details in a readable format
        bookDetails.innerHTML = `
            <p><strong>Title:</strong> ${book.title}</p>
            <p><strong>Authors:</strong> ${authorNames}</p>
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



async function editBook(event) {
    event.preventDefault();

    const bookId = document.getElementById("editBookId").value.trim();
    if (!bookId) {
        alert("Please enter a valid Book ID.");
        return;
    }

    const title = document.getElementById("editTitle").value.trim();
    const pages = document.getElementById("editPages").value.trim();
    const description = document.getElementById("editDescription").value.trim();
    const authorInput = document.getElementById("editAuthor").value.trim();
    const genre = document.getElementById("editGenre").value;
    const published_date = document.getElementById("editPublishedDate").value;

    // Split the comma-separated author input into an array of objects
    const authors = authorInput
        .split(",")
        .map((name) => ({ name: name.trim() }))
        .filter((author) => author.name !== "");

    // Build the book update object
    const updatedBook = {};
    if (title) updatedBook.title = title;
    if (pages) updatedBook.pages = parseInt(pages);
    if (description) updatedBook.description = description;
    if (authors.length > 0) updatedBook.author = authors;
    if (genre) updatedBook.genre = genre;
    if (published_date) updatedBook.published_date = published_date;

    try {
        const response = await fetch(`${apiUrl}${bookId}/`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(updatedBook),
        });

        if (!response.ok) {
            const errorData = await response.json();
            alert("Error updating book: " + JSON.stringify(errorData));
            return;
        }

        const updatedBookData = await response.json();
        alert("Book updated successfully: " + JSON.stringify(updatedBookData));
        getAllBooks(); // Refresh the book list
    } catch (error) {
        console.error("Error updating book:", error);
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
