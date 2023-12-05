from django import template

from menu.models import MenuItem


register = template.Library()

@register.inclusion_tag('menu/menu_tags.html')
def draw_menu(menu_name):
    menu = MenuItem.objects.filter(menu_name__name=menu_name, parent=None).prefetch_related('children')
    
    return {'menu': menu}
