import pytest

import data
from main import BooksCollector


@pytest.fixture
def book_collector():
    collector = BooksCollector()

    return collector

@pytest.fixture
def book_collector_with_new_name(book_collector):
    book_collector.add_new_book(data.BookNameTest.NEW_BOOK_NAME)

    return book_collector
