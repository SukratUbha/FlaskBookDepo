import json
from typing import List
from pathlib import Path
from library.domain.model import Publisher, Author, Book


class BooksJSONReader:

    def __init__(self, books_file_name: str, authors_file_name: str):
        self.__books_file_name = books_file_name
        self.__authors_file_name = authors_file_name
        self.__dataset_of_books = []

    @property
    def dataset_of_books(self) -> List[Book]:
        return self.__dataset_of_books

    def read_books_file(self) -> list:
        books_json = []
        with open(self.__books_file_name, encoding='UTF-8') as books_jsonfile:
            for line in books_jsonfile:
                book_entry = json.loads(line)
                books_json.append(book_entry)
        return books_json

    def read_authors_file(self) -> list:
        authors_json = []
        with open(self.__authors_file_name, encoding='UTF-8') as authors_jsonfile:
            for line in authors_jsonfile:
                author_entry = json.loads(line)
                authors_json.append(author_entry)
        return authors_json


    def read_json_files(self):
        authors_json = self.read_authors_file()
        books_json = self.read_books_file()

        for book_json in books_json:
            book_instance = Book(int(book_json['book_id']), book_json['title'])
            book_instance.publisher = Publisher(book_json['publisher'])
            authorString = []
            if book_json['image_url']:
                book_instance.img = book_json['image_url']
            if book_json['publication_year'] != "":
                book_instance.release_year = int(book_json['publication_year'])
            if book_json['is_ebook'].lower() == 'false':
                book_instance.ebook = False
            else:
                if book_json['is_ebook'].lower() == 'true':
                    book_instance.ebook = True
            book_instance.description = book_json['description']
            if book_json['num_pages'] != "":
                book_instance.num_pages = int(book_json['num_pages'])

            # extract the author ids:
            list_of_authors_ids = book_json['authors']
            # print(list_of_authors_ids)
            for author_id in list_of_authors_ids:
                # print("jsondatareader", author_id)
                numerical_id = int(author_id['author_id'])
                # We assume book authors are available in the authors file,
                # otherwise more complex handling is required.
                author_name = None
                for author_json in authors_json:
                    if int(author_json['author_id']) == numerical_id:
                        author_name = author_json['name']
                        role = author_id['role']
                        if not role == "":
                            authorString.append(f' {author_name} ({role})')
                        else:
                            authorString.append(f' {author_name}')
                book_instance.authorString = ""
                for i in range(len(authorString)):
                    if i == len(authorString) -1:
                        book_instance.authorString += authorString[i]
                    else:
                        book_instance.authorString += authorString[i]
                        book_instance.authorString += " and "
                # book_instance.authorString = authorString
                book_instance.add_author(Author(numerical_id, author_name))
            # print(book_instance.authorString)
            # print("a string", authorString)

            self.__dataset_of_books.append(book_instance)



# authors_filename = 'data/book_authors_excerpt.json'
# books_filename = 'data/comic_books_excerpt.json'
# reader = BooksJSONReader(books_filename , authors_filename)
# reader.read_json_files()
# print(reader.dataset_of_books[0])
# # print(reader.dataset_of_books[0].authors[0].full_name)