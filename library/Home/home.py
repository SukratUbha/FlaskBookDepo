from flask import Blueprint, render_template
from library.adapters.repository import repo_instance, books
import library.adapters.repository as repo
from library.adapters.repository import AbstractRepository

'''have to modify'''
home_blueprint = Blueprint(
    'home_bp', __name__)
# book = create_some_book()
# books = read_datasets()
# all_files = repo_instance
# print(all_files.read_json_files())
# print(books[0].authors)

@home_blueprint.route('/', methods=['GET'])
def home():
    # print(vars(books[0]))
    # print(books[0].book_image)
    # return render_template('simple_book.html',book = book)
    # print(books[0].authors)

    return render_template('home/home2.html', all_books = books)
    # return "<h1> Hello </h1>"

@home_blueprint.route('/Book/<book_id>')
def book_display(book_id: int):
    book_instance = get_book(book_id, repo.repo_instance)
    return render_template('Book Information.html', book = book_instance)

def get_book(id, rep: AbstractRepository):  #put in the repo
    a = rep.get_book_by_id(id)
    return a
