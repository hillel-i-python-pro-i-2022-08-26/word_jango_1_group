from django import forms

from .models import Word, Room


# from apps.words_game.services.app import validate_words


class StartGameForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ("host", "room_name")


class WordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ("word", "room")
        widgets = {"room": forms.HiddenInput()}
