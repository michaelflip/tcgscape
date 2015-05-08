from django.contrib import admin
from cards.models import Card, Deck, DeckCard

admin.site.register([Card, Deck, DeckCard])
