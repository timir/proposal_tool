# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoicer', '0003_proposal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=200)),
                ('size', models.CharField(max_length=200)),
                ('rates', models.IntegerField(default=0)),
                ('remark', models.TextField()),
                ('city_name', models.ForeignKey(to='invoicer.City')),
                ('mall_name', models.ForeignKey(to='invoicer.Mall')),
            ],
        ),
        migrations.RemoveField(
            model_name='proposal',
            name='city_name',
        ),
        migrations.RemoveField(
            model_name='proposal',
            name='mall_name',
        ),
    ]
