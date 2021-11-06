from django import template
from django.conf import settings

import logging

register = template.Library()
logger = logging.getLogger(__name__) 

@register.simple_tag
def i18n_url_switch(request, language):
    #print(request)
    if not hasattr(request, 'path'):
        return '#'
    request_parts = (request.path).strip('/').split('/')
    langs = settings.LANGUAGES

    if isinstance(langs, tuple):
        if language in [tup[0] for tup in langs]:
            request_parts[0] = language
            return '/' + '/'.join(request_parts) + '/'
    return request.path

