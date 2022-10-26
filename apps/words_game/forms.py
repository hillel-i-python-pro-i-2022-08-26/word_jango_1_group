from django import forms
from django.core.exceptions import ValidationError
from django.urls import reverse

from .models import Word, Room
from apps.words_game.services.app import validate_words


class StartGameForm(forms.ModelForm):
#class StartGameForm(forms.Form):
    #host = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    #room_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))

    # host = forms.CharField(max_length=50)    #for choice room
    # room_name = forms.ModelChoiceField(queryset=Room.objects.all()) #for choice room
    # def clean_room_name(self):
    #     room =
    class Meta:
        model = Room
        fields = ("host", "room_name",)
        widgets = {
            'host': forms.TextInput(attrs={'class': 'form-control'}),
            'room_name': forms.TextInput(attrs={'class': 'form-control'})
        }




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
