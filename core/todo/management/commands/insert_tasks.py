from django.core.management.base import BaseCommand

from faker import Faker
import random
from datetime import datetime

from accounts.models import User
from ...models import Task


class Command(BaseCommand):
    help = "inserting dummy data"

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.fake = Faker()

    def handle(self, *args, **options):
        user = User.objects.create_user(phone_number='09122222222', password="1234")
        for _ in range(5):
            Task.objects.create(
                user=user,
                title=self.fake.paragraph(nb_sentences=1),
                complete=random.choice([True, False]),
            )