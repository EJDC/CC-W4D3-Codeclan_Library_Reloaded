class Book:

    def __init__(self, title, description, genre, author, checked_out = False, id = None):
        self.title = title
        self.description = description
        self.genre = genre
        self.author = author
        self.checked_out = checked_out
        self.id = id




# CREATE TABLE books (
#   id SERIAL PRIMARY KEY,
#   title VARCHAR(255),
#   description VARCHAR(255),
#   genre INT,
#   checked_out BOOLEAN,
#   author_id INT NOT NULL REFERENCES authors(id)
# );
