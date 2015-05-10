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

def deck(request, deck_name):
	my_dict = {
		"deck": Deck.objects.get(name=deck_name),
		"decks": Deck.objects.all(),
	}
	return render(request, "deck.html", my_dict)

def card(request, deck_name):
	my_dict = {
		"card": Card.objects.get(name=card_name),
		"cards": Card.objects.all(),
	}
	return render(request, "card.html", my_dict)