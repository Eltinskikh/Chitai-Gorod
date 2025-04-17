class TestData:
    """Класс для хранения тестовых данных."""

    SEARCH_TERM_RUS = "Слово пацана"
    SEARCH_TERM_ENG = "Geroi nashego vremeni"
    INVALID_SEARCH_TERM = "))))))))))"
    EXPECTED_RUS_RESULT = "Результаты поиска: Слово пацана"
    EXPECTED_ENG_RESULT = "Результаты поиска: Geroi nashego vremeni"
    EXPECTED_EMPTY_RESULT = "По вашему запросу ничего не найдено"
    CATALOG_RESULT = "Поэзия"
    EMPTY_CART_MESSAGE = "Ваша корзина пуста"
    BOOK_ID = "geroy-nashego-vremeni-roman-2480417"
    AUTHOR_ID = "593251"


test_data = TestData()
