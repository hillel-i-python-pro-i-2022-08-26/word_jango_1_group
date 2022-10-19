from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from .forms import WordForm
from .models import Word


def input_words(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        word_post = request.POST["word"]
        last_word = request.session.get("last_word", None)
        form = WordForm(request.POST)
        if not form.is_valid():
            return render(request, "base.html", {"form": form})
        form.save()
        return redirect("words:game")
    form = WordForm()

    return render(request, "base.html", {"form": form})
