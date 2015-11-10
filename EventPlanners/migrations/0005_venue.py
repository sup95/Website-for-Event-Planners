# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EventPlanners', '0004_themes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('venue_id', models.AutoField(serialize=False, primary_key=True)),
                ('venue_name', models.CharField(max_length=100)),
                ('venue_type', models.CharField(max_length=100)),
                ('venue_location', models.CharField(max_length=100)),
            ],
        ),
    ]
