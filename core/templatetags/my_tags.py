from django import template


register = template.Library()


@register.assignment_tag
def inlist(value, _list):
    return value in _list