import allure
import pytest
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from pages.main_page import MainPage
from config.test_data import test_data


@allure.feature("UI Тесты")
class TestUI:
    @pytest.fixture(autouse=True)
    def setup(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-extensions")
        options.add_argument("--no-sandbox")
        self.driver = webdriver.Chrome(options=options)
        self.main_page = MainPage(self.driver)
        try:
            self.main_page.set_cookie_policy()
            yield
        except WebDriverException as e:
            pytest.fail(f"Ошибка WebDriver: {str(e)}")
        finally:
            self.main_page.close_driver()

    @allure.title("Открытие главной страницы")
    @allure.severity("blocker")
    @pytest.mark.ui_test
    @pytest.mark.positive_test
    def test_open_main_page(self):
        assert "Читай-город" in self.driver.title, (
            "Главная страница не открылась"
        )

    @allure.title("Поиск книги на кириллице")
    @allure.severity("blocker")
    @pytest.mark.ui_test
    @pytest.mark.positive_test
    def test_search_book_rus_ui(self):
        try:
            text = self.main_page.search_book_rus_ui()
            assert test_data.EXPECTED_RUS_RESULT in text, (
                f"Ожидалось '{test_data.EXPECTED_RUS_RESULT}', "
                f"получено '{text}'"
            )
        except Exception as e:
            pytest.fail(f"Тест не пройден: {str(e)}")

    @allure.title("Поиск книги на латинице")
    @allure.severity("blocker")
    @pytest.mark.ui_test
    @pytest.mark.positive_test
    def test_search_book_eng_ui(self):
        try:
            text = self.main_page.search_book_eng_ui()
            assert test_data.EXPECTED_ENG_RESULT in text, (
                f"Ожидалось '{test_data.EXPECTED_ENG_RESULT}', "
                f"получено '{text}'"
            )
        except Exception as e:
            pytest.fail(f"Тест не пройден: {str(e)}")

    @allure.title("Поиск по невалидному значению")
    @allure.severity("normal")
    @pytest.mark.ui_test
    @pytest.mark.negative_test
    def test_search_invalid_ui(self):
        try:
            text = self.main_page.search_invalid_ui()
            assert test_data.EXPECTED_EMPTY_RESULT in text, (
                f"Ожидалось '{test_data.EXPECTED_EMPTY_RESULT}', "
                f"получено '{text}'"
            )
        except Exception as e:
            pytest.fail(f"Тест не пройден: {str(e)}")

    @allure.title("Поиск через каталог")
    @allure.severity("normal")
    @pytest.mark.ui_test
    @pytest.mark.positive_test
    def test_catalog_search(self):
        try:
            text = self.main_page.catalog_search()
            assert test_data.CATALOG_RESULT in text, (
                f"Ожидалось '{test_data.CATALOG_RESULT}', "
                f"получено '{text}'"
            )
        except Exception as e:
            pytest.fail(f"Тест не пройден: {str(e)}")

    @allure.title("Проверка пустой корзины")
    @allure.severity("blocker")
    @pytest.mark.ui_test
    @pytest.mark.positive_test
    def test_empty_cart(self):
        try:
            msg = self.main_page.get_empty_result_message()
            assert test_data.EMPTY_CART_MESSAGE in msg, (
                f"Ожидалось '{test_data.EMPTY_CART_MESSAGE}', "
                f"получено '{msg}'"
            )
        except Exception as e:
            pytest.fail(f"Тест не пройден: {str(e)}")
