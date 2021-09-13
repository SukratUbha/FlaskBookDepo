import abc
from typing import List
from datetime import date
from library.domain.model import Publisher, Author, Book, User

repo_instance = None
books = None


class RepositoryException(Exception):

    def __init__(self, message=None):
        pass


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add_user(self, user: User):
        """" Adds a User to the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def search_filter(self, search_query):
        raise NotImplementedError

    @abc.abstractmethod
    def get_book_by_id(self, id):
        raise NotImplementedError