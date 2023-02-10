import pytest
import requests

def test_flask_app():
    # Make a GET request to the Flask app endpoint
    response = requests.get('http://localhost:5000/')

    # Check that the response status code is 200 (success)
    assert response.status_code == 200

    # Check that the response contains the expected message
    assert b'Hello World' in response.content
