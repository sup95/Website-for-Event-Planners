# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EventPlanners', '0007_accomodations'),
    ]

    operations = [
        migrations.CreateModel(
            name='Decorators',
            fields=[
                ('dec_id', models.AutoField(serialize=False, primary_key=True)),
                ('dec_name', models.CharField(max_length=100)),
                ('dec_cost', models.IntegerField()),
                ('dec_fk', models.ForeignKey(to='EventPlanners.Themes')),
            ],
        ),
    ]
