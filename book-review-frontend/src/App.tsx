import { useEffect, useState } from "react";
import "./App.css"; // Import the CSS file

interface Review {
  id: number;
  reviewer: string;
  content: string;
  rating: number;
  created_at: string;
}

interface Book {
  id: number;
  title: string;
  author: string;
  reviews?: Review[];
}

function App() {
  const [books, setBooks] = useState<Book[]>([]);
  const [loading, setLoading] = useState(true);
  const [loadingReviews, setLoadingReviews] = useState<number | null>(null);
  const [showBookModal, setShowBookModal] = useState(false);
  const [showReviewModal, setShowReviewModal] = useState<null | number>(null);

  const [title, setTitle] = useState("");
  const [author, setAuthor] = useState("");
  const [reviewer, setReviewer] = useState("");
  const [content, setContent] = useState("");
  const [rating, setRating] = useState<number>();

  const fetchBooks = async () => {
    setLoading(true);
    const res = await fetch("http://localhost:8000/books");
    const data = await res.json();
    setBooks(data);
    setLoading(false);
  };

  useEffect(() => {
    fetchBooks();
  }, []);

  const handleAddBook = async () => {
    await fetch("http://localhost:8000/books", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ title, author }),
    });
    await fetchBooks();
    setShowBookModal(false);
    setTitle("");
    setAuthor("");
  };

  const handleShowReviews = async (bookId: number) => {
    setLoadingReviews(bookId);
    const res = await fetch(`http://localhost:8000/books/${bookId}/reviews`);
    const reviews: Review[] = await res.json();
    setBooks((prev) =>
      prev.map((book) => (book.id === bookId ? { ...book, reviews } : book))
    );
    setLoadingReviews(null);
  };

  const handleAddReview = async (bookId: number) => {
    await fetch(`http://localhost:8000/books/${bookId}/reviews`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ reviewer, content, rating }),
    });
    await handleShowReviews(bookId);
    setShowReviewModal(null);
    setReviewer("");
    setContent("");
    setRating(5);
  };

  return (
    <div className="container">
      <h1>📚 Elegant Book Review App</h1>

      <div style={{ textAlign: "right", marginBottom: "1.5rem" }}>
        <button onClick={() => setShowBookModal(true)} className="btn">
          ➕ Add Book
        </button>
      </div>

      {loading ? (
        <p>Loading books...</p>
      ) : (
        <div className="table-container">
          <table>
            <thead>
              <tr>
                <th>📖 Title</th>
                <th>✍️ Author</th>
                <th>⭐ Reviews</th>
                <th>🛠 Actions</th>
              </tr>
            </thead>
            <tbody>
              {books.map((book) => (
                <tr key={book.id}>
                  <td>{book.title}</td>
                  <td>{book.author}</td>
                  <td>
                    {loadingReviews === book.id ? (
                      <p>Loading...</p>
                    ) : book.reviews ? (
                      book.reviews.length === 0 ? (
                        <p className="text-muted">No reviews yet.</p>
                      ) : (
                        <ul>
                          {book.reviews.map((r) => (
                            <li key={r.id}>
                              <strong>{r.reviewer}</strong>: {r.content} (
                              {r.rating}/5)
                            </li>
                          ))}
                        </ul>
                      )
                    ) : (
                      <button
                        className="btn"
                        onClick={() => handleShowReviews(book.id)}
                      >
                        🔍 Show Reviews
                      </button>
                    )}
                  </td>
                  <td className="actions">
                    <button
                      className="btn"
                      onClick={() => setShowReviewModal(book.id)}
                    >
                      📝 Add Review
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      {/* Book Modal */}
      {showBookModal && (
        <div className="modal">
          <div className="modal-content">
            <h2>Add Book</h2>
            <input
              type="text"
              placeholder="Title"
              value={title}
              onChange={(e) => setTitle(e.target.value)}
            />
            <input
              type="text"
              placeholder="Author"
              value={author}
              onChange={(e) => setAuthor(e.target.value)}
            />
            <div style={{ textAlign: "right" }}>
              <button
                className="btn"
                onClick={handleAddBook}
                style={{ marginRight: "10px" }}
              >
                Add
              </button>
              <button className="btn" onClick={() => setShowBookModal(false)}>
                Cancel
              </button>
            </div>
          </div>
        </div>
      )}

      {/* Review Modal */}
      {showReviewModal && (
        <div className="modal">
          <div className="modal-content">
            <h2>Add Review</h2>
            <input
              type="text"
              placeholder="Reviewer Name"
              value={reviewer}
              onChange={(e) => setReviewer(e.target.value)}
            />
            <textarea
              placeholder="Review Content"
              value={content}
              onChange={(e) => setContent(e.target.value)}
            />
            <input
              type="number"
              placeholder="Rating (1-5)"
              min={1}
              max={5}
              value={rating}
              onChange={(e) => setRating(parseInt(e.target.value))}
            />
            <div style={{ textAlign: "right" }}>
              <button
                className="btn"
                onClick={() => handleAddReview(showReviewModal)}
                style={{ marginRight: "10px" }}
              >
                Submit
              </button>
              <button
                className="btn"
                onClick={() => setShowReviewModal(null)}
              >
                Cancel
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
