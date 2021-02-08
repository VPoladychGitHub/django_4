import datetime
from django import template

register = template.Library()


@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)


@register.inclusion_tag('sale\city_results.html')
def show_results(p):
    return {'populations': p}
