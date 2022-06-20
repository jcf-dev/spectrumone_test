import pytest

from django.conf import settings
from django.contrib.auth import get_user_model

UserModel = get_user_model()


@pytest.mark.django_db
class TestAuthView:
    def test_register(self, client):
        response = client.post(
            f"/{settings.API_PREFIX}/auth/register/",
            dict(
                email="test@test.com",
                username="test_username",
                password1="test_password",
                password2="test_password",
            ),
        )

        assert response.status_code == 201, response.json()

    def test_invalid_credentials(self, client):
        UserModel.objects.create_user(
            username="test_username", email="test@test.com", password="test_password"
        )
        response = client.post(
            f"/{settings.API_PREFIX}/auth/login/",
            dict(username="test_username", password="invalid_password"),
        )

        assert response.status_code == 400, response.json()
