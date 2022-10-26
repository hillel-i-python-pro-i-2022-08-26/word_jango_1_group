from django.http import HttpRequest, HttpResponse, QueryDict
from django.shortcuts import render, redirect, get_object_or_404

from .forms import WordForm, StartGameForm
from .models import Word, Room


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
            #room = form.save()
            room = Room.objects.create(**form.cleaned_data)
            return redirect(room)
        return render(request, "start_game.html", {"form": form})
    form = StartGameForm()
    return render(request, "start_game.html", {"form": form})


def room_game(request, room_name):
    room = get_object_or_404(Room, room_name=room_name)
    if request.method == "POST":
        form = WordForm(room_name, request.POST)
        print("Method POST")
        if form.is_valid():
            print("valid")
            room.last_word = request.POST["word"].lower()
            room.save()
            word = Word(word=room.last_word, room_id=room.pk)
            word.save()
            # return redirect("words:room_in", room_name=room_name, form=form)
            return render(request, "game_room.html", {"form": form, "room_name": room_name})
        print("Nevalid")
        return render(request, "game_room.html", {"form": form, "room_name": room_name})
    form = WordForm(room_name)
    return render(request, "game_room.html", {"form": form, "room_name": room_name})


def load_game(request):
    if request.method == "POST":
        form = StartGameForm(request.POST)
        # form = StartGameForm() #for choice room
        print(form)
        if form.is_valid():
            redirect("words:room_in", room_name=request.POST["room_name"])
    form = StartGameForm()
    return render(request, "load_game.html", {"form": form})


def stop_game(request):
    pass
