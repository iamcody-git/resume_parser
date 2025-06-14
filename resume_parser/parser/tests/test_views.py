import pytest
from django.test import Client
from django.urls import reverse

@pytest.mark.django_db
def test_home():
    client = Client()
    url = reverse('home_page')  # Make sure 'home_page' is defined in urls.py
    response = client.get(url)
    assert response.status_code == 200
    assert b"Resume Parser" in response.content  # Ensure byte string for content check
