from django import forms
from django.core.exceptions import ValidationError
from django.urls import reverse

from .models import Word, Room
from apps.words_game.services.app import validate_words


class StartGameForm(forms.ModelForm):
    # def clean_room_name(self):
    #     room =
    class Meta:
        model = Room
        fields = ("host", "room_name")


class WordForm(forms.ModelForm):
    def __init__(self, room_name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.room_name = room_name

    def clean_word(self):
        new_word = self.cleaned_data["word"].lower()
        if not validate_words(new_word, self.room_name):
            raise ValidationError("This word is bad")
        return new_word

    class Meta:
        model = Word
        fields = ("word",)
