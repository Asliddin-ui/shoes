from django import template

register = template.Library()


@register.filter
def in_cart(burger, request):
    print(request.session.get("data", {}))
    return request.session.get("data", {}).get(str(burger.id), 0)


@register.simple_tag
def cart_total(request):
    return sum(request.session.get("data", {}).values())


@register.filter
def flag(country_code):
    return f'&#x1F1{ord(country_code[0])-ord("A")+65};&#x1F1{ord(country_code[1])-ord("A")+65};'