from django import template

register = template.Library()


@register.simple_tag
@register.filter
def photo_list(array):
    array = array.split(',')
    return array




