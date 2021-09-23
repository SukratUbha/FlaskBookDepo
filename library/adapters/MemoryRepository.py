from pathlib import Path
from datetime import date, datetime
from typing import List
from library.adapters.jsondatareader import BooksJSONReader
from bisect import bisect, bisect_left, insort_left
import library.adapters.repository as repo
from werkzeug.security import generate_password_hash

from library.adapters.repository import AbstractRepository, RepositoryException
from library.domain.model import Publisher, Author, Book, User


class MemoryRepository(AbstractRepository):
    def __init__(self):
        self.__users = list()

    def search_filter(self, q):
        search_output = []
        search_mismatch = []
        for i in repo.books:
            tString = " ".join(i.authorString.split()).lower()
            if q.lower() in i.title.lower():
                search_output.append(i)
            elif q.lower() in tString:
                search_output.append(i)
            elif q.lower() in i.publisher.name.lower():
                search_output.append(i)
            elif q in str(i.release_year):
                search_output.append(i)
            else:
                search_mismatch.append(i)
        search_output += search_mismatch
        return search_output

    def get_book_by_id(self, id_id):
        print(id_id)
        for i in repo.books:

            if str(id_id) == str(i.book_id):
                return i
        return Book(404, "Not Found")

    def add_user(self, user: User):
        print(user)
        self.__users.append(user)

    def get_user(self, user_name) -> User:
        print(self.__users)
        return next((user for user in self.__users if user.user_name == user_name), None)

#
# def read_datasets():
#     authors_filename = 'library/adapters/data/book_authors_excerpt.json'
#     books_filename = 'library/adapters/data/comic_books_excerpt.json'
#     reader = BooksJSONReader(books_filename, authors_filename)
#     reader.read_json_files()
#     return reader.dataset_of_books
    # print(reader.dataset_of_books)
def read_datasets(books_filename: Path, authors_filename: Path):
    reader = BooksJSONReader(books_filename, authors_filename)
    reader.read_json_files()
    return reader.dataset_of_books

