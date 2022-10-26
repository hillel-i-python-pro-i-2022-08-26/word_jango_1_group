from django import template
from apps.words_game.models import Room

register = template.Library()


@register.simple_tag(name="get_list_rooms")
def get_rooms():
    return Room.objects.all()


# @register.inclusion_tag('путь где использ')
# def show_rooms():
# rooms = Room.objects.all()
# return {'rooms': rooms}
