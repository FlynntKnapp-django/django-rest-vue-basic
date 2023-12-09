from django.urls import path
from rest_framework.routers import DefaultRouter

from api import views

app_name = "api"

router = DefaultRouter()
router.register("things", views.ThingViewSet, basename="things")

# Add a named URL pattern for the API root
urlpatterns = [
    path("", router.get_api_root_view(), name="api-root"),
] + router.urls
