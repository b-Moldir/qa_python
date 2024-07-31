from data import BookNameTest
from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self, book_collector):
        # создаем экземпляр (объект) класса BooksCollector
        # добавляем две книги
        book_collector.add_new_book('Гордость и предубеждение и зомби')
        book_collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(book_collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_set_book_genre_set_one_genre(self, book_collector_with_new_name):
        book_collector_with_new_name.set_book_genre(BookNameTest.NEW_BOOK_NAME, BookNameTest.NEW_GENRE_BOOK)
        assert book_collector_with_new_name.get_book_genre(BookNameTest.NEW_BOOK_NAME) == BookNameTest.NEW_GENRE_BOOK

    def test_get_book_genre_add_new_book_no_genre(self, book_collector_with_new_name):
        book_collector_with_new_name.add_new_book(BookNameTest.NEW_BOOK_NAME)
        assert BookNameTest.NEW_BOOK_NAME not in book_collector_with_new_name.get_book_genre(BookNameTest.NEW_BOOK_NAME)

    def test_get_books_with_specific_genre_add_book_one_genre(self, book_collector_with_new_name):
        book_collector_with_new_name.set_book_genre(BookNameTest.NEW_BOOK_NAME, BookNameTest.NEW_GENRE_BOOK)
        book_collector_with_new_name.get_books_with_specific_genre(BookNameTest.NEW_GENRE_BOOK)
        assert book_collector_with_new_name.get_book_genre(BookNameTest.NEW_BOOK_NAME) == BookNameTest.NEW_GENRE_BOOK

    def test_get_books_genre_add_five_books(self,book_collector):
        book_collector.add_new_book('Алхимик')
        book_collector.add_new_book('Рискуя собственной шкурой')
        book_collector.add_new_book('Атлант расправил плечи')
        assert len(book_collector.get_books_genre()) == 3

    def test_get_books_for_children_with_age_restrictions(self, book_collector):
        book_collector.set_book_genre(BookNameTest.NEW_BOOK_NAME, BookNameTest.NEW_GENRE_BOOK)
        print(book_collector.get_books_for_children())
        assert len(book_collector.get_books_for_children()) == 0

    def test_add_book_in_favorites_add_one_book(self, book_collector_with_new_name):
        book_collector_with_new_name.add_book_in_favorites(BookNameTest.NEW_BOOK_NAME)
        assert BookNameTest.NEW_BOOK_NAME in book_collector_with_new_name.get_list_of_favorites_books()

    def test_delete_book_from_favorites_delete_book_in_favorites(self, book_collector_with_new_name):
        book_collector_with_new_name.add_book_in_favorites(BookNameTest.NEW_BOOK_NAME)
        book_collector_with_new_name.delete_book_from_favorites(BookNameTest.NEW_BOOK_NAME)
        assert BookNameTest.NEW_BOOK_NAME not in book_collector_with_new_name.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_add_one_book_in_favorites(self, book_collector_with_new_name):
        book_collector_with_new_name.add_book_in_favorites(BookNameTest.NEW_BOOK_NAME)
        assert BookNameTest.NEW_BOOK_NAME in book_collector_with_new_name.get_list_of_favorites_books()

