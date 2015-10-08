# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoicer', '0004_auto_20151007_1058'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='client_name',
            field=models.ForeignKey(default=0, to='invoicer.Client'),
        ),
    ]
