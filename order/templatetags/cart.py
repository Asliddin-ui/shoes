from django import template

register = template.Library()


@register.filter
def in_cart(burger, request):
    print(request.session.get("data", {}))
    return request.session.get("data", {}).get(str(burger.id), 0)


@register.simple_tag
def cart_total(request):
    return sum(request.session.get("data", {}).values())