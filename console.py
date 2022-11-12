import pdb
from models.book import Book
from models.author import Author

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

book_repository.delete_all()
author_repository.delete_all()

author1 = Author("Joanne", "Rowling")
author_repository.save(author1)
author2 = Author("George", "Martin")
author_repository.save(author2)

# print(author_repository.select_all())
# # Can save and author and show an authoris id
# print(author_repository.select(37).id)

# CREATE TABLE books (
#   id SERIAL PRIMARY KEY,
#   title VARCHAR(255),
#   description VARCHAR(255),
#   genre VARCHAR(255),
#   checked_out BOOLEAN,
#   author_id INT NOT NULL REFERENCES authors(id)
# );



author_repository.select_all()

book_1 = Book("Harry Potter", "Child becomes wizard saves world etc", "Childrens", author1, False)
book_repository.save(book_1)

book_2 = Book("Lord of the Rings", "4 Hobbits and a wizard set out to save the world etc", "Fantasy", author2, False )
book_repository.save(book_2)

pdb.set_trace()
