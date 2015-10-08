# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('invoicer', '0002_auto_20151007_0948'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proposal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('city_name', models.ForeignKey(to='invoicer.City')),
                ('client_name', models.ForeignKey(to='invoicer.Client')),
                ('mall_name', models.ForeignKey(to='invoicer.Mall')),
            ],
        ),
    ]
