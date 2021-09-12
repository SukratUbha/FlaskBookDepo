import abc
from typing import List
from datetime import date
from library.domain.model import Publisher, Author, Book
repo_instance = None
books = None

class RepositoryException(Exception):

    def __init__(self, message=None):
        pass


class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def dataset_of_books(self):
        """" Returns dataset of all books. """
        raise NotImplementedError
