from datetime import date, datetime
from typing import List

import pytest

from library.domain.model import User
from library.adapters.repository import RepositoryException


def test_repository_can_add_a_user(in_memory_repo):
    user = User('dave', '123456789')
    user2 = User('fmercury', '323492348')
    in_memory_repo.add_user(user)
    in_memory_repo.add_user(user2)
    assert in_memory_repo.get_user('dave') is user


def test_repository_does_not_retrieve_a_non_existent_user(in_memory_repo):
    user = in_memory_repo.get_user('prince')
    assert user is None

