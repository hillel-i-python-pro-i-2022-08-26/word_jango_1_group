from django.shortcuts import render, redirect
import copy

import copy

from django.shortcuts import render, redirect

from .forms import WordForm, StartGameForm
from .models import Room


# def input_words(request: HttpRequest) -> HttpResponse:
#     if request.method == "POST":
#         word_post = request.POST["word"]
#         last_word = request.session.get("last_word", None)
#         form = WordForm(request.POST)
#         if not form.is_valid():
#             return render(request, "index.html", {"form": form})
#         form.save()
#         return redirect("words:game")
#     form = WordForm()
#
#     return render(request, "index.html", {"form": form})


def index(request):
    return render(request, "index.html")


def start_game(request):
    if request.method == "POST":
        form = StartGameForm(request.POST)
        if form.is_valid():
            room = form.save()
            return redirect(room)
        return render(request, "start_game.html", {"form": form})
    form = StartGameForm()
    return render(request, "start_game.html", {"form": form})


def room_game(request, room_name):
    room = Room.objects.get(room_name=room_name)
    previous_words = room.words.all()
    context = {"room_name": room_name, "previous_words": previous_words}
    if request.method == "POST":
        post_data = copy.copy(request.POST)
        post_data["room"] = room.pk
        form = WordForm(data=post_data)
        if form.is_valid():
            room.last_word = post_data["word"].lower().strip()
            room.save()
            form.save()
            return render(request, "game_room.html", {"form": WordForm(), "room_name": room_name})
        return render(request, "game_room.html", {"form": form, "room_name": room_name})
    form = WordForm()
    return render(request, "game_room.html", {"form": form, "room_name": room_name})


def load_game(request):
    if request.method == "POST":
        form = StartGameForm(request.POST)
        if form.is_valid():
            redirect("words:room_in", room_name=request.POST["room_name"])
    form = StartGameForm()
    return render(request, "load_game.html", {"form": form})


def stop_game(request):
    pass
