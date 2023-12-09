from django.core.management.base import BaseCommand

from favorites.models import Thing


class Command(BaseCommand):
    help = "Creates 5 things"

    def handle(self, *args, **kwargs):
        for i in range(1, 6):
            Thing.objects.create(name=f"Thing {i}", description=f"Description {i}")
        self.stdout.write(self.style.SUCCESS("5 things created!"))
