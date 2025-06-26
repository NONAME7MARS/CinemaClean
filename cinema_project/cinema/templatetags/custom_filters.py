from django import template

register = template.Library()

@register.filter
def calculate_row(seat_number):
    return (seat_number - 1) // 10 + 1

@register.filter
def calculate_seat(seat_number):
    return (seat_number - 1) % 10 + 1

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
