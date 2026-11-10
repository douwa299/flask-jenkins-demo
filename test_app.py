from app import app, add


def test_add_function():
    assert add(2, 3) == 5


def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_json()["message"] == "Hello from Flask + Jenkins!"


def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_add_route():
    client = app.test_client()
    response = client.get("/add?a=2&b=3")
    assert response.status_code == 200
    assert response.get_json()["result"] == 5


def test_add_route_invalid_input():
    client = app.test_client()
    response = client.get("/add?a=hello&b=3")
    assert response.status_code == 400