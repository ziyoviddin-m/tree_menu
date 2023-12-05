from django.shortcuts import render
from menu.templatetags.menu_tags import draw_menu


def index(request):
    return render(request, 'menu/index.html')


def about(request):
    return render(request, 'menu/about.html')


def our_projects(request):
    return render(request, 'menu/our_projects.html')


...