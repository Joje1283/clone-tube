from django import template

register = template.Library()


@register.filter
def is_subscribe(creater, subscriber):
    return creater.is_subscribe(subscriber)