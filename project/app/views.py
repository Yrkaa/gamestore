from django.shortcuts import render
from django.urls import path

from app.models import Game

from project import urls

# Create your views here.
def index(request):
    games = Game.objects.all()
    for i in games:
        urls.urlpatterns.append(path(str(i.id), game_page, name = None, kwargs={'name': i.name, 'description': i.description, 'price': i.price, 'href': i.href}))
    return render(request, 'index.html', context={'games': games})

def add_game(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        href = request.POST.get('href')
        new_game = Game(name=name, description=description, price=price, href=href)
        new_game.save()
    return render(request, 'add_game.html')

def game_page(request, name, description, price, href):
    data = {'description': description, 'name': name, 'price': price, 'href': href}
    return render(request, 'game_page.html', context=data)
    