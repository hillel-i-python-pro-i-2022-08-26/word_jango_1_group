from django.db import models


# class Word(models.Model):
#     word = models.CharField(max_length=50, unique=True)


class Room(models.Model):
    host = models.CharField(max_length=50)
    last_word = models.CharField(max_length=70)


class Word(models.Model):
    word = models.CharField(max_length=70)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, related_name="words")

    def __hash__(self):
        return hash(self.word)
