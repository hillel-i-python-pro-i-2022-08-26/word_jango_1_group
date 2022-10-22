from django.urls import path

from . import views

app_name = "words"

urlpatterns = [
    path("", views.index, name="game"),
    path("start_game/", views.start_game, name="start"),
    path("load_game/", views.load_game, name="load"),
    path("room/<str:room_name>/", views.room_game, name="room_in"),
]
