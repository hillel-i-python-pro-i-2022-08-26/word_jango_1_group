import copy


def fill_context(room_obj):
    return {
        "room_name": room_obj.room_name,
        "previous_words": room_obj.words.all(),
        "last_word": room_obj.last_word,
    }


def update_post_data(request_data, room_id):
    post_data = copy.copy(request_data)
    post_data["word"] = post_data["word"].lower().strip()
    post_data["room"] = room_id
    return post_data


def update_last_word(room, last_word):
    room.last_word = last_word
    room.save()
