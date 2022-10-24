from django.shortcuts import render, redirect, get_object_or_404

from .forms import WordForm, StartGameForm
from .models import Room
from .services import GameCircle


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
    room = get_object_or_404(Room, room_name=room_name)
    game_circle = GameCircle(room)
    context = game_circle.fill_context()
    if request.method == "POST":
        post_data = game_circle.update_post_data(request.POST)
        form = WordForm(data=post_data)
        if form.is_valid():
            game_circle.update_last_word(post_data["word"])
            form.save()
            return redirect(room.get_absolute_url())
        context["form"] = form
        return render(request, "game_room.html", context)
    context["form"] = WordForm()
    return render(request, "game_room.html", context)


def load_game(request):
    if request.method == "POST":
        room = get_object_or_404(Room, room_name=request.POST["room_name"])
        if request.POST["password"] == room.password:
            return redirect(room.get_absolute_url())
    form = StartGameForm()
    return render(request, "load_game.html", {"form": form})


def stop_game(request, room_name):
    room = Room.objects.get(room_name=room_name)
    context = {
        "count_words": room.words.all().count(),
        "room_name": room.room_name,
    }
    room.delete()
    return render(request, "stop_game.html", context)
