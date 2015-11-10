# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EventPlanners', '0005_venue'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='venue_cost',
            field=models.IntegerField(default=65000),
            preserve_default=False,
        ),
    ]
