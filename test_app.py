import app

def test_flask_app():
    with app.app.test_client() as client:
        response = client.get("/hello")
        assert response.status_code == 200
        assert response.data == b"Hello World"
