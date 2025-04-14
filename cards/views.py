

# Create your views here.
from django.shortcuts import render, redirect
from .models import WordCard
from .forms import WordCardForm
import random


def home(request):
    return render(request, 'cards/home.html')

def add_card(request):
    if request.method == 'POST':
        form = WordCardForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cards')
    else:
        form = WordCardForm()
    return render(request, 'cards/add_card.html', {'form': form})

def cards_view(request):
    cards = WordCard.objects.all()
    return render(request, 'cards/cards.html', {'cards': cards})

def practice(request):
    cards = list(WordCard.objects.all())
    card = random.choice(cards) if cards else None
    return render(request, 'cards/practice.html', {'card': card})