import pytest
from app import app  # Import Flask app

def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to the ML Flask App!" in response.data  # Check response content
