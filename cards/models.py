from django.db import models

class Card(models.Model):
	name = models.CharField(max_length=255)
	card_number = models.CharField(max_length=12)
	description = models.CharField(max_length=255, null=True, blank=True)
	def __unicode__(self):
		return self.name

class Deck(models.Model):
	name = models.CharField(max_length=255)
	cards = models.ManyToManyField(Card)
	description = models.CharField(max_length=255, null=True, blank=True)
	def __unicode__(self):
		return self.name

