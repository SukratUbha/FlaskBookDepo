from flask import Flask, render_template
import library.adapters.repository as repo
from pathlib import Path
from library.domain.model import Book
from library.adapters.MemoryRepository import MemoryRepository, read_datasets

def create_some_book():
    some_book = Book(1, "Harry Potter and the Chamber of Secrets")
    some_book.description = "Ever since Harry Potter had come home for the summer, the Dursleys had been so mean \
                             and hideous that all Harry wanted was to get back to the Hogwarts School for \
                             Witchcraft and Wizardry. But just as he’s packing his bags, Harry receives a \
                             warning from a strange impish creature who says that if Harry returns to Hogwarts, \
                             disaster will strike."
    some_book.release_year = 1999
    return some_book
    # Configure the app from configuration-file settings.


def create_app(test_config=None):
    app = Flask(__name__)

    app.config.from_object('config.Config')

    if test_config is not None:
        # Load test configuration, and override any configuration settings.
        app.config.from_mapping(test_config)

    repo.repo_instance = MemoryRepository()
    repo.books = read_datasets()
    with app.app_context():
        # Register blueprints.
        from .Home import home
        app.register_blueprint(home.home_blueprint)

        from .search import search
        app.register_blueprint(search.search_blueprint)

        from .Authentication import Authentication
        app.register_blueprint(Authentication.authentication_blueprint)
        # from .utilities import utilities
        # app.register_blueprint(utilities.utilities_blueprint)

    return app

    # @app.route('/')
    # def home():
    #     some_book = create_some_book()
    #     # Use Jinja to customize a predefined html page rendering the layout for showing a single book.
    #     return render_template('simple_book.html', book=some_book)
