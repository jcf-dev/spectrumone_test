import pytest

from django.contrib.auth import get_user_model

UserModel = get_user_model()


@pytest.mark.django_db
class TestUser:
    def test_user_create(self, client):
        user = UserModel.objects.create_user(
            username="test_username", email="test@test.com", password="test_password"
        )
        assert user
