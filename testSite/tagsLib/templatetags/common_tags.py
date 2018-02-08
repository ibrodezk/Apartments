# This Python file uses the following encoding: utf-8
# owned by Ilya Brodetsky #2017 not to be used
from django import template
from django.core.urlresolvers import reverse,resolve
from django.utils import translation
from common import privateCommon

register = template.Library()

class TranslatedURL(template.Node):
    def __init__(self, language):
        self.language = language
    def render(self, context):
        view = resolve(context['request'].path)
        request_language = translation.get_language()
        translation.activate(self.language)
        url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)
        translation.activate(request_language)
        return url

# not sure why but this refuses to take variable input
# @register.tag(name='translate_url')
# def do_translate_url(parser, token):
#     language = token.split_contents()[1]
#     return TranslatedURL(language)

@register.simple_tag(name='translate_url',takes_context=True)
def do_translate_url(context, language):
    test = TranslatedURL(language)
    return test.render(context)


@register.simple_tag( name='googleKey')
def getGoogleApi():
    return "https://maps.googleapis.com/maps/api/js?key=" + privateCommon.returnApiKey() + "&libraries=places&callback=initialize"

@register.simple_tag( name='googleKeyApiAutoComplete')
def getGoogleApi():
    return "https://maps.googleapis.com/maps/api/js?key=" + privateCommon.returnApiKey() + "&libraries=places&callback=initAutocomplete"
