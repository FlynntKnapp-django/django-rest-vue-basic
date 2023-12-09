from django.core.management.base import BaseCommand

from favorites.models import Thing


class Command(BaseCommand):
    help = "Creates Programming Things"

    def handle(self, *args, **kwargs):
        Thing.objects.create(
            name="Django",
            description="The web framework for perfectionists with deadlines.",
        )
        Thing.objects.create(name="Flask", description="A microframework for Python.")
        Thing.objects.create(
            name="Bottle",
            description="Fast, simple and lightweight WSGI micro web-framework for Python.",
        )
        Thing.objects.create(
            name="Pyramid",
            description="A small, fast, down-to-earth, open source Python web framework.",
        )
        Thing.objects.create(
            name="Falcon",
            description="The no-nonsense REST API and microservices framework for Python developers, with a focus on reliability, correctness, and performance at scale.",
        )
        Thing.objects.create(
            name="Tornado",
            description="A Python web framework and asynchronous networking library, originally developed at FriendFeed.",
        )
        Thing.objects.create(
            name="Sanic",
            description="Sanic is a Python 3.6+ web server and web framework that's written to go fast. It allows the usage of the async/await syntax added in Python 3.5, which makes your code non-blocking and speedy.",
        )
        Thing.objects.create(
            name="FastAPI",
            description="FastAPI framework, high performance, easy to learn, fast to code, ready for production.",
        )
        Thing.objects.create(
            name="Starlette",
            description="Starlette is a lightweight ASGI framework/toolkit, which is ideal for building high performance asyncio services.",
        )
        Thing.objects.create(
            name="Quart",
            description="The Quart web framework is a Python ASGI web microframework. It is intended to provide the easiest way to use asyncio functionality in a web context, especially with existing Flask apps.",
        )
        Thing.objects.create(
            name="Responder",
            description="A familiar HTTP Service Framework for Python.",
        )
        Thing.objects.create(
            name="Django REST framework",
            description="A powerful and flexible toolkit for building Web APIs.",
        )
        Thing.objects.create(
            name="Flask-RESTful", description="Simple framework for creating REST APIs."
        )
        Thing.objects.create(
            name="Falcon",
            description="The no-nonsense REST API and microservices framework for Python developers, with a focus on reliability, correctness, and performance at scale.",
        )
        Thing.objects.create(
            name="FastAPI",
            description="FastAPI framework, high performance, easy to learn, fast to code, ready for production.",
        )
        Thing.objects.create(
            name="Starlette",
            description="Starlette is a lightweight ASGI framework/toolkit, which is ideal for building high performance asyncio services.",
        )
