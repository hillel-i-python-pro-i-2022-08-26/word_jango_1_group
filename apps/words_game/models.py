from django.db import models
from django.urls import reverse


# class Word(models.Model):
#     word = models.CharField(max_length=50, unique=True)


class Room(models.Model):
    host = models.CharField(max_length=50)
    room_name = models.CharField(max_length=50, null=True, unique=True)
    last_word = models.CharField(max_length=70)

    def get_absolute_url(self):
        return reverse("words:room_in", kwargs={"room_name": self.room_name})

    def get_words(self):
        return self.words.filter(room_id=self.pk)




class Word(models.Model):
    word = models.CharField(max_length=70)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, related_name="words")

    def __hash__(self):
        return hash(self.word)
