class Settings:
    """Класс для хранения настроек приложения."""

    BASE_URL = "https://www.chitai-gorod.ru/"
    API_BASE_URL = "https://web-gate.chitai-gorod.ru/api/v1"
    API_BASE_URL_V2 = "https://web-gate.chitai-gorod.ru/api/v2"
    # Длинный токен разбит на несколько строк для читаемости
    TOKEN = (
        "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NDUwNzQ5NzIsImlhdCI6"
        "MTc0NDkwNjk3MiwiaXNzIjoiL2FwaS92MS9hdXRoL2Fub255bW91cyIsInN1YiI6ImRjM2"
        "I3ZTliYThlMmUxYzI3YjZkZTc3NWZlMjdkNjc4Yjg2YjUwYzVkNzNkOTRmNTI0MGIyYjRi"
        "ZWU0MDBkZTciLCJ0eXBlIjoxMH0.Oj4yRtQPSaFSqs7Tn-TD1Qj9YG778NSdOs4ikB41lOk"
    )


settings = Settings()
