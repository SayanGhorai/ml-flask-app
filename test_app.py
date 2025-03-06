import pytest
from app import app  # Assuming your Flask app is in app.py

def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
