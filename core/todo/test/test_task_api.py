import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from accounts.models import User


@pytest.fixture
def api_client():
    client = APIClient()
    return client


@pytest.fixture
def common_user():
    user = User.objects.create_user(
        phone_number="09356165600", password="1234")
    return user


@pytest.mark.django_db
class TestTaskApi:
    def test_get_task_response_200_status(self, api_client, common_user):

        url = reverse("todo:api-v1:task-list")
        user = common_user
        api_client.force_authenticate(user=user)
        response = api_client.get(url)
        assert response.status_code == 200

    def test_create_post_invalid_data_response_400_status(self, api_client, common_user):
        url = reverse("todo:api-v1:task-list")
        user = common_user
        api_client.force_authenticate(user=user)
        data = {
            "": ""
        }
        response = api_client.post(url, data)
        assert response.status_code == 400

    def test_create_post_response_201_status(self, api_client, common_user):
        url = reverse("todo:api-v1:task-list")
        data = {
            "title": "test post"
        }
        user = common_user
        api_client.force_authenticate(user=user)
        response = api_client.post(url, data)
        assert response.status_code == 201

    def test_delete_task_response_204_status(self, api_client, common_user):
        create_url = reverse("todo:api-v1:task-list")
        data = {
            "title": "task to be deleted"
        }
        api_client.force_authenticate(user=common_user)
        create_response = api_client.post(create_url, data)
        assert create_response.status_code == 201
        task_id = create_response.data["id"]

        delete_url = reverse("todo:api-v1:task-detail", kwargs={"pk": task_id})
        delete_response = api_client.delete(delete_url)
        assert delete_response.status_code == 204

    def test_delete_task_response_404_status(self, api_client, common_user):
        create_url = reverse("todo:api-v1:task-list")
        data = {
            "title": "task to be deleted"
        }
        api_client.force_authenticate(user=common_user)
        create_response = api_client.post(create_url, data)
        assert create_response.status_code == 201
        # create wrong id
        task_id = create_response.data["id"] + 100

        delete_url = reverse("todo:api-v1:task-detail", kwargs={"pk": task_id})
        delete_response = api_client.delete(delete_url)
        assert delete_response.status_code == 404

    def test_update_task_response_200_status(self, api_client, common_user):
        create_url = reverse("todo:api-v1:task-list")
        data = {
            "title": "task to be updated"
        }

        api_client.force_authenticate(user=common_user)
        create_response = api_client.post(create_url, data)
        assert create_response.status_code == 201
        task_id = create_response.data["id"]
        update_data = {
            "title": "task updated"
        }
        update_url = reverse("todo:api-v1:task-detail", kwargs={"pk": task_id})
        update_response = api_client.patch(update_url, update_data)
        assert update_response.status_code == 200

    def test_update_task_response_404_status(self, api_client, common_user):
        create_url = reverse("todo:api-v1:task-list")
        data = {
            "title": "task to be updated"
        }

        api_client.force_authenticate(user=common_user)
        create_response = api_client.post(create_url, data)
        assert create_response.status_code == 201
        # create wrong id
        task_id = create_response.data["id"] + 100
        update_data = {
            "title": "task updated"
        }
        update_url = reverse("todo:api-v1:task-detail", kwargs={"pk": task_id})
        update_response = api_client.patch(update_url, update_data)
        assert update_response.status_code == 404
