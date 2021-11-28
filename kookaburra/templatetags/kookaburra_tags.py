from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def user_is_following(context):
    cntx = context
    return cntx["post"].pk in cntx["user"].posts_following.values_list("pk", flat=True)
