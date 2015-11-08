# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EventPlanners', '0003_entertainment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Themes',
            fields=[
                ('theme_id', models.AutoField(serialize=False, primary_key=True)),
                ('theme_type', models.CharField(max_length=100)),
                ('theme_name', models.CharField(max_length=100)),
            ],
        ),
    ]
