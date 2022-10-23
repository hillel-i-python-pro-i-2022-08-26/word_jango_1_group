def fill_context(room_obj):
    return {
        "room_name": room_obj.room_name,
        "previous_words": room_obj.words.all(),
        "last_word": room_obj.last_word,
    }
