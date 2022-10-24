from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse


class Room(models.Model):
    room_name = models.CharField(max_length=50, null=True, unique=True)
    password = models.CharField(max_length=150, null=True)
    last_word = models.CharField(max_length=70)

    def get_absolute_url(self):
        return reverse("words:room_in", kwargs={"room_name": self.room_name})

    def get_words(self):
        return self.words.filter(room_id=self.pk)


class Word(models.Model):
    word = models.CharField(max_length=70)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, related_name="words")

    def clean(self):
        last_word = self.room.last_word
        new_word = self.word[0].lower().strip()
        if not last_word:
            return
        if new_word != last_word[-1]:
            raise ValidationError("Last char is not equal to first")

    class Meta:
        unique_together = ("word", "room")
