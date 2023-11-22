from django.http import HttpResponse
from django.shortcuts import render

MENU = {"Персонажи": "/", "О блоге": "/about", }
HEROES = {"Кастиэль": "/castiel", "Дин Винчестер": "/dean", "Сэм Винчестер": "/sam"}


def main_page(request):
    data = {"menu": MENU, "heroes": HEROES}
    return render(request, './main.html', context=data)


def about_page(request):
    data = {"menu": MENU}
    return render(request, './about.html', context=data)

def castiel_page(request):
    data = {"menu": MENU}
    return render(request, './castiel.html', context=data)

def dean_page(request):
    data = {"menu": MENU}
    return render(request, './dean.html', context=data)

def sam_page(request):
    data = {"menu": MENU}
    return render(request, './sam.html', context=data)