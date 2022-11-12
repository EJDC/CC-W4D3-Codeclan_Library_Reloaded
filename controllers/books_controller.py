# Import Flask and render_template
from flask import Flask, render_template, request, redirect

# Import Blueprint class from flask
from flask import Blueprint

# Import Book and Author Repository
from repositories import author_repository, book_repository

# Import Book Class
from models.book import Book

import pdb

# Create a new instance of Blueprint called "books"
books_blueprint = Blueprint("books", __name__)

# Declare a route for the list of books
@books_blueprint.route("/books")
def books():
    books = book_repository.select_all()
    authors = author_repository.select_all()
    # pdb.set_trace()
    return render_template("books/index.html", all_books = books, all_authors = authors)

    # controllers/books_controller.py

# NEW
# GET '/books/new'
@books_blueprint.route("/books/new")
def new_book():
    authors = author_repository.select_all()
    return render_template("books/new.html", all_authors = authors)

# CREATE
# POST '/books'
@books_blueprint.route("/books", methods =["POST"])
def create_book():
    title       = request.form['title']
    description = request.form['description']
    genre       = request.form['genre']
    author_id     = request.form['author_id']
    checked_out = request.form['checked_out']
    author        = author_repository.select(author_id)
    book        = Book(title, description, genre, author, checked_out)
    book_repository.save(book)
    return redirect('/books')
    # def __init__(self, title, description, genre, author, checked_out = False, id = None):

# SHOW
# GET '/books/<id>'
@books_blueprint.route("/books/<id>")
def show_book(id):
    book = book_repository.select(id)
    return render_template('books/book.html', book = book)

# EDIT
# GET '/books/<id>/edit'
@books_blueprint.route("/books/<id>/edit")
def edit_book(id):
    book = book_repository.select(id)
    authors = author_repository.select_all()
    return render_template('books/edit.html', book = book, all_authors = authors)
    

# UPDATE
# PUT '/books/<id>'
@books_blueprint.route("/books/<id>", methods=['POST'])
def update_book(id):
    title       = request.form['title']
    description = request.form['description']
    genre       = request.form['genre']
    author_id   = request.form['author_id']
    checked_out = request.form['checked_out']
    author      = author_repository.select(author_id)
    book        = Book(title, description, genre, checked_out, author)
    book_repository.update(book)
    return redirect('/books')

# DELETE
# DELETE '/books/<id>'
@books_blueprint.route("/books/<id>/delete", methods =["POST"])
def delete_book(id):
    book_repository.delete(id)
    return redirect('/books')


@books_blueprint.route('/books/check_in/<id>', methods=['POST'])
def checkin_book(id):
    book_repository.mark_checked_in(id)
    return redirect(request.referrer)

@books_blueprint.route('/books/check_out/<id>', methods=['POST'])
def checkout_book(id):
    book_repository.mark_checked_out(id)
    return redirect(request.referrer)