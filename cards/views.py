from django.shortcuts import render
from django.http import HttpResponse
from cards.models import Card, Deck


# Create your views here.
def home(request):
	my_dict = {
		"name": "Michael",
		"decks": Deck.objects.all(),
	}
	return render(request, "home.html", my_dict)

def recentdecks(request):
	another_dict = {
		"name": "Flip",
		"decks": Deck.objects.all(),
	}
	return render(request, "recentdecks.html", another_dict)

def collection(request):
	third_dict = {
		"name": "MFlip",
		"decks": Deck.objects.all(),
	}
	return render(request, "collection.html", third_dict)