from django.shortcuts import render

from app.models import Game

# Create your views here.
def index(request):
    return render(request, 'index.html')

def add_game(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        href = request.POST.get('href')
    return render(request, 'add_game.html')
    