from django.urls import path
from favorites import views

app_name = "favorites"
urlpatterns = [
    path("", views.home, name="home"),
    path("things/", views.ThingListView.as_view(), name="thing-list"),
    # path("things/<int:pk>/", views.ThingDetailView.as_view(), name="thing-detail"),
    # path("things/create/", views.ThingCreateView.as_view(), name="thing-create"),
    # path(
    #     "things/<int:pk>/update/", views.ThingUpdateView.as_view(), name="thing-update"
    # ),
    # path(
    #     "things/<int:pk>/delete/", views.ThingDeleteView.as_view(), name="thing-delete"
    # ),
]
