from django.db import models

class Card(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    card_number = models.CharField(max_length=12, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    image_url = models.CharField(max_length=255, null=True, blank=True)
    def __unicode__(self):
        return self.name

class Deck(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, unique=True)
    cards = models.ManyToManyField(Card, through='DeckCard')
    description = models.CharField(max_length=255, null=True, blank=True)
    author = models.CharField(max_length=255, null=True, blank=True)
    def __unicode__(self):
        return self.name


class DeckCard(models.Model):
    card = models.ForeignKey(Card)
    deck = models.ForeignKey(Deck)
    quantity = models.IntegerField()
    def __unicode__(self):
        return "Card:" + self.card.name + " Deck:" + self.deck.name
