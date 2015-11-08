# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EventPlanners', '0002_photographers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entertainment',
            fields=[
                ('e_id', models.AutoField(primary_key=True, serialize=False)),
                ('entertainers_name', models.CharField(max_length=100)),
                ('entertainers_type', models.CharField(max_length=100)),
                ('entertainment_cost', models.IntegerField()),
            ],
        ),
    ]
