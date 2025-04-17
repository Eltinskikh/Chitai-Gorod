import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from config.settings import settings
from config.test_data import test_data


class MainPage:
    def __init__(self, driver):
        self._driver = driver
        self._driver.maximize_window()
        self._driver.get(settings.BASE_URL)
        self._wait = WebDriverWait(self._driver, 20)
        self._driver.implicitly_wait(5)

    @allure.step("Принять политику куки")
    def set_cookie_policy(self):
        try:
            cookie_button = self._wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[contains(text(), 'Принять') "
                     "or contains(text(), 'Согласен')]")
                )
            )
            cookie_button.click()
            self._driver.refresh()
        except TimeoutException:
            print("Кнопка куки не найдена, продолжаем без изменений")
        except Exception as e:
            print(f"Не удалось установить куки: {str(e)}")

    @allure.step("Закрыть попап региона")
    def close_region_popup(self):
        try:
            region_button = self._wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[contains(text(), 'Да, я здесь') "
                     "or contains(text(), 'Понятно')]")
                )
            )
            region_button.click()
        except TimeoutException:
            print("Попап региона не найден")

    @allure.step("Поиск книги на кириллице")
    def search_book_rus_ui(self):
        try:
            self.close_region_popup()
            search_input = self._wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "input.search-field__input"))
            )
            search_input.clear()
            search_input.send_keys(test_data.SEARCH_TERM_RUS)

            search_button = self._wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "button.search-field__btn"))
            )
            search_button.click()

            result = self._wait.until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, "div.search__title, "
                     "div.search-results__title, p.search-results__text"))
            )
            return result.text
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Ошибка при поиске книги на кириллице: {str(e)}")
            raise

    @allure.step("Поиск книги на латинице")
    def search_book_eng_ui(self):
        try:
            self.close_region_popup()
            search_input = self._wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "input.search-field__input"))
            )
            search_input.clear()
            search_input.send_keys(test_data.SEARCH_TERM_ENG)

            search_button = self._wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "button.search-field__btn"))
            )
            search_button.click()

            result = self._wait.until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, "div.search__title, "
                     "div.search-results__title, p.search-results__text"))
            )
            return result.text
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Ошибка при поиске книги на латинице: {str(e)}")
            raise

    @allure.step("Ввод невалидного значения")
    def search_invalid_ui(self):
        try:
            self.close_region_popup()
            search_input = self._wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "input.search-field__input"))
            )
            search_input.clear()
            search_input.send_keys(test_data.INVALID_SEARCH_TERM)

            search_button = self._wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "button.search-field__btn"))
            )
            search_button.click()

            result = self._wait.until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, "div.search__empty, "
                     "div.catalog-empty-result, p.search-results__empty-text"))
            )
            return result.text
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Ошибка при вводе невалидного значения: {str(e)}")
            raise

    @allure.step("Поиск через каталог")
    def catalog_search(self):
        try:
            self.close_region_popup()

            catalog = self._wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "button.header__catalog-btn, "
                     "a.header__catalog-link"))
            )
            catalog.click()

            literature = self._wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//a[contains(text(), "
                     "'Художественная литература')]"))
            )
            literature.click()

            poetry = self._wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//a[contains(text(), 'Поэзия')]"))
            )
            poetry.click()

            result = self._wait.until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, "h1.catalog__title, h1.category__title"))
            )
            return result.text
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Ошибка при поиске через каталог: {str(e)}")
            raise

    @allure.step("Проверка пустой корзины")
    def get_empty_result_message(self):
        try:
            self._driver.get(f"{settings.BASE_URL}/cart")
            result = self._wait.until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, "div.cart-empty__title, "
                     "h2.cart-empty__message, p.cart-empty__text"))
            )
            return result.text
        except Exception as e:
            print(f"Ошибка при проверке корзины: {str(e)}")
            raise

    @allure.step("Закрытие веб-браузера")
    def close_driver(self):
        self._driver.quit()
