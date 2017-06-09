from django import template

register = template.Library()


@register.simple_tag
@register.filter
def itera(array, num):
    return array[num]
