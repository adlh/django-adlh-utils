from django import template

register = template.Library()

@register.filter()
def url_target_blank(text):
    return text.replace('<a ', '<a target="_blank" ')

