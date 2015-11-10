# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EventPlanners', '0006_venue_venue_cost'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accomodations',
            fields=[
                ('acc_id', models.AutoField(serialize=False, primary_key=True)),
                ('acc_name', models.CharField(max_length=100)),
                ('acc_type', models.CharField(max_length=100)),
                ('acc_location', models.CharField(max_length=100)),
                ('acc_cost', models.IntegerField()),
                ('acc_fk', models.ForeignKey(to='EventPlanners.Venue')),
            ],
        ),
    ]
