import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from accounts.models import User


@pytest.fixture
def api_client():
    client = APIClient()
    return client


@pytest.fixture
def common_user(db):
    user = User.objects.create_user(
        phone_number="09356165600", password="1234")
    return user


@pytest.mark.django_db
class TestTaskApi:
    def test_login_response_200_status(self, api_client, common_user):
        login_url = reverse("accounts:api-v1:login")
        user = common_user
        data = {
            "phone_number": user.phone_number,
            "password": '1234',
        }
        response = api_client.post(login_url, data=data)
        assert response.status_code == 200

    def test_login_response_400_status(self, api_client):
        login_url = reverse("accounts:api-v1:login")
        data = {
            "phone_number": 'wrong number',
            "password": 'wrong password',
        }
        response = api_client.post(login_url, data=data)
        assert response.status_code == 400

    def test_register_response_201_status(self, api_client):
        register_url = reverse("accounts:api-v1:register")
        data = {
            "phone_number": '09122222222',
            "password": '12345678',

        }
        response = api_client.post(register_url, data=data)
        assert response.status_code == 201

    def test_register_response_400_status(self, api_client):
        register_url = reverse("accounts:api-v1:register")
        data = {
            "phone_number": '09122222222',
            "password": '1234',

        }
        response = api_client.post(register_url, data=data)
        assert response.status_code == 400

    def test_password_reset_response_200_status(self, api_client):
        register_url = reverse("accounts:api-v1:register")
        data = {
            "phone_number": '09122222222',
            "password": '12345678',

        }
        response = api_client.post(register_url, data=data)
        phone_number = response.data.get('phone_number')
        assert response.status_code == 201
        user_obj = User.objects.get(phone_number =phone_number )
        api_client.force_authenticate(user=user_obj)
        
        reset_password_url = reverse("accounts:api-v1:password_reset")
        data = {
            "new_password":"12345jafna",
            "old_password":"12345678"
        }
        response = api_client.patch(reset_password_url, data=data)
        print(response.data)
        assert response.status_code == 200




