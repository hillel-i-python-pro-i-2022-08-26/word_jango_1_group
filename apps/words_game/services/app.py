# from django.utils import timezone
from apps.words_game.models import Room

#
#
# def validate_words(input_word):
#     required_datetime = timezone.now()
#     last_word = Word.objects.get(input_word, ).filter(created_at__lt=required_datetime)
#     if input_word[-1] == last_word[0]:
#
#


def validate_words(new_word, room_name):
    room = Room.objects.get(room_name=room_name)
    last_word = room.last_word
    all_words = set(map(lambda obj: obj.word, room.words.all()))
    if last_word:
        if new_word[0] != last_word[-1] or new_word in all_words:
            return False
    return True
