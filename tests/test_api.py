import allure
import pytest
import requests
from config.settings import settings
from config.test_data import test_data


@allure.feature("API Тесты")
class TestAPI:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {settings.TOKEN}',
            'User-Agent': (
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                'AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/91.0.4472.124 Safari/537.36'
            )
        }

    def _make_request(self, url, params=None):
        response = requests.get(url, headers=self.headers, params=params)
        return response

    @allure.title("Получение списка книг")
    @allure.severity("blocker")
    @pytest.mark.api_test
    @pytest.mark.positive_test
    def test_get_books(self):
        url = f"{settings.API_BASE_URL_V2}/products"
        response = self._make_request(url)
        assert response.status_code == 200, f"Ошибка: {response.text}"

    @allure.title("Получение информации о книге по ID")
    @allure.severity("blocker")
    @pytest.mark.api_test
    @pytest.mark.positive_test
    def test_get_book_by_id(self):
        url = f"{settings.API_BASE_URL}/products/slug/{test_data.BOOK_ID}"
        response = self._make_request(url)
        assert response.status_code == 200, f"Ошибка: {response.text}"
        assert ("Михаил" in response.text
                and "Лермонтов" in response.text)

    @allure.title("Поиск книг на кириллице")
    @allure.severity("blocker")
    @pytest.mark.api_test
    @pytest.mark.positive_test
    def test_search_books_rus(self):
        params = {'phrase': 'герой нашего времени'}
        url = f"{settings.API_BASE_URL_V2}/search/product"
        response = self._make_request(url, params=params)
        assert response.status_code == 200, f"Ошибка: {response.text}"

    @allure.title("Поиск книг на латинице")
    @allure.severity("blocker")
    @pytest.mark.api_test
    @pytest.mark.positive_test
    def test_search_books_eng(self):
        params = {'phrase': 'geroi nashego vremeni'}
        url = f"{settings.API_BASE_URL_V2}/search/product"
        response = self._make_request(url, params=params)
        assert response.status_code == 200, f"Ошибка: {response.text}"

    @allure.title("Пустое поле поиска")
    @allure.severity("normal")
    @pytest.mark.api_test
    @pytest.mark.negative_test
    def test_search_empty(self):
        params = {'phrase': ''}
        url = f"{settings.API_BASE_URL_V2}/search/product"
        response = self._make_request(url, params=params)
        assert response.status_code in [400, 422], (
            f"Ожидалась ошибка, но получили: {response.status_code}"
        )

    @allure.title("Получение списка книг по автору")
    @allure.severity("normal")
    @pytest.mark.api_test
    @pytest.mark.positive_test
    def test_get_books_by_author(self):
        params = {'filters[authors]': test_data.AUTHOR_ID}
        url = f"{settings.API_BASE_URL_V2}/products/facet"
        response = self._make_request(url, params=params)
        assert response.status_code == 200, f"Ошибка: {response.text}"
