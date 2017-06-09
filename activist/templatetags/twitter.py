from django import template

register = template.Library()


@register.simple_tag
@register.filter
def twitter(username):
    return username.split('@')[1]
