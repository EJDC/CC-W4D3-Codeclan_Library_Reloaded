from db.run_sql import run_sql

from models.book import Book
from models.author import Author
import repositories.author_repository as author_repository



# CREATE TABLE books (
#   id SERIAL PRIMARY KEY,
#   title VARCHAR(255),
#   description VARCHAR(255),
#   genre INT,
#   checked_out BOOLEAN,
#   author_id INT NOT NULL REFERENCES authors(id)
# );

# post
def save(book):
    sql = "INSERT INTO books (title, description, genre, checked_out, author_id) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [book.title, book.description, book.genre, book.checked_out, book.author.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    return book

# Get
def select_all():
    books = []

    sql = "SELECT * FROM books ORDER BY LOWER(title)"
    results = run_sql(sql)

    for row in results:
        author = author_repository.select(row['author_id'])
        book = Book(row['title'], row['description'], row['genre'], author, row['checked_out'], row['id'])
        books.append(book)
    return books


# Get
def select(id):
    book = None
    sql = "SELECT * FROM books WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        author = author_repository.select(result['author_id'])
        book = Book(result['title'], result['description'], result['genre'], author, result['checked_out'], result['id'])
    return book


def delete_all():
    sql = "DELETE  FROM books"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM books WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(book):
    sql = "UPDATE books SET (title, description, genre, checked_out, author_id) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [book.title, book.description, book.genre, book.checked_out, book.author.id, book.id]
    run_sql(sql, values)


def mark_checked_out(id):
    sql = "UPDATE books SET checked_out = True WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def mark_checked_in(id):
    sql = "UPDATE books SET checked_out = False WHERE id = %s"
    values = [id]
    run_sql(sql, values)



# def mark_checked_out(book):
#     sql = "UPDATE books SET (title, description, genre, checked_out, author_id) = (%s, %s, %s, %s, %s) WHERE id = %s"
#     book.checked_out = True

# def mark_checked_in(book):
#     book.checked_out = False
