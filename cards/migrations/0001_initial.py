# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, null=True, blank=True)),
                ('card_number', models.CharField(max_length=12, null=True, blank=True)),
                ('description', models.CharField(max_length=255, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Deck',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, unique=True, null=True, blank=True)),
                ('description', models.CharField(max_length=255, null=True, blank=True)),
                ('author', models.CharField(max_length=255, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DeckCard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField()),
                ('card', models.ForeignKey(to='cards.Card')),
                ('deck', models.ForeignKey(to='cards.Deck')),
            ],
        ),
        migrations.AddField(
            model_name='deck',
            name='cards',
            field=models.ManyToManyField(to='cards.Card', through='cards.DeckCard'),
        ),
    ]
