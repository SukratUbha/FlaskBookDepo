from flask import Flask, render_template
import library.adapters.repository as repo
from pathlib import Path
from library.domain.model import Book
from library.adapters.MemoryRepository import MemoryRepository, read_datasets

def create_app(test_config=None):
    app = Flask(__name__)

    app.config.from_object('config.Config')

    data_path = Path('library') / 'adapters' / 'data'
    if test_config is not None:
        # Load test configuration, and override any configuration settings.
        app.config.from_mapping(test_config)
        data_path = app.config['TEST_DATA_PATH']
    # authors_filename = 'library/adapters/data/book_authors_excerpt.json'
    # books_filename = 'library/adapters/data/comic_books_excerpt.json'
    authors_filename = data_path / 'book_authors_excerpt.json'
    books_filename = data_path / 'comic_books_excerpt.json'
    repo.repo_instance = MemoryRepository()
    repo.books = read_datasets(books_filename, authors_filename)

    with app.app_context():
        # Register blueprints.
        from .Home import home
        app.register_blueprint(home.home_blueprint)

        from .search import search
        app.register_blueprint(search.search_blueprint)

        from .Authentication import Authentication
        app.register_blueprint(Authentication.authentication_blueprint)

    return app