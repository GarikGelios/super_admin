from django import template

register = template.Library()


@register.inclusion_tag('core/nav/top.html', takes_context=True)
def top_navigation(context, **kwargs):
    request = context.get('request')
    active = kwargs
    return locals()
