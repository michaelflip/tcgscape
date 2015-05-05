from django.db import models

class Card(models.Model):
	name = models.CharField(max_length=255, null=True, blank=True)
	card_number = models.CharField(max_length=12, null=True, blank=True)
	description = models.CharField(max_length=255, null=True, blank=True)
	def __unicode__(self):
		return self.name

class Deck(models.Model):
	name = models.CharField(max_length=255, null=True, blank=True)
	cards = models.ManyToManyField(Card)
	description = models.CharField(max_length=255, null=True, blank=True)
	author = models.CharField(max_length=255, null=True, blank=True)
	def __unicode__(self):
		return self.name

