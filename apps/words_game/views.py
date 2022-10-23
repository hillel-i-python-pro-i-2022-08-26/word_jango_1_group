from django.shortcuts import render, redirect

from .forms import WordForm, StartGameForm
from .models import Room
from .services.app import fill_context, update_post_data, update_last_word


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
    context = fill_context(room)
    if request.method == "POST":
        post_data = update_post_data(request.POST, room.pk)
        form = WordForm(data=post_data)
        if form.is_valid():
            update_last_word(room, post_data["word"])
            form.save()
            return redirect("words:room_in", room_name=room_name)
        context["form"] = form
        return render(request, "game_room.html", context)
    context["form"] = WordForm()
    return render(request, "game_room.html", context)


def load_game(request):
    if request.method == "POST":
        form = StartGameForm(request.POST)
        if form.is_valid():
            redirect("words:room_in", room_name=request.POST["room_name"])
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
