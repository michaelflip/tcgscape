# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_card_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='card_power',
            field=models.CharField(max_length=12, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='card',
            name='card_set_name',
            field=models.CharField(max_length=12, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='card',
            name='card_type',
            field=models.CharField(max_length=12, null=True, blank=True),
        ),
    ]
