from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value, arg):
    """
        This cuts outs all values or arg of this string
    """

    return value.replace(arg, '')
