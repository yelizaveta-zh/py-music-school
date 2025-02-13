from django.urls import path, include
from rest_framework.routers import DefaultRouter

from musician import views
from musician.views import MusicianViewSet


router = DefaultRouter()
router.register("musicians", MusicianViewSet, basename="musician")

urlpatterns = [
    path("api/", include(router.urls)),
    path("api/musicians",
         views.MusicianViewSet.as_view({"get": "list"}),
         name="musician-manage-list"),
]

app_name = "musician"
