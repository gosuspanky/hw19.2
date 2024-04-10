# catalog/templatetags/my_tags.py

from django import template

register = template.Library()


# Создание тега
@register.filter
def my_media(data):
    if data:
        return f'/media/{data}'
    else:
        return 'ошибка'
