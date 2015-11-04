# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Caterers',
            fields=[
                ('caterer_id', models.AutoField(serialize=False, primary_key=True)),
                ('caterer_name', models.CharField(max_length=100)),
                ('cuisine', models.CharField(max_length=100)),
                ('cost', models.IntegerField()),
            ],
        ),
    ]
