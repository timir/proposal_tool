# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('invoicer', '0005_item_client_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='AvailableDate',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('available_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('client_name', models.ForeignKey(default=0, to='invoicer.Proposal')),
            ],
        ),
        migrations.AlterField(
            model_name='item',
            name='client_name',
            field=models.ForeignKey(default=0, to='invoicer.Proposal'),
        ),
    ]
