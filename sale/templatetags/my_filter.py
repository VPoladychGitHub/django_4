from django import template

register = template.Library()


def cut(value, arg):
    """Removes all values of arg from the given string"""
    return value.replace(arg, '')


@register.filter(name='replc_xxx')
def replc_xxx(s: str):
    """Replace XXX  string to city"""
    return s.replace("XXX", "  city is beatifull")
