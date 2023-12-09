from .models import Thing
from django.contrib import admin


@admin.register(Thing)
class ThingAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name", "description")
