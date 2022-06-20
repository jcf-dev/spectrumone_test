import factory
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from factory.django import DjangoModelFactory


@factory.django.mute_signals(post_save)
class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("name")
    email = factory.Faker("email")

    def __init__(self):
        self.password = None

    @factory.post_generation
    def is_organizer(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted is not None:
            self.profile.is_organizer = extracted
            self.profile.save()

    @factory.post_generation
    def password(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted is not None:
            self.password = make_password(extracted)
            self.save()
