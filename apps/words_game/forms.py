from django import forms

from .models import Word, Room


# from apps.words_game.services.app import validate_words


class StartGameForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ("room_name", "password")
        widgets = {
            "password": forms.PasswordInput(),
        }


class WordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ("word", "room")
        widgets = {
            "room": forms.HiddenInput(),
        }
