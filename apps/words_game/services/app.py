import copy


class GameCircle:
    def __init__(self, room):
        self.room = room

    def fill_context(self):
        return {
            "room_name": self.room.room_name,
            "previous_words": self.room.words.all(),
            "last_word": self.room.last_word,
        }

    def update_post_data(self, request_data):
        post_data = copy.copy(request_data)
        post_word_cleaned = post_data["word"].lower().strip()
        post_data["word"] = post_word_cleaned
        post_data["room"] = self.room.pk
        return post_data

    def update_last_word(self, last_word):
        self.room.last_word = last_word
        self.room.save()


"""Old style"""
# def fill_context(room_obj):
#     return {
#         "room_name": room_obj.room_name,
#         "previous_words": room_obj.words.all(),
#         "last_word": room_obj.last_word,
#     }
#
#
# def update_post_data(request_data, room_id):
#     post_data = copy.copy(request_data)
#     post_data["word"] = post_data["word"].lower().strip()
#     post_data["room"] = room_id
#     return post_data
#
#
# def update_last_word(room, last_word):
#     room.last_word = last_word
#     room.save()
