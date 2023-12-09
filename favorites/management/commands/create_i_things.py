from django.core.management.base import BaseCommand

from favorites.models import Thing


class Command(BaseCommand):
    help = "Creates i things"

    def add_arguments(self, parser):
        parser.add_argument("things", type=int, help="Number of things to create")

    def handle(self, *args, **kwargs):
        number_of_things = kwargs.get("things", 10)

        self.stdout.write(f"Creating {number_of_things} things...")
        for i in range(1, number_of_things + 1):
            Thing.objects.create(name=f"Thing {i}", description=f"Description {i}")
            self.stdout.write(self.style.SUCCESS(f"Created Thing {i}"))
        self.stdout.write(self.style.SUCCESS(f"Created {number_of_things} things."))
