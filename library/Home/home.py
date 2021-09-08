from flask import Blueprint, render_template
from library import create_some_book
import library.utilities.utilities as utilities
from library.adapters.repository import repo_instance
from library.adapters.MemoryRepository import read_datasets
'''have to modify'''
home_blueprint = Blueprint(
    'home_bp', __name__)

# all_files = repo_instance
# print(all_files.read_json_files())
book = create_some_book()
books = read_datasets()
# print(books[0])

@home_blueprint.route('/', methods=['GET'])
def home():
    # return render_template('simple_book.html',book = book)
    return render_template('home/home.html', all_books = books)
    # return "<h1> Hello </h1>"