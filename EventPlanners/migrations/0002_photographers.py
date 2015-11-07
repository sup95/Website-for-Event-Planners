# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EventPlanners', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photographers',
            fields=[
                ('photographer_id', models.AutoField(primary_key=True, serialize=False)),
                ('photographer_name', models.CharField(max_length=100)),
                ('photography_type', models.CharField(max_length=100)),
                ('videography', models.CharField(max_length=20)),
                ('photo_cost', models.IntegerField()),
            ],
        ),
    ]
