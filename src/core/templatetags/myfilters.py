"""modules to create custom filter tags, which will be used in the django templates
"""

from django import template
from django.utils import timezone

register = template.Library()

@register.filter(name='addcss')
def addcss(value, arg):
    return value.as_widget(attrs={'class': arg})


@register.filter(name="gt")
def get(a, b):
    return a > b

@register.filter(name="today")
def today():
    return "hello world"
