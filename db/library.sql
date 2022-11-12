DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS authors;

CREATE TABLE authors (
  id SERIAL PRIMARY KEY,
  first_name VARCHAR(255),
  last_name VARCHAR(255)
);

CREATE TABLE books (
  id SERIAL PRIMARY KEY,
  title VARCHAR(255),
  description VARCHAR(255),
  genre VARCHAR(255),
  author_id INT NOT NULL REFERENCES authors(id),
  checked_out BOOLEAN
);
