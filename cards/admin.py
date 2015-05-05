from django.contrib import admin
from cards.models import Card, Deck
admin.site.register([Card, Deck])