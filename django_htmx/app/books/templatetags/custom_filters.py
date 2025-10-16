from django import template
from django_htmx.settings import RUB_PER_USD

register = template.Library()


@register.filter()
def convert_currency_filter(value):
    return round(value / RUB_PER_USD)