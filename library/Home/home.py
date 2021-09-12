from flask import Blueprint, render_template
from library import create_some_book
import library.utilities.utilities as utilities
from library.adapters.repository import repo_instance, books
from library.adapters.MemoryRepository import read_datasets
from library.domain.model import BooksInventory

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
    print(vars(books[0]))
    # return render_template('simple_book.html',book = book)
    # print(books[0].authors[0].full_name)

    return render_template('home/home2.html', all_books = books)
    # return "<h1> Hello </h1>"
