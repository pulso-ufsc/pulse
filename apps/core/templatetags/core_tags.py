from django import template
from django.urls import NoReverseMatch, reverse

register = template.Library()


@register.simple_tag(takes_context=True)
def active(context, url_name):
    try:
        url = reverse(url_name)
    except NoReverseMatch:
        return ""

    current_path = context.request.path.rstrip("/") or "/"
    reversed_url = url.rstrip("/") or "/"

    if current_path == reversed_url:
        return "active"
    return ""
