from django import template

register = template.Library()

@register.filter()
def replace_under_with(value, arg):
    return value.replace("_", arg)