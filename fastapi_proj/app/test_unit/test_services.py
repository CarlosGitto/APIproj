from fastapi.testclient import TestClient
from main import app


client = TestClient(app=app)


def calculator_test():
    """Does a test to check the calculator service"""

    response = client.post(
        '/services/calculator', json={"a": 1, "b": 0, "operation": "div"}
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "Division by 0 is not supported"}


def date_test():
    """Does a test to check the date_calculator service"""

    response = client.post(
        '/services/date-fmt', json={"date": "2020-01-01T00:00:00", "days": 2}
    )
    assert response.status_code == 200
    assert response.json() == {"date": "2020-01-03T00:00:00"}