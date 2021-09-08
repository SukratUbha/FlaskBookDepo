from pathlib import Path
from datetime import date, datetime
from typing import List
from library.adapters.jsondatareader import BooksJSONReader
from bisect import bisect, bisect_left, insort_left

from werkzeug.security import generate_password_hash

from library.adapters.repository import AbstractRepository, RepositoryException
from library.domain.model import Publisher, Author, Book


class MemoryRepository(AbstractRepository):
    # Articles ordered by date, not id. id is assumed unique.

    def __init__(self):
        self.__articles = list()
        self.__articles_index = dict()
        self.__tags = list()
        self.__users = list()
        self.__comments = list()

def read_datasets():
    authors_filename = 'library/adapters/data/book_authors_excerpt.json'
    books_filename = 'library/adapters/data/comic_books_excerpt.json'
    reader = BooksJSONReader(books_filename, authors_filename)
    reader.read_json_files()
    return reader.dataset_of_books
    # print(reader.dataset_of_books)

