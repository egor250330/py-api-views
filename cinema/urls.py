from django.urls import path
from rest_framework.routers import DefaultRouter

from cinema.views import (
    GenreAPIView,
    ActorsGenericAPIView,
    CinemaHallGenericViewSet,
    MovieModelViewSet
)

app_name = "cinema"

router = DefaultRouter()
router.register("cinema_halls", CinemaHallGenericViewSet)
router.register("movies", MovieModelViewSet)
urlpatterns = [
    path("genres/", GenreAPIView.as_view(), name="genre"),
    path("actors/", ActorsGenericAPIView.as_view(), name="actors"),
]
