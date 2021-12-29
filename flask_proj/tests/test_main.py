from ..main import app


def test_home_page():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """
    flask_app = app('flask_test.cfg')

    with flask_app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200

def test_calculator_service():
    
    flask_app = app('flask_test.cfg')

    
    with flask_app.test_client() as test_client:
        response = test_client.post(
            '/services/calculator', json={"a": 1, "b": 0, "operation": "div"}
        )
        assert response.status_code == 400
        assert response.json() == {"detail": "Division by 0 is not supported"}

def test_date_calculator_service():
    """Does a test to check the date_calculator service"""
    
    flask_app = app('flask_test.cfg')

    
    with flask_app.test_client() as test_client:
        response = test_client.post(
            '/services/date-fmt', json={"date": "2020-01-01T00:00:00", "days": 2}
        )
        assert response.status_code == 200
        assert response.json() == {"date": "2020-01-03T00:00:00"}