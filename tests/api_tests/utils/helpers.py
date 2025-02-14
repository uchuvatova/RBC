from requests import Response


def assert_status_code(response: Response, expected_status_code: int | None = 200) -> None:
    assert response.status_code == expected_status_code, (
        f"Ошибка: Ожидаемый статус код {expected_status_code}, получен {response.status_code} \n Тело ответа - {response.json()}")
